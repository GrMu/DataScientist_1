"""
Proefexamen Pandas
"""

import clevercsv
import random
import pandas as pd
import matplotlib.pyplot as plt

# Read data
csv_file = "Data_in_de_praktijk_les3/shopdata.csv"
with open(csv_file, newline='') as csvfile:
    data = clevercsv.read_dataframe(csv_file)
    '''
    Schrijf code om index te ontdubbelen en van naam te voorzien
    '''
    # data.iloc[0]=["index"]
# data = pd.read_csv(csv_file)
# print(data)
# print(df)

# Make column selection and translate
columns_ = list(data.columns)
print("Existing columns: ", columns_)
Needed_columns = ['Age', 'Gender', 'Item Purchased', 'Category', 'Purchase Amount (USD)', 'Location', 'Season', 'Payment Method']
data = data[Needed_columns]
data.columns = ['Leeftijd', 'Geslacht', 'Voorwerp', 'Categorie', 'Kostprijs_(USD)', 'Staat', 'Seizoen', 'Betaalmethode']
print(data)

# DF1 hoeveel mannen en vrouwen zijn er per staat(kies er 6)
'''
Avail_states = data['Staat'].unique()
# Avail_states = Avail_states.transpose()
Avail_states = list(Avail_states)
print("Aanwezige staten: ", Avail_states)
# print("Type: Aanwezige staten: ", type(Avail_states))
num_to_select = 6
Wanted_states = random.sample(Avail_states, num_to_select)
print("Selected states: ", Wanted_states)
df_filt_states = data[data['Staat'].isin(Wanted_states)]
# print(df_filt_states)
DF1_pivot = df_filt_states.pivot_table(index='Geslacht',
                                          columns='Staat',
                                          aggfunc='size',
                                          fill_value=0)
print("Aantal mannen en vrouwen in 6 gekozen staten:")
pd.options.display.max_columns = None
print(DF1_pivot)

DF1_pivot_2 = df_filt_states.pivot_table(index='Staat',
                                          columns='Geslacht',
                                          aggfunc='size',
                                          fill_value=0)
print("Aantal mannen en vrouwen in 6 gekozen staten:")
pd.options.display.max_columns = None
print(DF1_pivot_2)

# GF1 Geef in een kolomgrafiek man/vrouw per staat
df_pivot_gender= data.pivot_table(index='Staat',
                                          columns='Geslacht',
                                          aggfunc='size',
                                          fill_value=0)
print("Aantal mannen en vrouwen in de staten:")
pd.options.display.max_columns = None
print(df_pivot_gender)

'''

# DF2 hoeveel keer zijn de categorieen (kies er 3) gekocht door mannen  tussen 20 en 40 per seizoen
'''
Avail_categories = list(data['Categorie'].unique())
# Avail_categories = list(Avail_categories)
print("Aanwezige categorieën: ", Avail_categories)
num_to_select = 3
Wanted_categories = random.sample(Avail_categories, num_to_select)
print("Selected categories: ", Wanted_categories)
df_filt_catg = data[data['Categorie'].isin(Wanted_categories)]
df_filt_catg_man = df_filt_catg[df_filt_catg['Geslacht'].isin(['Male'])]
# print(df_filt_catg_man)
# Define age categories
age_bins = [0, 20,40, float('inf')]
age_labels = ['jong', '20-39', 'ouder']
# Create age categories
df_filt_catg_man['leeftijd_categorie'] = pd.cut(df_filt_catg_man['Leeftijd'], bins=age_bins, labels=age_labels,
                                              right=False)
print(df_filt_catg_man)
df_filt_catg_man_bin = df_filt_catg_man[df_filt_catg_man['leeftijd_categorie']=='20-39']
DF2_pivot = df_filt_catg_man_bin.pivot_table(index='Categorie',
                                          columns='Seizoen',
                                          aggfunc='size',
                                          fill_value=0)
print(f"De geselecteerde categorieën zijn zo vaak gekocht door mannen per seizoen: ")
# pd.options.display.max_columns = None
print(DF2_pivot)
'''

# DF2 Tweede methode (zonder binning)
# hoeveel keer zijn de categorieen (kies er 3) gekocht door mannen  tussen 20 en 40 per seizoen
'''
Avail_categories = list(data['Categorie'].unique())
# Avail_categories = list(Avail_categories)
print("Aanwezige categorieën: ", Avail_categories)
num_to_select = 3
Wanted_categories = random.sample(Avail_categories, num_to_select)
print("Selected categories: ", Wanted_categories)
df_filt_catg = data[data['Categorie'].isin(Wanted_categories)]
df_filt_catg_man = df_filt_catg[df_filt_catg['Geslacht'].isin(['Male'])]
df_filt_catg_man = df_filt_catg[(df_filt_catg['Leeftijd']>=20) & (df_filt_catg['Leeftijd']<=40)]
DF2_pivot = df_filt_catg_man.pivot_table(index='Categorie',
                                          columns='Seizoen',
                                          aggfunc='size',
                                          fill_value=0)
print(f"De geselecteerde categorieën zijn zo vaak gekocht door mannen per seizoen: ")
# pd.options.display.max_columns = None
print(DF2_pivot)

# GF2  Geef in een kolomgrafiek seizoenen daarin per seizoen het aantal categorieën
# shadowoptions = {'ox': -0.02, 'edgecolor': 'none', 'shade': 0.1}
DF2_pivot.transpose().plot(kind='bar', figsize=(10, 9))  # , shadow=shadowoptions, autopct='%1.0f%%', explode=b, startangle=20)  # , y='Betaalmethode', figsize=(10, 6), pctdistance=1.25, labeldistance=.6
plt.title('De geselecteerde categorieën zijn zo vaak gekocht door mannen per seizoen:')
plt.xlabel('Seizoen')
plt.ylabel('Aantal')  # Remove the 'Betaalmethode' that will otherwise appear.
plt.xticks(rotation=45)
plt.legend(title='Categorie')
# plt.savefig('kleur_per_seizoen_vrouwelijke_klanten.png')
plt.show()
'''

# DF3 Hoeveel schoenen zijn er door mannen en vrouwen verkocht per seizoen

df_filt_shoes= data[data['Voorwerp']=='Shoes']
print(df_filt_shoes)
# print(df_filt_shoes)
DF3_pivot = df_filt_shoes.pivot_table(index='Geslacht',
                                          columns='Seizoen',
                                          aggfunc='size',
                                          fill_value=0)
# print(f"Schoenen zijn zo vaak gekocht door mannen en vrouwen per seizoen: ")
# pd.options.display.max_columns = None
# print("DF3_pivot, type ", DF3_pivot, type(DF3_pivot))

# GF3 geef een taart diagram per seizoen(subgrafiekenvan df 3)
figure, axes = plt.subplots(2, 2, figsize=(10, 7))
seasons = list(DF3_pivot.columns)
# first method with axes.flatten
axes = axes.flatten()  # Zo geen aparte rij- en kolomnummer nodig
for i, season in enumerate(seasons):
    DF3_pivot[season].plot(kind='pie', ax=axes[i], title=season, legend=False, labeldistance=.5, autopct='%1.1f%%', pctdistance=1.25)
    # axes[i].pie(list(DF3_pivot[season]))  # werkt ook maar geeft geen labels
    axes[i].set_ylabel(' ')  # Onderdruk een y-as-opschrift
    # plt.savefig('subplot_kleur_per_seizoen.png')
plt.show()
# second method with modulo

figure2, axes = plt.subplots(2, 2, figsize=(8, 6))
for i, season in enumerate(seasons):
    row = i // 2
    col = i % 2
    axes[row, col].pie(list(DF3_pivot[season]), labels=DF3_pivot.index, autopct='%1.1f%%')
    axes[row, col].set_title(season)
    axes[row, col].set_ylabel('Number per gender')

plt.show()


# axis[0, 0].bar(casus_reeks, output_reeks)

# DF 4: Hoeveel keer is er met elke betaalmethode betaald + taartdiagram
'''
df_group_paymeth= data.groupby('Betaalmethode')['Betaalmethode'].count()
# print(df_filt_shoes)
print(f"Zo vaak is er met elke betaalmethode betaald: ")
# pd.options.display.max_columns = None
print((df_group_paymeth))

# GF4 maak een taart diagram waarin de betaalmiddelen zijn opgenomen.
b = [0.05 for x in range(len(df_group_paymeth))]  # Slightly separate all slices
shadowoptions = {'ox': -0.02, 'edgecolor': 'none', 'shade': 0.1}
df_group_paymeth.plot(kind='pie', shadow=shadowoptions, autopct='%1.0f%%', explode=b, startangle=20)  # , y='Betaalmethode', figsize=(10, 6), pctdistance=1.25, labeldistance=.6
plt.title('Zo vaak is er met elke betaalmethode betaald')
# plt.xlabel('Kleur')
plt.ylabel(' ')  # Remove the 'Betaalmethode' that will otherwise appear.
plt.xticks(rotation=45)
# plt.legend(title='Betaalmiddel')
# plt.savefig('kleur_per_seizoen_vrouwelijke_klanten.png')
plt.show()
'''