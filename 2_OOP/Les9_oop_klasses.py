class Persoon:
    def __init__(self, id, naam, leeftijd, woonplaats):
        self.id = id
        self.naam = naam
        self.leeftijd = leeftijd
        self.woonplaats = woonplaats

    def __str__(self):
        return f"{self.id} {self.naam} {self.leeftijd} {self.woonplaats}"

    def __add__(self, other):  # returns int
        return self.leeftijd + other.leeftijd

    def __eq__(self, other): # boolean
        return self.leeftijd == other.leeftijd

class Docent(Persoon):
    def __init__(self, id, naam, leeftijd, woonplaats, maandloon):
        super().__init__(id, naam, leeftijd, woonplaats)
        self.maandloon = maandloon
        self.vakken = []

    def __str__(self):
        # return f"{super().__str__()} {self.maandloon} {self.vakken}"
        return f"{super().__str__()} {self.maandloon} {self.vakken}"

    def __add__(self, other):
        if isinstance(other, Docent):
            return self.maandloon + other.maandloon
        else:
            print("Geen twee docenten", "Maandloon 1ste wordt slechts genomen. ")
            return self.maandloon

    def voeg_cursus_toe(self, c):
        self.vakken.append(c)

class Cursist(Persoon):
    def __init__(self, id, naam, leeftijd, woonplaats, jaar_inschrijving):
        super().__init__(id, naam, leeftijd, woonplaats)
        self.inschrijvingsjaar = jaar_inschrijving
        self.vakken = []

    def __str__(self):
        return f"{super().__str__()} {self.inschrijvingsjaar}"

class Cursus:
    def __init__(self, id, naam, kostprijs):
        self.id = id
        self.naam = naam
        self.kostprijs = kostprijs

    def __str__(self):
        return f"{self.id} {self.naam} {self.kostprijs}"

