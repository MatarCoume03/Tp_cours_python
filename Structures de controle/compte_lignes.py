import sys
if len(sys.argv) != 2:
    sys.exit("Erreur: Il faut exactement deux arguments!")
nom_fichier = sys.argv[1]
taille = 0
with open(nom_fichier, "r") as fichier:
    taille = len(fichier.readlines())
print(f"le fichier {nom_fichier} contient {taille} lignes") 