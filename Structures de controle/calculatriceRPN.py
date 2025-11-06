# Implémentez une calculatrice qui utilise la notation polonaise inverse
# L'utilisateur entre des nombres et opérateurs un par un
# Exemple: "2", "3", "+" donne 5

def calculatrice_rpn():
    """
    La version modifiée pour être plus RPN
    """

    while True:
        try:
            # Premier nombre
            print("\nÉtape 1: Entrez le premier nombre")
            nb1 = float(input("Nombre 1: "))
            
            # Second nombre
            print("Étape 2: Entrez le second nombre") 
            nb2 = float(input("Nombre 2: "))
            
            # Opérateur
            print("Étape 3: Choisissez l'opération")
            print("Opérateurs: +, -, *, /, %")
            op = input("Opérateur: ")
            
            # Calcul
            if op == "+":
                resultat = nb1 + nb2
                print(f"🎉 {nb1} {op} {nb2} = {resultat}")
            elif op == "-":
                resultat = nb1 - nb2
                print(f"🎉 {nb1} {op} {nb2} = {resultat}")
            elif op == "*":
                resultat = nb1 * nb2
                print(f"🎉 {nb1} {op} {nb2} = {resultat}")
            elif op == "/":
                if nb2 == 0:
                    print("❌ Erreur: Division par zéro !")
                else:
                    resultat = nb1 / nb2
                    print(f"🎉 {nb1} {op} {nb2} = {resultat}")
            elif op == "%":
                resultat = nb1 % nb2
                print(f"🎉 {nb1} {op} {nb2} = {resultat}")
            else:
                print("❌ Opérateur non valide !")
                continue
                
            continuer = input("\nNouveau calcul ? (o/n): ")
            if continuer.lower() != 'o':
                print("Merci d'avoir utilisé la calculatrice RPN !")
                break
                
        except ValueError:
            print("❌ Veuillez entrer un nombre valide !")
        except:
            print("❌ Une erreur est survenue !")

if __name__ == "__main__":
    calculatrice_rpn()