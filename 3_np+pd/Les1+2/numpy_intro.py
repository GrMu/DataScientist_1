import numpy as np


arr = np.array([1,3,5,7,5,6])
data = [7,5,3,9,4,2]
arr2 = np.array(data)
print(arr)
print(arr2*arr)#som van de 2 lijsten
print(type(arr))
l1 = [4,5,9]
l2 = [6,5,1]
#lijsten worden samengevoegd
print(l1+l2)

arrd0 = np.array(45)
arrd1 = np.array([4,5,9,8])
arrd2 = np.array([[6,3,6],[5,2,6],[6,2,1]])
arrd3 = np.array([[[2,5,6],[3,8,3]],[[5,5,9],[9,6,3]]])
print(arrd3)
print(arrd0.ndim)

print(arrd3[1,0:2])

print(arrd3[-1,0]*1.5)

org_lijst = np.array([1,2,3,4,5,6,7,8,9])
nieuw = org_lijst.reshape(1,9)#hervorm 1 rij van 9 kolomen
nieuw = org_lijst.reshape(3,3)#hervorm 3 rijen van 3 kolomen
print(nieuw)
for rij in nieuw:
    for item in rij:
        print(item,end="\t")
    print("")