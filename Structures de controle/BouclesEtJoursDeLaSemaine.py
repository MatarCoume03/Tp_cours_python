""""
Boucles et jours de la semaine
Constituez une liste semaine contenant les 7 jours de la semaine.
Écrivez une série d’instructions affichant les jours de la semaine (en utilisant une boucle for), ainsi qu’une autre série
d’instructions affichant les jours du week-end (en utilisant une boucle while).
"""
semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
#Écrivez une série d’instructions affichant les jours de la semaine en utilisant une boucle for
for jour in semaine:
    print(f"{jour}")
print(f"{'X':X>10s}")
#Écrivez une série d’instructions affichant les jours de la semaine en utilisant une boucle for
i = 5
while i in range(5,7):
    print(f"{semaine[i]}")
    i += 1