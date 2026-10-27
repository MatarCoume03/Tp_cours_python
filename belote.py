"""
On considère un jeu de belote avec la variante sans-atout, où chaque carte vaut un certain nombre de points quelle
que soit sa couleur (trèfle, carreau, coeur, pique). Un dictionnaire permet de mettre la correspondance entre chaque carte
et son nombre de points :
1 # Nombre de points de chaque carte.
2 # (V = valet, D = dame, R = roi, # d = 10, A = as).
3 dico_points_sans_atouts = {"7": 0, "8": 0, "9": 0, "V": 2, "D": 3, "R": 4, "d": 10, "A": 11}
Par ailleurs, on peut représenter un jeu de 32 cartes par une liste :
jeu_cartes = ["7", "8", "9", "d", "V", "D", "R", "A"] * 4
Créez un programme belote.py qui tire huit cartes au hasard sans remise et qui affiche le nombre de points
correspondant. Pour cela, vous pouvez utiliser la fonction random.sample() et son argument par mot-clé k. N’hésitez
pas à consulter la documentation 24. On souhaite une sortie de ce style :
$ python belote.py
La main est ['7', 'A', '9', 'A', 'R', 'd', 'V', 'D'].
7 --> 0 points
A --> 11 points
9 --> 0 points
A --> 11 points
R --> 4 points
d --> 10 points
V --> 2 points
D --> 3 points
Le nombre total de points de la main est 41.
"""
import random 
dico_point_sans_atout = {"7": 0, "8": 0, "9": 0, "V": 2, "D": 3, "R": 4, "d": 10, "A": 11}
jeu_cartes = ["7", "8", "9", "d", "V", "D", "R", "A"] * 4
main = random.sample(jeu_cartes, k = 8)
print(f"La main est: {main}")