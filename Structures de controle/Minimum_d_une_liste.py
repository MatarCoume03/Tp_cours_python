"""
Minimum d’une liste
La fonction min() de Python renvoie l’élément le plus petit d’une liste constituée de valeurs numériques ou de chaînes
de caractères. Sans utiliser cette fonction, créez un script qui détermine le plus petit élément de la liste [8, 4, 6, 1, 5].
"""
liste = [8, 4, 6, 1, 5]
i = 0
minimum = 0
for i in range(len(liste) - 1):
    if liste[i] <= liste[i + 1]:
        minimum = liste[i]
    else:
        minimum = liste[i + 1]
print(minimum)