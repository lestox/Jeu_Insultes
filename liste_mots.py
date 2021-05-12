from menu import menu
from personnage import personnage
import random

class liste_mots:

    def __init__(self, mots_map, mots_basiques, mots_perso, mots_utilisables):
    # Création et Concaténation des mots de base + des mots liés à la map (+ possiblement des mots liés aux personnages)
        mots_map()
        mots_basiques()
        mots_perso()
        print(self.mots_utilisables = [mots_map + mots_basiques + mots_perso])
    
    def mots_map(self, choix_map, mots_map):
        self.choix_map = menu().choose_map().choix = choix_map
        self.mots_map = mots_map
        if choix_map == 1:
            return mots_map = random.choice([wagon, train, billet])*2 # Les mots de la map : Train
        elif choix_map == 2:
            return mots_map = random.choice([soleil, sable, mer])*2 # Les mots de la map : Plage
        elif choix_map == 3:
            return mots_map = random.choice([bureau, ordinateur, boss])*2 # Les mots de la map : Bureau
        # etc ...

    def mots_basiques(self, mots_basiques):
        self.mots_basiques = []
        sujet = ["Je", "Tu", "Ils", "Toi", "Vous", "Les gens commme toi"] # à compléter
        verbe = ["mange", "bois", "me fait", "es", "pense"] # à compléter
        adverbe = ["vraiment", "trop", "pas du tout", "sérieusement", "gravement"] #à compléter
        complement_1 = ["pas beau", "limite", "atteint de"] # à compléter
        mots_basiques = [random.choice(sujet)*2 += random.choice(verbe)*2 += random.choice(adverbe)*2 += random.choice(complement_1)*2]
        return mots_basiques

    def mots_perso(self, style_perso, mots_perso)
        self.mots_perso = mots_perso
        style_perso = personnage().style
        if style_perso == 0 :
            return mots_perso = random.choice(["chauve", "calv", "calcivie"])*2 #à compléter
        elif style_perso == 1 :
            return mots_perso = random.choice(["roux", "rouquin", "poil de carotte"])*2 #à compléter
        elif style_perso == 2 :
            return mots_perso = random.choice(["petit", "minus", "gnome"])*2 #à compléter
        elif style_perso == 3 :
            return mots_perso = random.choice(["vieille peau", "mamie", "le vioque"])*2 #à compléter

liste_mots()