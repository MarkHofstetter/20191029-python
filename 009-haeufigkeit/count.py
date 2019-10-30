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

def count_occurences(data):
    count = {}
    for d in data:
        if d in count:
            count[d] += 1
        else:
            count[d] = 1
    return count


if __name__ == '__main__':
    user_data = []
    while True:
        user_input = get_user_number_input(prompt = 'Bitte Zahl eingeben: ')
        if user_input == 0:
            break
        user_data.append(user_input)
        
    count = count_occurences(user_data)    
    pprint(count)        