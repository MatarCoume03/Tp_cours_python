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
    print("1) Saisi du nombre")
    nb = int(input("Nombre: "))
    print("1) Saisi de la somme misee")
    sm = int(input("Somme: "))

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


if __name__ == "__main__":
    ZCasino()