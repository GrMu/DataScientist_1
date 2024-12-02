# Overerven
class persoon:
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def __str__(self):
        return(f"Naam: {self.naam} , met leeftijd: {self.leeftijd}")

P1 = persoon("Ben", 45)
print(P1)
output = [(k, v) for k, v in persoon.__dict__.items()]
print(output)