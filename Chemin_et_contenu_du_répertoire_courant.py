"""
Affichez le chemin et le contenu du répertoire courant (celui depuis lequel vous avez lancé l’interpréteur Python).
Déterminez également le nombre total de fichiers et de répertoires présents dans le répertoire courant.
"""
from pathlib import Path
print(f"Le repertoire courant est: {Path().cwd()}\n")
print("================================================================\n")
nb_file = 0
nb_dir = 0
print("Liste des fichiers et repertoires:")
for nom in Path().iterdir():
    print(nom)
    if nom.is_file():
        nb_file += 1
    else:
        nb_dir += 1
print("\n================================================================\n")
print(f"Le repertoire {Path().cwd().name} contient {nb_file} fichiers et {nb_dir} repertoires!")