import pandas as pd

dag1 = "14-3-2025 14:33"
dag2 = "15-3-2025 12:00"
dag3 = "14-3-2024 16:00"
dag4 = "15-3-2024 16:00"
dag5 = "28-3-2024 16:00"
day_format = '%d-%m-%Y %H:%M'
data = { "dag_string": [dag1, dag2, dag3, dag4, dag5], "waardes": [1,2,3,4,5], "waardes2": [10,20,30,40,50]}
df_dagen = pd.DataFrame(data)
df_dagen["timestamp"]=pd.to_datetime(df_dagen["dag_string"], format=day_format)
df_dagen["weekdag"] = df_dagen["timestamp"].dt.isocalendar().day
print(df_dagen)
print(type(df_dagen))

totaal_waardes = [[0.0, 0.0] for x in [4,5,6]]
totaal_dagen = [0.0 for x in [4,5,6]]
kolommen = ["waardes", "waardes2"]
for i, value in enumerate([4,5,6]):
    for j, kolom in enumerate(kolommen):
        selectie = df_dagen[kolom][df_dagen["weekdag"]==value]
        totaal_dagen[i] = len(selectie)
        totaal_waardes[i][j] = sum(selectie)
print(totaal_dagen)
print(totaal_waardes)