"""
Triangle gauche
Créez un script qui dessine un triangle gauche
"""
i = 10
j = 1
while i >= 1:
    while j <= 10:
        print(f"{'*'*j:>{i}s}")
        j += 1
    i -= 1