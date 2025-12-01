def afficher_flottant(nb):
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