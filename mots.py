class mots:
    def __str__(self):
        return "je suis le mot : "+self.text+" ; je suis de type : "+self.type
    def __init__(self,text,type):
        self.text = text 
        self.type = type
    
# monMot1 = mots("Tu","Sujet")
# print(monMot1)

# monMot2 = mots("très moche","Adjectif")
# print(monMot2)