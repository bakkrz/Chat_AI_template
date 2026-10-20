"""
Run server for AI chat

by https://github.com/bakkrz
ver. 1.1
year 2026

"""

from flask import Flask, render_template,send_from_directory
import os


server_model = os.getenv('SERVER_MODEL','http://localhost:8000/v1')
server_ip = os.getenv('SERVER_LOCAL_IP','127.0.0.1')
server_port =  os.getenv('SERVER_LOCAL_PORT','8800')
system="Jesteś pomocnym asystentem. Odpowiadaj po polsku, zwięźle i rzeczowo. Kod umieszczaj w blokach markdown."
model_name="Bielik-7B-v0.1"
key=""
temperature = 0.3
max_tokens = 1024

  
  
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index_en.html', 
                           server_model=server_model,
                           ip=server_ip,
                           port=server_port,
                           system=system,
                           model=model_name,
                           key=key,
                           temperature=temperature,
                           tokens=max_tokens
                           )

if __name__ == "__main__":
    app.run(debug=True, host=server_ip, port=server_port)