"""
Générez une séquence aléatoire de six chiffres, ceux-ci étant des entiers tirés entre 1 et 4. 
Utilisez le module random avec la fonction randint().
Consultez pour cela la documentation 23 de la fonction random.randint().
"""
import random
sequence = ""
cpt = 1
while cpt <= 6:
    sequence += str(random.randint(1, 4))
    cpt += 1
print(sequence)