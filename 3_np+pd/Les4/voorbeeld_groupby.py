import pandas as pd

df = pd.read_csv("belgische_bieren.csv", delimiter=";")
df2 = df[["Merk", "Productnaam", "Type", "Alcohol_percentage","Adviesverkoopsprijs (€)" ]]
# print(df2)
# mean(kolom) geeft in print-statement ook verkoopprijs
df_type_alc2 = df2.groupby(["Type"]).mean("Alcohol_percentage")
print("df_type_alc2", df_type_alc2)
print()
# kolom.mean() geeft geen verkoopsprijs in print. Wel dubbele haken nodig om kolomnaam te krijgen
df_type_alc = df2.groupby(["Type"])[["Alcohol_percentage"]].mean()
print("df_type_alc", df_type_alc)
print()

df_merk_type_alc = df.groupby(["Merk", "Type"])[["Alcohol_percentage"]].mean()
print("type: ", type(df_merk_type_alc), "size", df_merk_type_alc.size )
print(df_merk_type_alc)
# Nu eerst er een dataframe van maken (het is een vector ('Series') momenteel) om makkelijk te kunnen wegschrijven
df_res = pd.DataFrame(df_merk_type_alc)
print("type: ", type(df_res), "size", df_res.size )
df_res.to_excel("merk_type_alc.xlsx")

'''
df_merk_type_prijs = df.groupby(["Merk", "Type"])["Adviesverkoopsprijs (€)"].mean()
print(df_merk_type_prijs)
df_res = pd.DataFrame(df_merk_type_prijs)
df_res.to_excel("merk_type_prijs.xlsx")
'''