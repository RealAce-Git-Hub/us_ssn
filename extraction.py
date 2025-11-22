import pandas as pd
df = pd.read_csv('data.csv')
'''print(df)
print(df.columns)

res = df.columns

for name in res:
    print(name)

print(df.head())
print(df.describe())'''

print(df['@type'].unique())
df_new = df.drop(["@type", "conformsTo"],axis=1) 
print(df_new)

for col in df_new.columns.tolist()[:5]:
    print(col,":", df_new[col].unique())