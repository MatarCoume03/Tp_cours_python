"""
Notes et mention d’un étudiant
Voici les notes d’un étudiant : 14, 9, 13, 15 et 12. Créez un script qui affiche la note maximum (utilisez la fonction
max()), la note minimum (utilisez la fonction min()) et qui calcule la moyenne.
Affichez la valeur de la moyenne avec deux décimales. Affichez aussi la mention obtenue sachant que la mention est
« passable » si la moyenne est entre 10 inclus et 12 exclus, « assez bien » entre 12 inclus et 14 exclus et « bien » au-delà
de 14.
"""
notes = [14, 9, 13, 15, 12]
print(f"La plus petite note de l'etudiant est de: {min(notes)}")
print(f"La plus grande note de l'etudiant est de: {max(notes)}")
print(f"L'etudiant a obtenu une moyenne de: {(sum(notes)/len(notes)):.2f}")