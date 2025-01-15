import pandas as pd
'''
data = [5,9,2,1,7,5,2]
x=pd.Series(data)
print(x)
data2 = { "min": [2,4,6,3,4,2], "max": [7,8,10,5,11,4]}
df = pd.DataFrame(data2)
print(df)
data3 = { "Naam": ["Alex", "Max", "Pauline"], "km": [8,4,11], "Tijd": [55,70,64]}
df3 = pd.DataFrame(data3)
print(df3)
'''
data4=pd.read_csv("Les1+2/muzikanten_data.csv")
# print(data4)
# data4.to_excel("Les1+2/muzikanten_data.xlsx")
# data4.to_json("Les1+2/muzikanten_data.json")
# print(data4.describe())
# Inhoud bestand: id,artiestennaam,instrument,genre,prijs_per_avond
df_naam_instr = data4[["artiestennaam", "instrument", "prijs_per_avond"]]  # Meerdere velden, meerdere vierkante haken!
# del data4
# print(df_naam_instr)
print(data4.shape)
# print(data4.tail(10)) # laatste 10
# print(data4.head(10)) # Eerste 1O
instr = data4["instrument"].value_counts() # Geeft lijst van instrumenten en hoe vaak die voorkomen
print(instr)
