"""
Générez une séquence aléatoire d’ADN de 20 bases de deux manières différentes. Utilisez le module random avec la
fonction choice() ou choices().
"""
import random
bases = ["A", "T", "C", "G"]
sequence = ""
i = 0
while i < len(bases * 5):
    sequence += random.choice(bases)
    i += 1
print(f"Voici la sequence d'ADN de 20 bases: {sequence}")