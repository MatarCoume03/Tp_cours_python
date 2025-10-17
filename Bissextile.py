annee = input("Entrer l\'annee dont vous souhaitez verifier si elle est bissextile ou non: ")
annee = int(annee)
bissextile = False
if annee % 4 == 0:
    bissextile = True
elif annee % 100 == 0:
    bissextile = False
elif annee % 400 == 0:
    bissextile = True
else:
    bissextile = False
if bissextile:
    print("L'annee que vous avez saisie est bel et bien bissextile")
else:
    print("L'annee que vous avez saisie n'est pas bissextile")