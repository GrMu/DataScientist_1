"""
Examen Pandas met data-opschonen en plotten
"""

import clevercsv
import pandas as pd
import matplotlib.pyplot as plt

"""
1.	Lees de dataset shopdata in
"""
csv_file = "Data_in_de_praktijk_les3/shopdata.csv"
with open(csv_file, newline='') as csvfile:
    data = clevercsv.read_dataframe(csv_file)

"""
2.	Behoud de kolommen Customer ID,Age,Gender,Item Purchased,Category,Color,Season,
            Payment Method,Frequency of Purchases
"""
columns_ = list(data.columns)
print("Existing columns: ", columns_)
Needed_columns = ['Customer ID','Age','Gender','Item Purchased','Category','Color','Season','Payment Method', \
                  'Frequency of Purchases']
data = data[Needed_columns]

"""
3. Geef de kolommen de volgende nieuwe namen: id,leeftijd,geslacht, gekocht_item,categorie, kleur, \ 
        seizoen, betaalmethode, frequentie.
"""
data.columns = ['ID', 'Leeftijd', 'Geslacht', 'Gekocht item', 'Categorie', 'Kleur', 'Seizoen', \
                'Betaalmethode', 'Frequentie']
print(data)

"""
4.	Verander het geslacht female naar vrouw, male naar man.
"""
data['Geslacht'] = ['vrouw' if person=='Female' else 'man' for person in data['Geslacht'] ]
print(data)

"""
Grafiek 1.	Hoeveel keer zijn de kleuren( “blue,red,black,beige,white’) per seizoen verkocht voor de mannen.
"""

nodige_kleuren = ['blue','red','black','beige','white']
data_subset= data[['Geslacht', 'Kleur', 'Seizoen']]
data_subset= data_subset[data_subset['Geslacht']=='man']
data_subset= data_subset[data_subset['Kleur'].str.lower().isin(nodige_kleuren)]
print(data_subset)
GF1_pivot = data_subset.pivot_table(index='Kleur',
                                          columns='Seizoen',
                                          aggfunc='size',
                                          fill_value=0)
print("Het verkochte aantal kleuren ( 'blue,red,black,beige,white’) per seizoen door mannen:")
pd.options.display.max_columns = None
print(GF1_pivot)
# maak de grafiek
colors = ['beige','black','blue','red','grey']
GF1_pivot.transpose().plot(kind='bar', color=colors, figsize=(10, 9))
plt.title("Het verkochte aantal kleuren ( 'blue,red,black,beige,white') per seizoen door mannen:")
plt.xlabel('Seizoen')
plt.ylabel('Aantal')  # Remove the 'Betaalmethode' that will otherwise appear.
plt.xticks(rotation=45)
plt.legend(title='Kleur')
# plt.savefig('grafiek1.png')
plt.show()


"""
Grafiek 2.	Wat is de verdeling van de kleuren(blue,red,black,white) bij vrouwen tussen de 30 en 50.
"""

nodige_kleuren2 = ['black','blue','red','white']
data_subset2= data[['Geslacht', 'Kleur', 'Leeftijd']]
data_subset2= data_subset2[data_subset2['Geslacht']=='vrouw']
data_subset2= data_subset2[data_subset2['Kleur'].str.lower().isin(nodige_kleuren2)]
data_subset2 = data_subset2[(data_subset2['Leeftijd']>=30) & (data_subset2['Leeftijd']<=50)]
print(data_subset2)
# Groeperen
data_subset2_groepsgewijs=data_subset2.groupby('Kleur').count()
print(data_subset2_groepsgewijs)
# maak de grafiek
explosie=[0.05 for _ in range(len(data_subset2_groepsgewijs))]
shadowoptions = {'ox': -0.02, 'edgecolor': 'none', 'shade': 0.1}
plt.figure(figsize=(8,8))
plt.pie(
    x=data_subset2_groepsgewijs['Geslacht'], labels=nodige_kleuren2,
    colors=nodige_kleuren2,
    shadow=shadowoptions, autopct='%1.0f%%', explode=explosie, startangle=20
    )
plt.title("Het verkochte aantal kleuren ( 'blue,red,black,white') door middelbare vrouwen:")
plt.ylabel('Aantal')
# plt.savefig('grafiek2.png')
plt.show()


"""
3.	Hoeveel mannen en vrouwen kopen wekelijks in de zomer. 
    Verdeel dit per leeftijdscategorie (20-40,41-60,60+) 
    2 Subgrafieken (1 kolomdiagram(mannen), 1 kolomdiagram(vrouwen)
"""
data_subset3= data[['Geslacht', 'Seizoen', 'Frequentie', 'Leeftijd']]
data_subset3= data_subset3[data_subset3['Seizoen']=='Summer']
data_subset3= data_subset3[data_subset3['Frequentie'].str.lower().isin(['weekly'])]
data_subset3= data_subset3[data_subset3['Leeftijd']>=20]
print(data_subset3)
age_bins = [0, 40, 60, float('inf')]
age_labels = ['20-40', '41-60', '60+']
# Create age categories
data_subset3['Leeftijdscategorie'] = pd.cut(data_subset3['Leeftijd'], bins=age_bins, labels=age_labels,
                                              right=False)
print(data_subset3)
# Groepeer de data
GF3_pivot = data_subset3.pivot_table(index='Leeftijdscategorie',
                                          columns='Geslacht',
                                          aggfunc='size',
                                          fill_value=0)
print("Het aantal mensen dat wekelijks aankoopt in de zomer:")
pd.options.display.max_columns = None
print(GF3_pivot)
# maak de grafiek
figure, axes = plt.subplots(1,2,  figsize=(8, 6))
axes = axes.flatten()
geslachten= list(data_subset3['Geslacht'].unique())
for i, item in enumerate(geslachten):
    GF3_pivot[item].plot(kind='bar', ax=axes[i],
                         title=f"Aantal {item}en dat wekelijks koopt in de zomer")
plt.tight_layout()
# plt.savefig('grafiek3.png')
plt.show()

