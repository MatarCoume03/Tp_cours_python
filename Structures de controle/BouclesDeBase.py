"""
Boucles de base
Soit la liste ["vache", "souris", "levure", "bacterie"]. Affichez l’ensemble des éléments de cette liste (un
élément par ligne) de trois façons différentes (deux méthodes avec for et une avec while).
"""
#Affichage 1 avec la boucle for:
liste = ["Vache", "Souris", "Levure", "Bacterie"]
for element in liste:
    print(element)
print(f"{'X':X>10s}")
for i in range(0,4):
    print(f"{liste[i]}")
print(f"{'X':X>10s}")
i = 0
while i in range(0,4):
    print(f"{liste[i]}")
    i += 1