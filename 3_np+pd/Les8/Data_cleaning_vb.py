import pandas as pd
df = pd.read_csv("data/personen.csv")
print("Oorspronkelijke lijst: ", df, "lengte: ", len(df))
df["woonplaats"]=df["woonplaats"].str.capitalize()
'''
# Volgende is niet handig want dan neemt gemiddelde af:
df["leeftijd"]=df["leeftijd"].fillna(0)
# Stel de getallen waren 'int' dan kan 'mean' niet met 'NaN' overweg. In dat geval moet met 'isnan' eerst de 'NaN' worden weggehaald.
df["leeftijd"]=df["leeftijd"].astype(int)
gemiddelde_leeftijd_per_woonplaats = df.groupby(["woonplaats"])["leeftijd"].mean().round(1)
print(gemiddelde_leeftijd_per_woonplaats)
'''

# df["woonplaats"]=df["woonplaats"].dropna()
df_clean=df.dropna(subset=["woonplaats", "leeftijd"])
print()
print("Gefilterde lijst:", df_clean, "lengte: ", len(df_clean))
gemiddelde2 = df_clean.groupby(["woonplaats"])["leeftijd"].mean().astype(int)
print(gemiddelde2)

