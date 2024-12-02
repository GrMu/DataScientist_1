"""persoon_orig = {"Naam":"Jan", "Leeftijd":26}
"""
class persoon_leeg:
    pass

p = persoon_leeg()
print(type(p))
p.naam = "Piet"
print(p.naam)
"""
class persoon:
    student_van = "Syntra"
    # Constructor met eigenschappen: naam, leeftijd, hobby
    def __init__(self, naam, leeftijd, hobby):
        self.naam = naam
        self.leeftijd = leeftijd
        self.hobby = hobby

    def stel_voor(self):
        print(f"ik ben {self.naam} en ik ben {self.leeftijd} jaar oud. "
              f"en mijn hobby is {self.hobby}")

    def voeg_woonplaats_toe(self, woonplaats):
        self.woonplaats = woonplaats

    def maak_email(self, email):
        self.email = naam + ".student@python.org"

    def __str__(self):
        return (f"ik ben {self.naam} en ik ben {self.leeftijd} jaar oud. "
              f"en mijn hobby is {self.hobby}")
p = persoon("Bjorn", 33, "voetballen")
p2 = persoon("Derik", 22, "voetballen")
print(p)
p.hobby = "Ballet"
print(p)
p.voeg_woonplaats_toe("Bilzen")
print(p.woonplaats)
print(p)    #instantie
print(persoon.__str__(p)) # vanuit de klasse persoon met p als parameter
print(p.student_van)
print(p2.student_van)
print(p2)

class werknemer:
    # klasse-variabelen: hetzelfde voor elke instantie van werknemer
    opslag = 1.05
    aantal_wn = 0
    def __init__(self, naam, loon):
        self.naam = naam
        self.loon = loon
        werknemer.aantal_wn += 1
    def geef_opslag(self):
        self.loon *= werknemer.opslag
w = werknemer("Bert", 3000)
w2 = werknemer("Bart", 1600)

print(w.loon)
w.geef_opslag()
print(w.loon)
werknemer.opslag =1.10
w.geef_opslag()
print(w.loon)
print("# werknemers: ", werknemer.aantal_wn)
dwn = w.__dict__
print(dwn)
for k,v in dwn.items():
    print(k,v)
"""