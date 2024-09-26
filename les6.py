# Werken met 2D-tabel
lijst = [["k1","k2","k3","k4"],[0,1,2,3],[4,5,6,7],[8,9,10,11]]
print(lijst)
"""
for rij in lijst:
    #print(rij)
    for item in rij:
        print(item,end="\t")
    print("De som hiervan is: ",sum(rij), end=". ")
    print("De kleinste hiervan is:", min(rij), end=" ")
    print("en de grootste:", max(rij))
print(lijst[1])
print("# kolommen: ", len(lijst[1]))
print("# rijen: ", len(lijst))
"""
print(lijst[2][2])

# Optellen over de kolommen
#Methode Grietus
kolomsommen = [0] * len(lijst[0])
gemiddelden = kolomsommen
print(kolomsommen)
for kolomindex in range(len(lijst[0])):
    for rijindex in range(len(lijst)-1):
        # kolomsommen[kolomindex] = kolomsommen[kolomindex] +lijst[rijindex][kolomindex]
        kolomsommen[kolomindex] += lijst[rijindex+1][kolomindex]
print("De kolomsommen zijn:",kolomsommen)
#gemiddelden= list(kolomsommen/3)
gemiddelden= ([x/3 for x in kolomsommen])
print("De gemiddelden zijn:",gemiddelden)

#print(gemiddelden)
"""
#voeg toe aan tabel
lijst2=lijst
lijst2.append(kolomsommen)
print(lijst2)


#Methode leraar

"""

