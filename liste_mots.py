class liste_mots:

    def __init__(self,choix):
    # Création et Concaténation des mots de base + des mots liés à la map (+ possiblement des mots liés aux personnages)
        self.mots_basiques = []
        self.mots_map = mots_variables(self.choix)
        self.mots_utilisables = mots_basiques + mots_map # [mots_basiques] + [mots_map] = [mots utilisables]
    
    def mots_variables(self,choix):
        if choix = 1: 
            return [] # Les mots de la map : Train
        elif choix = 2:
            return [] # Les mots de la map : Plage
        elif choix = 3: 
            return [] # Les mots de la map : Bureau
        # etc ...