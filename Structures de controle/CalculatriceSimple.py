# Demandez deux nombres et une opération (+, -, *, /, %)
# Affichez le résultat en gérant la division par zéro

number1 = input("Saisissez le premier nombre: ")
number1 = float(number1)
number2 = input("Saisissez le second nombre: ")
number2 = float(number2)
operation = input("Veuillez entrer le symbole de l'operation que vous souhaitez executer: ")

match operation:
    case "+":
        resultat = number1 + number2
        print("Vous avez choisi l'addition et voici le resultat: \n",number1 ," + ",number2, " = ", resultat)
    case "-":
        resultat = number1 - number2
        print("Vous avez choisi la soustraction et voici le resultat: \n",number1," - ",number2," = ",resultat)
    case "*":
        resultat = number1 * number2
        print("Vous avez choisi la multiplication et voici le resultat: \n",number1," * ",number2," = ",resultat)
    case "/":
        if number2 == 0:
            print("Le denominateur doit imperativement etre different de 0!")
        else:
            resultat = number1 / number2
            print("Vous avez choisi la division et voici le resultat: \n",number1," / ",number2," = ",resultat)
    case "%":
        resultat = number1 % number2
        print("Vous avez choisi l'operation modulo et voici le resultat: \n",number1," % ",number2," = ",resultat)
    case _:
        print("Choix non disponible")