"""
Affichez les nombres de 1 à 10 avec 1 seconde d’intervalle. Utilisez pour cela le module time et sa fonction sleep().
Consultez pour cela la documentation 22 de la fonction time.sleep()"""
import time
for nbr in range(1, 11):
    print(nbr)
    time.sleep(1)