from flask import Flask
from flask import request
from flask_cors import CORS
import json
from main import handle_user_input, newgame

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["GET", "POST"])
def handle_interaction():
    command = str(request.args.get('command'))
    output = handle_user_input(command)
    data_set = {'output': output}
    json_dump = json.dumps(data_set)
    return json_dump


@app.route('/new', methods=["POST"])
def handle_new_game():
    data_set = {'confirmation': 'New game created'}
    json_dump = json.dumps(data_set)
    return json_dump


@app.route('/save', methods=["POST"])
def handle_save():
    data_set = {'startDialogue': ''}
    json_dump = json.dumps(data_set)
    return json_dump


@app.route('/load', methods=["GET"])
def handle_load():
    intro = newgame()
    data_set = {'intro': intro}
    json_dump = json.dumps(data_set)
    return json_dump


if __name__ == '__main__':
    app.run_server(debug=False)
