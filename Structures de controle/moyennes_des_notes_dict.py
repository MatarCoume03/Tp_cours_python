"""
Soit le dictionnaire suivant donnant les notes d’un étudiant :
1 dico_notes = {
2 "math": 14, "programmation": 12,
3 "anglais": 16, "biologie": 10,
4 "sport": 19
5 }
Calculez la moyenne de ses notes de deux manières différentes. Calculez à nouveau la moyenne sans la note de biologie
"""
dico_notes = {
    "math": 14,
    "programmation": 12,
    "anglais": 16,
    "biologie": 10,
    "sport": 19
}
#listeNotes = list(dico_notes.values())
print(f"L'eleve a une moyenne de: {sum(dico_notes.values())/len(dico_notes)}")