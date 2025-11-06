#Programme verifiant si une annee entree au clavier est bissextile ou non
from os import system #importation de la fonction system du module os

try:
    annee = input("Entrer l\'annee dont vous souhaitez verifier si elle est bissextile ou non: ")
    annee = int(annee)
    assert annee > 0
except ValueError:
    print("Vous n'avez pas saisi de valeur!")
except AssertionError:
    print("L'année saisie est inférieure ou égale à 0.")
    
if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'année que vous avez saisie est bel et bien bissextile")
else:
    print("L'annee que vous avez saisie n'est pas bissextile")

system("pause") #cette fonction empeche votre programme de se refermer 