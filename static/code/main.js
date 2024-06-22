let prompt_textarea = document.getElementById('prompt');
let output_textarea = document.getElementById('output');
let run_elem = document.getElementById('run');
var websock = null;

function update_check(){
	if (prompt_textarea.value.length != 0 & output_textarea.value.length != 0){
		run_elem.className = 'data can-run';
		run_elem.disabled = false;
	} else {
		run_elem.className = 'data can-not-run';
		run_elem.disabled = true;
	}
}


function check(){
	data = {'prompt': prompt_textarea.value, 'output': output_textarea.value};

	if (data.prompt == '' || data.output == ''){return;};

	if (websock != null){
		websock.close()
	}

	websock = new WebSocket('/api/check');
	websock.onmessage = (message) => {
		console.log(message.data);
		data = JSON.parse(message.data);
		console.log(data);
		console.log(`${data.model} | ${data["match-text"]}:${data["match-percentage"]} |\n${data.response}`);
		element = document.getElementById(data.model);
		element.className = `data ${data.status}`;

		element.children[1].children[0].textContent = data["match-text"];
		element.children[1].children[1].textContent = String(data["match-percentage"]).padStart(2, '0') + "%";
		element.children[2].children[1].children[2].textContent = data.response;

	};
	websock.onopen = () => {websock.send(JSON.stringify(data));};
}