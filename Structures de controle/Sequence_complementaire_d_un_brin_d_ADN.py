"""
Séquence complémentaire d’un brin d’ADN
La liste ci-dessous représente la séquence d’un brin d’ADN :
["A", "C", "G", "T", "T", "A", "G", "C", "T", "A", "A", "C", "G"]
Créez un script qui transforme cette séquence en sa séquence complémentaire.
Rappel : la séquence complémentaire s’obtient en remplaçant A par T, T par A, C par G et G par C.
"""
sequence = ["A", "C", "G", "T", "T", "A", "G", "C", "T", "A", "A", "C", "G"]
sequenceCompl = []
for base in sequence:
    if base == 'A':
        base = 'T'
    elif base == 'T':
        base = 'A'
    elif base == 'C':
        base = 'G'
    elif base == 'G':
        base = 'c'
    sequenceCompl.append(base)
print(sequenceCompl)