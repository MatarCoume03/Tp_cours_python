"""
Attribution de la structure secondaire des acides aminés d’une protéine
Dans une protéine, les différents acides aminés sont liés entre eux par une liaison peptidique. Les angles phi et psi sont
deux angles mesurés autour de cette liaison peptidique. Leurs valeurs sont utiles pour définir la conformation spatiale
(appelée « structure secondaire ») adoptée par les acides aminés.
Par exemple, les angles phi et psi d’une conformation en « hélice alpha » parfaite ont une valeur de -57 degrés et -47
degrés respectivement. Bien sûr, il est très rare que l’on trouve ces valeurs parfaites dans une protéine, et il est habituel
de tolérer une déviation de ± 30 degrés autour des valeurs idéales de ces angles.
Vous trouverez ci-dessous une liste de listes contenant les valeurs des angles phi et psi de 15 acides aminés de la
protéine 1TFE 3
:
1 [[48.6, 53.4],[-124.9, 156.7],[-66.2, -30.8], \
2 [-58.8, -43.1],[-73.9, -40.6],[-53.7, -37.5], \
3 [-80.6, -26.0],[-68.5, 135.0],[-64.9, -23.5], \
4 [-66.9, -45.5],[-69.6, -41.0],[-62.7, -37.5], \
5 [-68.2, -38.3],[-61.2, -49.1],[-59.7, -41.1]]
Pour le premier acide aminé, l’angle phi vaut 48.6 et l’angle psi 53.4. Pour le deuxième, l’angle phi vaut -124.9 et
l’angle psi 156.7, etc.
En utilisant cette liste, créez un script qui teste, pour chaque acide aminé, s’il est ou non en hélice et affiche les
valeurs des angles phi et psi et le message adapté est en hélice ou n’est pas en hélice.
Par exemple, pour les trois premiers acides aminés :
[48.6, 53.4] n'est pas en hélice
[-124.9, 156.7] n'est pas en hélice
[-66.2, -30.8] est en hélice
D’après vous, quelle est la structure secondaire majoritaire de ces 15 acides aminés?"""
import math
phi_ideal = -57.0
psi_ideal = -47.0
tolerance = 30.0
tfe1 = [
[48.6, 53.4],[-124.9, 156.7],[-66.2, -30.8], 
[-58.8, -43.1],[-73.9, -40.6],[-53.7, -37.5],
[-80.6, -26.0],[-68.5, 135.0],[-64.9, -23.5],
[-66.9, -45.5],[-69.6, -41.0],[-62.7, -37.5],
[-68.2, -38.3],[-61.2, -49.1],[-59.7, -41.1]
]
for acide in tfe1:
    phi = acide[0]
    psi = acide[1]
    if math.isclose(phi_ideal, phi, abs_tol= tolerance) and math.isclose(psi_ideal, psi, abs_tol= tolerance):
        print(f"{acide} est en Helice!")
    else:
        print(f"{acide} n'est en pas Helice!")
