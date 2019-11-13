from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask_cors import CORS, cross_origin

app = FlaskAPI(__name__)
cors = CORS(app)

teilnehmer_dict = {
    'Mark'      : {'yob': 1975, 'fav_col': 'blau', 'edu': ['vs', 'gym', 'uni']},
    'Herbert'   : {'yob': 1973, 'edu': [ 'vs', 'gym', 'htl', 'uni']},
    'Stefan'    : {'yob':1976},
    'Johann'    : {'yob':1987},
    'Marian'    : {'yob':1980},
    'Magdalena' : {'yob':1982},
    'Stefan'    : {'yob':1983},
    'Kurt'      : {'yob':1995},
    'Karl'      : {'yob':1960},
    'Latchezar' : {'yob':1972},
    }

@app.route("/", methods=['GET'])
def welcome():
    return {'data': 'Hello World'}

@app.route("/demo", methods=['GET'])
def demo():
    return {'data': 'demo'}

@app.route("/teilnehmer", methods=['GET'])
def alle_teilnehmer():
    ret = []
    for name, data in teilnehmer_dict.items():
        ret.append(
           {'name': name, 
            'yob' : data['yob']} )

    return ret
    


@app.route("/teilnehmer/<string:key>", methods=['GET'])
def teilnehmer(key):
    try:
        return [{'name': key , 'year_of_birth': teilnehmer_dict[key]['yob']}]
    except KeyError:
        return {'error': 'nothing found'}, 404


if __name__ == '__main__':
    app.run(debug=True)