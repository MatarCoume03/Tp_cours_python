"""
L’âge de Camille et Céline en jours est respectivement de 8 331 jours et 8 660 jours. Quel est leur âge en années,
mois et jours, en supposant qu’une année compte 365 jours et qu’un mois compte 30 jours? La fonction divmod() vous
aidera à nouveau.
"""
#Conversion de l'âge de Camille
ageCa = 8331
an = divmod(ageCa, 365)
mois = divmod(an[1], 30)
jours = mois[1]
print(f"Camille est âgee de {an[0]} ans, {mois[0]} mois et {jours} jours")
#Conversion de l'âge de Céline
ageCe = 8660
an = divmod(ageCe, 365)
mois = divmod(an[1], 30)
jours = mois[1]
print(f"Céline est âgee de {an[0]} ans, {mois[0]} mois et {jours} jours")