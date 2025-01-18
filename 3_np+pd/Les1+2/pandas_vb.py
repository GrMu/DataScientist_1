import pandas as pd
"""
data = pd.read_csv("muzikanten_data.csv")
df_naam_instr = data[["artiestennaam","instrument"]]
del data
print(df_naam_instr)
print("")"""

"""data = pd.read_csv("muzikanten_data.csv")
data = data[["artiestennaam","instrument"]]
print(data)
print("")
"""
data = pd.read_csv("muzikanten_data.csv")
print(data.shape)
print(data.tail(10))#laatste 10
print(data.head(10))#eerste 10
print(data["genre"].value_counts())


