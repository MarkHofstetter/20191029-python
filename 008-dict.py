# import pprint
# from pprint import pprint
# from pprint import *
from pprint import pprint as pp

teilnehmer = {
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

pp(teilnehmer)

'''
for k in teilnehmer:
    print(k, teilnehmer[k])
'''

'''
+ so vorhanden die Lieblingfarbe ausgeben

+ und die LETZTE Ausbildung
'''

teilnehmer['Eva'] = { 'yob': 1998, 'fav_col': 'rot' }

for k, v in teilnehmer.items():
    print(k, end = ' ')
    try:
        print(v['fav_col'])
    except KeyError:
        print('keine Lieblingsfarbe')
        
    if 'edu' in v:
        print("Letzte Bildung {:s}".format(v['edu'][-1]))
        
