import random
#from personnage import personnage
#from menu import menu
#from map import *


l = []
def liste():
    global l
    liste_finale = mots_map(l) + mots_basiques(l) + mots_perso(l)
    print(liste_finale)
    return liste_finale

def mots_map(x):
        #choix_map = menu().choose_map().choix
        choix_map = 1
        if choix_map == 1:
            x = x + random.choices(["wagon", "train", "billet"], k=2) # Les mots de la map : Train
            return x
        elif choix_map == 2:
            x = x + random.choices(["soleil", "sable", "mer"], k=2) # Les mots de la map : Plage
            return x
        elif choix_map == 3:
            x = x + random.choices(["bureau", "ordinateur", "boss"], k=2) # Les mots de la map : Bureau
            return x
        # etc ...

def mots_basiques(x):
        sujet = ["Je", "Tu", "Ils", "Toi", "Vous", "Les gens commme toi"] # à compléter
        verbe = ["mange", "bois", "me fait", "es", "pense"] # à compléter
        adverbe = ["vraiment", "trop", "pas du tout", "sérieusement", "gravement"] #à compléter
        complement_1 = ["pas beau", "limite", "atteint de"] # à compléter
        x = x + (random.choices(sujet, k=2) + random.choices(verbe, k=2) + random.choices(adverbe, k=2) + random.choices(complement_1, k=2))
        return x

def mots_perso(x):
        #style_perso = personnage().style
        style_perso = 1
        if style_perso == 0 :
            x = x + random.choices(["chauve", "calv", "calcivie"], k=2) #à compléter
            return x
        elif style_perso == 1 :
            x = x + random.choices(["roux", "rouquin", "poil de carotte"], k=2) #à compléter
            return x
        elif style_perso == 2 :
            x = x + random.choices(["petit", "minus", "gnome"], k=2) #à compléter
            return x
        elif style_perso == 3 :
            x = x + random.choices(["vieille peau", "mamie", "le vioque"], k=2) #à compléter
            return x

liste()