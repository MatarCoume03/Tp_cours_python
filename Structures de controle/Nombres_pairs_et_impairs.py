"""
Nombres pairs et impairs
Soit impairs la liste de nombres [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]. Écrivez un programme qui, à
partir de la liste impairs, construit une liste pairs dans laquelle tous les éléments de impairs sont incrémentés de 1.
"""
impairs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
pairs = []
for i in range(0,11):
    pairs.append(impairs[i] + 1)
print(pairs)