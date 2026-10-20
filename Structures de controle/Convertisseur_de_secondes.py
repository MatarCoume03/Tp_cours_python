"""
Un athlète court un marathon, malheureusement sa montre ne mesure son temps qu’en secondes. Celle-ci affiche 11
905. Aidez-le à convertir son temps en heures, minutes et secondes avec la fonction divmod().
"""
temps = 11905
heures = divmod(temps, 3600)
minutes = divmod(heures[1], 60)
secondes = minutes[1]
print(f"l'athlète a couru {heures[0]}h {minutes[0]}mn et {secondes}s")