"""
Créez un script dna_random.py qui prend comme argument un nombre de bases, construit une séquence aléatoire
d’ADN dont la longueur est le nombre de bases fourni en argument, puis affiche cette séquence.
Le script devra vérifier qu’un argument est bien fourni et renvoyer un message d’erreur si ce n’est pas le cas.
"""
import sys
import random
bases = ["A", "T", "C", "G"]
sequence = ""
if len(sys.argv) == 2:
    for i in range(0, int(sys.argv[1])):
        sequence += random.choice(bases)
else:
    sys.exit("Vous n'avez pas fourni d'argument pour la longueur de la Sequence d'ADN")
print(sequence)