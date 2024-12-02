"""# Test dictionary
Doktersdata= [{'voornaam': 'David', 'achternaam': 'Mertens', 'woonplaats': 'Hasselt', 'ziekenhuis': 'Ziekenhuis Genk', 'ereloon': '180', 'specialisatie': 'Gastro-enterologie'}, {'voornaam': 'Frank', 'achternaam': 'Vandenberg', 'woonplaats': 'Hasselt', 'ziekenhuis': 'Ziekenhuis Hasselt', 'ereloon': '200', 'specialisatie': 'Cardiologie'}, {'voornaam': 'Bart', 'achternaam': 'Vandenberg', 'woonplaats': 'Hasselt', 'ziekenhuis': 'Ziekenhuis Hasselt', 'ereloon': '200', 'specialisatie': 'Dermatologie'}]

def myFunc(e):
  return e['achternaam']
Doktersdata.sort(key = myFunc)
print(Doktersdata)
"""

import math
A = [2, 4, 6]
math.ceil(A[2])
import statistics as stat
A = [2, 4, 6]
gem = stat.mean(A)
Stdev = stat.stdev(A)
print(f"Gemiddelde: {gem} met afwijking {Stdev:.0f}")

x = 5
y = 9
print(x,"+",y,"=",x+y)
print("{} + {} = {}".format(x,y,x+y))

Getallen = [[1, 3, 4], [1, 8, 7], [2, 4, 6]]
Reeks = [getal for Row in Getallen for getal in Row]
print("Reeks: ", Reeks, "met maximum ", max(Reeks))
Max1 = max(Getallen)
print(Max1)