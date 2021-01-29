import pygame

import time
from time import time

from player_code import Player 
from monster_code import Monster
from bouteille_code import Bouteille
from affichage_code import Affichage
from salles_code import Salle
from objet_code import Coffre
from objet_code import Objet

class Game:
    def __init__(self):
        #Initialise tt le jeux 
        self.running = True
        self.affichage = Affichage(self)
        self.player = Player(self)
        self.salle = Salle(self,1)
        
        self.salle_list = [0,self.salle]
        for k in range (2,50):
            salle = Salle(self,k)
            salle.salle_init()
            self.salle_list.append(salle) 

        print("Toutes les salles initialisée")
        self.pressed = {}
        self.clock = pygame.time.Clock()

        self.time_init = time()
        self.time = 0
        self.pause = True
        self.restart = False

        self.salle.salle_init()
        self.salle = self.salle_list[3]
        self.affichage.affichage_update(2)
        print("Game initialized")

    def check_collision_group(self ,sprite1, group): 
        #Detecte la colision en prenant compte les plans (sprite vs groupe de sprite)
        L = []
        for sprite2 in group :
            if (sprite2.y_real - 20 < sprite1.y_real and sprite1.y_real < sprite2.y_real + 20):
                if (sprite1.rect.colliderect(sprite2.rect)):
                    L.append(sprite2)
        return L

    def check_collision_meuble(self ,sprite1, group): 
        #Detecte la colision en prenant compte les plans (sprite vs groupe de sprite)
        L = []
        for sprite2 in group :
            if (sprite2.y_real - 30 < sprite1.y_real and sprite1.y_real < sprite2.y_real + 30):
                if (sprite1.rect.colliderect(sprite2.rect)):
                    L.append(sprite2)
        return L

    def check_collision_self(self ,sprite1, sprite2):
        #Detecte la colision en prenant compte les plans (sprite vs sprite)
        if (sprite2.y_real - 20 < sprite1.y_real and sprite1.y_real < sprite2.y_real + 20):                                                                         
            if (sprite1.rect.colliderect(sprite2.rect)):
                return True

    def check_collision_rect(self ,sprite1, group):
        #Detecte la colision d'un rect avec un groupe de rect
        L = []
        for sprite2 in group :
            if (sprite1.rect.colliderect(sprite2.rect)):
                L.append(sprite2)
        return L

    def check_collision_mur(self ,sprite1, group):
        #Detecte la colision en prenant compte les plans (sprite vs sprite)                                                                                         
        L = []
        for sprite2 in group :
            if (pygame.sprite.collide_mask(sprite1, sprite2)):
                L.append(sprite2)
        return L

    def time_update(self):
        #Mets a jour le temps
        self.time = time() - self.time_init

    def framerate_update(self):
        #Affiche le framerate
        fps = self.clock.get_fps()
        myfont = pygame.font.SysFont("Times New Roman", 20)
        frame_display = myfont.render(str("FPS:" + str(int(fps))),1, (255, 255, 255))
        self.affichage.screen.blit(frame_display, (50,20))

    def deplacement(self):
        #bouge le player
        if (self.player.etat_vomis == 0):
            if (self.pressed.get(pygame.K_RIGHT)):
                if (self.pressed.get(pygame.K_DOWN) and self.player.rect.x <  self.salle.max_x):
                    if (self.player.y_real < self.salle.max_y):
                        self.player.move_down()
                        self.player.move_right()
                        self.player.etat = 1
                elif (self.pressed.get(pygame.K_UP) and self.player.rect.x <  self.salle.max_x):
                    if (self.player.y_real > self.salle.min_y):
                        self.player.move_up()
                        self.player.move_right()
                        self.player.etat = 1
                elif (self.player.rect.x <  self.salle.max_x ):
                        self.player.move_right()
                        self.player.etat = 1
            elif (self.pressed.get(pygame.K_LEFT)):
                if (self.pressed.get(pygame.K_DOWN)):
                    if (self.player.y_real < self.salle.max_y and self.player.rect.x > self.salle.min_x):
                        self.player.move_down()
                        self.player.move_left()
                        self.player.etat = 2
                elif (self.pressed.get(pygame.K_UP)):
                    if (self.player.y_real > self.salle.min_y and self.player.rect.x > self.salle.min_x):
                        self.player.move_up()
                        self.player.move_left()
                        self.player.etat = 2
                elif (self.player.rect.x > self.salle.min_x ):
                        self.player.move_left()
                        self.player.etat = 2
            elif (self.pressed.get(pygame.K_DOWN)):
                if (self.player.y_real < self.salle.max_y):
                    self.player.move_down()
            elif (self.pressed.get(pygame.K_UP)):
                if (self.player.y_real > self.salle.min_y):
                    self.player.move_up()

    def evenements(self):
        #update la list des evenement clavier
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                self.running = False
                pygame.quit()
                print("Fermeture du jeu")

            elif (event.type == pygame.KEYDOWN):
                self.pressed[event.key] = True
                if (event.key == pygame.K_SPACE):
                    self.player.lancer_vomis()
                if (event.key == pygame.K_f):
                    self.player.lancer_feuille()
                if (event.key == pygame.K_ESCAPE):
                    self.pause = True
                    print("Pause")
            elif (event.type == pygame.KEYUP):
                self.pressed[event.key] = False

            elif (event.type == pygame.MOUSEBUTTONDOWN):
                if self.affichage.play_button_rect.collidepoint(event.pos):
                    self.pause = False
                if self.affichage.quit_button_rect.collidepoint(event.pos):
                    self.running = False
                    pygame.quit()
                    print("Fermeture du jeu")
                if self.affichage.restart_button_rect.collidepoint(event.pos):
                    self.restart = True



        
            