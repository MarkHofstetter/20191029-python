import csv
from pprint import pprint

with open('daten.csv') as csvfile:
    lines = csv.reader(csvfile, delimiter = ';')
    data = list(lines)

'''
['Preise in EUR', '', '', '', '', '', '', '', '', '', '', '', '', '']
['Nettopreis', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
[' Steinkohle (Industrie)/t ', '76,34', '85,69', '91,58', '88,36', '95,95', '117,96', '122,62', '105,14', '126,79', '142,83', '143,84', '105,09', '103,07']
[' Naturgas (Haushalte)/kWh ', '0,034', '0,034', '0,036', '0,039', '0,043', '0,044', '0,048', '0,045', '0,05', '0,053', '0,052', '0,052', '0,058']
'''
    
data_clean = [data[1]]    
for line in data[2:]:    
    row = []
    row.append(line[0].strip())
    for col in line[1:]:
       row.append(float(col.replace(',', '.')))
    data_clean.append(row)       
    # print(line)
    '''
    row = []
    row.append(line[0].strip())    
    row.append([float(col.replace(',', '.')) for col in line[1:] ] )       
    data_clean.append(row)       
    '''

with open('data_clean.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ',', 
                          quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for row in data_clean:
        csvwriter.writerow(row)
    
