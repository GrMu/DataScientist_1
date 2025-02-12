import openpyxl
import pandas as pd
#df_muziek = pd.read_csv("muzikanten.csv")
df_muziek = pd.read_excel("muzikanten_data.xlsx")
#print(df_muziek)
df_muziek.columns = df_muziek.columns.str.upper()
df_muziek["INSTRUMENT"] = df_muziek["INSTRUMENT"].str.lower()
#print(df_muziek)
df_jazz = df_muziek[df_muziek["GENRE"]=="Jazz"]
#print(df_jazz)
gemiddelde_prijs = df_jazz["PRIJS_PER_AVOND"].mean()
#print(f"gemiddelde_prijs Jazz : {gemiddelde_prijs:.2f}")
df_piano =  df_muziek[df_muziek["INSTRUMENT"]=="piano"]
gemiddelde_prijs = df_piano["PRIJS_PER_AVOND"].mean()
print(f"gemiddelde_prijs piano : {gemiddelde_prijs:.2f}")
df_piano = df_piano.sort_values(by="PRIJS_PER_AVOND")
df_piano.rename(columns={"PRIJS_PER_AVOND":"AVONDPRIJS"}, inplace=True)
print(df_piano.head())
piano_opgeschoond = df_piano[["ARTIESTENNAAM", "INSTRUMENT", "GENRE"]]
print(piano_opgeschoond.head())