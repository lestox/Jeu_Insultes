class map:
# Sert juste à print le nom de la map avant de lancer le combat
    def __str__(self):
        return "C'est la map : "+str(self.styleMap)+"."

    def __init__(self,choix):
        self.list_map = ["Train","Plage","Bureau","Piscine","Magasin"]
        self.styleMap = self.list_map[choix]