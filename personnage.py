import time
import random

class personnage:
    def __str__(self):
# Le print du style du personnage (ex : C'est un Chauve)
        return "C'est un "+str(self.style)+"."

    def __init__(self,choix):
# Création des variables des personnages utilisables pour le combats
        self.phrase_insulte = [] # La phrase d'insulte que charge notre personnage
        self.list_styles = ["Chauve","Roux","Nain","Vieille"]
        self.style = self.list_styles[choix]
        self.pv = 100


# Fonction pour prendre des dégats lorsque une attaque touche le personnage
    def damage(self,dmg):
        self.pv -= dmg


    def Ajout_mots(self,maList,choix_mode):
        if choix_mode == 0: # Joueur 1, ET Joueur 2 si humain
            print("\nChoisissez vos mots (Exemple : pour selectionner la 1ere proposition // Tapez 1):\n")
            choix = int(input()) - 1
            if choix >= 0 and choix < len(maList):
                mots = maList[choix]
                self.phrase_insulte.append(mots)
                return choix
            else: # Si il y a erreur lors du choix des mots (index invalide)
                print("Erreur, vous n'avez pas sélectionner un mot de la liste // Rappel : Tappez 1, 2, 3, etc...\n")
                choix = self.Ajout_mots(maList,choix_mode) # Je relance
                return choix

        elif choix_mode == 1 or 2: # Joueur 2 si IA
            time.sleep(1)
            print("\nL'IA choisis son mot :\n")
            time.sleep(3)
            choix = random.randint(1,len(maList)) - 1
            mots = maList[choix]
            self.phrase_insulte.append(mots)
            return choix



        
