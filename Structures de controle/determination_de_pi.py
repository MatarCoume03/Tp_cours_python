import random
import math
xa = random.uniform(-1, 1)
ya = random.uniform(-1, 1)
n = 0 # Cette variable represente le nombre de points dans le cercle
n_iter = 10000 # Cette variable represente le nombre d'iteration
i = 0 # Ceci est notre compteur
while i <= n_iter:
    # on rappelle que le centre du cercle est le point o de coordonees (xo = 0, yo = 0)
    distance = math.sqrt((xa*xa)+(ya*ya)) # Normalement ca devrait etre distance = math.sqrt(((xa*xa) - (xo*xo))+((ya*ya) - (yo*yo))) mais comme que les coordonees du point o sont nulles...
    if distance <= 1:
        n += 1
    else:
        n += 0
    i += 1
rapport = n / n_iter
pi = 4 * rapport
print(f"Pour N = 100 la valeur estimee de π est de: {pi}")