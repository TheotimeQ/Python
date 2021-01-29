
import pygame
import random 
class playerhitbox(pygame.sprite.Sprite):
    def __init__(self,game):
        #Chargement image + initialisation
        super().__init__()
        self.game = game
        self.image = pygame.image.load("Img/objet/hitbox.png")
        self.image = pygame.transform.scale(self.image,(50 , 1))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0    

    def hitbox_update(self):
        #update la hitbox
        self.rect.x = self.game.player.rect.x
        self.rect.y = self.game.player.y_real 

class Objethitbox(pygame.sprite.Sprite):
    def __init__(self,game,x,y,w,h):
        #Chargement image + initialisation
        super().__init__()
        self.game = game
        self.image = pygame.image.load("Img/objet/hitbox.png")
        self.image = pygame.transform.scale(self.image,(50 , 1))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.w = w
        self.rect.h = h   
        self.x_blit = 0
        self.y_blit = 0
        self.rect_blit = [self.rect.x + self.x_blit,self.rect.y,self.rect.w,self.rect.h]  
        self.y_real = y

class Mur(pygame.sprite.Sprite):
    def __init__(self,game,x,y,type=0):
        #Chargement image + initialisation
        super().__init__()
        self.game = game
        self.image = pygame.image.load("Img/objet/objet_vide.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(10 , 10)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.x_blit = 0    
        self.y_blit = 0
        self.rect_blit = [self.rect.x + self.x_blit,self.rect.y,self.rect.w,self.rect.h]  
        self.y_real = self.rect.y    
        self.type = type   
        self.mur_set_type() 
        
    def remove(self):
        #Suprime le mur
        self.game.salle.all_collide.remove(self)
        self.game.salle.all_mur.remove(self)

    def mur_set_type(self):
        #donne un type a l'objet
        if(self.type == 1 ):
            self.image = pygame.image.load("Img/objet/mur_gauche.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(314 , 658)).convert_alpha()
            self.rect = self.image.get_rect() 
        elif(self.type == 2 ):
            self.image = pygame.image.load("Img/objet/mur_droit.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(252,376)).convert_alpha()
            self.rect = self.image.get_rect() 
            self.rect.x = 1536 - self.rect.w
            self.rect.y = 864 - self.rect.h 
        elif(self.type == 3 ):
            self.image = pygame.image.load("Img/objet/mur_3.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(157 , 329)).convert_alpha()
        elif(self.type == 4 ):
            self.image = pygame.image.load("Img/objet/mur_4.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(157 , 329)).convert_alpha()
class Objet(pygame.sprite.Sprite):
    def __init__(self , game ,type=0):
        #Chargement image + initialisation
        super().__init__()
        self.game = game
        self.image = pygame.image.load("Img/objet/objet_vide.png")
        self.image = pygame.transform.scale(self.image,(50 , 50)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.rect.w = 50
        self.rect.h = 50
        self.x_blit = 0    
        self.y_blit = 0
        self.rect_blit = [self.rect.x + self.x_blit,self.rect.y,self.rect.w,self.rect.h]  
        self.y_real = self.rect.y    

        #Variables :
        self.type = type           #0:undefined ,  

    def remove(self):
        #Suprime la bouteille
        self.game.player.object_list.remove(self)

    def objet_set_type(self):
        #donne un type a l'objet
        if(self.type == 1 ):
            self.image = pygame.image.load("Img/objet/objet_1.png")
            self.image = pygame.transform.scale(self.image,(50 , 50)).convert_alpha()
        elif(self.type == 2 ):
            self.image = pygame.image.load("Img/objet/objet_2.png")
            self.image = pygame.transform.scale(self.image,(50 , 50)).convert_alpha()
        elif(self.type == 3 ):
            self.image = pygame.image.load("Img/objet/objet_3.png")
            self.image = pygame.transform.scale(self.image,(50 , 50)).convert_alpha()
        elif(self.type == 4 ):
            self.image = pygame.image.load("Img/objet/objet_4.png")
            self.image = pygame.transform.scale(self.image,(50 , 50)).convert_alpha()
class Coffre(pygame.sprite.Sprite):
    def __init__(self , game ,x ,y,type=0,contenu=0):
        #Chargement image + initialisation
        super().__init__()
        self.game = game
        self.image = pygame.image.load("Img/objet/objet_vide.png")
        self.image = pygame.transform.scale(self.image,(200 , 120)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.w = 130
        self.rect.h = 50
        self.x_blit = - 25   
        self.y_blit = - 60
        self.rect_blit = [self.rect.x + self.x_blit,self.rect.y,self.rect.w,self.rect.h]  
        self.y_real = 40 + self.rect.y    

        #Variables :
        self.type = type           #0:undefined ,  
        self.etat = 0              #0:fermé , 1:ouvert
        self.contenu = contenu           #0 rien

    def coffre_set_type(self):
        #donne un type au coffre
        if(self.type == 0 ):
            self.type = random.randint(0,100)
            if(self.type < 30):
                self.type == 1
            elif(self.type < 60):
                self.type == 2
            elif(self.type < 90):
                self.type == 3
            else : 
                self.type == 4
            
        if(self.type == 1 ):
            if(self.etat == 0):
                self.image = pygame.image.load("Img/objet/coffre_1_0.png")
                self.image = pygame.transform.scale(self.image,(200 , 120)).convert_alpha()
            elif(self.etat == 1):
                self.image = pygame.image.load("Img/objet/coffre_1_1.png")
                self.image = pygame.transform.scale(self.image,(200 , 120)).convert_alpha()
        elif(self.type == 2 ):
            if(self.etat == 0):
                self.image = pygame.image.load("Img/objet/coffre_2_0.png")
                self.image = pygame.transform.scale(self.image,(200 , 120)).convert_alpha()
            elif(self.etat == 1):
                self.image = pygame.image.load("Img/objet/coffre_2_1.png")
                self.image = pygame.transform.scale(self.image,(200 , 120)).convert_alpha() 
        elif(self.type == 3 ):
            if(self.etat == 0):
                self.image = pygame.image.load("Img/objet/coffre_3_0.png")
                self.image = pygame.transform.scale(self.image,(200 , 120)).convert_alpha()
            elif(self.etat == 1):
                self.image = pygame.image.load("Img/objet/coffre_3_1.png")
                self.image = pygame.transform.scale(self.image,(200 , 120)).convert_alpha() 
        elif(self.type == 4 ):
            if(self.etat == 0):
                self.image = pygame.image.load("Img/objet/coffre_4_0.png")
                self.image = pygame.transform.scale(self.image,(200 , 120)).convert_alpha() 
            elif(self.etat == 1):
                self.image = pygame.image.load("Img/objet/coffre_4_1.png")
                self.image = pygame.transform.scale(self.image,(200 , 120)).convert_alpha() 

    def remove(self):
        #Suprime la bouteille
        self.game.salle_all_coffres.remove(self)
        self.game.salle_all_sprites.remove(self)

    def check_coffre(self):
        #Check si colision avec un joueur, si oui , ouvre le coffre , et ajoute un objet au joueur
        if (self.game.check_collision_self(self,self.game.player) == True):
            if(self.etat == 0):
                self.etat = 1
                self.coffre_set_type()
                if(self.contenu == 1):
                    objet = Objet(self.game,1)
                    self.game.player.object_list.add(objet)
                elif(self.contenu == 2):
                    objet = Objet(self.game,2)
                    self.game.player.object_list.add(objet)
                elif(self.contenu == 3):
                    objet = Objet(self.game,3)
                    self.game.player.object_list.add(objet)
                elif(self.contenu == 4):
                    objet = Objet(self.game,4)
                    self.game.player.object_list.add(objet)

                #ajout des feuilles
                if(self.contenu == 10):
                    if(self.game.player.feuille_lvl < 0):
                        self.game.player.feuille_lvl = 0

                elif(self.contenu == 11):
                    if(self.game.player.feuille_lvl < 1):
                        self.game.player.feuille_lvl = 1

                elif(self.contenu == 12):
                    if(self.game.player.feuille_lvl < 2):
                        self.game.player.feuille_lvl = 2

                elif(self.contenu == 13):
                    if(self.game.player.feuille_lvl < 3):
                        self.game.player.feuille_lvl = 3

                elif(self.contenu == 14):
                    if(self.game.player.feuille_lvl < 4):
                        self.game.player.feuille_lvl = 4

                elif(self.contenu == 15):
                    if(self.game.player.feuille_lvl < 5):
                        self.game.player.feuille_lvl = 5

                elif(self.contenu == 16):
                    if(self.game.player.feuille_lvl < 6):
                        self.game.player.feuille_lvl = 6

                elif(self.contenu == 17):
                    if(self.game.player.feuille_lvl < 7):
                        self.game.player.feuille_lvl = 7

                elif(self.contenu == 18):
                    if(self.game.player.feuille_lvl < 8):
                        self.game.player.feuille_lvl = 8

                elif(self.contenu == 19):
                    if(self.game.player.feuille_lvl < 9):
                        self.game.player.feuille_lvl = 9

                elif(self.contenu == 20):
                    if(self.game.player.feuille_lvl < 10):
                        self.game.player.feuille_lvl = 10

                elif(self.contenu == 21):
                    if(self.game.player.feuille_lvl < 11):
                        self.game.player.feuille_lvl = 11

                elif(self.contenu == 22):
                    if(self.game.player.feuille_lvl < 12):
                        self.game.player.feuille_lvl = 12

                elif(self.contenu == 23):
                    if(self.game.player.feuille_lvl < 13):
                        self.game.player.feuille_lvl = 13

                elif(self.contenu == 24):
                    if(self.game.player.feuille_lvl < 14):
                        self.game.player.feuille_lvl = 14

                elif(self.contenu == 25):
                    if(self.game.player.feuille_lvl < 15):
                        self.game.player.feuille_lvl = 15

                elif(self.contenu == 26):
                    if(self.game.player.feuille_lvl < 16):
                        self.game.player.feuille_lvl = 16

                elif(self.contenu == 26):
                    if(self.game.player.feuille_lvl < 17):
                        self.game.player.feuille_lvl = 17

                elif(self.contenu == 28):
                    if(self.game.player.feuille_lvl < 18):
                        self.game.player.feuille_lvl = 18

                elif(self.contenu == 29):
                    if(self.game.player.feuille_lvl < 19):
                        self.game.player.feuille_lvl = 19

                elif(self.contenu == 30):
                    if(self.game.player.feuille_lvl < 20):
                        self.game.player.feuille_lvl = 20
        
class Meuble(pygame.sprite.Sprite):
    def __init__(self,game,x,y,type):
        #Chargement image + initialisation
        super().__init__()
        self.game = game
        self.image = pygame.image.load("Img/objet/objet_vide.png")
        self.image = pygame.transform.scale(self.image,(1,1)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.w = 100
        self.rect.h = 100
        self.x_blit = 0 
        self.y_blit = 0
        self.rect_blit = [self.rect.x + self.x_blit,self.rect.y,self.rect.w,self.rect.h]  
        self.y_real = self.rect.y 

        #Variables :
        self.type = type   
        self.meuble_set_type()        

    def meuble_set_type(self):
        #donne un type au coffre    
        if(self.type == 1 ):
            self.image = pygame.image.load("Img/objet/meuble_1.png")
            self.image = pygame.transform.scale(self.image,(300 , 150)).convert_alpha()
            self.rect.w = 300
            self.rect.h = 150
            self.y_real = self.rect.y + int(self.rect.h/2) + 40
        elif(self.type == 2 ):
            self.image = pygame.image.load("Img/objet/pillier.png")
            self.image = pygame.transform.scale(self.image,(90 , 378)).convert_alpha()
            self.rect.w = 90
            self.rect.h = 378
            self.y_real = self.rect.y + 378 

    def remove(self):
        #Suprime la bouteille
        self.game.salle_all_coffres.remove(self)
        self.game.salle_all_sprites.remove(self)
