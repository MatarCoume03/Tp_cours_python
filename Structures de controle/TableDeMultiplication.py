# Affichez la table de multiplication d'un nombre donné
# de 1 à 10, en utilisant une boucle for

nb = input("Saisissez un nombre pour qu'on vous donne sa table de multiplication: ")
nb = int(nb)
print("Vous avez saisi le nombre ", nb, "et voici sa table de multiplication:")
table = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for nombre in table:
    resultat = nb * nombre
    print(nb , " * " , nombre, " = ", resultat)