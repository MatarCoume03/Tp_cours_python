# Demandez deux nombres et une opération (+, -, *, /, %)
# Affichez le résultat en gérant la division par zéro

number1 = input("Saisissez le premier nombre: ")
number1 = float(number1)
number2 = input("Saisissez le second nombre: ")
number2 = float(number2)
operation = input("Veuillez entrer le symbole de l'operation que vous souhaitez executer: ")

if operation == "+":
    resultat = number1 + number2
elif operation == "-":
    resultat = number1 - number2
elif operation == "*":
    resultat = number1 * number2
elif operation == "/":
    if number2 == 0:
        print("Le denominateur doit imperativement etre different de 0!")
    else:
        resultat = number1 / number2
elif operation == "%":
    resultat = number1 % number2
else:
    print("Choix non disponible")

print(resultat)