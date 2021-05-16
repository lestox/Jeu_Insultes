import random
from mots import mots

class liste_mots:
    def __str__(self):
        return "Je suis la class liste_mots"

    def __init__(self,choix_map,choix_perso1,choix_perso2):
        # La totalité de mes variables 
        self.Mots1 = mots("Je","Sujet")
        self.Mots2 = mots("Tu","Sujet")
        self.Mots3 = mots("Ils","Sujet")
        self.Mots4 = mots("Toi","Sujet")
        self.Mots5 = mots("Vous","Sujet")
        self.Mots6 = mots("Les gens commme toi","Sujet")

        self.Mots7 = mots("manges","Verbe")
        self.Mots8 = mots("bois","Verbe")
        self.Mots9 = mots("me fais","Verbe")
        self.Mots10 = mots("es","Verbe")
        self.Mots11 = mots("penses","Verbe")

        self.Mots12 = mots("vraiment","Adverbe")
        self.Mots13 = mots("trop","Adverbe")
        self.Mots14 = mots("pas du tout","Adverbe")
        self.Mots15 = mots("sérieusement","Adverbe")
        self.Mots16 = mots("gravement","Adverbe")

        self.Mots17 = mots("pas beau","Adjectif")
        self.Mots18 = mots("moche","Adjectif")
        self.Mots19 = mots("minable","Adjectif")
        self.Mots20 = mots("puant","Adjectif")
        self.Mots21 = mots("éclaté au sol","Adjectif")

        self.Mots22 = mots("prends ça ","Finish")
        self.Mots23 = mots("j'en ai finis avec toi !","Finish")
        self.Mots24 = mots("allez, pleure pas !","Finish")

        self.Mots25 = mots("à l'intérieur du wagon","Train")
        self.Mots26 = mots("dans ce train","Train")
        self.Mots27 = mots("avec ton billet","Train")
        self.Mots28 = mots("au soleil","Plage")
        self.Mots29 = mots("sur le sable","Plage")
        self.Mots30 = mots("dans la mer","Plage")
        self.Mots31 = mots("dans le bureau","Bureau")
        self.Mots32 = mots("sur ton ordinateur","Bureau")
        self.Mots33 = mots("devant le boss","Bureau")

        self.Mots34 = mots("chauve","Chauve")
        self.Mots35 = mots("crane d'oeuf","Chauve")
        self.Mots36 = mots("calvitie","Chauve")
        self.Mots37 = mots("roux","Roux")
        self.Mots38 = mots("rouquin","Roux")
        self.Mots39 = mots("poil de carotte","Roux")
        self.Mots40 = mots("petit","Nain")
        self.Mots41 = mots("minus","Nain")
        self.Mots42 = mots("gnome","Nain")
        self.Mots43 = mots("vieille peau","Vieille")
        self.Mots44 = mots("mamie","Vieille")
        self.Mots45 = mots("la vioque","Vieille")

        # mes autres variables
        self.choix_map = choix_map
        self.choix_perso1 = choix_perso1
        self.choix_perso2 = choix_perso2
        self.list_sujet = [self.Mots1,self.Mots2,self.Mots3,self.Mots4,self.Mots5,self.Mots6] 
        self.list_verbe = [self.Mots7,self.Mots8,self.Mots9,self.Mots10,self.Mots11]
        self.list_adverbe = [self.Mots12,self.Mots13,self.Mots14,self.Mots15,self.Mots16]
        self.list_adjectif = [self.Mots17,self.Mots18,self.Mots19,self.Mots20,self.Mots21]
        self.list_finish = [self.Mots22,self.Mots23,self.Mots24]
        self.maListe = []

    def prepare_list(self):
        self.maListe += self.mots_map(self.choix_map) + self.mots_basiques() + self.mots_perso(self.choix_perso1) + self.mots_perso(self.choix_perso2)
        return self.maListe


    def mots_map(self,choix_map):
        if self.choix_map == 0:
            x = random.choices([self.Mots25,self.Mots26,self.Mots27], k=2) # Les mots de la map : Train
            return x
        elif self.choix_map == 1:
            x = random.choices([self.Mots28,self.Mots29,self.Mots30], k=2) # Les mots de la map : Plage
            return x
        elif self.choix_map == 2:
            x = random.choices([self.Mots31,self.Mots32,self.Mots33], k=2) # Les mots de la map : Bureau
            return x
        # etc...

    def mots_basiques(self):
        x = (random.choices(self.list_sujet, k=2) + random.choices(self.list_verbe, k=2) + random.choices(self.list_adverbe, k=2) + random.choices(self.list_adjectif, k=2)) + random.choices(self.list_finish, k=2) 
        return x

    def mots_perso(self,choix_perso):
        if choix_perso == 0 :
            x = random.choices([self.Mots34,self.Mots35,self.Mots36], k=2) #à compléter
            return x
        elif choix_perso == 1 :
            x = random.choices([self.Mots37,self.Mots38,self.Mots39], k=2) #à compléter
            return x
        elif choix_perso == 2 :
            x = random.choices([self.Mots40,self.Mots41,self.Mots42], k=2) #à compléter
            return x
        elif choix_perso == 3 :
            x = random.choices([self.Mots43,self.Mots44,self.Mots45], k=2) #à compléter
            return x

