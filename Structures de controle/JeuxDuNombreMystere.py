# Générez un nombre aléatoire entre 1 et 100
# L'utilisateur doit deviner le nombre en recevant des indices
# ("Trop grand", "Trop petit") jusqu'à trouver
import random
nombre = random.choice(range(1,101))
print(f"Le nombre aleatoire est {nombre}")
n = int(input("Entrer un nombre compris entre 1 et 100: "))
while n != nombre:
    if n < nombre:
        print("Trop petit!")
        n = int(input("Veuillez entrer un nombre plus grand: "))
        if n == nombre:
            print(f"Bravo vous avez trouve le nombre qui etait {nombre}")
    elif n > nombre:
        print("Trop grand!")
        n = int(input("Veuillez entrer un nombre plus petit: "))
        if n == nombre:
            print(f"Bravo vous avez trouve le nombre qui etait {nombre}")