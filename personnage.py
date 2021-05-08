class personnage:
    def __str__(self):
    # Le print du style du personnage (ex : C'est un Chauve)
        return "C'est un "+str(self.style)+"."

    def __init__(self,choix):
    # Création des variables des personnages utilisables pour le combats
        self.list_insult = [] # TO DO : La liste d'insultes qui sont très efficaces contre notre personnage 
        self.list_styles = ["Chauve","Roux","Nain","Vieille"]
        self.style = self.list_styles[choix]
        self.pv = 100

    # Fonction pour prendre des dégats lorsque une attaque touche le personnage
    def damage(self,dmg):
        dmg = dmg - self.Def 
        self.pv -= dmg