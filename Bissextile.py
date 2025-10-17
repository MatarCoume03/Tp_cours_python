#Programme verifiant si une annee entree au clavier est bissextile ou non
annee = input("Entrer l\'annee dont vous souhaitez verifier si elle est bissextile ou non: ")
annee = int(annee)
bissextile = False
if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    bissextile = True
if bissextile:
    print("L'annee que vous avez saisie est bel et bien bissextile")
else:
    print("L'annee que vous avez saisie n'est pas bissextile")