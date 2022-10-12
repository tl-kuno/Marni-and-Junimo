from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    if request.args.get('userInput'):
        userInput = request.args.get('userInput')
        gameOutputBase = "returning output for: "
        gameOutput = gameOutputBase + userInput
        return jsonify({'output': gameOutput})
    else:
        return jsonify({'output': 'no input was provided'})
