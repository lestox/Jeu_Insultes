class mots:
# C'est grâce à cette petite classe qu'on peut stocker et utiliser nos variables mots
    def __str__(self):
        return "je suis le mot : "+self.text+" ; je suis de type : "+self.type
    def __init__(self,text,type):
        self.text = text 
        self.type = type
        