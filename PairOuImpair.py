# Écrivez un programme qui demande un nombre à l'utilisateur
# et affiche s'il est pair ou impair

nombre = input(" Veuillez entrer un nombre pour verifier s'il est pair ou impair:")
nombre = int(nombre)
if nombre % 2 == 0:
    print("Le nombre que vous avez saisi est bien un nombre pair")
else:
    print("Le nombre que vous avez saisi est impair")