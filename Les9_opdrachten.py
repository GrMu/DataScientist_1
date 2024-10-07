# Methode 1: lijst met daarin een dictionary
Woordenboek=[{"Engels woord":"if", "Nederlands woord":"als"},  {"Engels woord":"then", "Nederlands woord":"dan"}, \
    {"Engels woord":"else", "Nederlands woord":"anders"}, {"Engels woord":"for", "Nederlands woord":"voor"}]
print(Woordenboek)
Zoek = "then"
print("Het woord '", Zoek, "' wordt gezocht")
for item in Woordenboek:
    if item["Engels woord"]==Zoek:
        print("Nederlands woord is:", item["Nederlands woord"])

# Methode 2: dictionary met 10 woorden
Woordenboek2 = {"if":"als", "else":"anders",
                "then":"dan", "for":"voor", "more":"more"}
print(Woordenboek2)
Zoek2= "else"
print("Het woord '", Zoek2, "' wordt gezocht")
for Key, Val in Woordenboek2.items():
    if Key == Zoek2:
        print("Nederlands woord is:", Val)



