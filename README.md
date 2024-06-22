# AI Prompt Testing app - AIPT
AIPT is a simple app that checks how each model suits specified prompt.  
Here's a video of it in action:  

https://github.com/NOTMEE12/AIPT/assets/103068655/55b72454-bf74-4b99-b213-c3225dbc4574

## How it works
The app is really simple.  
You give it a prompt and desired output.   
It then gives that prompt to every model and compares the output.  

## How to run
Here are the requirements.
You have to have:
- python3
- ollama (must also be running)
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


## Questions:
- Q: How to run this tool with ollama from different device/url?
- A: To run this tool with ollama from different device/url, you need to just change this line `client = ollama.Client()` in `main.py` to `client = ollama.Client("YOUR_OLLAMA_IP_HERE")`
- Q: Can I use X model which is not on ollama?
- A: AIPT currently only supports ollama models. 
- Q: Can I exclude X model from being tested?
- A: Not yet.
