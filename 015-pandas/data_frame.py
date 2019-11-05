import pandas as pd

df = pd.DataFrame([{'c1':10, 'c2':100}, {'c1':20, 'c2':200}, {'c1':30, 'c2':300}])

print(df) 
print(df['c1'].mean())

# zeile, spalte
print(df.iloc[0,1])

# zb nur eine Spalte mit Bezeichner
print(df.loc[:, 'c2'])

df['mean'] = df.mean(axis = 1)
print(df) 