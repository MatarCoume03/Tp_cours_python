"""
Pyramide
Créez un script pyra.py qui dessine une pyramide:
"""
reponse = input("Entrer le nombre de lignes (entier positif): ")
N = int(reponse)
i = N * 2
j = 1
while i >= 1:
    while j <= i:
        print(f"{'*'*j:^{i}s}")
        j += 2
    i -= 1