import pandas as pd

df = pd.read_csv("voorbeeld_transpose.csv")
print(df)
# Onderstaande laat de oorspronkelijke index in stand
df2 = df.T
print(df2)
df3 = df2.copy()
#df3 = df2.reset_index(drop=True)
df3.columns = df3.iloc[0]
df3 = df3[1:].reset_index(drop=True)
print(df3)
#print zinder index te tonen
print(df3.to_string(index=False))

