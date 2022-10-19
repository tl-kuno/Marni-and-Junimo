from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
import json
from main import test_function

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["GET", "POST"])
@cross_origin(origin='*', headers=['Content-Type', 'application/json'])
def handle_request():
    command = str(request.args.get('command'))
    output = test_function(command)
    data_set = {'output': output}
    json_dump = json.dumps(data_set)
    return json_dump


if __name__ == '__main__':
    app.run_server(debug=False)
