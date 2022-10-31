from flask import Flask
from flask import request
from flask_cors import CORS
import json
from main import handle_user_input

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["GET", "POST"])
def handle_interaction():
    command = str(request.args.get('command'))
    output = handle_user_input(command)
    data_set = {'output': output}
    json_dump = json.dumps(data_set)
    return json_dump

@app.route('/save', methods=["POST"])
def handle_save():
    data_set = {'confirmation': 'Game Progress Saved'}
    json_dump = json.dumps(data_set)
    return json_dump

@app.route('/load', methods=["GET"])
def handle_load():
    data_set = {'confirmation': 'Game Loaded from Last Save'}
    json_dump = json.dumps(data_set)
    return json_dump


if __name__ == '__main__':
    app.run_server(debug=False)
