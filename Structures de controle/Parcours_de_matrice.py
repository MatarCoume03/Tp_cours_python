"""
 Parcours de matrice
Imaginons que l’on souhaite parcourir tous les éléments d’une matrice carrée, c’est-à-dire d’une matrice qui est
constituée d’autant de lignes que de colonnes.
Créez un script qui parcourt chaque élément de la matrice et qui affiche le numéro de ligne et de colonne uniquement
avec des boucles for.
Pour une matrice de dimensions 2 × 2, le schéma de la figure 5.1 vous indique comment parcourir une telle matrice.
L’affichage attendu est :
ligne colonne
  1     1
  1     2
  2     1
  2     2
Attention à bien respecter l’alignement des chiffres qui doit être justifié à droite sur 4 caractères. Testez avec une
matrice de dimensions 3 × 3, puis 5 × 5, et enfin 10 × 10.
Créez une seconde version de votre script, cette fois-ci avec deux boucles while.
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
    while colonne < len(matriceCarree[ligne]):
        print(f"  {ligne + 1}         {matriceCarree[ligne][colonne]}")
        colonne += 1
    ligne += 1
    