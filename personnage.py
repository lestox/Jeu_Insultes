class personnage:
    def __str__(self):
        return "C'est un "+str(self.style)+"."

    def __init__(self,style):
        self.list_insult = []
        self.style = style
        self.pv = 100

    def Damage(self,dmg):
        dmg = dmg - self.Def 
        self.pv -= dmg