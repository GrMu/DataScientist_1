import pandas as pd
df = pd.read_csv("data/personen.csv")
print("Oorspronkelijke lijst: ", df, "lengte: ", len(df))
df["woonplaats"]=df["woonplaats"].str.capitalize()
df_clean=df.dropna(subset=["woonplaats", "leeftijd"])
print()
print("Gefilterde lijst:", df_clean, "lengte: ", len(df_clean))
gemiddelde2 = df_clean.groupby(["woonplaats"])["leeftijd"].mean().astype(int)
print(gemiddelde2)
# Nu gemiddeldes plaatsen in de NaN
df["leeftijd"]=df["leeftijd"].fillna(gemiddelde2)
df["leeftijd"]=df["leeftijd"].astype(int)
gemiddelde_leeftijd_per_woonplaats = df.groupby(["woonplaats"])["leeftijd"].mean().round(1)
print(gemiddelde_leeftijd_per_woonplaats)
'''

