import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')
'''print(df)
print(df.columns)

res = df.columns

for name in res:
    print(name)

print(df.head())
print(df.describe())'''

print(df['@type'].unique())
keys = ["@type", "conformsTo", "issued"] + ["keyword_" + str(i) for i in range(0,37)]
print(keys)
# Only drop columns that actually exist in the DataFrame to avoid KeyError
keys_to_drop = [k for k in keys if k in df.columns]
df_new = df.drop(keys_to_drop, axis=1)
print(df_new)

for col in df_new.columns.tolist()[:5]:
    print(col, ":", df_new[col].unique())

if 'issued' in df.columns:
    print(df['issued'].unique())
else:
    print("'issued' column not found in dataframe")

print(df_new["accessLevel"].unique())
print(df_new["accessLevel"].count())

for i in df_new["accessLevel"].unique():
    print(i, ":", df_new[df_new["accessLevel"] == i].shape[0])

plt.bar(["public", "non-public", "restricted"], [2589, 489, 99])
plt.show()