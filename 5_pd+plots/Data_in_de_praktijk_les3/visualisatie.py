from analyse import filter_op_kleur,kleuren_man_leeftijd
import matplotlib.pyplot as plt
#Load df filter from analyse
df_kleur_seizoen = filter_op_kleur()
df_kleur_man_lft = kleuren_man_leeftijd()

def grafiek_kleur_per_seizoen():
    df_kleur_seizoen.plot(kind='bar', figsize=(10, 6))
    plt.title('Frequentie van Kleuren per Seizoen voor Vrouwelijke Klanten')
    plt.xlabel('Kleur')
    plt.ylabel('Frequentie')
    plt.xticks(rotation=45)
    plt.legend(title='Seizoen')
    plt.tight_layout()

    # Save the plot as an image file
    plt.savefig('kleur_per_seizoen_vrouwelijke_klanten.png')

    # Show the plot
    plt.show()

def grafiek_kleur_per_man_leeftijd():
    df_kleur_man_lft.plot(kind='bar', figsize=(10, 6))
    plt.title('Frequentie van Kleuren per leeftijd voor mannelijke Klanten')
    plt.xlabel('Kleur')
    plt.ylabel('Frequentie')
    plt.xticks(rotation=45)
    plt.legend(title='Kleur_per_leeftijd')
    plt.tight_layout()

    # Save the plot as an image file
    plt.savefig('kleur_per_leeftijd_mannelijke_klanten.png')

    # Show the plot
    plt.show()


def grafiek_kleur_per_seizoen_subplot():
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    colors = ['Blue', 'Red', 'Black', 'Beige', 'Brown', 'White']

    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    axes = axes.flatten()

    for i, season in enumerate(seasons):
        df_kleur_seizoen[season].loc[colors].plot(kind='bar', ax=axes[i], title=season, legend=False)
        axes[i].set_ylabel('Number of Female Customers')
        axes[i].set_xlabel('Color')

    plt.tight_layout()

    plt.savefig('subplot_kleur_per_seizoen.png')
    plt.show()



