import random
import math
xa = random.uniform(-1, 1)
ya = random.uniform(-1, 1)
# on rappelle que le centre du cercle est le point o de coordonees (xo = 0, yo = 0)
distance = math.sqrt((xa*xa)+(ya*ya))
print(f"distance = {distance}")
# Normalement ca devrait etre distance = math.sqrt(((xa*xa) - (xo*xo))+((ya*ya) - (yo*yo))) mais comme que les coordonees du point o sont nulles...
if distance <= 1:
    print(f"Comme que la distance est inferieure a 1 donc le point a de coordonnees ({xa}, {ya}) est dans le cercle")
else:
    print(f"Comme que la distance est superieure a 1 donc le point a de coordonnees ({xa}, {ya}) n'est pas dans le cercle")