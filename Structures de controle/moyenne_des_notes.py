"""
Le fichier notes.txt contient les notes obtenues par des étudiants pour le cours de Python. Chaque ligne du fichier
ne contient qu’une note.
Téléchargez le fichier notes.txt et enregistrez-le dans votre répertoire de travail. N’hésitez pas à l’ouvrir avec un
éditeur de texte pour voir à quoi il ressemble.
Créez un script Python qui lit chaque ligne de ce fichier, extrait les notes sous forme de float et les stocke dans une
liste.
Terminez le script en calculant et affichant la moyenne des notes avec deux décimales.
"""
notes = open("notes.txt", "r")
listeNotes = []
for note in notes:
    note = note.replace(',', '.')
    note = float(note)
    print(f"{note:.2f}")
    listeNotes.append(note)
print(listeNotes)
print(f"La moyenne des notes est de: {sum(listeNotes)/len(listeNotes):.2f}")
notes.close()