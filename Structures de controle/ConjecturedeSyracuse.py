"""
Conjecture de Syracuse
La conjecture de Syracuse est une conjecture mathématique qui reste improuvée à ce jour et qui est définie de la
manière suivante.
Soit un entier positif n. Si n est pair, alors le diviser par 2. S’il est impair, alors le multiplier par 3 et lui ajouter 1.
En répétant cette procédure, la suite de nombres atteint la valeur 1 puis se prolonge indéfiniment par une suite de trois
valeurs triviales appelée cycle trivial.
Jusqu’à présent, la conjecture de Syracuse, selon laquelle depuis n’importe quel entier positif la suite de Syracuse
atteint 1, n’a pas été mise en défaut.
Par exemple, les premiers éléments de la suite de Syracuse si on prend comme point de départ 10 sont : 10, 5, 16, 8,
4, 2, 1…
Créez un script qui, partant d’un entier positif n (par exemple 10 ou 20), crée une liste des nombres de la suite de
Syracuse. Avec différents points de départ (c’est-à-dire avec différentes valeurs de n), la conjecture de Syracuse est-elle
toujours vérifiée? Quels sont les nombres qui constituent le cycle trivial ?
"""
n = int(input("Veuillez saisir un entier positif de votre choix: "))
syracuse = [n,]
while n > 1:
    if (n % 2) == 0:
        n /= 2
        syracuse.append(n)
        if (n % 2) != 0:
            n = n * 3 + 1
            syracuse.append(n)
        elif (n % 2) == 0:
            n /= 2
            syracuse.append(n)
    elif (n % 2) != 0:
        n = n * 3 + 1
        syracuse.append(n)
print(f"Voici la suite de syracuse avec comme point de depart l'entier positif n fourni: \n{syracuse}")