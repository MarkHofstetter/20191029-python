'''
+ wir wollen Zahlen vom user einlesen
+ ermitteln wie oft ein Zahl eingegeben wurde, bis er 0 eingibt

Usereingabe 
3,4,5,2,3,4,3,0

Ausgabe 
3: 3
4: 2
5: 1

( + das ganze automatisch testbar machen )
'''

import sys
from pprint import pprint
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))

from WifiUtil import get_user_number_input

count = {} # count = dict()

while True:
    user_input = get_user_number_input(prompt = 'Bitte Zahl eingeben: ')
    if user_input == 0:
        break
    elif user_input in count:
        count[user_input] += 1
    else:
        count[user_input] = 1
        
pprint(count)        