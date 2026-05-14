#Exercise 2 Shopping Cart Program

article = input("Quel article Souhaiteriez-vous acheter?: ")
prix = float(input("Entrer le prix de l'article: "))
nombre = int(input("Combien Voulez-vous en acheter?: "))
total = prix * nombre

print(f"Vous avez achete {nombre} {article}(s)")
print(f"Voici le montant de la facture: {total}fcfa")