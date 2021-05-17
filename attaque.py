# Nous n'avons finalement pas intégré de classe attaque, mais voici la réflexion de l'algo syntaxique pour y voir + clair

# Les possibilités d'une attaque sont par exemples : 
    # I - Nulle (si atk entre 0 et 1) => 0% degat
    # II - Peu efficace (si atk entre 2 et 3) => 10% degat
    # III - Efficace (si atk de 4) => 25% degat
    # IV - Très efficace (si atk de 5 et plus) => 33% degat
# Si il y a un mot lié à la map : + 1 niveau d'efficacité (ex : II -> III)
# Si il y a un mot lié au style de l'adversaire : + 1 niveau d'efficacité (ex : IV -> V)
# Ainsi : 
    #  V - Hyper efficace (si atk de 5 et plus dont un mot lié à la map OU un mot lié au style) => 50% degat
    # VII - GIGA efficace (si atk de 5 et plus dont un mot lié à la map ET un mot lié au style) => 100% de degat
    #  (exemple contre un "Chauve" : 
        # Tu(+1 point) // Niveau d'efficacité de I
        # Es(+1 point) // Niveau d'efficacité de II
        # Vraiment(+1 point) // Niveau d'efficacité de III
        # Pas Beau(+1 point) // Niveau d'efficacité de IV
        # Dans ce train(+1 point BONUS) // Niveau d'efficacité +1 (V -> VI)
        # Avec ta calvitie(+1 point BONUS) // Niveau d'efficacité +1 (VI -> VII)
        # Prend ça !(+1 point) Niveau d'efficacité de V
            # 5 points + 2 points BONUS =>  VII, donc KO en 1 coup
# Ensuite : Round suivant
# Puis, dans le game.py ça va appeler "personnage.damage(atk)" pour retirer les points de vie