from WifiUtil import get_user_number_input

'''
vom Benutzer 2 Zahlen abfragen 
Dividend (Zähler) und Divisor (Nenner)
und dann das Ergennis ausgeben

+ Fehler abfangen

+ der user wird solange gefragt bis er entweder:
    + eine gültige Zahl oder 
    + q eingibt, dann wird das Programm beendet
   (+ das Beenden des Programm 
      soll nicht aus der Fkt erfolgen)

'''

try:
    dividend = get_user_number_input('Dividend: ')
    divisor  = get_user_number_input('Divisor: ')
except:
    print('user mag nicht mehr')
    exit()
    
try:
    result = dividend / divisor    
except ZeroDivisionError:
    print("Division durch 0 nicht erlaubt")
else:
    print("Quotient {0:.3f}".format(result))
   




