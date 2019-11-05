import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

'''
durchschnittlichen Brennstoffpreis über die Jahre
'''

with open('data_clean.csv') as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    data = list(lines)

for row in data[1:]:
    row_float = [float(x) for x in row[1:]]
    print("{:40s} {:6.2f}".format(row[0], np.mean(row_float)))
    plt.plot(data[0][1:], row_float, label = row[0])    
    
    # plt.plot(data[0][1:], row[1:])    
    
plt.xlabel('Jahr')
plt.ylabel('Brennstoff')
plt.legend()
plt.savefig('brennstoffe.png')

    
