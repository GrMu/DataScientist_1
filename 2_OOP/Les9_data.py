from Les9_oop_klasses import *

p1 = Persoon(1, "Jan", 40, "Alken")
p2 = Persoon(2, "An", 52, "Genk")
d1 = Docent(1, "Jan", 40, "Genk", 3000)
d2 = Docent(2, "Piet", 40, "Aarschot", 4000)
c1 = Cursist(1, "Mark", 42, "Alken", 2021)
c2 = Cursist(2, "Marieke", 39, "As", 2023)
v1 = Cursus(1, "Engels", 200)
v2 = Cursus(2, "Frans", 200)
v3 = Cursus(3, "Wiskunde", 220)

data_personen = [d1, d2, c1, c2]
data_cursi = [v1, v2, v3]

d1.voeg_cursus_toe(v3)
print(d1)

print("Zelfde leeftijd: ", p1==p2)

print("Tel leeftijden op: ", d1+d2)
print("De maandlonen zijn opgeteld, niet de leeftijden")

print("Tel leeftijden op: ", Persoon.__add__(d1, d2))
print("Tel leeftijden op: ", d1.leeftijd + d2.leeftijd)

print("Tel leeftijden op: ", c1+d2)
print("Nu zijn de leeftijden wel opgeteld: cursist heeft geen add-methode, daardoor wordt er hoger gezocht.")

print("Tel leeftijden op: ", d1+c1)
print("Nu zijn de leeftijden niet opgeteld (error): de add-methode van Docent wordt genomen, maar dat data hiertoe ontbreekt bij Cursist.")
print("Dit is daarna opgelost via 'isinstance': eerst een controle op de klasses.")
