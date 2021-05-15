import random 
import time

class menu:
    def __str__(self):
    # Message de bienvenu
        return "Bienvenu dans le menu du jeu CLASH"

    def __init__(self):
    # Nos listes de paramètres à choisir afin de préparer la partie
        self.list_mode = ["1/J VS J","2/J VS IA","3/DEMO"]
        self.list_perso = ["1/Le Chauve","2/Le Roux", "3/Le Nain","4/La Vieille"]
        self.list_map = ["1/Le Train","2/La Plage", "3/Le Bureau", "4/La Piscine","5/Le Magasin"]
    

    # La fonction qui choisit le mode
    def choose_mode(self):
        self.print_mode()
        print("Choix du mode :")
        choix = int(input()) - 1 # Le "- 1" sert juste à pouvoir selectionner dans les listes puisque une liste commence par 0 et pas par 1.
        print("---------- "+self.list_mode[choix], ": sélectionné "+"---------- ")
        return choix
    def print_mode(self):
        for mode in self.list_mode:
            print(mode)
    
    # La fonction qui choisit le perso
    def choose_perso(self,choix_mode):
        if choix_mode == 0:
            self.print_perso()
            print("Choix du perso :")
            choix = int(input()) - 1
            print("---------- "+self.list_perso[choix], ": sélectionné "+"---------- ")
            return choix
        elif choix_mode == 1: 
            time.sleep(1)
            self.print_perso()
            print("Choix du perso de l'IA :")
            time.sleep(3)
            choix = random.randint(1,len(self.list_perso)) - 1
            print("---------- "+self.list_perso[choix], ": sélectionné "+"---------- ")
            return choix
    def print_perso(self):
        for perso in self.list_perso:
            print(perso)
    
    # La fonction qui choisit la map
    def choose_map(self):
        self.print_map()
        print("Choix de la map :")
        choix = int(input()) - 1
        print("---------- "+self.list_map[choix], ": sélectionné "+"---------- ")
        return choix
    def print_map(self):
        for map in self.list_map:
            print(map)
    

