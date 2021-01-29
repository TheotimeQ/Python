import pygame
import random 
from tete_monster_code import tete_monster
from objet_code import Objethitbox

class Monster(pygame.sprite.Sprite):
    def __init__(self ,game ,salle ,type ,x ,y,x1=0,y1=0,x2=0,y2=0):
        #initialise un monstre
        super().__init__()
        self.game = game
        self.salle = salle

        self.image = pygame.image.load("Img/monster/monster_vide.png")
        self.image = pygame.transform.scale(self.image,(1,1)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.w = 30
        self.rect.h = 180
        self.x_blit = -35    #variable declage blit sur x
        self.y_blit = -30
        self.rect_blit = [self.rect.x + self.x_blit,self.rect.y + self.y_blit,self.rect.w,self.rect.h]
        self.y_real = 200 + self.rect.y - 30

        #variable
        self.velocity = 1
        self.monster_variante = type     
        self.dans_vomi = 0
        self.bouteille_etat = 0
        self.but_x = random.randint(317,1250)
        self.but_y = random.randint(self.game.salle.min_y + 10,self.game.salle.max_y - 10)

        self.x_but1 = x1
        self.y_but1 = y1
        self.x_but2 = x2
        self.y_but2 = y2
        self.actualgoal = 1

        self.max_health = -1
        self.health = -1
        self.health_bar = 0

        self.taunt = 0

        self.tete = tete_monster(self)
        self.salle.salle_all_monster_tete.add(self.tete)
        self.salle.salle_all_sprites.add(self.tete)
        self.monster_load_model()
        
    def remove(self):
        #surprime le monstre et sa tete
        self.salle.salle_all_monster.remove(self)
        self.salle.salle_all_collide.remove(self)
        self.salle.salle_all_sprites.remove(self)
        self.salle.salle_all_sprites.remove(self.tete)
        self.salle.salle_all_monster_tete.remove(self.tete)
        print("monster removed")

    def monster_load_model(self):
        if(self.monster_variante == 1):
            #Eleve 1
            self.image_monster_1 = pygame.image.load("Img/monster/monster_1.png")
            self.image_monster_1_vomi = pygame.image.load("Img/monster/monster_1_vomi.png")
            self.image_monster_1_bouteille = pygame.image.load("Img/monster/monster_1_bouteille.png")
            self.image_monster_1_bouteille_vomi = pygame.image.load("Img/monster/monster_1_bouteille_vomi.png")
            self.image_monster_1 = pygame.transform.scale(self.image_monster_1,(100 ,200)).convert_alpha()
            self.image_monster_1_vomi = pygame.transform.scale(self.image_monster_1_vomi,(100 , 200)).convert_alpha()
            self.image_monster_1_bouteille = pygame.transform.scale(self.image_monster_1_bouteille,(100 , 200)).convert_alpha()
            self.image_monster_1_bouteille_vomi = pygame.transform.scale(self.image_monster_1_bouteille_vomi,(100 , 200)).convert_alpha()

        if(self.monster_variante == 2):
            #Eleve 2 
            self.image_monster_2 = pygame.image.load("Img/monster/monster_2.png")
            self.image_monster_2_vomi = pygame.image.load("Img/monster/monster_2_vomi.png")
            self.image_monster_2 = pygame.transform.scale(self.image_monster_2,(100 ,200)).convert_alpha()
            self.image_monster_2_vomi = pygame.transform.scale(self.image_monster_2_vomi,(100 , 200)).convert_alpha()

        if(self.monster_variante == 3):
            #Eleve 3
            self.image_monster_3 = pygame.image.load("Img/monster/monster_3.png")
            self.image_monster_3_vomi = pygame.image.load("Img/monster/monster_3_vomi.png")
            self.image_monster_3 = pygame.transform.scale(self.image_monster_3,(100 ,200)).convert_alpha()
            self.image_monster_3_vomi = pygame.transform.scale(self.image_monster_3_vomi,(100 , 200)).convert_alpha()

        if(self.monster_variante == 4):
            #Pion
            self.image_monster_4 = pygame.image.load("Img/monster/monster_4.png")
            self.image_monster_4_vomi = pygame.image.load("Img/monster/monster_4_vomi.png")
            self.image_monster_4 = pygame.transform.scale(self.image_monster_4,(100 ,200)).convert_alpha()
            self.image_monster_4_vomi = pygame.transform.scale(self.image_monster_4_vomi,(100 , 200)).convert_alpha()
            self.max_health = 75
            self.health = self.max_health
            self.health_bar_position = [self.rect.x,self.rect.y,self.health,10]
            self.health_bar_color = (246, 9, 9)
            self.health_bar_position_back = [self.rect.x,self.rect.y,self.max_health,10]
            self.health_bar_color_back = (255, 255, 255)

        if(self.monster_variante == 5):
            #Prof
            self.image_monster_5 = pygame.image.load("Img/monster/monster_5.png")
            self.image_monster_5_vomi = pygame.image.load("Img/monster/monster_5_vomi.png")
            self.image_monster_5 = pygame.transform.scale(self.image_monster_5,(100 ,200)).convert_alpha()
            self.image_monster_5_vomi = pygame.transform.scale(self.image_monster_5_vomi,(100 , 200)).convert_alpha()
            self.max_health = 150
            self.health = self.max_health
            self.health_bar_position = [self.rect.x,self.rect.y,self.health,10]
            self.health_bar_color = (246, 9, 9)
            self.health_bar_position_back = [self.rect.x,self.rect.y,self.max_health,10]
            self.health_bar_color_back = (255, 255, 255)

        if(self.monster_variante == 6):
            self.image_monster_2 = pygame.image.load("Img/monster/monster_2.png")

        if(self.monster_variante == 7):
            self.image_monster_2 = pygame.image.load("Img/monster/monster_2.png")

        if(self.monster_variante == 8):
            self.image_monster_2 = pygame.image.load("Img/monster/monster_2.png")

        if(self.monster_variante == 9):
            self.image_monster_2 = pygame.image.load("Img/monster/monster_2.png")
            
    def monster_set_type(self):
        #Gere le modele en fonction de l'etat et le type du monstre
        # 1: Eleve 1 , 2: Eleve 2 , 3:Eleve 3, 4: Eleve 4 , 5: Eleve 5 , 6:Prof ,7:Pion ,8:Agent Service ,9:Boss
        if(self.monster_variante == 1):
            #Eleve 1
            if(self.dans_vomi == 0):
                self.velocity = 2
                if(self.bouteille_etat == 1):
                    self.image = self.image_monster_1_bouteille
                else :
                    self.image = self.image_monster_1

            elif(self.dans_vomi == 1):
                self.velocity = 1
                if(self.bouteille_etat == 1):
                    self.image = self.image_monster_1_bouteille_vomi
                    self.velocity = 3
                else :
                    self.image = self.image_monster_1_vomi

        elif(self.monster_variante == 2):
            #Eleve 2
            if(self.dans_vomi == 0):
                self.image = self.image_monster_2
                self.velocity = 1
            elif(self.dans_vomi == 1):
                self.image = self.image_monster_2_vomi
                self.velocity = 0
        
        elif(self.monster_variante == 3):
            #Eleve 3
            if(self.dans_vomi == 0):
                self.image = self.image_monster_3
                self.velocity = 1
            elif(self.dans_vomi == 1):
                self.image = self.image_monster_3_vomi
                self.velocity = 2

        elif(self.monster_variante == 4):
            #Pion
            self.tete.tete_variante = 100
            if(self.dans_vomi == 0):
                self.image = self.image_monster_4
                self.velocity = 1
            elif(self.dans_vomi == 1):
                self.image = self.image_monster_4_vomi
                self.velocity = 2

        elif(self.monster_variante == 5):
            self.tete.tete_variante = 100
            if(self.dans_vomi == 0):
                self.image = self.image_monster_5
                self.velocity = 2
            elif(self.dans_vomi == 1):
                self.image = self.image_monster_5_vomi
                self.velocity = 1

        elif(self.monster_variante == 7):
            if(self.dans_vomi == 0):
                self.image = self.image_monster_1
                self.velocity = 1
            elif(self.dans_vomi == 1):
                self.image = self.image_monster_1
                self.velocity = 1

        elif(self.monster_variante == 8):
            if(self.dans_vomi == 0):
                self.image = self.image_monster_1
                self.velocity = 1
            elif(self.dans_vomi == 1):
                self.image = self.image_monster_1
                self.velocity = 1

        elif(self.monster_variante == 9):
            if(self.dans_vomi == 0):
                self.image = self.image_monster_1
                self.velocity = 1
            elif(self.dans_vomi == 1):
                self.image = self.image_monster_1
                self.velocity = 1

    def monster_dans_vomis(self):
        #Modifie le monstre s'il est dans le vomis
        if(self.monster_variante == 142):
            self.taunt = self.taunt

    def update_health_bare(self):
        if(self.monster_variante in (4,5,6)):
            self.health_bar_position = [self.rect.x - 40 ,self.rect.y + 20 ,self.health,10]
            self.health_bar_position_back = [self.rect.x - 40,self.rect.y + 20,self.max_health,10]
            if (self.health <= 0 ):
                self.remove()

    def forward (self):
        #gere les deplacement en fonction du type
        if (self.monster_variante == 1 ):
            #Si c'est un monstre du type 1 et qu'il est pas dans le vomis, il se deplace ...
            if not (self.game.check_collision_self(self,self.game.player)):
                if (self.bouteille_etat == 0):
                    if (self.rect.x > self.game.player.rect.x):
                        self.move_left()
                    elif (self.rect.x < self.game.player.rect.x):
                        self.move_right()
                    if (self.y_real > self.game.player.y_real):
                        self.move_up()
                    elif (self.y_real < self.game.player.y_real):
                        self.move_down()
                if (self.bouteille_etat == 1):
                    if (self.rect.x > self.game.player.rect.x):
                        self.rect.x += 0
                    elif (self.rect.x < self.game.player.rect.x):
                        self.rect.x -= 0
            else : 
                if (self.game.player.bouteille_etat == 1):
                    self.game.player.pique_bouteille()
                    self.bouteille_etat = 1

        elif(self.monster_variante == 2 and self.dans_vomi == 0):
            #Si c'est un monstre du type 2 et qu'il est pas dans le vomis, il se deplace ...
            if not (self.game.check_collision_self(self,self.game.player)):
                if ( self.rect.x < self.but_x-2 or self.rect.x > self.but_x + 2 or self.y_real < self.but_y - 2 or self.y_real > self.but_y + 2):
                    if (self.rect.x > self.but_x + 1):
                        self.rect.x -= self.velocity 
                        if (self.game.check_collision_meuble(self,self.game.salle.salle_all_meuble)) :
                            self.rect.x += self.velocity 
                            self.but_x = random.randint(50,1450)
                            self.but_y = random.randint(self.game.salle.min_y + 10,self.game.salle.max_y - 10)
                    if (self.rect.x < self.but_x - 1):
                        self.rect.x += self.velocity 
                        if (self.game.check_collision_meuble(self,self.game.salle.salle_all_meuble)) :
                            self.rect.x -= self.velocity 
                            self.but_x = random.randint(50,1450)
                            self.but_y = random.randint(self.game.salle.min_y + 10,self.game.salle.max_y - 10)

                    if (self.y_real > self.but_y + 1):
                        self.rect.y = self.rect.y - self.velocity
                        self.y_real = 200 + self.rect.y - 30
                        if (self.game.check_collision_meuble(self,self.game.salle.salle_all_meuble)) :
                            self.rect.y =  self.rect.y + self.velocity
                            self.y_real = 200 + self.rect.y - 30
                            self.but_x = random.randint(50,1450)
                            self.but_y = random.randint(self.game.salle.min_y + 10,self.game.salle.max_y - 10)

                    if (self.y_real < self.but_y - 1):
                        self.rect.y = self.rect.y + self.velocity 
                        self.y_real = 200 + self.rect.y - 30
                        if (self.game.check_collision_meuble(self,self.game.salle.salle_all_meuble)) :
                            self.rect.y =  self.rect.y - self.velocity 
                            self.y_real = 200 + self.rect.y - 30
                            self.but_x = random.randint(50,1450)
                            self.but_y = random.randint(self.game.salle.min_y + 10,self.game.salle.max_y - 10)
                else : 
                    self.but_x = random.randint(50,1450)
                    self.but_y = random.randint(self.game.salle.min_y + 10,self.game.salle.max_y - 10)
            else : 
                self.game.player.chaparde_alcool()

        elif(self.monster_variante == 3 and self.dans_vomi == 0):
            #Monstre 3 suis un chemin precis
            if not (self.game.check_collision_self(self,self.game.player)):
                if (self.actualgoal == 1):
                    if ( self.rect.x < self.x_but1-2 or self.rect.x > self.x_but1 + 2 or self.y_real < self.y_but1 - 2 or self.y_real > self.y_but1 + 2):
                        if (self.rect.x > self.x_but1 + 1):
                            self.rect.x -= self.velocity
                        if (self.rect.x < self.x_but1 - 1):
                            self.rect.x += self.velocity
                        if (self.y_real > self.y_but1 + 1):
                            self.rect.y -= self.velocity
                            self.y_real = 200 + self.rect.y - 30
                        if (self.y_real < self.y_but1 - 1):
                            self.rect.y += self.velocity
                            self.y_real = 200 + self.rect.y - 30
                    else :
                        self.actualgoal = 2

                else :
                    if ( self.rect.x < self.x_but2-2 or self.rect.x > self.x_but2 + 2 or self.y_real < self.y_but2 - 2 or self.y_real > self.y_but2 + 2):
                        if (self.rect.x > self.x_but2 + 1):
                            self.rect.x -= self.velocity
                        if (self.rect.x < self.x_but2 - 1):
                            self.rect.x += self.velocity
                        if (self.y_real > self.y_but2 + 1):
                            self.rect.y -= self.velocity
                            self.y_real = 200 + self.rect.y - 30
                        if (self.y_real < self.y_but2 - 1):
                            self.rect.y += self.velocity
                            self.y_real = 200 + self.rect.y - 30
                    else :
                        self.actualgoal = 1

            else : 
                self.game.player.chaparde_alcool()

        elif(self.monster_variante == 4):
            #Monstre 3 suis un chemin precis
            if not (self.game.check_collision_self(self,self.game.player)):
                if ( (self.game.player.rect.x < self.rect.x + 400 and self.game.player.rect.x > self.rect.x - 400) and (self.game.player.y_real > self.y_real - 300 and self.game.player.y_real < self.y_real + 300)):
                    if (self.rect.x > self.game.player.rect.x):
                        self.move_left()
                    elif (self.rect.x < self.game.player.rect.x):
                        self.move_right()
                    if (self.y_real > self.game.player.y_real):
                        self.move_up()
                    elif (self.y_real < self.game.player.y_real):
                        self.move_down()
            else : 
                self.game.salle = self.game.salle_list[3]
                self.game.player.rect.x = 1000
                self.game.player.rect.y = 500

        elif(self.monster_variante == 5):
            #Monstre 3 suis un chemin precis
            if not (self.game.check_collision_self(self,self.game.player)):
                if (self.actualgoal == 1):
                    if ( self.rect.x < self.x_but1-2 or self.rect.x > self.x_but1 + 2 or self.y_real < self.y_but1 - 2 or self.y_real > self.y_but1 + 2):
                        if (self.rect.x > self.x_but1 + 1):
                            self.rect.x -= self.velocity
                        if (self.rect.x < self.x_but1 - 1):
                            self.rect.x += self.velocity
                        if (self.y_real > self.y_but1 + 1):
                            self.rect.y -= self.velocity
                            self.y_real = 200 + self.rect.y - 30
                        if (self.y_real < self.y_but1 - 1):
                            self.rect.y += self.velocity
                            self.y_real = 200 + self.rect.y - 30
                    else :
                        self.actualgoal = 2
                else :
                    if ( self.rect.x < self.x_but2-2 or self.rect.x > self.x_but2 + 2 or self.y_real < self.y_but2 - 2 or self.y_real > self.y_but2 + 2):
                        if (self.rect.x > self.x_but2 + 1):
                            self.rect.x -= self.velocity
                        if (self.rect.x < self.x_but2 - 1):
                            self.rect.x += self.velocity
                        if (self.y_real > self.y_but2 + 1):
                            self.rect.y -= self.velocity
                            self.y_real = 200 + self.rect.y - 30
                        if (self.y_real < self.y_but2 - 1):
                            self.rect.y += self.velocity
                            self.y_real = 200 + self.rect.y - 30
                    else :
                        self.actualgoal = 1
            else : 
                self.game.salle = self.game.salle_list[10]
                self.game.player.rect.x = 1000
                self.game.player.rect.y = 500

            if(self.taunt == 1):
                self.taunt = 10
                self.game.salle.set_monster(4,self.rect.x + 30,self.rect.y)
                self.game.salle.set_monster(4,self.rect.x - 30,self.rect.y)
            
        #Dans tout les cas , s'il sort du cadre il est suprimé
        if (self.rect.x < self.game.salle.min_x or self.rect.x > self.game.salle.max_x  or self.y_real < self.game.salle.min_y - 10 or self.y_real > self.game.salle.max_y + 10):
            self.remove()
            print("Monster out")

    def move_right(self):
        #Deplacement droite
        self.rect.x += self.velocity 
        self.y_real = 200 + self.rect.y - 30
        if (self.game.check_collision_meuble(self,self.game.salle.salle_all_meuble)) :
            self.rect.x -= self.velocity 
    
    def move_left(self):
        #Deplacement gauche
        self.rect.x -= self.velocity 
        self.y_real = 200 + self.rect.y - 30
        if (self.game.check_collision_meuble(self,self.game.salle.salle_all_meuble)) :
            self.rect.x += self.velocity 

    def move_up(self):
        #Deplacement haut
        self.rect.y = self.rect.y - self.velocity
        self.y_real = 200 + self.rect.y - 30
        if (self.game.check_collision_meuble(self,self.game.salle.salle_all_meuble)) :
            self.rect.y =  self.rect.y + self.velocity
            self.y_real = 200 + self.rect.y - 30
            
    def move_down(self):
        #Deplacement bas
        self.rect.y = self.rect.y + self.velocity 
        self.y_real = 200 + self.rect.y - 30
        if (self.game.check_collision_meuble(self,self.game.salle.salle_all_meuble)) :
            self.rect.y =  self.rect.y - self.velocity 
            self.y_real = 200 + self.rect.y - 30
            
        