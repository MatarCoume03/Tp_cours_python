"""
Améliorez le script compte_lignes.py, dont le code a été donné précédemment, de façon à ce qu’il renvoie un
message d’erreur si le fichier n’existe pas.
Par exemple, si les fichiers animaux1.txt et animaux2.txt sont bien dans le répertoire courant, mais pas animaux3.txt :
$ python compte_lignes.py animaux1.txt
animaux1.txt contient 4 lignes.
$ python compte_lignes.py animaux2.txt
animaux2.txt contient 3 lignes.
$ python compte_lignes.py animaux3.txt
ERREUR : animaux3.txt n'existe pas."""
import sys
from pathlib import Path
if len(sys.argv) == 2:
    if Path(sys.argv[1]).exists():
        with open(sys.argv[1], "r") as file:
            print(f"Le fichier {sys.argv[1]} contient {len(file.readlines())} lignes!")
    else:
        sys.exit(f"ERREUR: {sys.argv[1]} n'existe pas.")
else:
    sys.exit("Erreur : Vous devez fournir exactement 2 arguments!")