from random import *
from personnage import personnage
from menu import menu
from map import map
from liste_mots import liste_mots

class game:
    def __init__(self):
    # 1) Je lance le menu
        self.launch_menu()
    # 3) Grâce aux paramètres choisis, je crée mes objets de class pour jouer
        self.perso1 = personnage(self.choix_perso1)
        self.perso2 = personnage(self.choix_perso2)
        self.map = map(self.choix_map)
        self.maList = []
        print("\n\n")
        print("Le "+str(self.perso1.style)+" et le "+str(self.perso2.style)+" vont se battre sur la map : "+str(self.map.styleMap)+" !")
        print("\n\n")
    # 4) Je crée et récupère la variable de ma liste de jeu
        self.game_list() 
        print(self.maList)
    # 5) Je lance le combat
        # self.Combat()


    def launch_menu(self):
    # 2) Je sélectionne les différents paramètres de ma partie
        print(menu())
        self.select_mode()
        self.select_perso1()
        self.select_perso2()
        self.select_map()

        
    def select_mode(self):
        print("Choisissez le mode de jeu :")
        self.choix_mode = menu().choose_mode()
    def select_perso1(self):
        print("Le joueur 1 choisit son personnage :")
        self.choix_perso1 = menu().choose_perso()
    def select_perso2(self):
        print("Le joueur 2 choisit son personnage :")
        self.choix_perso2 = menu().choose_perso()
    def select_map(self):
        print("Choisissez le lieu du CLASH :")
        self.choix_map = menu().choose_map()


    def game_list(self):
        self.maList = liste_mots(self.choix_map,self.choix_perso1,self.choix_perso2).prepare_list()
    



    # def Combat(self,choix_mode,perso1,perso2,mots):
    # 6) Le combat va prendre en paramètre les objets que je viens de créer
        # 
        # 
        # 
        # 
        
