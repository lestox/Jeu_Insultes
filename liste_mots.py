from menu import menu
class liste_mots:

    def __init__(self, choix_map, mots_map, mots_basiques, mots_perso, mots_utilisables):
    # Création et Concaténation des mots de base + des mots liés à la map (+ possiblement des mots liés aux personnages)
        self.choix_map = menu().choose_map().choix = choix_map
        self.mots_map = []
        self.mots_basiques = []
        self.mots_perso = []
        self.mots_utilisables = mots_utilisables
        #mots_utilisables = mots_basiques += mots_perso += mots_map
    
    def mots_map(self, choix_map):
        if choix_map == 1:
            return self.mots_map += [wagon, train, billet] # Les mots de la map : Train
        elif choix_map == 2:
            return self.mots_map +=[soleil, sable, mer] # Les mots de la map : Plage
        elif choix_map == 3:
            return self.mots_map +=[bureau, ordinateur, boss] # Les mots de la map : Bureau
        # etc ...

    def mots_basiques(self):
        sujet = ["Je", "Tu", "Ils", "Toi", "Vous", "Les gens commme toi"]
        verbe = ["mange", "bois", "me fait", "es", "pense"]
        adverbe = ["vraiment", "trop", "pas du tout", "sérieusement", "gravement"]
        complement_1 = ["pas beau", "limite", "atteint de"]

    def mots_perso(self, )