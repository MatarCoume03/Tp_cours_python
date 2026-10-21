"""
À partir de la liste de tuples suivante :
[("chien", 3), ("chat", 4), ("souris", 16)]
affichez chaque animal et son nombre en utilisant qu’une seule boucle for. Attention, pour cet exercice, il est interdit
d’utiliser l’indiçage des listes.
"""
listeTuples = [("chien", 3), ("chat", 4), ("souris", 16)]
for animal in listeTuples:
    nom, nbr = animal
    print(nom, nbr)