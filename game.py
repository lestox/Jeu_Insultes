import random
import time
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
    # 5) Je lance le combat
        self.Combat(self.map,self.perso1,self.perso2,self.maList)

    def launch_menu(self):
    # 2) Je sélectionne les différents paramètres de ma partie
        print(menu())
        self.select_mode()
        self.select_perso1()
        self.select_perso2()
        self.select_map()

        
    def select_mode(self):
        print("Choisissez le mode de jeu :\n")
        self.choix_mode = menu().choose_mode()
    def select_perso1(self):
        print("Le joueur 1 choisit son personnage :\n")
        self.choix_perso1 = menu().choose_perso(0)
    def select_perso2(self):
        print("Le joueur 2 choisit son personnage :\n")
        self.choix_perso2 = menu().choose_perso(self.choix_mode)
    def select_map(self):
        print("Choisissez le lieu du CLASH :\n")
        self.choix_map = menu().choose_map()


    def game_list(self):
        self.maList = liste_mots(self.choix_map,self.choix_perso1,self.choix_perso2).prepare_list()
        random.shuffle(self.maList)
    



    # def Combat(self,choix_mode,perso1,perso2,mots):
    # 6) Le combat va prendre en paramètre les objets que je viens de créer


    def Combat(self,map,perso1,perso2,maList):
        # Joueur 1
        print("\nAu tour du joueur 1\n")
        self.PlayerTurn(perso1,maList,0)
        print("\nAu tour du joueur 2\n")
        self.PlayerTurn(perso2,maList,self.choix_mode)
        print("\n La phrase du perso1",perso1.phrase_insulte)
        print("\n La phrase du perso2",perso2.phrase_insulte,"\n")
        


    def PlayerTurn(self,perso,maList,choix_mode):
        if choix_mode == 0: # tour du joueur 1 / Et du joueur 2 si le mode est [J vs J]
            print("1/Ajouter des mots")
            print("2/Envoyer la phrase")
            choix = int(input())
            if choix == 1:
                self.choix_insulte = perso.Ajout_mots(maList,0)
                self.maList.pop(self.choix_insulte) # Ma nouvelle liste avec le mot sélectionné en moins

            elif choix == 2:
                self.Envoyer_phrase(perso)

        elif choix_mode == 1 or 2: # tour du joueur 2 si le mode est [J vs IA] ou [Démo]
            time.sleep(1)
            print("\n Au tour de l'IA de choisir (1/Ajouter des mots 2/Envoyer la phrase):\n")
            time.sleep(3)
            choix = random.randint(1,2)
            if choix == 1:
                self.choix_insulte = perso.Ajout_mots(maList,choix_mode)
                self.maList.pop(self.choix_insulte)
            elif choix == 2:
                self.Envoyer_phrase(perso)
            


    def Envoyer_phrase(self,perso):
        print("Ma fonction Envoyer_phrase")
        
