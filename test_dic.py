# Test dictionary
Doktersdata= [{'voornaam': 'David', 'achternaam': 'Mertens', 'woonplaats': 'Hasselt', 'ziekenhuis': 'Ziekenhuis Genk', 'ereloon': '180', 'specialisatie': 'Gastro-enterologie'}, {'voornaam': 'Frank', 'achternaam': 'Vandenberg', 'woonplaats': 'Hasselt', 'ziekenhuis': 'Ziekenhuis Hasselt', 'ereloon': '200', 'specialisatie': 'Cardiologie'}, {'voornaam': 'Bart', 'achternaam': 'Vandenberg', 'woonplaats': 'Hasselt', 'ziekenhuis': 'Ziekenhuis Hasselt', 'ereloon': '200', 'specialisatie': 'Dermatologie'}]

def myFunc(e):
  return e['achternaam']
Doktersdata.sort(key = myFunc)
print(Doktersdata)
"""
List = [["a","b"], ["c","d"], ["e", "f"]]
print(List)
List.sort(key=[1])
print(List)
"""