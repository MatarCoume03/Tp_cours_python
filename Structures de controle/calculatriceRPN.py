# Implémentez une calculatrice qui utilise la notation polonaise inverse
# L'utilisateur entre des nombres et opérateurs un par un
# Exemple: "2", "3", "+" donne 5

def calculatrice():
    
    nb1 = float(input("Entrer le premier nombre: "))
    nb2 = float(input("Entrer le second nombre: "))
    signe = input("Saisisser le signe de l'operation que vous souhaitez effectuer: ")

    match signe:
        case "+":
            print("Vous avez choisi l'addition et voici le resultat:\n", nb1, "+ ", nb2, " = ", nb1 + nb2)
        case "-":
            print("Vous avez choisi la soustraction et voici le resultat:\n ", nb1, " - ", nb2, " = ", nb1 - nb2)
        case "*":
            print("Vous avez choisi la multiplication et voici le resulat:\n ", nb1, " x ", nb2, " = ", nb1 * nb2)
        case "/":
            print("Vous avez choisi la division et voici le resultat:\n ", nb1, " / ", nb2, " = ", nb1 / nb2)
        case "%":
            print("Vous avez choisi le modulo et voici le resultat:\n ", nb1, " %", nb2, " = ", nb1 % nb2)
        case __:
            print("Choix non disponible")
    
if __name__ == "__main__":
    calculatrice()