import pygame
import random 

class Bouteille(pygame.sprite.Sprite):
    def __init__(self , game ,x ,y,type=0):
        #Chargement image + initialisation
        super().__init__()
        self.game = game
        self.image = pygame.image.load("Img/bouteille/bouteille.png")
        self.image = pygame.transform.scale(self.image,(25 , 50)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.w = 25
        self.rect.h = 50
        self.x_blit = 0    #variable declage blit sur x
        self.y_blit = 0
        self.rect_blit = [self.rect.x + self.x_blit,self.rect.y,self.rect.w,self.rect.h]  
        self.y_real = 50 + self.rect.y    

        #Variables :
        self.type = type           #0:undefined
        self.boisson_coef = 1
        self.alcool_coef = 1
        self.decuve_coef = 1

    def bouteille_set_type(self):
        #donne un type a la bouteille
        if(self.type == 0 ):
            self.type = random.randint(0,100)
            if(self.type < 40):
                self.type == 1
            elif(self.type < 60):
                self.type == 2
            elif(self.type < 80):
                self.type == 3
            elif(self.type < 10):
                self.type == 4
            elif(self.type < 5):
                self.type == 5
            else : 
                self.type == 6
            
        if(self.type == 1 ):
            self.image = pygame.image.load("Img/bouteille/bouteille_1.png")
            self.image = pygame.transform.scale(self.image,(25 , 50)).convert_alpha() 
            self.boisson_coef = 3.0
            self.alcool_coef = 3.0
            self.decuve_coef = 3.0
            self.color = (234, 123, 12 )
        
        if(self.type == 2 ):
            self.image = pygame.image.load("Img/bouteille/bouteille_2.png")
            self.image = pygame.transform.scale(self.image,(25 , 50)).convert_alpha()
            self.boisson_coef = 2.0
            self.alcool_coef = 4.0
            self.decuve_coef = 3.0
            self.color = (236, 219, 13)

        if(self.type == 3 ):
            self.image = pygame.image.load("Img/bouteille/bouteille_3.png")
            self.image = pygame.transform.scale(self.image,(25 , 50)).convert_alpha()
            self.boisson_coef = 1.0
            self.alcool_coef = 1.0
            self.decuve_coef = 4.0
            self.color = (18, 63, 239)
        
        if(self.type == 4 ):
            self.image = pygame.image.load("Img/bouteille/bouteille_4.png")
            self.image = pygame.transform.scale(self.image,(25 , 50)).convert_alpha()
            self.boisson_coef = 3.0
            self.alcool_coef = 5.0
            self.decuve_coef = 2.0
            self.color = (219, 18, 239)
        
        if(self.type == 5 ):
            self.image = pygame.image.load("Img/bouteille/bouteille_5.png")
            self.image = pygame.transform.scale(self.image,(25 , 50)).convert_alpha()
            self.boisson_coef = 2.0
            self.alcool_coef = 10.0
            self.decuve_coef = 1.0
            self.color = (239, 18, 18)

        if(self.type == 6 ):
            self.image = pygame.image.load("Img/bouteille/bouteille_6.png")
            self.image = pygame.transform.scale(self.image,(25 , 50)).convert_alpha()
            self.boisson_coef = 10.0
            self.alcool_coef = 1
            self.decuve_coef = 10
            self.color = (62, 239, 18)

    def remove(self):
        #Suprime la bouteille
        self.game.salle.salle_all_bouteilles.remove(self)
        self.game.salle.salle_all_sprites.remove(self)

    def check_bouteille(self):
        #Check si colision avec un joueur, si oui , detruit la bouteille, update etat player, et rempli sa bouteille
        if (self.game.check_collision_self(self,self.game.player) == True):
            self.remove()

            self.game.player.bouteille_etat = 1
            self.game.player.bouteille_lvl = self.game.player.max_bouteille_lvl
            self.game.player.bouteille_lvl_origine = self.game.player.max_bouteille_lvl
            
            self.game.player.time_recup_bouteille = self.game.time
            self.game.player.alcool_origine = self.game.player.alcool_lvl

            self.game.player.time_boit = self.game.time

            self.game.player.boisson_coef = self.boisson_coef
            self.game.player.alcool_coef = self.alcool_coef
            self.game.player.decuve_coef = self.decuve_coef
            self.game.player.bouteille_color = self.color 
            #transmission color joueur bar acoll
            
            
        