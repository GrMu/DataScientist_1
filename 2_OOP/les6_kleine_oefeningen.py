"""
List comprehension
* Scripten binnen een list.
* Return een list met nieuwe waarde.
* for en if binnen een list als krachtige notatie
"""
Result = [(x, x**2, x**0.5) for x in range(1, 10)]
print(Result)
Result = [(x, x**2, x**0.5) for x in range(1, 10) if x%2 == 0]
 # alleen hele getallen als x
print(Result)

Numbers = [-2, 5, -2, 3, 0, 8]
Non_negative = [x if x>=0 else abs(x) for x in Numbers]
print(Non_negative)

Matrix = [[ x*y for x in range(1, 4)] for y in range(1, 4)] # 3bij3 matrix
print(Matrix)

Fruit = ["apple", "banana", "kiwi", "cherish"]
Selection = [x for x in Fruit if "a" in x ] # moet worden: bevat a's of juist geen a's (if not)
print("Met a: ", Selection)
Selection = [x for x in Fruit if not "a" in x ] # moet worden: bevat a's of juist geen a's (if not)
print("Zonder a: ",Selection)

# map-functie
maandlonen = [100, 200, 150]
jaarlonen = [12*x for x in maandlonen]
print("jaarlonen1: ", jaarlonen)
jaarlonen = list(map(lambda x: 12*x, maandlonen))
print("jaarlonen2: ", jaarlonen)

a = [1, 2, 3]
b = [4, 5, 6]
res = map(lambda x, y: x + y, a, b)
print("Elementesgewijze vermenigvuldiging van vectoren:", list(res))

celsius = [0, 20, 37, 100]
fahrenheit = map(lambda c: (c * 9/5) + 32, celsius)
print("Van Celsius naar °F: ", list(fahrenheit))

Reeks = ["apple", "banana", "kiwi", "cherish"]
Resultaat = map(str.upper, Reeks)
print("Naar hoofdletters: ", list(Resultaat))
Resultaat2 = [x.upper() for x in Reeks ]
print("Naar hoofdletters (2e methode): ", Resultaat2)

# De list comprehension is handig voor dictionaries en JSON-bestanden
Data = { "1": {"Naam": "Jan", "Loon":2000, "Beroep": "arbeider"},
         "2": {"Naam": "Piet", "Loon":3000 , "Beroep": "bediende"},
         "3": {"Naam": "Klaas", "Loon":3200 , "Beroep": "bediende"}}
print(Data)
Hoge_lonen = [persoon for persoon in Data.values() if persoon["Loon"] > 2200]
for mw in Hoge_lonen:
    print(*mw.values()) #alles in 1 keer
    print(mw["Naam"])

"""
# Oefeningen
Reeks = [x for x in range(1,11)]
Resultaat = list(map(lambda x: x if x%3==0 else None, Reeks ))
Resultaat2 = [x for x in Resultaat if not x == None]
print("Door 3 deelbare getallen: ", Resultaat)
print("Door 3 deelbare getallen: ", Resultaat2)

Reeks = [x for x in range(1,11)]
Resultaat = list(map(lambda x: x if (x%2==0 or x%5==0) else None, Reeks ))
Resultaat2 = [x for x in Resultaat if not x == None]
print("Door 2 en 5 deelbare getallen: ", Resultaat)
print("Door 2 en 5 deelbare getallen: ", Resultaat2)

Reeks = ["apple", "banana", "kiwi", "cherish"]
Resultaat = list(map(lambda x: x if len(x)>5 else None, Reeks ))
Resultaat2 = [x for x in Resultaat if not x == None]
print("Lange woorden: ", Resultaat2)
Resultaat3 = [x for x in Reeks if len(x) > 5]
print("Lange woorden (for-methode): ", Resultaat3)
"""
