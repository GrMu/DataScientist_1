import numpy as np

# Oorspronkelijke rechthoek
rechthoek = [[1, 2], [2, 5]]  # Oorsprong en x, y-coördinaat
schaal = 1.5

# Bereken de lengte en breedte
lengte = rechthoek[1][0] - rechthoek[0][0]
breedte = rechthoek[1][1] - rechthoek[0][1]

# Schaal de lengte en breedte
nieuwe_lengte = lengte * schaal
nieuwe_breedte = breedte * schaal

# Bereken de nieuwe rechterbovenhoek
nieuwe_rechterbovenhoek = [rechthoek[0][0] + nieuwe_lengte, rechthoek[0][1] + nieuwe_breedte]

# Nieuwe rechthoek
nieuwe_rechthoek = [rechthoek[0], nieuwe_rechterbovenhoek]

# Bereken de oppervlakte
oude_oppervlakte = lengte * breedte
oppervlakte = nieuwe_lengte * nieuwe_breedte

print("Geschaalde rechthoek:")
print(f"Linkerbenedenhoek: {nieuwe_rechthoek[0]}")
print(f"Rechterbovenhoek: {nieuwe_rechthoek[1]}")
print(f"Oude oppervlakte: lengte {lengte} x breedte {breedte} = {oude_oppervlakte}")
print(f"Nieuwe oppervlakte: lengte {nieuwe_lengte} x breedte {nieuwe_breedte} = {oppervlakte}")