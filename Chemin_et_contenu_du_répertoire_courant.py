"""
Affichez le chemin et le contenu du répertoire courant (celui depuis lequel vous avez lancé l’interpréteur Python).
Déterminez également le nombre total de fichiers et de répertoires présents dans le répertoire courant.
"""
from pathlib import Path
print(Path().cwd())
nb_file = 0
nb_dir = 0
for nom in Path().iterdir():
    print(nom)
    if nom.is_file():
        nb_file += 1
    else:
        nb_dir += 1
print(f"Le repertoire {Path().cwd().name} contient {nb_file} fichiers et {nb_dir} repertoires!")