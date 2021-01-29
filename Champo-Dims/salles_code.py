import pygame
#import random

from monster_code import Monster
from bouteille_code import Bouteille
from objet_code import Coffre
from objet_code import Objet
from objet_code import Mur
from objet_code import Objethitbox
from objet_code import Meuble

class Salle():
    def __init__(self ,game ,type):
        #initialise la salle

        self.game = game

        self.image_background_vide = pygame.image.load("Img/background/background_vide.png") 
        self.image_background_vide = pygame.transform.scale(self.image_background_vide,(1080 ,512))
        self.image = self.image_background_vide
        self.rect = self.image.get_rect()

        #Groupes de sprites de la salle
        self.salle_all_sprites = pygame.sprite.Group()
        self.salle_all_bouteilles = pygame.sprite.Group()
        self.salle_all_monster = pygame.sprite.Group()
        self.salle_all_monster_tete = pygame.sprite.Group()
        self.salle_all_vomis_sol = pygame.sprite.Group()
        self.salle_all_vomis = pygame.sprite.Group()
        self.salle_all_coffres = pygame.sprite.Group()
        self.salle_all_object = pygame.sprite.Group()
        self.salle_all_collide = pygame.sprite.Group()
        self.salle_all_mur = pygame.sprite.Group()
        self.salle_all_feuille = pygame.sprite.Group()
        self.salle_all_meuble = pygame.sprite.Group()
        self.salle_all_sprites.add(self.game.player)

        #Variables:
        self.salle_type = type       #Chaque salle a un nombre associer
        self.max_x = 1100
        self.min_x = 0
        self.max_y = 550
        self.min_y = 350

    def salle_init(self):
        #On initialise la salle avec le chargement de son fond + le spawn monster/bouteille/coffre ou plus
        if(self.salle_type == 1):
            self.image = pygame.image.load("Img/background/background_test2.png").convert_alpha()
            self.set_mur(0,0,1)
            self.set_mur(0,0,2)

        if(self.salle_type == 2):
            self.image = pygame.image.load("Img/background/classe_gauche.png")
            self.set_mur(0,0,1)
            self.set_mur(0,0,2)

        if(self.salle_type == 3):
            self.image = pygame.image.load("Img/background/cour.png") 

            self.set_monster(1,772,400)

            self.set_monster(2,1100,500)
            self.set_monster(2,1100,500)
            self.set_monster(2,1100,500)
            self.set_monster(2,1100,500)
            self.set_monster(2,1100,500)
            self.set_monster(2,1100,500)
            self.set_monster(2,1100,500)

            self.set_bouteille(100,775,1)
            self.set_bouteille(250,775,2)
            self.set_bouteille(400,775,3)
            self.set_bouteille(550,775,4)
            self.set_bouteille(700,775,5)
            self.set_bouteille(850,775,6)

            self.set_coffre(400,400,1,1)
            self.set_coffre(800,400,1,17)
            self.set_coffre(1200,400,1,28)

        if(self.salle_type == 4):
            self.image = pygame.image.load("Img/background/couloir.png") 

            self.set_meuble(200,290,2)
            self.set_meuble(600,290,2)
            self.set_meuble(1000,290,2)
            self.set_meuble(1400,290,2)

            for x in range(100,1100,75):
                for y in range(400,750,75):
                    self.set_monster(2,x,y)

            self.set_monster(1,100,500)
            self.set_monster(4,900,500)

        if(self.salle_type == 5):
            self.image = pygame.image.load("Img/background/couloir.png") 
            self.set_meuble(200,290,2)
            self.set_meuble(600,290,2)
            self.set_meuble(1000,290,2)
            self.set_meuble(1400,290,2)

            self.set_monster(3,772,400,2,790,772,400)

            self.set_monster(1,1100,500)
            self.set_monster(2,1100,500)
            self.set_monster(2,1100,500)
            self.set_monster(2,1100,500)
            self.set_monster(2,1100,500)
            self.set_monster(2,1100,500)
            self.set_monster(2,1100,500)
            self.set_monster(2,1100,500)
            self.set_monster(3,772,400,2,790,772,400)
            self.set_monster(3,1180,400,2,790,1180,400)
            self.set_monster(3,300,400,2,790,772,400)
            self.set_monster(3,500,400,2,790,1180,400)
            self.set_monster(3,500,400,2,790,1180,400)
            self.set_monster(4,1000,500)

        if(self.salle_type == 6):
            self.image = pygame.image.load("Img/background/classe_gauche.png") 
            self.set_mur(0,0,1)
            self.set_mur(0,0,2)

            self.set_meuble(75,650,1)
            self.set_meuble(450,650,1)
            self.set_meuble(850,650,1)

            self.set_meuble(250,500,1)
            self.set_meuble(650,500,1)
            self.set_meuble(1050,500,1)

            self.set_meuble(400,350,1)
            self.set_meuble(800,350,1)
            self.set_meuble(1200,350,1)

            self.set_monster(2,1100,400)
            self.set_monster(2,1300,400)

            self.set_monster(3,772,400,2,790,772,400)
            self.set_monster(3,1180,400,2,790,1180,400)
            self.set_monster(5,500,500,700,350,1100,350)

            self.set_coffre(500,400,1,10)

        if(self.salle_type == 7):
            self.image = pygame.image.load("Img/background/classe_droit.png") 
            self.set_mur(0,0,1)
            self.set_mur(0,0,2)

            self.set_meuble(75,650,1)
            self.set_meuble(450,650,1)
            self.set_meuble(850,650,1)

            self.set_meuble(250,500,1)
            self.set_meuble(650,500,1)
            self.set_meuble(1050,500,1)

            self.set_meuble(400,350,1)
            self.set_meuble(800,350,1)
            self.set_meuble(1200,350,1)

            self.set_monster(3,772,400,2,790,772,400)
            self.set_monster(3,1180,400,2,790,1180,400)
            self.set_monster(5,500,500,700,350,1100,350)
            self.set_coffre(500,400,1,1)

        if(self.salle_type == 8):
            self.image = pygame.image.load("Img/background/classe_droit.png") 
            self.set_mur(0,0,1)
            self.set_mur(0,0,2)

            self.set_meuble(75,650,1)
            self.set_meuble(450,650,1)
            self.set_meuble(850,650,1)

            self.set_meuble(250,500,1)
            self.set_meuble(650,500,1)
            self.set_meuble(1050,500,1)

            self.set_meuble(400,350,1)
            self.set_meuble(800,350,1)
            self.set_meuble(1200,350,1)

            self.set_monster(3,772,400,2,790,772,400)
            self.set_monster(3,1180,400,2,790,1180,400)

            self.set_monster(3,300,400,2,790,772,400)
            self.set_monster(3,500,400,2,790,1180,400)

            self.set_monster(5,500,500,700,350,1100,350)
            self.set_coffre(800,800,1,15)

        if(self.salle_type == 9):
            self.image = pygame.image.load("Img/background/classe_gauche.png") 
            self.set_mur(0,0,1)
            self.set_mur(0,0,2)

            self.set_meuble(75,650,1)
            self.set_meuble(450,650,1)
            self.set_meuble(850,650,1)

            self.set_meuble(250,500,1)
            self.set_meuble(650,500,1)
            self.set_meuble(1050,500,1)

            self.set_meuble(400,350,1)
            self.set_meuble(800,350,1)
            self.set_meuble(1200,350,1)

            self.set_monster(3,772,400,2,790,772,400)
            self.set_monster(3,1180,400,2,790,1180,400)
            self.set_monster(5,500,500,700,350,1100,350)

        if(self.salle_type == 10):
            self.image = pygame.image.load("Img/background/background_test2.png") 

        if(self.salle_type == 11):
            self.image = pygame.image.load("Img/background/background_11.png") 

        if(self.salle_type == 12):
            self.image = pygame.image.load("Img/background/background_12.png") 

        if(self.salle_type == 13):
            self.image = pygame.image.load("Img/background/background_13.png") 

        if(self.salle_type == 14):
            self.image = pygame.image.load("Img/background/background_14.png") 

        if(self.salle_type == 15):
            self.image = pygame.image.load("Img/background/background_15.png") 

        if(self.salle_type == 16):
            self.image = pygame.image.load("Img/background/background_16.png") 
        
        if(self.salle_type == 17):
            self.image = pygame.image.load("Img/background/background_17.png") 

        if(self.salle_type == 18):
            self.image = pygame.image.load("Img/background/background_18.png") 

        if(self.salle_type == 19):
            self.image = pygame.image.load("Img/background/background_19.png") 

        if(self.salle_type == 20):
            self.image = pygame.image.load("Img/background/background_20.png") 

        if(self.salle_type == 21):
            self.image = pygame.image.load("Img/background/background_21.png") 

        if(self.salle_type == 22):
            self.image = pygame.image.load("Img/background/background_22.png") 

        if(self.salle_type == 23):
            self.image = pygame.image.load("Img/background/background_23.png") 

        if(self.salle_type == 24):
            self.image = pygame.image.load("Img/background/background_24.png") 

        if(self.salle_type == 25):
            self.image = pygame.image.load("Img/background/background_25.png") 

        if(self.salle_type == 26):
            self.image = pygame.image.load("Img/background/background_26.png") 
        
        if(self.salle_type == 27):
            self.image = pygame.image.load("Img/background/background_27.png") 

        if(self.salle_type == 28):
            self.image = pygame.image.load("Img/background/background_28.png") 

        if(self.salle_type == 29):
            self.image = pygame.image.load("Img/background/background_29.png") 

        if(self.salle_type == 30):
            self.image = pygame.image.load("Img/background/background_30.png") 

        if(self.salle_type == 31):
            self.image = pygame.image.load("Img/background/background_31.png") 

        if(self.salle_type == 32):
            self.image = pygame.image.load("Img/background/background_32.png") 

        if(self.salle_type == 33):
            self.image = pygame.image.load("Img/background/background_33.png") 

        if(self.salle_type == 34):
            self.image = pygame.image.load("Img/background/background_34.png") 

        if(self.salle_type == 35):
            self.image = pygame.image.load("Img/background/background_35.png") 

        if(self.salle_type == 36):
            self.image = pygame.image.load("Img/background/background_36.png") 
        
        if(self.salle_type == 37):
            self.image = pygame.image.load("Img/background/background_37.png") 

        if(self.salle_type == 38):
            self.image = pygame.image.load("Img/background/background_38.png") 

        if(self.salle_type == 39):
            self.image = pygame.image.load("Img/background/background_39.png") 

        if(self.salle_type == 40):
            self.image = pygame.image.load("Img/background/background_40.png") 

        if(self.salle_type == 41):
            self.image = pygame.image.load("Img/background/background_41.png") 

        if(self.salle_type == 42):
            self.image = pygame.image.load("Img/background/background_42.png") 

        if(self.salle_type == 43):
            self.image = pygame.image.load("Img/background/background_43.png") 

        if(self.salle_type == 44):
            self.image = pygame.image.load("Img/background/background_44.png") 

        if(self.salle_type == 45):
            self.image = pygame.image.load("Img/background/background_45.png") 

        if(self.salle_type == 46):
            self.image = pygame.image.load("Img/background/background_46.png") 
        
        if(self.salle_type == 47):
            self.image = pygame.image.load("Img/background/background_47.png") 

        self.image = pygame.transform.scale(self.image,(self.game.affichage.screen_rect.w ,self.game.affichage.screen_rect.h)).convert_alpha()
        self.rect = self.image.get_rect()
        self.max_x = self.game.affichage.screen_rect.w
        self.min_x = 0
        self.max_y = self.game.affichage.screen_rect.h
        self.min_y = int(self.game.affichage.screen_rect.h*0.4) + 5

    def salle_changement(self):
        #Gere les changement de salle si on est a tel endroit dans tel salle 
        if(self.salle_type == 1):
            self.test_1(3)
            self.test_2(3)
            self.test_3(2)

        elif(self.salle_type == 2):
            self.test_12(1)
            
        elif(self.salle_type == 3):
            self.test_gauche(4)
            self.test_droit(5)
        
        elif(self.salle_type == 4):
            self.test_droit(3)
            self.test_porte_couloir_droit(7)
            self.test_porte_couloir_gauche(6)
        
        elif(self.salle_type == 5):
            self.test_gauche(3)
            self.test_porte_couloir_droit(8)
            self.test_porte_couloir_gauche(9)

        elif(self.salle_type == 6):
            self.test_12(4)

        elif(self.salle_type == 7):
           self.test_9(4)
        
        elif(self.salle_type == 8):
            self.test_12(5)

        elif(self.salle_type == 9):
            self.test_12(5)

        elif(self.salle_type == 10):
            self.test_1(1)

        elif(self.salle_type == 11):
            self.test_1(1)

        elif(self.salle_type == 12):
            self.test_1(1)

        elif(self.salle_type == 13):
            self.test_1(1)

        elif(self.salle_type == 14):
            self.test_1(1)

        elif(self.salle_type == 15):
            self.test_1(1)

        elif(self.salle_type == 16):
            self.test_1(1)

        elif(self.salle_type == 17):
            self.test_1(1)

        elif(self.salle_type == 18):
            self.test_1(1)

        elif(self.salle_type == 19):
            self.test_1(1)

        elif(self.salle_type == 20):
            self.test_1(1)

        elif(self.salle_type == 21):
            self.test_1(1)

        elif(self.salle_type == 23):
            self.test_1(1)

        elif(self.salle_type == 24):
            self.test_1(1)

        elif(self.salle_type == 25):
            self.test_1(1)

        elif(self.salle_type == 26):
            self.test_1(1)

        elif(self.salle_type == 27):
            self.test_1(1)

        elif(self.salle_type == 28):
            self.test_1(1)

        elif(self.salle_type == 29):
            self.test_1(1)
        
        elif(self.salle_type == 31):
            self.test_1(1)

        elif(self.salle_type == 32):
            self.test_1(1)

        elif(self.salle_type == 33):
            self.test_1(1)

        elif(self.salle_type == 35):
            self.test_1(1)

        elif(self.salle_type == 36):
            self.test_1(1)

        elif(self.salle_type == 37):
            self.test_1(1)

        elif(self.salle_type == 38):
            self.test_1(1)

        elif(self.salle_type == 39):
            self.test_1(1)

        elif(self.salle_type == 40):
            self.test_1(1)

        elif(self.salle_type == 41):
            self.test_1(1)

        elif(self.salle_type == 42):
            self.test_1(1)

        elif(self.salle_type == 43):
            self.test_1(1)

        elif(self.salle_type == 44):
            self.test_1(1)

        elif(self.salle_type == 45):
            self.test_1(1)

        elif(self.salle_type == 46):
            self.test_1(1)

        elif(self.salle_type == 47):
            self.test_1(1)

        elif(self.salle_type == 48):
            self.test_1(1)

        elif(self.salle_type == 49):
            self.test_1(1)

        self.y_real = 200 + self.rect.y

    def set_monster(self,type,x,y,x1=0,y1=0,x2=0,y2=0):
        #Spawn un monstre d'un certain type a une certaine porsition
        monster = Monster(self.game,self,type,x,y,x1,y1,x2,y2)
        monster.monster_set_type()
        monster.tete.tete_set_type()
        self.salle_all_sprites.add(monster)
        self.salle_all_monster.add(monster)
        self.salle_all_collide.add(monster) 

    def set_bouteille(self,x,y,type):   #ajout type
        #Spawn une bouteille d'un certain type a une certaine porsition
        bouteille = Bouteille(self.game,x,y,type)
        bouteille.bouteille_set_type()
        self.salle_all_sprites.add(bouteille)
        self.salle_all_bouteilles.add(bouteille)

    def set_coffre(self,x,y,type,contenu):
        #Spawn un coffre d'un certain type a une certaine position vec un certain contenu
        coffre = Coffre(self.game,x,y,type,contenu)
        coffre.coffre_set_type()
        self.salle_all_sprites.add(coffre)
        self.salle_all_coffres.add(coffre)
        hitbox = Objethitbox(self.game,x,y+25,100,10)
        self.salle_all_collide.add(hitbox)   
        self.salle_all_meuble.add(coffre)  

    def set_meuble(self,x,y,type):
        meuble = Meuble(self.game,x,y,type)
        meuble.meuble_set_type()
        self.salle_all_sprites.add(meuble)
        self.salle_all_meuble.add(meuble)  
        self.salle_all_collide.add(meuble)  

    def set_mur(self,x,y,type):
        #Ajoute un mur d'un certain type a un endroit
        mur = Mur(self.game,x,y,type)
        self.salle_all_mur.add(mur)
        self.salle_all_meuble.add(mur)  

    def test(self ,x_gauche,x_droit ,y_haut, y_bas):
        #Test position Joueur
        if(self.game.player.rect.x >= x_gauche and self.game.player.rect.x <= x_droit):
            if(self.game.player.y_real >= y_haut and self.game.player.y_real <= y_bas):
                return True
            else :
                return False
        else: 
            return False

    def test_1(self,salle_number):
        #Test prefait
        if(self.test(10,40,620,640) == True):
            if(self.game.pressed.get(pygame.K_LEFT)):
                self.game.salle = self.game.salle_list[salle_number]
                self.game.player.rect.x = 1330 
                self.game.player.rect.y = 480

    def test_2(self,salle_number):
        #Test prefait
        if(self.test(185,205,450,470) == True):
            if(self.game.pressed.get(pygame.K_LEFT)):
                self.game.salle = self.game.salle_list[salle_number]
                self.game.player.rect.x = 1350
                self.game.player.rect.y = 340

    def test_3(self,salle_number):
        #Test prefait
        if(self.test(380,440,330,360) == True):
            if(self.game.pressed.get(pygame.K_UP)):
                self.game.salle = self.game.salle_list[salle_number]
                self.game.player.rect.x = 160
                self.game.player.rect.y = 640

    def test_4(self,salle_number):
        #Test prefait
        if(self.test(730,770,340,360) == True):
            if(self.game.pressed.get(pygame.K_UP)):
                self.game.salle = self.game.salle_list[salle_number]
                self.game.player.rect.x = 390
                self.game.player.rect.y = 640

    def test_5(self,salle_number):
        #Test prefait
        if(self.test(1060,1090,340,360) == True):
            if(self.game.pressed.get(pygame.K_UP)):
                self.game.salle = self.game.salle_list[salle_number]
                self.game.player.rect.x = 720
                self.game.player.rect.y = 640

    def test_6(self,salle_number):
        #Test prefait
        if(self.test(1380,1400,340,360) == True):
            if(self.game.pressed.get(pygame.K_UP)):
                self.game.salle = self.game.salle_list[salle_number]
                self.game.player.rect.x = 1100
                self.game.player.rect.y = 630

    def test_7(self,salle_number):
        #Test prefait
        if(self.test(1430 ,1460,530,550) == True):
            if(self.game.pressed.get(pygame.K_RIGHT)):
                self.game.salle = self.game.salle_list[salle_number]
                self.game.player.rect.x = 220
                self.game.player.rect.y = 250

    def test_8(self,salle_number):
        #Test prefait
        if(self.test(1340,1400,660,680) == True):
            if(self.game.pressed.get(pygame.K_RIGHT)):
                self.game.salle = self.game.salle_list[salle_number]
                self.game.player.rect.x = 80
                self.game.player.rect.y = 440

    def test_9(self,salle_number):
        #Test prefait
        if(self.test(1025,1120,840,870) == True):
            if(self.game.pressed.get(pygame.K_DOWN)):
                self.game.salle = self.game.salle_list[salle_number]
                self.game.player.rect.x = 1370
                self.game.player.rect.y = 170

    def test_10(self,salle_number):
        #Test prefait
        if(self.test(710,745,840,870) == True):
            if(self.game.pressed.get(pygame.K_DOWN)):
                self.game.salle = self.game.salle_list[salle_number]
                self.game.player.rect.x = 1060
                self.game.player.rect.y = 170

    def test_11(self,salle_number):
        #Test prefait
        if(self.test(380,405,840,870) == True):
            if(self.game.pressed.get(pygame.K_DOWN)):
                self.game.salle = self.game.salle_list[salle_number]
                self.game.player.rect.x = 730
                self.game.player.rect.y = 170

    def test_12(self,salle_number):
        #Test prefait
        if(self.test(100,150,840,870) == True):
            if(self.game.pressed.get(pygame.K_DOWN)):
                self.game.salle = self.game.salle_list[salle_number]
                self.game.player.rect.x = 370
                self.game.player.rect.y = 170

    def test_gauche(self,salle_number):
        #Test prefait
        if(self.test(-10,0,0,900) == True):
            if(self.game.pressed.get(pygame.K_LEFT)):
                self.game.salle = self.game.salle_list[salle_number]
                self.game.player.rect.x = 1500 

    def test_droit(self,salle_number):
        #Test prefait
        if(self.test(1500,1550,0,900) == True):
            if(self.game.pressed.get(pygame.K_RIGHT)):
                self.game.salle = self.game.salle_list[salle_number]
                self.game.player.rect.x = 50 

    def test_porte_couloir_droit(self,salle_number):
        #Test prefait
        if(self.test(1370,1410,340,360) == True):
            if(self.game.pressed.get(pygame.K_UP)):
                self.game.salle = self.game.salle_list[salle_number]
                self.game.player.rect.x = 1100
                self.game.player.rect.y = 630

    def test_porte_couloir_gauche(self,salle_number):
        #Test prefait
        if(self.test(180,250,340,360) == True):
            if(self.game.pressed.get(pygame.K_UP)):
                self.game.salle = self.game.salle_list[salle_number]
                self.game.player.rect.x = 160
                self.game.player.rect.y = 640








            

           

        





    

        

        