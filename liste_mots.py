import random
from mots import mots

class liste_mots:
    def __str__(self):
        return "Je suis la class liste_mots"

    def __init__(self,choix_map,choix_perso1,choix_perso2):
    
    # La totalité de mes variables 
        # Répartion de base prévu :
            # 30 sujet
            # 40 verbe
            # 40 adv
            # 40 adj
            # 20 finish
            # 10 map1
            # 10 map2
            # 10 map3
            # 10 map4
            # 10 map5
        # Il est possible que la répartition ait changé en fonction du nombre de mots trouvés (+ ou -), des ecarts ont donc été laissé c'est pour ça que par endroit comme ligne 44 on passe de self.Mots21 à self.Mots31 ligne 46 : cela est fait en sorte à ce qu'on garde la marge initial prévu si on souhaite rajouter des mots.

        # Tout les sujets
        self.Mots1 = mots("Ton appartement","Sujet")
        self.Mots2 = mots("Ton chien","Sujet")
        self.Mots3 = mots("Tu","Sujet")
        self.Mots4 = mots("Tu","Sujet")
        self.Mots5 = mots("Tu","Sujet")
        self.Mots6 = mots("Tu","Sujet")
        self.Mots7 = mots("Les gens comme toi","Sujet")
        self.Mots8 = mots("Ton crane","Sujet")
        self.Mots9 = mots("Ta voiture","Sujet")
        self.Mots10 = mots("Ta dégaine","Sujet")
        self.Mots11 = mots("Ton charisme","Sujet")
        self.Mots12 = mots("Ta prestance","Sujet")
        self.Mots13 = mots("Ton chapeau","Sujet")
        self.Mots14 = mots("Ton ventre","Sujet")
        self.Mots15 = mots("Ta paire de lunette","Sujet")
        self.Mots16 = mots("Ton avis","Sujet")
        self.Mots17 = mots("Ton chat","Sujet")
        self.Mots18 = mots("Ta démarche","Sujet")
        self.Mots19 = mots("Tes muscles","Sujet")
        self.Mots20 = mots("Tes vêtements","Sujet")
        self.Mots21 = mots("Tes oreilles","Sujet")

        # Tout les verbes
        self.Mots31 = mots("ressemble","Verbe")
        self.Mots32 = mots("a","Verbe")
        self.Mots33 = mots("es","Verbe")
        self.Mots34 = mots("sont","Verbe")
        self.Mots35 = mots("ont","Verbe")
        self.Mots36 = mots("es","Verbe")
        self.Mots37 = mots("es","Verbe")
        self.Mots38 = mots("a","Verbe")
        self.Mots39 = mots("possèdes","Verbe")
        self.Mots40 = mots("deforme","Verbe")
        self.Mots41 = mots("est","Verbe")
        self.Mots42 = mots("survie","Verbe")
        self.Mots43 = mots("est","Verbe")
        #self.Mots44 = mots("","Verbe")
        #self.Mots45 = mots("","Verbe")
        #self.Mots46 = mots("","Verbe")
        #self.Mots47 = mots("","Verbe")
        #self.Mots48 = mots("","Verbe")
        #self.Mots49 = mots("","Verbe")
        #self.Mots50 = mots("","Verbe")
        #self.Mots51 = mots("","Verbe")
        #self.Mots52 = mots("","Verbe")
        #self.Mots53 = mots("","Verbe")
        #self.Mots54 = mots("","Verbe")
        #self.Mots55 = mots("","Verbe")
        #self.Mots56 = mots("","Verbe")
        #self.Mots57 = mots("","Verbe")
        #self.Mots58 = mots("","Verbe")
        #self.Mots59 = mots("","Verbe")
        #self.Mots60 = mots("","Verbe")
        #self.Mots61 = mots("","Verbe")
        #self.Mots62 = mots("","Verbe")
        #self.Mots63 = mots("","Verbe")
        #self.Mots64 = mots("","Verbe")
        #self.Mots65 = mots("","Verbe")
        #self.Mots66 = mots("","Verbe")
        #self.Mots67 = mots("","Verbe")
        #self.Mots68 = mots("","Verbe")
        #self.Mots69 = mots("","Verbe")
        #self.Mots70 = mots("","Verbe")
        #self.Mots71 = mots("","Verbe")

        # Tout les adverbes
        self.Mots72 = mots("vraiment","Adverbe")
        self.Mots73 = mots("un peu","Adverbe")
        self.Mots74 = mots("enormement","Adverbe")
        self.Mots75 = mots("a peine","Adverbe")
        self.Mots76 = mots("un poil","Adverbe")
        self.Mots77 = mots("vraiment pas","Adverbe")
        self.Mots78 = mots("rien de","Adverbe")
        self.Mots79 = mots("pas du tout","Adverbe")
        self.Mots80 = mots("pas","Adverbe")
        self.Mots81 = mots("tout le contraire de","Adverbe")
        self.Mots82 = mots("aucune","Adverbe")
        self.Mots83 = mots("pas une once de","Adverbe")
        self.Mots84 = mots("encore","Adverbe")
        self.Mots85 = mots("assez peu","Adverbe")
        self.Mots86 = mots("très","Adverbe")
        self.Mots87 = mots("moins","Adverbe")
        self.Mots88 = mots("guère","Adverbe")
        self.Mots89 = mots("certainement","Adverbe")
        self.Mots90 = mots("toutefois","Adverbe")
        self.Mots91 = mots("tout a fait","Adverbe")
        self.Mots92 = mots("toujours","Adverbe")
        self.Mots93 = mots("si","Adverbe")
        self.Mots94 = mots("tant","Adverbe")
        self.Mots95 = mots("vraiment aucune","Adverbe")
        #self.Mots96 = mots("","Adverbe")
        #self.Mots97 = mots("","Adverbe")
        #self.Mots98 = mots("","Adverbe")
        #self.Mots99 = mots("","Adverbe")
        #self.Mots100 = mots("","Adverbe")
        #self.Mots101 = mots("","Adverbe")
        #self.Mots102 = mots("","Adverbe")
        #self.Mots103 = mots("","Adverbe")
        #self.Mots104 = mots("","Adverbe")
        #self.Mots105 = mots("","Adverbe")
        #self.Mots106 = mots("","Adverbe")
        #self.Mots107 = mots("","Adverbe")
        #self.Mots108 = mots("","Adverbe")
        #self.Mots109 = mots("","Adverbe")
        #self.Mots110 = mots("","Adverbe")
        #self.Mots111 = mots("","Adverbe")
        #self.Mots112 = mots("","Adverbe")

        # Tout les adjectifs
        self.Mots113 = mots("absurde","Adjectif")
        self.Mots114 = mots("ridicule","Adjectif")
        self.Mots115 = mots("malaisant","Adjectif")
        self.Mots116 = mots("moche","Adjectif")
        self.Mots117 = mots("drôle","Adjectif")
        self.Mots118 = mots("osé","Adjectif")
        self.Mots119 = mots("minable","Adjectif")
        self.Mots120 = mots("puant","Adjectif")
        self.Mots121 = mots("éclaté au sol","Adjectif")
        self.Mots122 = mots("pas beau","Adjectif")
        self.Mots123 = mots("laid","Adjectif")
        self.Mots124 = mots("beaucoup","Adjectif")
        self.Mots125 = mots("amorphe","Adjectif")
        self.Mots126 = mots("crasseux","Adjectif")
        self.Mots127 = mots("vilain","Adjectif")
        self.Mots128 = mots("fade","Adjectif")
        self.Mots129 = mots("mou","Adjectif")
        self.Mots130 = mots("terne","Adjectif")
        self.Mots131 = mots("superficiel","Adjectif")
        self.Mots132 = mots("inculte","Adjectif")
        self.Mots133 = mots("lâche","Adjectif")
        self.Mots134 = mots("indigne","Adjectif")
        self.Mots135 = mots("frustré","Adjectif")
        self.Mots136 = mots("coincé","Adjectif")
        self.Mots137 = mots("drôle","Adjectif")
        self.Mots138 = mots("élégant","Adjectif")
        self.Mots139 = mots("beauté","Adjectif")
        self.Mots140 = mots("credible","Adjectif")

        # Tout les "Finish" : expression pour finir sa phrase de manière originale/"clash"
        self.Mots154 = mots("j'en ai finis avec toi !","Finish")
        self.Mots155 = mots("allez, prends ça !","Finish")
        self.Mots156 = mots("dans ta face !","Finish")
        self.Mots157 = mots("allez, pleure pas !","Finish")
        self.Mots158 = mots("et c'est mon dernier mot !","Finish")
        self.Mots159 = mots("c\'est tout pour moi !","Finish")
        self.Mots160 = mots("j'en dirai pas plus.","Finish")
        self.Mots161 = mots("allez, maintenant vas-t\'en !","Finish")
        self.Mots162 = mots("bref fini de perdre mon temps avec toi.","Finish")
        self.Mots163 = mots("et surtout reste tranquille que je te fasse pas plus mal...","Finish")
        self.Mots164 = mots("ni plus, ni moins !","Finish")
        self.Mots165 = mots("de toute façon cause toujours ça m\'atteint pas.","Finish")

        # Mots en rapport avec la map Train
        self.Mots175 = mots("à l\'interieur du wagon","Train")
        self.Mots176 = mots("dans ce train","Train")
        self.Mots177 = mots("avec ton billet","Train")
        self.Mots178 = mots("déraille","Train")
        self.Mots179 = mots("tes bagages","Train")
        self.Mots180 = mots("déclassé","Train")
        self.Mots181 = mots("dans la classe éco","Train")

        # Mots en rapport avec la map Plage
        self.Mots186 = mots("sable","Plage")
        self.Mots187 = mots("à la mer","Plage")
        self.Mots188 = mots("parasol","Plage")
        self.Mots189 = mots("le soleil","Plage")
        self.Mots190 = mots("tes coquillages","Plage")
        self.Mots191 = mots("un coup de soleil","Plage")
        self.Mots192 = mots("chateau de sable","Plage")

        # Mots en rapport avec la map Bureau
        self.Mots197 = mots("ordinateur","Bureau")
        self.Mots198 = mots("à la cafétériat","Bureau")
        self.Mots199 = mots("à l\'accueil","Bureau")
        self.Mots200 = mots("Ton bureau","Bureau")
        self.Mots201 = mots("boss","Bureau")
        self.Mots202 = mots("secretaire","Bureau")
        self.Mots203 = mots("bientôt au chômage","Bureau")
        self.Mots204 = mots("licensié","Bureau")

        # Mots en rapport avec la map Piscine
        self.Mots208 = mots("dans le pédiluve","Piscine")
        self.Mots209 = mots("dans les vestiaires","Piscine")
        self.Mots210 = mots("l\'étoile de mer","Piscine")
        self.Mots211 = mots("boué de sauvetage","Piscine")
        self.Mots212 = mots("avec des brassards aux bras","Piscine")
        self.Mots213 = mots("te noies","Piscine")
        self.Mots214 = mots("boies la tasse","Piscine")
        self.Mots215 = mots("pouille mouillé","Piscine")
        
        # Mots en rapport avec la map Magasin
        self.Mots219 = mots("devant les portes automatiques","Magasin")
        self.Mots220 = mots("dans ton cadis","Magasin")
        self.Mots221 = mots("périmé","Magasin")
        self.Mots222 = mots("qu\'une boite de","Magasin")
        self.Mots223 = mots("en solde","Magasin")
        self.Mots224 = mots("dans les rayons","Magasin")
        self.Mots225 = mots("à la caisse","Magasin")

        # Mots en rapport avec le personnage Chauve
        self.Mots226 = mots("crâne d\'oeuf !","Chauve") 
        self.Mots227 = mots("petite boule de billard","Chauve") 
        self.Mots228 = mots("sale chauve","Chauve") 
        self.Mots229 = mots("avec ta calvitie","Chauve") 
        self.Mots230 = mots("avec ton crâne luisant","Chauve") 
        self.Mots231 = mots("avec ta boule de cristal","Chauve") 
        self.Mots232 = mots("avec ton caillou","Chauve") 
        #self.Mots233 = mots("","Chauve") 
        #self.Mots234 = mots("","Chauve") 
        #self.Mots235 = mots("","Chauve")   
        #self.Mots236 = mots("","Chauve") 

        # Mots en rapport avec le personnage Roux
        self.Mots237 = mots("rouquin","Roux")
        self.Mots238 = mots("poil de carotte","Roux")
        self.Mots239 = mots("roux","Roux")
        self.Mots240 = mots("avec tes tâches de rousseur","Roux")
        self.Mots241 = mots("sale rouquemoute","Roux")
        #self.Mots242 = mots("","Roux")
        #self.Mots243 = mots("","Roux")
        #self.Mots244 = mots("","Roux")
        #self.Mots245 = mots("","Roux")
        #self.Mots246 = mots("","Roux")
        #self.Mots247 = mots("","Roux")

        # Mots en rapport avec le personnage Nain
        self.Mots248 = mots("mon petit pote","Nain")
        self.Mots249 = mots("petit","Nain")
        self.Mots250 = mots("minus !","Nain")
        self.Mots251 = mots("gnome","Nain")
        self.Mots252 = mots("et tu rentres dans ma poche","Nain")
        self.Mots253 = mots("minuscule","Nain")
        self.Mots254 = mots("petit microbe","Nain")
        #self.Mots255 = mots("","Nain")
        #self.Mots256 = mots("","Nain")
        #self.Mots257 = mots("","Nain")
        #self.Mots258 = mots("","Nain")

        # Mots en rapport avec le personnage Vieille
        self.Mots259 = mots("vieille peau","Vieille")
        self.Mots260 = mots("la vioque","Vieille")
        self.Mots261 = mots("la centenaire","Vieille")
        self.Mots262 = mots("ok mamie","Vieille")
        self.Mots263 = mots("et n'oublie pas ta canne !","Vieille")
        #self.Mots264 = mots("","Vieille")
        #self.Mots265 = mots("","Vieille")
        #self.Mots266 = mots("","Vieille")
        #self.Mots267 = mots("","Vieille")
        #self.Mots268 = mots("","Vieille")
        #self.Mots269 = mots("","Vieille")

    # Mes autres variables
        self.choix_map = choix_map
        self.choix_perso1 = choix_perso1
        self.choix_perso2 = choix_perso2
        self.list_sujet = [self.Mots1,self.Mots2,self.Mots3,self.Mots4,self.Mots5,self.Mots6,self.Mots7,self.Mots8,self.Mots9,self.Mots10,self.Mots11,self.Mots13,self.Mots14,self.Mots15,self.Mots16,self.Mots17,self.Mots18,self.Mots19,self.Mots20,self.Mots21]
        self.list_verbe = [self.Mots39,self.Mots40,self.Mots41,self.Mots42,self.Mots43]
        self.list_adverbe = [self.Mots72,self.Mots73,self.Mots74,self.Mots75,self.Mots76,self.Mots77,self.Mots78,self.Mots79,self.Mots80,self.Mots81,self.Mots82,self.Mots83,self.Mots84,self.Mots85,self.Mots86,self.Mots87,self.Mots88,self.Mots89,self.Mots90,self.Mots91,self.Mots92,self.Mots93,self.Mots94,self.Mots95]
        self.list_adjectif = [self.Mots113,self.Mots114,self.Mots115,self.Mots116,self.Mots117,self.Mots118,self.Mots119,self.Mots120,self.Mots121,self.Mots122,self.Mots123,self.Mots124,self.Mots125,self.Mots126,self.Mots127,self.Mots128,self.Mots129,self.Mots130,self.Mots131,self.Mots132,self.Mots133,self.Mots134,self.Mots135,self.Mots136,self.Mots137,self.Mots138,self.Mots139,self.Mots140]
        self.list_finish = [self.Mots154,self.Mots155,self.Mots156,self.Mots157,self.Mots158,self.Mots159,self.Mots160,self.Mots161,self.Mots162,self.Mots163,self.Mots164,self.Mots165]
        self.maListe = []

    def prepare_list(self):
        self.maListe += self.mots_map(self.choix_map) + self.mots_basiques() + self.mots_perso(self.choix_perso1) + self.mots_perso(self.choix_perso2)
        return self.maListe


    def mots_map(self,choix_map):
        if self.choix_map == 0:
            x = random.choices([self.Mots175,self.Mots176,self.Mots177,self.Mots178,self.Mots179,self.Mots180,self.Mots181], k=3) # Les mots de la map : Train
            return x
        elif self.choix_map == 1:
            x = random.choices([self.Mots186,self.Mots187,self.Mots188,self.Mots189,self.Mots190,self.Mots191,self.Mots192], k=3) # Les mots de la map : Plage
            return x
        elif self.choix_map == 2:
            x = random.choices([self.Mots197,self.Mots198,self.Mots199,self.Mots200,self.Mots201,self.Mots202,self.Mots203,self.Mots204], k=3) # Les mots de la map : Bureau
            return x
        elif self.choix_map == 3:
            x = random.choices([self.Mots208,self.Mots209,self.Mots210,self.Mots211,self.Mots212,self.Mots213,self.Mots214,self.Mots215], k=3) # Les mots de la map : Piscine
            return x
        elif self.choix_map == 4:
            x = random.choices([self.Mots219,self.Mots220,self.Mots221,self.Mots222,self.Mots223,self.Mots224,self.Mots225], k=3) # Les mots de la map : Magasin
            return x

    def mots_basiques(self):
        # 4 mots tirés dans liste sujet + 4 mots tirés dans la liste verbe + 3 mots tirés dans la liste adverbe + 3 mots tirés dans la liste adjectif + 3 mots tirés dans la liste finish
        x = (random.choices(self.list_sujet, k=4) + random.choices(self.list_verbe, k=4) + random.choices(self.list_adverbe, k=3) + random.choices(self.list_adjectif, k=3)) + random.choices(self.list_finish, k=3)
        return x

    def mots_perso(self,choix_perso):
        if choix_perso == 0 :
            x = random.choices([self.Mots226,self.Mots227,self.Mots228,self.Mots229,self.Mots230,self.Mots231,self.Mots232], k=2) # Les mots forts contre le style : Chauve
            return x
        elif choix_perso == 1 :
            x = random.choices([self.Mots237,self.Mots238,self.Mots239,self.Mots240,self.Mots241], k=2) # Les mots forts contre le style : Roux
            return x
        elif choix_perso == 2 :
            x = random.choices([self.Mots248,self.Mots249,self.Mots250,self.Mots251,self.Mots252,self.Mots253,self.Mots254], k=2) # Les mots forts contre le style : Nain
            return x
        elif choix_perso == 3 :
            x = random.choices([self.Mots259,self.Mots260,self.Mots261,self.Mots262,self.Mots263], k=2) # Les mots forts contre le style : Vieille
            return x

