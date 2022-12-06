from crypt import methods
from flask import Flask, jsonify
import requests, json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_targets():
    sensors = requests.get('http://localhost:1337/inventory').json()
    targets = [
    {
        "targets": sensors,
        "labels": {
            "type": "sensors",
        }
    }
]
    return targets

if __name__ == '__main__':
    app.run(debug=True, port=8000)