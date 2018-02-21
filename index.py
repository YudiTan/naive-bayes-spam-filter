from flask import Flask, jsonify, request
from naivebayes import yieldResult
import json

app = Flask(__name__)

@app.route('/naivebayes/<string:message>')
def spamHam(message):
    return json.dumps({'result': yieldResult(message).tolist()})


if __name__ == '__main__':
    app.run(port=5000)