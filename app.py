import pandas as pd

ds = pd.read_csv('assets/real_estate.csv', sep=';')
print(ds.iloc[0])