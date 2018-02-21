from flask import Flask, jsonify, request
from naivebayes import yieldResult
import json

application = Flask(__name__)

@application.route('/naivebayes/<string:message>')
def spamHam(message):
    return json.dumps({'result': yieldResult(message).tolist()})


if __name__ == '__main__':
    application.run()