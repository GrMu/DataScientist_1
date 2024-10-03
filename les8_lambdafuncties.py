x = lambda a: a**2+5
rechthoek = lambda b,h: b*h
Functie_1 = lambda a,b: a*2+b
Functie_2 = lambda a,b: a**2+b**2
Functie_3 = lambda a,b: (a+b)**2 #=a²+2ab+b²  (4,3) = 49
Functie_4 = lambda a:    a/3 if a%3==0 else a*2 #  Als a deelbaar is door 3, a/3 anders a*2
Functie_5 = lambda a,b: a/2 if  a > b*2 else a*2
Functie_6 = lambda a,b,c: c-(a+b) if a + b < c else a+b+c


print("Oppervlakte rechthoek", rechthoek(2,3)) # Deze regel hoort niet in dit bestand

