import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('data_clean.csv', encoding='latin1')

print(data)
# data.plot(kind='bar', x=2, y=1)
# plt.show()

print(data['2004'])

print(data.iloc[1])

# print(data.iloc[1].mean())
data['mean'] = data.mean(axis = 1)
print(data)
