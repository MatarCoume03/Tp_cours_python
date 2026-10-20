"""
Les acides aminés peuvent être séparés en quatre grandes catégories : apolaires (a), polaires (p), chargés positivement
(+) et chargés négativement (-). Le dictionnaire suivant implémente cette classification :
aa2prop = 
{
'A': 'a', 'V': 'a', 'L': 'a', 'G': 'a', 'I': 'a', 'M': 'a', 'W': 'a', 'F': 'a', 'P': 'a',
'S': 'p', 'C': 'p', 'N': 'p', 'Q': 'p', 'T': 'p', 'Y': 'p',
'D': '-', 'E': '-',
'K': '+', 'R': '+', 'H': '+' 
}
On souhaite convertir la séquence en acide aminé du domaine transmembranaire d’une intégrine humaine SNADVVYEKQMLYLYVLSGIG 
en une série de signes indiquant la nature des acides aminés (a, p, + et -). 
Affichez tout d’abord la séquence sur une ligne, puis la nature des acides aminés sur une seconde ligne.
La séquence contient une hélice transmembranaire, donc une succession de résidus apolaires, essayez de la retrouver
visuellement.
Pour cet exercice, nous vous conseillons d’itérer sur la chaîne de caractères contenant la séquence. Nous reverrons
cela dans le chapitre 11 Plus sur les chaînes de caractères
"""
aa2prop = {
'A': 'a', 'V': 'a', 'L': 'a', 'G': 'a', 'I': 'a', 'M': 'a', 'W': 'a', 'F': 'a', 'P': 'a',
'S': 'p', 'C': 'p', 'N': 'p', 'Q': 'p', 'T': 'p', 'Y': 'p',
'D': '-', 'E': '-',
'K': '+', 'R': '+', 'H': '+' 
}
sequence = "SNADVVYEKQMLYLYVLSGIG"
for base in sequence:
    print(f"{base}", end= " ")
print("\n")
for base in sequence:
    print(aa2prop.get(base), end= " ")
hélice_trans = []
for base in sequence:
    if aa2prop.get(base) == 'a':
        hélice_trans.append(base)
print(f"\n\nl'hélice transmembranaire est la suivante: {str(hélice_trans)}")