"""
Générez une séquence aléatoire d’ADN de 20 bases de deux manières différentes. Utilisez le module random avec la
fonction choice() ou choices().
"""
import random
bases = ["A", "T", "C", "G"]
liste = random.choices(bases, k=20)
sequence = ""
for base in liste:
    sequence += base
print(f"Voici la sequence d'ADN de 20 bases: {sequence}")