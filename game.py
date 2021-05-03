from personnage import personnage
from menu import menu

class game:
    def __init__(self):
        self.launch_menu()
        self.perso1 = personnage("Chauve")
        self.perso2 = personnage("Nain")
        print("Le "+str(self.perso1.style)+" et le "+str(self.perso2.style)+" vont se battre !")
        print("(lancement de la fonction combat)")
        self.Combat()

    def launch_menu(self):
        print(menu())
        menu().choose_mode()
        print("Le joueur 1 choisit son personnage :")
        str(input()) #Fonction pour choisir son personnage
        print("Le joueur 2 choisit son personnage :")
        str(input()) # IF J VS J : Fonction pour choisir son personnage  ; ELSE IF J VS IA : Fonction pour choisir un personnage random 
        print("Choisissez le lieu du CLASH :")
        str(input()) # Fonction pour choisir le scenario (la map)

    def Combat(self):
        return None # Lance le combat, while pv > 0 : blablabla
