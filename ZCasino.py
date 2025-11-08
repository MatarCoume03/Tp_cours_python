#importation des modules necessaires
import random, math

def ZCasino():
    #acceuil;
    print("==================================================================")
    print("******************************************************************")
    print("\tBienvenu(e) dans notre casino ZCasino :)")
    print("==================================================================")
    print("******************************************************************\n")

    #jeu de la roulette
    while True:
        print("1) Saisi du nombre")
        try:
            nb = int(input("Nombre: "))
            assert 0 <= nb <= 49
        except AssertionError:
            print("Le nombre saisi doit etre compris entre 0 et 49")
            continue

        print("2) Saisi de la somme misee")
        try:
            sm = int(input("Somme: "))
            assert sm > 0
        except AssertionError:
            print("LA Somme saisie doit etre strictement positif")
            continue

        #resume des choix du client
        print(f"\nNombre Choisi: {nb}")
        print(f"Somme misee: {sm}")

        #mise en marche de la roulette
        hasar = random.randrange(0, 49)
        print(f"Nombre sorti par la roulette: {hasar}")
        if nb == hasar:
            print("Felicitation vous etes l'heureux gagnant et vous remportez 3X la somme misee :)")
            print(f"Somme gagnee = {3*sm}")
        else:
            if (nb % 2 == hasar % 2 == 0) or (nb % 2 != 0 and hasar % 2 != 0):
                print("Ca va vous remporter la moitie de la somme misee comme recompense :|")
                print(f"Somme gagnee: {math.ceil(sm + (sm / 2))}")
            else:
                print("Desole une prochaine fois peut etre :(")

        continuer = input("Voulez vous faire une autre partie?")
        if continuer.lower() != 'o':
            break

if __name__ == "__main__":
    ZCasino()