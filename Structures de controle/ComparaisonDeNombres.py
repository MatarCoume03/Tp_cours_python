# Demandez deux nombres à l'utilisateur
# Affichez le plus grand des deux, ou "Égaux" s'ils sont identiques

#saisi et conversion des nombres en flottant
number1 = input("entrer le premier nombre: ")
number1 = float(number1)
number2 = input("entrer le second nombre: ")
number2 = float(number2)

#comparaison des nombres
if number1 > number2:
    print(number1)
elif number2 > number1:
    print(number2)
else:
    print("egaux")