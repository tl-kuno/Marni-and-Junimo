from flask import Flask
from flask import request
from flask_cors import CORS
import json
from character import Character

app = Flask(__name__)
CORS(app)
player = Character('Marni')


@app.route('/', methods=["GET", "POST"])
def handle_interaction():
    command = str(request.args.get('command'))
    output = player.handle_user_input(command)
    data_set = {'output': output, 'location': player.location.room_name}
    json_dump = json.dumps(data_set)
    return json_dump


@app.route('/new', methods=["POST"])
def handle_new_game():
    ip_address = str(request.remote_addr)
    intro = player.newgame(ip_address)
    data_set = {'output': intro, 'location': player.location.room_name}
    json_dump = json.dumps(data_set)
    return json_dump


@app.route('/quit', methods=["POST"])
def handle_quit_game():
    data_set = {'output': 'Game Over', 'location': player.location.room_name}
    json_dump = json.dumps(data_set)
    return json_dump


@app.route('/save', methods=["POST"])
def handle_save():
    # output = player.savegame()
    data_set = {'output': 'Game Progress Saved', 'location': player.location.room_name}
    json_dump = json.dumps(data_set)
    return json_dump


@app.route('/load', methods=["GET"])
def handle_load():
    # output = player.loadgame()
    data_set = {'output': 'Game Loaded from Last Save', 'location': player.location.room_name}
    json_dump = json.dumps(data_set)
    return json_dump


if __name__ == '__main__':
    app.run_server(debug=False)
