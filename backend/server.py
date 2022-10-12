from flask import Flask
from flask import request
import json

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def handle_request():
    command = str(request.args.get('command'))
    output_base = "You have sent the following command: "
    output = output_base + command

    data_set = {'output': output}
    json_dump = json.dumps(data_set)
    return json_dump
