from tabulate import tabulate

"""
#Onevenwichtige matrix: blijkt te kunnen.
vector1 = [1,2,3]
vector2=[4,5]
matrx=[vector1,vector2]
print(matrx)
"""
"""
#Gebruik van index
lijst_namen=["Ben","Bert","Bart","Benny"]
oude_naam=input("Geef bestaande naam: ")

if oude_naam in lijst_namen:
    nieuwe_naam=input("Geef nieuwe naam: ")
    plaats = lijst_namen.index(oude_naam)
    lijst_namen[plaats]=nieuwe_naam
else:
    print("Naam is niet in lijst.")
print(lijst_namen)
"""
"""
# Meer index-bewerkingen
if oude_naam in lijst_namen:
    nieuwe_naam=input("Geef nieuwe naam: ")
    plaats = lijst_namen.index(oude_naam)
    lijst_namen.pop(plaats) #index based
    lijst_namen.insert(plaats, nieuwe_naam)
    print(lijst_namen)
    lijst_namen.remove(nieuwe_naam) #value based
else:
    print("Naam is niet in lijst.")
print(lijst_namen)
"""
# Werken met matrix (list van list) van strings waarbij met de getallen gerekend moet worden
#Bepaal totalen en gemiddelden
Klasmatrix = [["Naam", "Wiskunde", "Engels", "Sport", "Leerlingtotaal"], ["Bert", 5, 5, 5, 0], ["Bart", 6, 5, 6, 0], ["Ben", 8, 5, 8, 0] , ["Klasgemiddelde", 0, 0, 0, 0] ]
print(Klasmatrix)
# Bereken Leerlingtotalen
Aantal_leerlingen = len(Klasmatrix)-2
# De getallen in Klasmatrix hebben type 'str'. Die per rij eerst omzetten naar 'int'. Daarna de rij optellen.
j = 0
for Rij in Klasmatrix[1:]: #Sla eerste rij over
    Getalrij= []
    for Element in Rij[1:]:
        Getalrij.append(int(Element)) # Omzetting naar 'int'
    Getalrij[-1] = sum(Getalrij[:-1])
    # print(Getalrij)
    # Som plaatsen in Klassematrix als 'str'
    Klasmatrix[1+j][-1] = str(Getalrij[-1])
    j +=1
print(Klasmatrix)
# Bereken Klasgemiddelden
Kolomsom= [0]* (Aantal_leerlingen + 1)
# De getallen in Klasmatrix hebben type 'str'. Die per rij eerst omzetten naar 'int'. Daarna de per kolom optellen.
for Rij in Klasmatrix[1:]: #Sla eerste rij over
    Getalrij= []
    for Element in Rij[1:]:
        Getalrij.append(int(Element)) # Omzetting naar 'int'
    # print(f"Getalrij {Getalrij} heeft erbinnen type {type(Getalrij[0])}")
    # print(Getalrij)
    i = 0
    for kol in Getalrij:
        Kolomsom[i] += kol
        i +=1
# print(Kolomsom)
Klasgemiddelde = [x/Aantal_leerlingen for x in Kolomsom]
# print(Klasgemiddelde)
# Resultaat terugzetten als 'str' op laatste rij van Klasmatrix
i= 0
for Getal in Klasgemiddelde:
    #Klasmatrix[-1][i+1]=(str(Getal))
    Klasmatrix[-1][i + 1] = (f"{Getal:.2f}")
    #print(Klasmatrix[-1][i + 1])
    i +=1
print(Klasmatrix)

# Licht andere for-methode
# Werken met matrix (list van list) van strings waarbij met de getallen gerekend moet worden
#Bepaal totalen en gemiddelden
print("")
Klasmatrix = [["Naam", "Wiskunde", "Engels", "Sport", "Leerlingtotaal"], ["Bert", 5, 5, 5, 0], ["Bart", 6, 5, 6, 0], ["Ben", 8, 5, 8, 0] , ["Klasgemiddelde", 0, 0, 0, 0] ]
print(Klasmatrix)
# Bereken Leerlingtotalen
Aantal_leerlingen = len(Klasmatrix)-2
# De getallen in Klasmatrix hebben type 'str'. Die per rij eerst omzetten naar 'int'. Daarna de rij optellen.
for j in range(Aantal_leerlingen):
    Rij = Klasmatrix[1+j]
    Getalrij= []
    for Element in Rij[1:]:
        Getalrij.append(int(Element)) # Omzetting naar 'int'
    Getalrij[-1] = sum(Getalrij[:-1])
    # print(Getalrij)
    # Som plaatsen in Klassematrix als 'str'
    Klasmatrix[1+j][-1] = str(Getalrij[-1])
print(Klasmatrix)
# Bereken Klasgemiddelden
Kolomsom= [0]* (Aantal_leerlingen + 1)
# De getallen in Klasmatrix hebben type 'str'. Die per rij eerst omzetten naar 'int'. Daarna de per kolom optellen.
for Rij in Klasmatrix[1:]: #Sla eerste rij over
    Getalrij= []
    for Element in Rij[1:]:
        Getalrij.append(int(Element)) # Omzetting naar 'int'
    # print(f"Getalrij {Getalrij} heeft erbinnen type {type(Getalrij[0])}")
    # print(Getalrij)
    Aantal_kolommen = len(Getalrij)
    for i in range(Aantal_kolommen):
        Kolomsom[i] += Getalrij[i]
# print(Kolomsom)
Klasgemiddelde = [x/Aantal_leerlingen for x in Kolomsom]
# print(Klasgemiddelde)
# Resultaat terugzetten als 'str' op laatste rij van Klasmatrix
i= 0
for Getal in Klasgemiddelde:
    #Klasmatrix[-1][i+1]=(str(Getal))
    Klasmatrix[-1][i + 1] = (f"{Getal:.2f}")
    #print(Klasmatrix[-1][i + 1])
    i +=1
print(Klasmatrix)
