import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('data_clean.csv', encoding='latin1')

print(data)
data.plot(kind='bar', x=2, y=1)
plt.show()

