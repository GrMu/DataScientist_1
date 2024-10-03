from tabulate import tabulate

Klasmatrix = [["Bert", 5, 5, 5, 0], ["Bart", 6, 5, 6, 0], ["Ben", 8, 5, 8, 0]]
Header = ["Naam", "Wiskunde", "Engels", "Sport", "Leerlingtotaal"]
Last_row = ["Klasgemiddelde", 0, 0, 0, 0]

print(Klasmatrix)
table = tabulate(Klasmatrix, headers=Header, tablefmt="grid")
print(table)

# Werken met matrix (list van list) van strings waarbij met de getallen gerekend moet worden
#Bepaal totalen en gemiddelden
print("")
# Bereken Leerlingtotalen
Aantal_leerlingen = len(Klasmatrix)
print("Aantal leerlingen: ",Aantal_leerlingen)
# De getallen in Klasmatrix hebben type 'str'. Die per rij eerst omzetten naar 'int'. Daarna de rij optellen.
for j in range(Aantal_leerlingen):
    Rij = Klasmatrix[j]
    Getalrij= []
    for Element in Rij[1:]:
        Getalrij.append(int(Element)) # Omzetting naar 'int'
    Getalrij[-1] = sum(Getalrij[:-1])
    # print(Getalrij)
    # Som plaatsen in Klassematrix als 'str'
    Klasmatrix[j][-1] = str(Getalrij[-1])
print(Klasmatrix)
# Bereken Klasgemiddelden
Kolomsom= [0]* (Aantal_leerlingen + 1)
# De getallen in Klasmatrix hebben type 'str'. Die per rij eerst omzetten naar 'int'. Daarna de per kolom optellen.
for Rij in Klasmatrix:
    Getalrij= []
    for Element in Rij[1:]:
        Getalrij.append(int(Element)) # Omzetting naar 'int'
    # print(f"Getalrij {Getalrij} heeft erbinnen type {type(Getalrij[0])}")
    # print(Getalrij)
    Aantal_kolommen = len(Getalrij)
    for i in range(Aantal_kolommen):
        Kolomsom[i] += Getalrij[i]
print("De Kolomsommen zijn: ",Kolomsom)
Klasgemiddelde = [x/Aantal_leerlingen for x in Kolomsom]
# print(Klasgemiddelde)
# Resultaat terugzetten als 'str' op laatste rij van Klasmatrix
Aantal_kolommen = len(Klasgemiddelde)
for k in range(Aantal_kolommen):
    #Klasmatrix[-1][i+1]=(str(Getal))
    Getal = Klasgemiddelde[k]
    Last_row[k + 1] = (f"{Getal:.2f}")
    #print(Klasmatrix[-1][i + 1])
print(Last_row)
Klasmatrix.append(Last_row)
table = tabulate(Klasmatrix, headers=Header, tablefmt="grid")
print(table)
table = tabulate(Klasmatrix, headers=Header, tablefmt="fancy_grid", numalign="center")
print(table)
