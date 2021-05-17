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
        # Tant qu'un des joueurs n'est pas mort
        while perso1.pv > 0 and perso2.pv > 0:
            if len(maList) <= 1: # Si la list est vide ou quasi vide, on la reremplit 
                print("jesuisdansleif")
                self.maList = liste_mots(self.choix_map,self.choix_perso1,self.choix_perso2).prepare_list()
                self.Combat(self.map,self.perso1,self.perso2,self.maList)
            # Tour du Joueur 1
            print("\n ------------------------------ Tour du joueur 1 ------------------------------ \n")
            self.PlayerTurn(perso1,perso2,maList,0)
            # Tour du Joueur 2
            print("\n ------------------------------ Tour du joueur 2 ------------------------------ \n")
            self.PlayerTurn(perso2,perso1,maList,self.choix_mode)
            print("\n ---------- La phrase du perso1 : ---------- ",end=" "),self.Print_phrase(perso1.phrase_insulte)
            print("\n ---------- La phrase du perso2 : ---------- ",end=" "),self.Print_phrase(perso2.phrase_insulte)
        
        


    def PlayerTurn(self,perso,persoAdverse,maList,choix_mode):
        if choix_mode == 0: # tour du joueur 1 / Et du joueur 2 si le mode est [J vs J]
            print("1/Ajouter des mots 2/Envoyer la phrase")
            choix = int(input())
            if choix == 1: # Ajouter des mots
                self.Print_mots(maList)
                self.choix_insulte = perso.Ajout_mots(maList,0)
                self.maList.pop(self.choix_insulte) # Ma nouvelle liste avec le mot sélectionné en moins

            elif choix == 2: # Envoyer la phrase
                print("\n ---------- Le "+perso.style+" envoie sa phrase ! ---------- \n")
                self.Print_phrase(perso.phrase_insulte)
                self.Envoyer_phrase(perso,persoAdverse)
                perso.phrase_insulte = []

        elif choix_mode == 1 or 2: # tour du joueur 2 si le mode est [J vs IA] ou [Démo]
            time.sleep(1)
            print("\nSelection de l'IA (1/Ajouter des mots 2/Envoyer la phrase):\n")
            time.sleep(3)
            choix = random.randint(1,2)
            if choix == 1: # Ajouter des mots
                self.Print_mots(maList)
                self.choix_insulte = perso.Ajout_mots(maList,choix_mode)
                self.maList.pop(self.choix_insulte)

            elif choix == 2: # Envoyer la phrase
                print("\n ---------- Le "+perso.style+" envoie sa phrase ! ---------- \n")
                self.Print_phrase(perso.phrase_insulte)
                self.Envoyer_phrase(perso,persoAdverse)
                perso.phrase_insulte = []
            

    def Envoyer_phrase(self,perso,persoAdverse):
        # 1) Récupérer la phrase du perso + Créer les variables utiles
        phrase = perso.phrase_insulte
        # 2) Faire le calcul du niveau de degat
        Niveau_Degat = self.Calcul_Atk(phrase,persoAdverse)
        print("Efficacité d'attaque de niveau",Niveau_Degat)
        # 3) Appeler perso.damage pour retirer les pv
        self.Atk(persoAdverse,Niveau_Degat)
        
    def Atk(self,persoAdverse,Niveau_Degat):
        if Niveau_Degat == 7: 
            print("L'adversaire perd 75 PV")
            persoAdverse.damage(75)
        elif Niveau_Degat == 6:
            print("L'adversaire perd 50 PV")
            persoAdverse.damage(50)
        elif Niveau_Degat == 5:
            print("L'adversaire perd 25 PV")
            persoAdverse.damage(25)
        elif Niveau_Degat == 4:
            print("L'adversaire perd 20 PV")
            persoAdverse.damage(20)
        elif Niveau_Degat == 3:
            print("L'adversaire perd 10 PV")
            persoAdverse.damage(10)
        elif Niveau_Degat == 2 or Niveau_Degat == 1:
            print("L'adversaire perd 5 PV")
            persoAdverse.damage(5)
        elif Niveau_Degat == 0:
            print("L'adversaire perd 0 PV")
            persoAdverse.damage(0)



    def Calcul_Atk(self,phrase,persoAdverse):
        indice = 0
        Niveau_Degat = 0
        if len(phrase) > 0:
            DernierMot = phrase[len(phrase)-1]
            if DernierMot.type == "Finish":
                Niveau_Degat += 1 
            if phrase[indice].type == "Sujet":
                Niveau_Degat += 1
            if len(phrase) > 1:
                if phrase[indice+1].type == "Verbe" and phrase[indice].type == "Sujet":
                    Niveau_Degat += 1
                if len(phrase) > 2:
                    if phrase[indice+2].type == "Adverbe" and phrase[indice+1].type == "Verbe":
                        Niveau_Degat += 1
                    if len(phrase) > 3:
                        if phrase[indice+3].type == "Adjectif" and phrase[indice+4].type == "Adverbe":
                            Niveau_Degat += 1
            for Mots in phrase:
                if Mots.type == "Chauve" and persoAdverse.style == "Chauve":
                    Niveau_Degat += 1
                    break # pour sortir de la boucle for et ne pas compter plusieurs points si SPAM
                elif Mots.type == "Roux" and persoAdverse.style == "Roux":
                    Niveau_Degat += 1
                    break
                elif Mots.type == "Nain" and persoAdverse.style == "Nain":
                    Niveau_Degat += 1
                    break
                elif Mots.type == "Vieille" and persoAdverse.style == "Vieille":
                    Niveau_Degat += 1
                    break
            for Mots in phrase: 
                if Mots.type == "Train" and self.map.styleMap == "Train":
                    Niveau_Degat += 1
                    break # pour sortir de la boucle for et ne pas compter plusieurs points si SPAM
                if Mots.type == "Plage" and self.map.styleMap == "Plage":
                    Niveau_Degat += 1
                    break
                if Mots.type == "Bureau" and self.map.styleMap == "Bureau":
                    Niveau_Degat += 1
                    break
                if Mots.type == "Magasin" and self.map.styleMap == "Magasin":
                    Niveau_Degat += 1
                    break
        else:
            print("Erreur, votre phrase doit au moins contenir 1 mot")
        return Niveau_Degat

# Affiche les mots d'une liste verticalement
    def Print_mots(self,liste):
        print("")
        for Mots in liste:
            print(Mots.text)
        print("")

# Affiche les mots d'une phrase (aussi une liste) avec un espace entre chaques mots
    def Print_phrase(self,liste):
        print("")
        for Mots in liste:
            print(Mots.text, end=" ")
        print("")
