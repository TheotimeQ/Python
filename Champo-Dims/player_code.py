import pygame
from vomis_code import Vomis
from objet_code import playerhitbox
from feuille_code import Feuille

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        #Chargement image + initialisation
        self.game = game
        self.imageN = pygame.image.load("Img/player/player0.png")
        self.imageD = pygame.image.load("Img/player/player1.png")
        self.imageG = pygame.image.load("Img/player/player2.png")
        self.imageNB = pygame.image.load("Img/player/player0B.png")
        self.imageDB = pygame.image.load("Img/player/player1B.png")
        self.imageGB = pygame.image.load("Img/player/player2B.png")
        self.imageN = pygame.transform.scale(self.imageN,(100 , 200)).convert_alpha()
        self.imageD = pygame.transform.scale(self.imageD,(100 , 200)).convert_alpha()
        self.imageG = pygame.transform.scale(self.imageG,(100 , 200)).convert_alpha()
        self.imageNB = pygame.transform.scale(self.imageNB,(100 , 200)).convert_alpha()
        self.imageDB = pygame.transform.scale(self.imageDB,(100 , 200)).convert_alpha()
        self.imageGB = pygame.transform.scale(self.imageGB,(100 , 200)).convert_alpha()
        self.image = self.imageN
        self.rect = self.image.get_rect()   #rect = hitbox
        self.rect.x = 500
        self.rect.y = 200
        self.rect.w = 60
        self.rect.h = 200
        self.x_blit = -20    #variable declage blit sur x
        self.y_blit = 0
        self.rect_blit = [self.rect.x + self.x_blit,self.rect.y,self.rect.w,self.rect.h]   #Rectangle pour blit decalé / hitbox
        self.image_bouteille_vide = pygame.image.load("Img/bouteille/bouteille_vide.png").convert_alpha()
        self.image_bouteille_vide = pygame.transform.scale(self.image_bouteille_vide,(50 , 100))
        self.rect_bouteille_vide = self.image_bouteille_vide.get_rect()
        self.rect_bouteille_vide.x = 500
        self.rect_bouteille_vide.y = 150
        self.y_real = 200 + self.rect.y

        #Initialisation variable
        self.etat = 0                 #0 haut ,1 bas, 1 droite , 2 gauche 
        self.bouteille_etat = 0       #0 pas de bouteille , 1 bouteille
        self.etat_vomis = 0           #0 vomis pas , 1 vomis
        self.alcool_lvl = 200
        self.alcool_origine = self.alcool_lvl
        self.max_alcool_lvl = 200
        self.time_recup_bouteille = 0
        self.bouteille_lvl = 0
        self.max_bouteille_lvl = 72
        self.bouteille_lvl_origine = self.max_bouteille_lvl
        self.time_bouteille_vide = 0
        self.bois_etat = 0 
        self.velocity = 5
        self.boisson_coef = 1.0
        self.alcool_coef = 1.0
        self.decuve_coef = 3.0
        self.time_decuve = 0
        self.time_boit = 0
        self.hitbox = playerhitbox(self.game)
        self.bouteille_color = (0,0,0)

        self.time_last_feuille = 0
        self.feuille_lvl = -1
        self.clef1 = 0
        self.clef2 = 0
        self.clef3 = 0
        self.clef4 = 0

        self.object_list = pygame.sprite.Group()
        print("Players initialized")

    #Gestion alcolisation
    def bar_bouteille_update(self,surface):
        #affiche une bare represantant l'alccol restant dans la bouteille
        bar_position = [self.game.affichage.screen_rect.w - 90,127,30,-self.bouteille_lvl]
        bar_color = self.bouteille_color
        self.rect_bouteille_vide.x = self.game.affichage.screen_rect.w - 100
        self.rect_bouteille_vide.y = 30

        if (self.bouteille_lvl > 0 and self.game.player.bouteille_etat == 1): 
            #Si la bouteille est pas vide , on boit
            pygame.draw.rect(surface,bar_color,bar_position)
            self.bouteille_lvl = self.bouteille_lvl_origine - self.boisson_coef*(self.game.time - self.time_recup_bouteille)
            self.game.affichage.screen.blit(self.image_bouteille_vide,self.rect_bouteille_vide)
            self.bois_etat = 1

        if (self.bouteille_lvl <= 0 and self.game.player.bouteille_etat == 1): 
            #Si bouteille vide, on la jette
            pygame.draw.rect(surface,bar_color,bar_position)
            self.time_bouteille_vide = self.game.time
            self.bouteille_lvl = 0
            self.bouteille_lvl_origine = self.max_bouteille_lvl
            self.alcool_origine = self.alcool_lvl
            self.time_recup_bouteille = 0
            self.game.player.bouteille_etat = 0
            self.bois_etat = 0
            self.time_decuve = self.game.time

    def bar_alcool_update(self,surface):
        #affiche une bare representant le niveau d'alcoolisation de Dims
        if (self.bois_etat == 1 and self.alcool_lvl < self.max_alcool_lvl):
            #Si on bois on s'alcolise tant que pas au max
            self.alcool_lvl = int((self.alcool_origine) + self.alcool_coef*(self.game.time - self.time_boit))
            self.time_decuve = self.game.time

        if (self.alcool_lvl > 0 and self.bois_etat == 0):
            #Si on est encore bourré et qu'on bois pas , on decuve
            self.alcool_lvl = int((self.alcool_origine) - self.decuve_coef*(self.game.time - self.time_decuve))
            self.time_boit = self.game.time

        back_bar_color = (255, 255, 255)
        back_bar_position = [20,225,20,-self.max_alcool_lvl]
        pygame.draw.rect(surface,back_bar_color,back_bar_position)
        bar_position = [20,225,20,-self.alcool_lvl]
        bar_color = (170, 85, 18)
        pygame.draw.rect(surface,bar_color,bar_position)
        
    def chaparde_alcool(self):
        #Quand un enemie touche dims , il bois sa bouteille
        self.bouteille_lvl_origine -= 0.1

    def pique_bouteille(self):
        #Quand un enemie touche dims , il lui pique sa bouteille
        if (self.bouteille_etat == 1):
            self.bouteille_etat = 0
            self.bois_etat = 0 
            self.alcool_origine = self.alcool_lvl
            self.time_bouteille_vide = self.game.time
                
    def lancer_vomis(self):
        #Vomir
        vomis = Vomis(self.game,self)
        self.game.salle.salle_all_vomis.add(vomis)
        self.game.salle.salle_all_sprites.add(vomis)
        if (self.alcool_lvl >= self.max_alcool_lvl):
            self.alcool_lvl -= 10
            self.alcool_origine = self.alcool_lvl
            self.time_boit = self.game.time

        if (self.bois_etat == 1 and self.alcool_lvl < self.max_alcool_lvl):
            self.alcool_origine -= 10 

        if (self.bois_etat == 0):
            self.alcool_origine -= 10 

    def lancer_feuille(self):
        #Lancer feuille
        if ( (self.game.time - self.time_last_feuille) > 1 and self.feuille_lvl >= 0):
            print("lance feuille")
            type_feuille = self.feuille_lvl
            moove = self.etat 
            self.time_last_feuille = self.game.time
            feuille = Feuille(self.game,self,type_feuille,moove)
            self.game.salle.salle_all_feuille.add(feuille)
            self.game.salle.salle_all_sprites.add(feuille)

    def move_right(self):
        #Deplacement droite
        self.rect.x += self.velocity
        self.y_real = 200 + self.rect.y
        self.hitbox.hitbox_update()
        if not (self.game.check_collision_group(self,self.game.salle.salle_all_collide)) :
            if not(self.game.check_collision_rect(self,self.game.salle.salle_all_mur)) :
                self.etat = 1
            else :
                if not (self.game.check_collision_mur(self.hitbox,self.game.salle.salle_all_mur)):
                    self.etat = 1
                else :
                    self.rect.x -= self.velocity
        else : 
            self.rect.x -= self.velocity
    
    def move_left(self):
        #Deplacement gauche
        self.rect.x -= self.velocity
        self.y_real = 200 + self.rect.y
        self.hitbox.hitbox_update()
        if not (self.game.check_collision_group(self,self.game.salle.salle_all_collide)) :
            if not(self.game.check_collision_rect(self,self.game.salle.salle_all_mur)) :
                self.etat = 2
            else :
                if not (self.game.check_collision_mur(self.hitbox,self.game.salle.salle_all_mur)):
                    self.etat = 2
                else :
                    self.rect.x += self.velocity
        else :
            self.rect.x += self.velocity

    def move_up(self):
        #Deplacement haut
        self.rect.y -= self.velocity
        self.y_real = 200 + self.rect.y
        self.hitbox.hitbox_update()
        if not (self.game.check_collision_group(self,self.game.salle.salle_all_collide)) :
            if not(self.game.check_collision_rect(self,self.game.salle.salle_all_mur)) :
                self.etat = 0
            else :
                if not (self.game.check_collision_mur(self.hitbox,self.game.salle.salle_all_mur)):
                    self.etat = 0
                else :
                    self.rect.y += self.velocity
                    self.y_real = 200 + self.rect.y
        else :
            self.rect.y += self.velocity
            self.y_real = 200 + self.rect.y
            
    def move_down(self):
        #Deplacement bas
        self.rect.y += self.velocity
        self.y_real = 200 + self.rect.y
        self.hitbox.hitbox_update()
        if not (self.game.check_collision_group(self,self.game.salle.salle_all_collide)) :
            if not(self.game.check_collision_rect(self,self.game.salle.salle_all_mur)) :
                self.etat = 3
            else :
                if not (self.game.check_collision_mur(self.hitbox,self.game.salle.salle_all_mur)):
                    self.etat = 3
                else :
                    self.rect.y -= self.velocity
                    self.y_real = 200 + self.rect.y
        else :
            self.rect.y -= self.velocity
            self.y_real = 200 + self.rect.y
            
    #Gestion du modele:
    def modele_update(self):
        if(self.etat == 0 or self.etat == 3):
            self.image = self.imageN
            if (self.bouteille_etat == 1):
                self.image = self.imageNB
        elif(self.etat == 1):
            self.image = self.imageD
            if (self.bouteille_etat == 1):
                self.image = self.imageDB
        elif(self.etat == 2):
            self.image = self.imageG
            if (self.bouteille_etat == 1):
                self.image = self.imageGB




    


