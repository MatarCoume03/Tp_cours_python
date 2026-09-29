"""
Parcours de demi-matrice sans la diagonale (exercice ++)
En se basant sur le script précédent, on souhaite réaliser le parcours d’une demi-matrice carrée sans la diagonale. On
peut noter que cela produit tous les couples possibles une seule fois (1 et 2 est équivalent à 2 et 1), en excluant par
ailleurs chaque élément avec lui même (1 et 1, 2 et 2, etc). Pour mieux comprendre ce qui est demandé, la figure 5.2
indique les cases à parcourir en gris :
Créez un script qui affiche le numéro de ligne et de colonne, puis la taille de la matrice N ×N et le nombre total de
cases parcourues.
"""
matriceCarree = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    
]
print("Ligne    Colonne")
ligne = 0
while ligne < len(matriceCarree):
    colonne = 0
    while colonne < len(matriceCarree[ligne]) and colonne != ligne:
        print(f"  {ligne + 1}         {matriceCarree[ligne][colonne]}")
        colonne += 1
    ligne += 1
print(f"Pour une marice 10X10, on a parcouru {ligne*colonne/2} cases")