class menu:
    def __str__(self):
        return "Bienvenu dans le menu du jeu CLASH"

    def __init__(self):
        self.list_mode = ["1/J VS J","2/J VS IA","3/DEMO"]
    
    def print_mode(self):
        for mode in self.list_mode:
            print(mode)

    def choose_mode(self):
        self.print_mode()
        print("Choisissez un mode :")
        choix = int(input()) - 1
        print(self.list_mode[choix])
        return self.list_mode[choix]

