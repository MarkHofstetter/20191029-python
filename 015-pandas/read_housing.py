import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


data = pd.read_csv("housing.csv") 
# data ist ein pandas dataframe
print(data.head())

# data.info()
print(data.describe())
print(data['population'].mean())

print(data['ocean_proximity'].value_counts())
# data.hist(bins=50, figsize=(20,15))
# plt.show()