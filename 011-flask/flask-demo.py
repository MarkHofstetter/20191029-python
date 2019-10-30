from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

@app.route("/", methods=['GET'])
def welcome():
    return {'data': 'Hello World'}

@app.route("/demo", methods=['GET'])
def demo():
    return {'data': 'demo'}

@app.route("/teilnehmer/<string:key>", methods=['GET'])
def teilnehmer(key):
    return {'data': key}


if __name__ == '__main__':
    app.run(debug=True)