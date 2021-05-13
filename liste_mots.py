from menu import menu
from personnage import personnage
import random
from map import map

l = []
def liste() :
    global l
    liste_finale = [mots_map(l) + mots_basiques(l) + mots_perso(l)]
    print(liste_finale)

def mots_map(x):
        choix_map = menu().choose_map().choix
        if choix_map == 1:
            return x + random.choices(["wagon", "train", "billet"], k=2) # Les mots de la map : Train
        elif choix_map == 2:
            return x + random.choices(["soleil", "sable", "mer"], k=2) # Les mots de la map : Plage
        elif choix_map == 3:
            return x + random.choices(["bureau", "ordinateur", "boss"], k=2) # Les mots de la map : Bureau
        # etc ...

def mots_basiques(x):
        sujet = ["Je", "Tu", "Ils", "Toi", "Vous", "Les gens commme toi"] # à compléter
        verbe = ["mange", "bois", "me fait", "es", "pense"] # à compléter
        adverbe = ["vraiment", "trop", "pas du tout", "sérieusement", "gravement"] #à compléter
        complement_1 = ["pas beau", "limite", "atteint de"] # à compléter
        return x + [random.choices(sujet, k=2) += random.choices(verbe, k=2) += random.choices(adverbe, k=2) += random.choices(complement_1, k=2)]

def mots_perso(x)
        style_perso = personnage().style
        if style_perso == 0 :
            return x + random.choices(["chauve", "calv", "calcivie"], k=2) #à compléter
        elif style_perso == 1 :
            return x + random.choices(["roux", "rouquin", "poil de carotte"], k=2) #à compléter
        elif style_perso == 2 :
            return x  random.choices(["petit", "minus", "gnome"], k=2) #à compléter
        elif style_perso == 3 :
            return x + random.choices(["vieille peau", "mamie", "le vioque"], k=2) #à compléter

print("coucou")
liste()