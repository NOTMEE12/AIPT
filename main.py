import difflib
import json
import flask
import flask_sock
import ollama
import os
import argparse

parser = argparse.ArgumentParser(description="AI model Prompt Tester (AIPT for short) is a simple app that will check how suitable each model is for a given prompt.")
parser.add_argument('--OLLAMA_HOST', default='127.0.0.1', type=str, help="Ollama host. Default: 127.0.0.1.")
parser.add_argument('--HOST', default='0.0.0.0', type=str, help="IP on which the app will be ran.")
parser.add_argument('--PORT', default=11432, type=int, help="Port on which the app will run")
parser.add_argument('--DEBUG', default=False, type=bool, help="Run the app on debug")

args = parser.parse_args()


OLLAMA_HOST = args.OLLAMA_HOST if args.OLLAMA_HOST is not None else os.getenv('OLLAMA_HOST')
if os.getenv('OLLAMA_HOST') is None: os.putenv('OLLAMA_HOST', args.OLLAMA_HOST if args.OLLAMA_HOST is not None else '127.0.0.1')
HOST = args.HOST
PORT = args.PORT
DEBUG = args.DEBUG

app = flask.Flask(__name__)
websock = flask_sock.Sock(app)


def compare(src: str, text: str):
	"""
	Give a percentage of how much `text` is in `src`.
	"""
	org_res = tuple(difflib.Differ().compare([*src], [*text]))
	res = tuple(r for r in org_res if r[0].isspace())
	return len(res) / len(org_res) * 100


def get_extractable_char(text: str, check_for: str):
	s = text.lower().find(check_for.lower())
	e = s + len(check_for) - 1
	if s == -1 or e == -1 or s-1 < 0 or e + 1 >= len(text):
		return None
	
	if text[s-1] == text[e+1]:
		return text[s-1]
	
	return None


@websock.route("/api/check")
def check(srv: flask_sock.Server):
	rsp = srv.receive()
	print(rsp)
	dt = json.loads(rsp)
	prompt = dt["prompt"]
	des_output = dt["output"]
	if len(prompt.strip()) == 0 or len(des_output.strip()) == 0:
		return tuple()
	print('#'*32)
	print('Starting Prompt test check.')
	chat = [{"role": "user", "content": prompt}]
	for model in models:
		srv.send(json.dumps({
			"model":            model,
			"match-text":       "Not tested",
			"match-percentage": 0,
			"response":         "",
			"status":           ""
		}))
	for model in models:
		print("=" * 32)
		print(f"{model}")
		print("-" * 32)
		srv.send(json.dumps({
			"model":            model,
			"match-text":       "...",
			"match-percentage": 0,
			"response":         "...",
			"status":           "calc"
		}))
		response: str = client.chat(model, chat)["message"]["content"]
		comp = round(compare(response, des_output))
		extractable_char = get_extractable_char(response, des_output)
		print(f"Similarity: {comp}%")
		print(f"Extractable char: {extractable_char}")
		print(f"Response: \n\"{response}\"")
		
		if extractable_char is None:
			if comp == 100:
				status = "perf"
			elif comp <= 40:
				status = "none"
			elif comp <= 80:
				status = "mid"
			else:
				status = "good"
		else:
			comp = round(compare(response, des_output))
			if comp == 100:
				status = "perf"
			elif comp <= 40:
				status = "mid"
			elif comp <= 80:
				status = "good"
			else:
				status = "perf"
			
		match_text = response
		
		srv.send(json.dumps({
			"model": model,
			"match-text": match_text,
			"match-percentage": comp,
			"response": response,
			"status": status
		}))


@app.route("/")
def main():
	return flask.render_template("main.html", models=models)



if __name__ == '__main__':
	client = ollama.Client(OLLAMA_HOST)
	models = tuple(map(lambda x: x["name"], client.list()["models"]))
	app.run(HOST, PORT, debug=DEBUG)
