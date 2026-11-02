"""
Générez une séquence aléatoire d’ADN de 20 bases de deux manières différentes. Utilisez le module random avec la
fonction choice() ou choices().
"""
import random
bases = ["A", "T", "C", "G"]
sequence = ""
for i in range(0, 20):
    sequence += random.choice(bases)
print(f"Voici la sequence d'ADN de 20 bases: {sequence}")