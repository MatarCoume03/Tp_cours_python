"""
Téléchargez le fichier notes.txt de l’exercice précédent et enregistrez-le dans votre répertoire de travail. N’hésitez
pas l’ouvrir avec un éditeur de texte pour voir à quoi il ressemble.
Créez un script Python qui lit chaque ligne de ce fichier, extrait les notes sous forme de float et les stocke dans une
liste.
Le script réécrira ensuite les notes dans le fichier notes2.txt avec une note par ligne suivie de « recalé » si la note
est inférieure à 10 et « admis » si la note est supérieure ou égale à 10. Toutes les notes seront écrites avec une décimale.
À titre d’exemple, voici les trois premières lignes attendues pour le fichier notes2.txt :
13.5 admis
17.0 admis
9.5 recalé
"""
with open("notes.txt", "r") as fichier1, open("notes2.txt", "w") as fichier2:
    listeNotes = []
    for note in fichier1:
        note = note.replace(",", ".")
        note = note.replace("\n", "")
        listeNotes.append(float(note))
    print(listeNotes)
    for note in listeNotes:
        if note < 10:
            fichier2.write(str(note) + " recalé")
        else:
            fichier2.write(str(note) + " admis")