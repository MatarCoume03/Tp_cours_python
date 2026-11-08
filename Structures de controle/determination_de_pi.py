import random
import math
xa = random.uniform(-1, 1)
ya = random.uniform(-1, 1)
# on rappelle que le centre du cercle est le point o de coordonees (xo = 0, yo = 0)
distance = math.sqrt((xa*xa)+(ya*ya))
# Normalement ca devrait etre distance = math.sqrt(((xa*xa) - (xo*xo))+((ya*ya) - (yo*yo))) mais comme que les coordonees du point o sont nulles...