from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_json():
    with open('data_s2.json') as json_file:
        data = json.load(json_file)
    return jsonify(data)

if __name__ == '__main__':
    app.run()
