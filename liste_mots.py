import random

class liste_mots:
    def __str__(self):
        return "Je suis la class liste_mots"

    def __init__(self,choix_map,choix_perso1,choix_perso2):
        self.choix_map = choix_map
        self.choix_perso1 = choix_perso1
        self.choix_perso2 = choix_perso2
        self.list_sujet = ["Je", "Tu", "Ils", "Toi", "Vous", "Les gens commme toi"] # à remplacer par, exemple : [mot("Je","sujet"),mot("Tu","sujet")]
        self.list_verbe = ["manges", "bois", "me fais", "es", "penses"]
        self.list_adverbe = ["vraiment", "trop", "pas du tout", "sérieusement", "gravement"]
        self.list_adjectif = ["pas beau", "moche", "minable"]
        self.list_finish = ["prends ça !", "j'en ai finis avec toi !", "allez, pleure pas !"]
        self.maListe = []

    def prepare_list(self):
        self.maListe += self.mots_map(self.choix_map) + self.mots_basiques() + self.mots_perso(self.choix_perso1) + self.mots_perso(self.choix_perso2)
        return self.maListe


    def mots_map(self,choix_map):
        if self.choix_map == 0:
            x = random.choices(["à l'intérieur du wagon", "dans ce train", "avec ton billet"], k=2) # Les mots de la map : Train
            return x
        elif self.choix_map == 1:
            x = random.choices(["au soleil", "sur le sable", "dans la mer"], k=2) # Les mots de la map : Plage
            return x
        elif self.choix_map == 2:
            x = random.choices(["dans le bureau", "sur ton ordinateur", "devant le boss"], k=2) # Les mots de la map : Bureau
            return x
        # etc...

    def mots_basiques(self):
        x = (random.choices(self.list_sujet, k=2) + random.choices(self.list_verbe, k=2) + random.choices(self.list_adverbe, k=2) + random.choices(self.list_adjectif, k=2)) + random.choices(self.list_finish, k=2) 
        return x

    def mots_perso(self,choix_perso):
        if choix_perso == 0 :
            x = random.choices(["chauve", "calv", "calcivie"], k=2) #à compléter
            return x
        elif choix_perso == 1 :
            x = random.choices(["roux", "rouquin", "poil de carotte"], k=2) #à compléter
            return x
        elif choix_perso == 2 :
            x = random.choices(["petit", "minus", "gnome"], k=2) #à compléter
            return x
        elif choix_perso == 3 :
            x = random.choices(["vieille peau", "mamie", "le vioque"], k=2) #à compléter
            return x




