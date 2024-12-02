"""
import les8_lambdafuncties as l8
print("Oppervlakte",l8.rechthoek(2,5))
print("Parabool",l8.x(3))
print("Functie_1 met",4,"en",2, "geeft", l8.Functie_1(4,2))
print("Functie_2 met",5,"en",3, "geeft", l8.Functie_2(5,3))
print("Functie_3 met",4,"en",3, "geeft", l8.Functie_3(4,3))
print("Functie_4 met",6, "geeft", l8.Functie_4(6))
print("Functie_4 met",7, "geeft", l8.Functie_4(7))
print("Functie_5 met",9, "en", 12, "geeft", l8.Functie_5(9,12)) #Als a > b*2 dan a/2 anders a*2
print("Functie_5 met",9, "en", 3, "geeft", l8.Functie_5(9,3))
print("Functie_6 met",3,",",4, "en", 3, "geeft", l8.Functie_6(3,4,3)) # als a + b kleiner is c dan c-(a+b) anders a+b+c
print("Functie_6 met",3,",",4, "en", 10, "geeft", l8.Functie_6(3,4,10)) # als a + b kleiner is c dan c-(a+b) anders a+b+c

Cijfers= [5,8,10]
for i, Cijfer in enumerate(Cijfers):
    print("i", i, "cijfer", Cijfer)
"""
"""
x= 10
for i in range(1,5):
    if (((x-i)%4))==0:
        print("in lijst",i,"komt",(x))
"""
# Functie dat getallen genereert en verdeelt over 4 lijsten
import random
lijstmatrix = [[] for _ in range(4)]
print(lijstmatrix)
for i in range(1,21):
    willekeur=random.randint(10,200)
    for lijst in range(1,5): # lijsten 1 tot en met 4
        if ((willekeur-lijst)%4)==0:
            lijstmatrix[lijst-1].append(willekeur)
print(lijstmatrix)
for k in range(len(lijstmatrix)):
    lijstmatrix[k].sort()
print(lijstmatrix)
"""
## List of lists vullen met programmeerbare lengtes
#Test dat invoegen mogelijk is
Onevenwichtige_lijst = [[1,2],[2,3,4],[],[5]]
print(Onevenwichtige_lijst)
Onevenwichtige_lijst[1].append(6)
Onevenwichtige_lijst[2].append(7)
Onevenwichtige_lijst[1].insert(2,8)
print(Onevenwichtige_lijst)
#
"""
"""
Lijst = [[],]*5
print(Lijst)
Lijst[3].append(6)
Lijst[4].append(7)
print(Lijst)

#
#Lijst = [[]] * 5  #maakt 5 keer link naar eenzelfde geheugen locatie
Lijst = [[] for i in range(5)]
print(Lijst)
Lijst[3].append(6)
Lijst[4].append(7)
print(Lijst)
"""
