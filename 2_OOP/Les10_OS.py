import os

#os.mkdir("c:/Temp/test") # forward shlashes
p="Jan"
# os.mkdir(f"c:/Temp/test/{p}")

try: os.remove(f"c:/Temp/test/{p}/testje.txt")
except: print("Bestand bestaat niet")


os.rmdir(f"c:/Temp/test/{p}")
os.rmdir()

