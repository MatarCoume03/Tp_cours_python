# Calculez la somme de tous les nombres pairs entre 1 et 100
# en utilisant une boucle while

number = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        number += i
    i += 1
print(number)