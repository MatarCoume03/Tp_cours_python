#Programme verifiant si une annee entree au clavier est bissextile ou non
annee = input("Entrer l\'annee dont vous souhaitez verifier si elle est bissextile ou non: ")
annee = int(annee)
if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'annee que vous avez saisie est bel et bien bissextile")
else:
    print("L'annee que vous avez saisie n'est pas bissextile")