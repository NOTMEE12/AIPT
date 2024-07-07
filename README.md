# AI Prompt Testing app - AIPT
AIPT is a simple app that checks how each model suits specified prompt.  
Here's a video of it in action:  

https://github.com/NOTMEE12/AIPT/assets/103068655/55b72454-bf74-4b99-b213-c3225dbc4574

## How it works
The app is really simple.  
You give it a prompt and desired output.   
It then gives that prompt to every model and compares the output.  

## How to run

> [!NOTE]  
> Running process shouldn't be different on different OS.

---

###  Git

Here are the requirements.
You have to have:
- python3
- ollama (must also be running)
- git

1. Clone this repo
   ```sh
   git clone https://github.com/NOTMEE12/AIPT
   cd AIPT
   ```
2. Install required libraries.
   ```sh
   pip install -r requirements.txt
   ```

3. Run the app
   ```sh
   python main.py
   # arguments:
   # --HOST - ip on which the app will run
   # --PORT - port
   # --DEBUG - run the app with debug turned on?
   # --OLLAMA_HOST - Ollama host (with port) eg.: http://127.0.0.1:11434
   ```
---

### 🐳 Docker

Run:
```shell
docker run --name AIPT -p 11432:11432 -e DEBUG=False -e PORT=11432 -h host.docker.internal:host-gateway notmee12/aipt python main.py --OLLAMA_HOST="http://host.docker.internal:11434" --HOST="0.0.0.0"
```
If you have ollama running on other url then replace the `--OLLAMA_HOST=...` - replace the `...` with url of ollama.


> [!IMPORTANT]  
> If you are using docker desktop, you have run this command in terminal. (Remember to have docker desktop active)
=======
- git (ofc)

> _**Running process shouldn't be different on different OS.**_

1. Clone this repo
```sh
git clone https://github.com/NOTMEE12/AIPT
cd AIPT
```
2. Install required libraries.
```sh
pip install flask flask_sock ollama
```

3. Run the app
```sh
python main.py
```

## Important:
### By default it will run the app on 0.0.0.0 (so on public port, which means you can access the app from other devices on the same network). You can change this behaviour in the `main.py` on the last line.  
### It also runs as debug by default. You can also change this in the `main.py`.

---

## Questions:
- Q: How to run this tool with ollama from different device/url?
<<<<<<< HEAD
- A: To run this tool with ollama from different device/url, you need to either:
  - pass an `--OLLAMA_HOST` argument to the run command,
    eg: `python main.py --OLLAMA_HOST=...` (replace `...` with the url of the ollama).
  - set an environment variable `OLLAMA_HOST` to the ollama host.

- Q: Can I use X model which is not on ollama?
- A: AIPT currently only supports ollama models.  

=======
- A: To run this tool with ollama from different device/url, you need to just change this line `client = ollama.Client()` in `main.py` to `client = ollama.Client("YOUR_OLLAMA_IP_HERE")`
- Q: Can I use X model which is not on ollama?
- A: AIPT currently only supports ollama models.
- Q: Can I exclude X model from being tested?
- A: Not yet.
