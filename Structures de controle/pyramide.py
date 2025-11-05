# Demandez un nombre n à l'utilisateur
# Affichez une pyramide d'étoiles de n lignes
# Exemple pour n=3:
#   *
#  ***
# *****
def main(nombre):
    for i in range(1, nombre + 1):
        espaces = " " * (nombre - i)
        etoiles = "*" * (2 * i - 1)
        print(espaces + etoiles)
if __name__ == "__main__":
    main(3)