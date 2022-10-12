from flask import Flask
from flask import request
from flask_cors import CORS
import json
from backend.main import test_function

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["GET", "POST"])
def handle_request():
    command = test_function()
    # command = str(request.args.get('command'))
    output_base = "You have sent the following command: "
    output = output_base + command

    data_set = {'output': output}
    json_dump = json.dumps(data_set)
    return json_dump


if __name__ == '__main__':
    app.run_server(debug=False)
