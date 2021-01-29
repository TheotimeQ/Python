import pygame
import random 

class tete_monster(pygame.sprite.Sprite):
    def __init__(self , monster):
        #initialise un monstre
        super().__init__()
        self.monster = monster

        self.image_tete_1 = pygame.image.load("Img/tetes/tete_vide.png")
        self.image_tete_1 = pygame.transform.scale(self.image_tete_1,(65 ,65)).convert_alpha()

        self.image = self.image_tete_1
        self.rect = self.image.get_rect()
        self.rect.x = self.monster.rect.x + 0
        self.rect.y = self.monster.rect.y + 0
        self.rect.w = 10
        self.rect.h = 10
        self.x_blit = 0
        self.y_blit = 0
        self.rect_blit = [self.rect.x + self.x_blit,self.rect.y + self.y_blit,self.rect.w,self.rect.h]
        self.y_real =  self.monster.y_real + 3

        #variable
        self.tete_variante = 0
           
    def tete_set_type(self):
        if(self.tete_variante == 0):
            self.tete_variante = random.randint(1,7)
            if(self.tete_variante == 1):
                self.image_tete_1 = pygame.image.load("Img/tetes/tete_1.png")
                self.image_tete_1 = pygame.transform.scale(self.image_tete_1,(65 ,65)).convert_alpha()
                self.image = self.image_tete_1
                self.rect = self.image.get_rect()
                self.rect.x = self.monster.rect.x - 0
                self.rect.y = self.monster.rect.y + 0
                self.x_blit = - 12
                self.y_blit = + 20
        
            if(self.tete_variante == 2):
                self.image_tete_2 = pygame.image.load("Img/tetes/tete_2.png")
                self.image_tete_2 = pygame.transform.scale(self.image_tete_2,(50 ,60)).convert_alpha()
                self.image = self.image_tete_2
                self.rect = self.image.get_rect()
                self.rect.x = self.monster.rect.x + 0
                self.rect.y = self.monster.rect.y + 0
                self.x_blit = - 20
                self.y_blit = + 10 

            if(self.tete_variante == 3):
                self.image_tete_3 = pygame.image.load("Img/tetes/tete_3.png")
                self.image_tete_3 = pygame.transform.scale(self.image_tete_3,(50 ,60)).convert_alpha()
                self.image = self.image_tete_3
                self.rect = self.image.get_rect()
                self.rect.x = self.monster.rect.x + 0
                self.rect.y = self.monster.rect.y + 0
                self.x_blit = - 15
                self.y_blit = + 5

            if(self.tete_variante == 4):
                self.image_tete_4 = pygame.image.load("Img/tetes/tete_4.png")
                self.image_tete_4 = pygame.transform.scale(self.image_tete_4,(50 ,60)).convert_alpha()
                self.image = self.image_tete_4
                self.rect = self.image.get_rect()
                self.rect.x = self.monster.rect.x + 0
                self.rect.y = self.monster.rect.y + 0
                self.x_blit = - 8
                self.y_blit = + 4

            if(self.tete_variante == 5):
                self.image_tete_5 = pygame.image.load("Img/tetes/tete_5.png")
                self.image_tete_5 = pygame.transform.scale(self.image_tete_5,(50 ,60)).convert_alpha()
                self.image = self.image_tete_5
                self.rect = self.image.get_rect()
                self.rect.x = self.monster.rect.x + 0
                self.rect.y = self.monster.rect.y + 0
                self.x_blit = - 10
                self.y_blit = + 8

            if(self.tete_variante == 6):
                self.image_tete_6 = pygame.image.load("Img/tetes/tete_6.png")
                self.image_tete_6 = pygame.transform.scale(self.image_tete_6,(50 ,60)).convert_alpha()
                self.image = self.image_tete_6
                self.rect = self.image.get_rect()
                self.rect.x = self.monster.rect.x + 0
                self.rect.y = self.monster.rect.y + 0
                self.x_blit = - 12
                self.y_blit = + 3

            if(self.tete_variante == 7):
                self.image_tete_7 = pygame.image.load("Img/tetes/tete_7.png")
                self.image_tete_7 = pygame.transform.scale(self.image_tete_7,(50 ,60)).convert_alpha()
                self.image = self.image_tete_7
                self.rect = self.image.get_rect()
                self.rect.x = self.monster.rect.x + 0
                self.rect.y = self.monster.rect.y + 0
                self.x_blit = - 8
                self.y_blit = + 3

            self.rect.w = 1
            self.rect.h = 1

            self.rect_blit = [self.rect.x + self.x_blit,self.rect.y + self.y_blit,self.rect.w,self.rect.h]
            self.y_real =  self.monster.y_real + 3


    def tete_update(self):
        self.rect.x = self.monster.rect.x 
        self.rect.y = self.monster.rect.y 
        self.rect_blit = [self.rect.x + self.x_blit,self.rect.y + self.y_blit,self.rect.w,self.rect.h]
        self.y_real =  self.monster.y_real + 3



        





    

        

        