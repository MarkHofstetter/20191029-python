import requests
from pprint import pprint

kelvin0 = 273.15

url = 'http://127.0.0.1:5000'

response = requests.get(url)
data = response.json()

pprint(data)

'''
{'base': 'stations',
 'clouds': {'all': 90},
 'cod': 200,
 'coord': {'lat': 51.51, 'lon': -0.13},
 'dt': 1485789600,
 'id': 2643743,
 'main': {'humidity': 81,
          'pressure': 1012,
          'temp': 280.32,
          'temp_max': 281.15,
          'temp_min': 279.15},
 'name': 'London',
 'sys': {'country': 'GB',
         'id': 5091,
         'message': 0.0103,
         'sunrise': 1485762037,
         'sunset': 1485794875,
         'type': 1},
 'visibility': 10000,
 'weather': [{'description': 'light intensity drizzle',
              'icon': '09d',
              'id': 300,
              'main': 'Drizzle'}],
 'wind': {'deg': 80, 'speed': 4.1}}
'''