#string-functies zonder dataframe
Voornaam = "Bj0rN"
Achternaam="C€liS😊🎉"
print(Voornaam[0:2], Achternaam[0:2])
print(Voornaam.lower(), Achternaam.upper())
print(Voornaam.lower().capitalize(), Achternaam.upper().capitalize())
print(Voornaam.lower().capitalize()[0:3], Achternaam.upper().capitalize()[0:3])
Naam = Voornaam + ' ' + Achternaam
print(Naam)
Gesplitst = Naam.split()
print(Gesplitst)
Voornaam_Gesplitst = Naam.split()[0]
print(Voornaam_Gesplitst)

#String-functies in dataframe
import pandas as pd
data1 = {"ID": [i+1 for i in range(4)],
         "Naam": ['heidi janssens', '  Bjorn CeliS   ', 'Piet-Jan Hendricks', ' KlaaS Van bommel']
         }
df = pd.DataFrame(data1)
df['Naam_zonder_spaties']=df['Naam'].str.strip()
df['Naam_met_hoofdletters']=df['Naam_zonder_spaties'].str.title()
df['Naam_opgesplitst'] = df['Naam_met_hoofdletters'].str.split()
df['Voornaam'] = df['Naam_opgesplitst'].str[0]
df['Achternaam'] = df['Naam_opgesplitst'].str[1:]
# df['Achternaam2'] = df['Naam_opgesplitst'].str[1:].str.cat(',')
df['Achternaam2'] = df['Achternaam'].apply(lambda x: " ".join(x) if isinstance(x, list) else x)
print(df )

