#Renaud Deschenes
#401
import random

def chiffre():
    nouvelle_liste = []
    for i in range(4):
        i = random.randint(1,6)
        nouvelle_liste.append(i)
    nouvelle_liste.sort()
    nouvelle_liste.pop(0)
    nombre = sum(nouvelle_liste)
    return nombre
class NPC:
    def __init__(self):
        self.force = chiffre()
        self.agilite = chiffre()
        self.constitution = chiffre()
        self.intelligence = chiffre()
        self.sagesse = chiffre()
        self.charisme = chiffre()
        self.classe_armure = random.randint(1, 12)
        self.nom = str
        self.race = str
        self.espece = str
        self.point_de_vie = random.randint(1, 20)
        self.profession = str

    def afficher_caracteristique(self):
        print('force: ',self.force, '\nagilite: ', self.agilite, '\nconstitution: ', self.constitution,'\nintelligence: ', self.intelligence, '\nsagesse:', self.sagesse, '\ncharisme:', self.charisme, '\nclasse d armure: ', self.classe_armure, '\nnom: ', self.nom, '\nrace: ', self.race, '\nespece: ',self.espece, '\npoint de vie: ',self.point_de_vie, '\nprofession: ', self.profession)
class kobold(NPC):
    def __init__(self):
        super().__init__()
    def attaque(self, cible):
        return
    def subir_dommage(self, recevoir_dommage):
        return


class hero(NPC):
    def __init__(self):
        super().__init__()
    def attaque(self, cible):
        return
    def subir_dommage(self, recevoir_dommage):
        return