from cleaning import df_filtered
import pandas as pd

def aantal_per_categorie():
    # Count the occurrences of each category
    categorie_tellingen = df_filtered['categorie'].value_counts()
    print(categorie_tellingen)

def aantal_kleur_per_seizoen():
    pivot_table = df_filtered.pivot_table(index='kleur',
                                          columns='seizoen',
                                          aggfunc='size',
                                          fill_value=0)
    print(pivot_table)

def aantal_kleur_per_seizoen_vrouw():
    # Filter for female customers
    df_female = df_filtered[df_filtered['geslacht'] == 'Female']

    # Create a pivot table: colors as rows, seasons as columns
    pivot_table_female = df_female.pivot_table(index='kleur', columns='seizoen', aggfunc='size', fill_value=0)
    print(pivot_table_female)

def filter_op_kleur():
    # Filter for female customers
    df_female = df_filtered[df_filtered['geslacht'] == 'Female']

    # Create a pivot table: colors as rows, seasons as columns
    pivot_table_female = df_female.pivot_table(index='kleur', columns='seizoen', aggfunc='size', fill_value=0)

    # Filter the pivot table to include only the specified colors
    filtered_colors = ['Blue', 'Red', 'Black', 'Beige', 'Brown', 'White']
    pivot_table_filtered = pivot_table_female.loc[filtered_colors]

    return pivot_table_filtered

def kleuren_man_leeftijd():
    df_male = df_filtered[df_filtered['geslacht'] == 'Male']

    # Filter for specific colors
    df_male_colors = df_male[df_male['kleur'].isin(['Black', 'Blue', 'White'])]

    # Define age categories
    age_bins = [20, 30, 40, 50, 60, float('inf')]
    age_labels = ['20-29', '30-39', '40-49', '50-59', '60+']

    # Create age categories
    df_male_colors['leeftijd_categorie'] = pd.cut(df_male_colors['leeftijd'], bins=age_bins, labels=age_labels,
                                                  right=False)

    # Create a pivot table with age categories as rows and colors as columns
    pivot_table_male = df_male_colors.pivot_table(index='leeftijd_categorie', columns='kleur', aggfunc='size',
                                                  fill_value=0)

    return(pivot_table_male)

def grafiek_kleur_per_man_per_leeftijdscategorie():
    hulp = kleuren_man_leeftijd()
    df_kleur_man_lft.plot(kind='pie', figsize='40x40')


print("aantal_per_categorie\n")
aantal_per_categorie()
print()
print("aantal_per kleur_per_seizoen\n")
aantal_kleur_per_seizoen()
print()
print("aantal_per kleur_per_seizoen_voor _vrouwen\n")
aantal_kleur_per_seizoen_vrouw()
print()
print("Filter op enkele kleuren")
hulp = filter_op_kleur()
print(hulp)
print()
print("Kleuren voor mannen")
hulp = kleuren_man_leeftijd()
print(hulp)
print()
print("Grafiek\n")
grafiek_kleur_per_man_per_leeftijdscategorie()
print()

