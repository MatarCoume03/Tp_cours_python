"""
Fréquence des acides aminés
La liste ci-dessous représente une séquence d’acides aminés :
["R", "A", "W", "W", "A", "W", "A", "R", "W", "W", "R", "A", "G"]
Calculez la fréquence des acides aminés alanine (A), arginine (R), tryptophane (W) et glycine (G) dans cette séquence.
"""
sequenceAM = ["R", "A", "W", "W", "A", "W", "A", "R", "W", "W", "R", "A", "G"]
a, r, w, g, i = 0 
for i in range(len(sequenceAM)):
    if sequenceAM[i] == 'A':
        a += 1
    elif sequenceAM[i] == 'R':
        r += 1
    elif sequenceAM[i] == 'W':
        w += 1
    elif sequenceAM[i] == 'G':
        g += 1
print(f"Dans cette séquence d’acides aminés, nous avons: {a} alanine, {r} arginine, {w} tryptophane et {g} glycine")