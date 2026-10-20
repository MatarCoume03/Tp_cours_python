def afficher_flottant(nb):
    """
    Fonction prenant en param ètre un flottant et renvoyant
    une chaîne de caract ères repr é sentant la troncature de
    ce nombre . La partie flottante doit avoir une longueur
    maximum de 3 caract è res.
    De plus , on va remplacer le point dé cimal par la virgule
    """
    chaine = str(nb)
    if type(nb) != float:
        print("le nombre que vous avez fourni en parametre n'est pas un flottant :)")

    else:
        echant = chaine.split(".")
        while len(echant[1]) > 3:
            echant[1] = echant[1][0:3]
            chaine = ",".join(echant)
    print(chaine)
if __name__ == "__main__":
    afficher_flottant(1)