"""
# Lijst met dictionary maken
"""
# Maak een list met daarin een dictionary tolken
# Naam, leeftijd, gemeente, talen
"""
# Overbodige initialisatie
Tolken = []
Tolken = [
    {"Naam":"Bert", "Leeftijd":20, "Woonplaats":"Genk", "Talen":["Limburgs", "Nederlands", "Arabisch"]},
    {"Naam":"Bart", "Leeftijd":33, "Woonplaats":"Gent", "Talen":["Limburgs", "Nederlands", "Xhosu"]},
    {"Naam":"Berend", "Leeftijd": 26, "Woonplaats": "Bilzen", "Talen":["Limburgs", "Nederlands", "Engels"]},
    {"Naam":"Bern", "Leeftijd":30, "Woonplaats":"Alken", "Talen":["Engels", "Nederlands", "Arabisch"]},
    {"Naam":"Berend", "Leeftijd":20, "Woonplaats":"Genk", "Talen":["Limburgs", "Nederlands", "Arabisch"]}
             ]
print(Tolken)
"""
"""
def myfunc(n):
  return abs(10-n)

a = (5, 3, 1, 11, 2, 12, 17)
x = sorted(a, key=myfunc)
print(x)

import re
string ="P10"
text = "hello 42 I'm a 32 string30"
x=re.findall(r'\d+', string)
print(x)
x=re.findall(r'\d+', text)
x2=[int(y) for y in x]
print(x)
print(x2)
"""
# Doel  ["P10", "P2"] wordt  [10, 2]
import re
vector = ["P10 v15", "P2 v3"]
items =[]
items2 =[]
for item in vector:
    getal_vector = re.findall(r'\d+', item)
    for number in getal_vector:
        items.append(int(number))
print(items)
# Result: [10, 15, 2, 3]

vector = ["P10 v15", "P2 v3"]
items2 =[]
for item in vector:
    getal_vector = re.findall(r'\d+', item)
    [items2.append(int(number)) for number in getal_vector]
print(items2)
# Result: [10, 15, 2, 3]

vector = ["P10 v15", "P2 v3"]
output =[]
for item in vector:
    getal_vector = re.findall(r'\d+', item)
    [output.append(int(getal_vector[0]))]
print(output)
# Result: [10, 2]

vector = ["P10 v15", "P2 v3"]
output =[]
for item in vector:
    [output.append(int((re.findall(r'\d+', item))[0]))]
print(output)
# Result: [10, 2]

vector = ["P10 v15", "P2 v3"]
output =[]
[output.append(int((re.findall(r'\d+', item))[0])) for item in vector]
print(output)
# Result: [10, 2]

# Verhoog het grootste getal en behoud prefix
vector = ["PR10 v15", "PR2 v3"]
for i in vector[0]:
    if i.isdigit():
        break
indx = vector[0].index(i)
Prefix = vector[0][:indx]
print(Prefix)
output =[]
for item in vector:
    getal_vector = re.findall(r'\d+', item)
    [output.append(int(getal_vector[0]))]
print(output)
output.sort()
verhoogd_getal = output[-1]+1
print(verhoogd_getal, type(verhoogd_getal))
nieuwe_string = Prefix + str(verhoogd_getal)


print(nieuwe_string)


# Result: [PR10, PR2]

txt = "hoofd3110 v23 cat 444.4 2 dog"
for i in txt:
    if i.isdigit():
        break
indx=txt.index(i)
txt3 = txt[:indx]
print(txt3)
