import pandas as pd

# Aanmaken van de DataFrame met de punten
gegevens = {
    "Leerling": ["Jan", "Piet", "An", "Sofie"],
    "Wiskunde": [78, 85, 90, 88],
    "IT": [92, 81, 76, 95],
    "Frans": [65, 72, 80, 78],
    "Nederlands": [74, 69, 88, 91],
    "Engels": [80, 85, 83, 87]
}

df = pd.DataFrame(gegevens)

# Berekenen van totaal en gemiddelde per leerling
df["Totaal"] = df.iloc[:, 1:].sum(axis=1)
df["Gemiddelde"] = df.iloc[:, 1:-1].mean(axis=1)

# Berekenen van statistieken per vak
statistieken = df.iloc[:, 1:-2].agg(["mean", "min", "max","count","sum"])

# Resultaten weergeven
print("Punten per leerling met totaal en gemiddelde:")
print(df)
print("\nStatistieken per vak:")
print(statistieken)
