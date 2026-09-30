"""
Jours de la semaine
Constituez une liste semaine contenant le nom des sept jours de la semaine.
En utilisant une boucle, écrivez chaque jour de la semaine ainsi que les messages suivants :
• "Au travail" s’il s’agit du lundi au jeudi;
• "Chouette c'est vendredi" s’il s’agit du vendredi;
• "Repos ce week-end" s’il s’agit du samedi ou du dimanche.
Ces messages ne sont que des suggestions, vous pouvez laisser libre cours à votre imagination.
"""
semaine =[
    'Lundi',
    'Mardi',
    'Mercredi',
    'Jeudi',
    'Vendredi',
    'Samedi',
    'Dimanche'
    ]
for jour in semaine:
    print(jour)
    if jour == 'Lundi' or jour == 'Mardi' or jour == 'Mercredi' or jour == 'Jeudi':
        print("Au travail")
    elif jour == 'Vendredi':
        print(f"Chouette c'est Vendredi")
    elif jour == 'Samedi' or jour =='Dimanche':
        print("Repos ce week-end")