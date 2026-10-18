"""
En utilisant un dictionnaire, déterminez le nombre d’occurrences de chaque acide aminé dans la séquence AGWPSGGASAGLAILWGASAIM. 
Le dictionnaire ne doit contenir que les acides aminés présents dans la séquence.
Vous ne pouvez pas utiliser autant d’instructions if que d’acides aminés différents. 
Pensez au test d’appartenance.
"""
sequence = "AGWPSGGASAGLAILWGASAIM"
occ = {}
for base in sequence:
    occ[base] = occ.get(base, 0) + 1
print(occ)