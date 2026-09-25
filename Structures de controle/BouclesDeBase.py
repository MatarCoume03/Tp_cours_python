"""
Boucles de base
Soit la liste ["vache", "souris", "levure", "bacterie"]. Affichez l’ensemble des éléments de cette liste (un
élément par ligne) de trois façons différentes (deux méthodes avec for et une avec while).
"""
#Affichage 1 avec la boucle for:
liste = ["Vache", "Souris", "Levure", "Bacterie"]
for element in liste:
    print(element)
print(f"{'-':->10s}")
for i in range(0,4):
    print(f"{liste[i]}")