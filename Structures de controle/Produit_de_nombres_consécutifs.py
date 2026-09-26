"""
Produit de nombres consécutifs
Avec les fonctions list() et range(), créez la liste entiers contenant les nombres entiers pairs de 2 à 20 inclus.
Calculez ensuite le produit des nombres consécutifs deux à deux de entiers en utilisant une boucle.
"""
entiers = list(range(2, 21, 2))
produit = []
i = 0
while i < (len(entiers) - 1) :
    produit.append(entiers[i] * entiers[i + 1]) 
    i += 1
print(produit)
