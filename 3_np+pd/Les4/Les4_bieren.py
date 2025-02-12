import pandas as pd
df_bier = pd.read_csv("belgische_bieren.csv", sep=';')
print(df_bier.head())
print(df_bier.columns)
gem_alc = df_bier["Alcohol_percentage"].mean()
max_alc = df_bier["Alcohol_percentage"].max()
print(f"Gem.alc.perc.: {gem_alc:.1f}, max. alc.perc.: {max_alc}")
df_blond = df_bier[df_bier["Type"]=="Blond"]
#print(df_blond)
gem_alc_blond = df_blond["Alcohol_percentage"].mean()
max_alc_blond = df_blond["Alcohol_percentage"].max()
print(f"Gem.alc.perc. blond: {gem_alc_blond:.1f}, max. alc.perc. blond: {max_alc_blond}")
df_bruin_zwaar = df_bier[(df_bier["Type"]=="Bruin")  & (df_bier['Alcohol_percentage'] > 7.0)]
#print(df_bruin_zwaar)
gem_prijs_bruin_zwaar = df_bruin_zwaar["Adviesverkoopsprijs (€)"].mean()
print(f"Gem.prijs zwaar bruin bier: {gem_prijs_bruin_zwaar:.2f}")
df_kriek_licht = df_bier[(df_bier["Type"]=="Kriek")  & (df_bier['Alcohol_percentage'] < 5.0)]
df_kriek_licht = df_kriek_licht.sort_values(by="Adviesverkoopsprijs (€)")
#print(df_kriek_licht.head(3))
df_bier["Literprijs"] = df_bier["Adviesverkoopsprijs (€)"]/df_bier["Inhoud (cl)"]*100
# print(df_bier["Productnaam"].head(), df_bier["Literprijs"].head())
df_bier["Literprijs_per_AlcPerc"] = df_bier["Literprijs"]/df_bier["Alcohol_percentage"]
df_bier = df_bier.sort_values(by="Literprijs_per_AlcPerc")
# print(df_bier["Productnaam"].head(3), df_bier["Literprijs_per_AlcPerc"].head(3))
resultaat_product = [x for x in df_bier["Productnaam"].head(3)]
resultaat_kost = [x for x in df_bier["Literprijs_per_AlcPerc"].head(3)]
print("De economischte bieren om drinken te worden zijn", end=" ")
for _ in resultaat_product:
    print(_, end=', ')
print(" met een literprijs per alcoholpercent van ", end=' ')
for _ in resultaat_kost:
    print(f"{_:.2f}", end=', ')
print("€/l/%abv")
Bier_statistieken = pd.DataFrame({
    "Gem. ABV br": [df_bier["Alcohol_percentage"].mean()],
    "Max. ABV br": [df_bier["Alcohol_percentage"].max()],
    "Gem. ABV zwaar bruin br": [df_bruin_zwaar["Alcohol_percentage"].mean()],
    "Max. ABV zwaar bruin br": [df_bruin_zwaar["Alcohol_percentage"].max()]
})
# Probeer df_bruin_zwaar te vervangen bij lange uitdrukking op bais van df_bier :
""""Gem. ABV zwaar bruin bier": [
    df_bier[(df_bier["Type"] == "Bruin") & (df_bier['Alcohol_percentage'] > 7.0)]["Alcohol_percentage"].mean()],
"""
pd.set_option("display.expand_frame_repr", True)
pd.set_option('display.width', 500)
pd.set_option("display.max_colwidth", 100)
print(f"Bierstatistieken: {Bier_statistieken}")
# Waarom kan opmaak niet werken ?? :
# print(f"Bierstatistieken: {Bier_statistieken:.1f}")

