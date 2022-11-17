import pandas as pd

df = pd.read_excel('DS1.xlsx')

x = df["AGE "].median()

df["AGE "].fillna(x, inplace = True)

print(df.to_string())

#Discovering duplicates

print(df.duplicated())

#Removing duplicates

df.drop_duplicates(inplace = True)

print(df.to_string())
