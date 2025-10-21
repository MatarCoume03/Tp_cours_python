# Affichez la table de multiplication d'un nombre donné
# de 1 à 10, en utilisant une boucle for

def table_de_multiplication():
    nb = input("Saisissez un nombre pour qu'on vous donne sa table de mutiplication: ")
    nb = int(nb)
    i = 0
    while i < 10:
        print(nb, " * ", (i + 1), " = ", (i + 1) * nb)
        i += 1
if __name__ == "__main__":
    table_de_multiplication()