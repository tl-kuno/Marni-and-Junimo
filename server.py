import pickle
import os
import json
from flask import Flask
from flask import request
from flask_cors import CORS
from character import Character
from messages import messages


app = Flask(__name__)
CORS(app)


home_dir = os.path.dirname(__file__)
users_dir = os.path.join(home_dir, "game_data/users")
game_instances = {}


def create_load_name_array(ip_address):
    load_games = []
    for filename in os.listdir(users_dir):
        split_file_ext = filename.split(".p")
        identifiers = split_file_ext[0].split("-")
        print(identifiers)
        if identifiers[1] == ip_address:
            load_games.append(identifiers[0])
    return load_games


@app.route('/start', methods=["GET"])
def handle_start():
    """
    Summary:
        When a user lands on the page, the welcome message is sent
    Returns:
        output: Junimo's welcome message to the user
    """
    ip_address = request.args.get('ip_address')
    load_games = create_load_name_array(ip_address)
    data_set = {'output': messages["welcome"], "loadGames": load_games}
    json_dump = json.dumps(data_set)
    return json_dump


@app.route('/new', methods=["GET"])
def handle_new_game():
    """
    Summary:
        When a new game is started, create a game instance and store it
        in the dict with a newly genereated num between 1-100 as the key
        TODO    Consider other options for the key, such as a user given "name"
                Benefits of this are making the load/save front end work better
    Returns:
        key: random int between 1-100 generated as a dictionary key
        output: Starting room introduction/description
        location: the current room that the player is located in
    """
    ip_address = request.args.get('ip_address')
    userName = request.args.get('userName')
    identifier = userName + "-" + ip_address
    player = Character(userName, ip_address)
    game_instances[identifier] = player
    intro = (game_instances[identifier]).newgame()
    data_set = {'output': intro,
                'location': game_instances[identifier].location.room_name,
                'ip_address': ip_address,
                'identifier': identifier,
                }
    json_dump = json.dumps(data_set)
    return json_dump


@app.route('/', methods=["GET"])
def handle_interaction():
    """
    Summary:
        When a user sends a command, use the proper Character class instance
        from the dictionarry lookup and send back a response string/room
    Params:
        command: the string entered by the user
        key: the dictionary key of the user's character class
    Returns:
        output: the game's response to the users command
        location: the current room that the player is located in
    """

    identifier = request.args.get('identifier')
    player = game_instances[identifier]
    command = str(request.args.get('command'))
    output = player.handle_user_input(command)
    data_set = {'output': output,
                'location': player.location.room_name,
                'ip_address': player.ip_address}
    json_dump = json.dumps(data_set)
    return json_dump


@app.route('/save', methods=["GET"])
def handle_save():
    """
    Summary:
        When a user saves via the button
    Params:
        key: the dictionary key of the user's character class
    Returns:
        output: Junimo's response to the end of game
    """
    identifier = request.args.get('identifier')
    player = game_instances[identifier]
    save_message = player.savegame()
    data_set = {'output': save_message}
    json_dump = json.dumps(data_set)
    return json_dump


# TODO, need to think about the reverse of save
# TODO have output return the long string from the current room
@app.route('/load', methods=["GET"])
def handle_load():
    """
    Summary:
        When a user loads via the load button
    Params:
        key: the dictionary key of the user's character class
    Returns:
        output: Junimo's response to the end of game
    """
    identifier = request.args.get('identifier')
    full_path = users_dir + "/" + identifier + ".pickle"
    try:
        player_pickle = open(full_path, "rb")
        player = pickle.load(player_pickle)
    except FileNotFoundError:
        data_set = {
            'output': 'No file found by that name',
            'is_loaded': False,
        }
        json_dump = json.dumps(data_set)
        return json_dump
    game_instances[identifier] = player
    data_set = {'output': 'Game Loaded from Last Save',
                'is_loaded': True,
                'identifier': player.identifier,
                'location': player.location.room_name,
                'key': player.key}
    json_dump = json.dumps(data_set)
    return json_dump


# TODO @ alex do you want Junimo to say something cuter than Game Over?
# TODO, I will be attempting to call this function on window close as well
# have to think about if a game has been saved and how to handle this
@app.route('/quit', methods=["GET"])
def handle_quit():
    """
    Summary:
        When a user quits (clicking the button, closing the browser)
        The information is removed from the array
    Params:
        key: the dictionary key of the user's character class
    Returns:
        output: Junimo's response to the end of game
    """
    identifier = request.args.get('identifier')
    data_set = {'output': 'Game Over'}
    json_dump = json.dumps(data_set)
    del game_instances[identifier]
    return json_dump


if __name__ == '__main__':
    app.run_server(debug=False)
