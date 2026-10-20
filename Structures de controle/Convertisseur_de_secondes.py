"""
Un athlète court un marathon, malheureusement sa montre ne mesure son temps qu’en secondes. Celle-ci affiche 11
905. Aidez-le à convertir son temps en heures, minutes et secondes avec la fonction divmod().
"""
temps = 11905
tupleHeures = divmod(temps, 3600)
heures = tupleHeures[0]
tupleMinutes = divmod(tupleHeures[1], 60)
minutes = tupleMinutes[0]
secondes = tupleMinutes[1]
print(f"l'athlète a couru {heures}h {minutes}mn et {secondes}s")