import pandas as pd

df = pd.read_csv('partners.csv', usecols=['partner'])
dups = df.groupby(df.columns.tolist()).size().reset_index().rename(columns={0:'count'})
print(dups)