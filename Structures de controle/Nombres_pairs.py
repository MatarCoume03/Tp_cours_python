"""
Nombres pairs
Construisez une boucle qui parcourt les nombres de 0 à 20 et qui affiche les nombres pairs inférieurs ou égaux à 10
d’une part, et les nombres impairs strictement supérieurs à 10 d’autre part.
"""
nombresPairs = []
nombresImpairs = []
for i in range(0, 21):
    if (i % 2) == 0 and i <= 10:
        nombresPairs.append(i)
    elif (i % 2) != 0 and i > 10:
        nombresImpairs.append(i)
print(f"Voici la liste des nombres pairs etant inferieurs ou egaux a 10: \n{nombresPairs}")
print(f"Voici la liste des nombres impairs etant strictement superieurs a 10: \n{nombresImpairs}") 