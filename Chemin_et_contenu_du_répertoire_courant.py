"""
Affichez le chemin et le contenu du répertoire courant (celui depuis lequel vous avez lancé l’interpréteur Python).
Déterminez également le nombre total de fichiers et de répertoires présents dans le répertoire courant.
"""
from pathlib import Path
print(Path().cwd())