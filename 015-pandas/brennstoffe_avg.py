import pandas as pd

data = pd.read_csv('data_clean.csv', encoding='latin1')
data['mean'] = data.mean(axis = 1, skipna = True)
data.rename(columns={'Nettopreis': 'Brennstoffart'}, inplace=True)
# print(data.loc[:, ['Brennstoffart','mean']])

for index, row in data.iterrows():
    print(index, row['Brennstoffart'], row['mean'])