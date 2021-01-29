import pygame

class Vomis(pygame.sprite.Sprite):
    def __init__(self, game ,player):
        #Initialise un vomis
        super().__init__()
        self.game = game
        self.player = player

        self.imageD_0 = pygame.image.load("Img/vomis/vomiD_0.png")
        self.imageD_1 = pygame.image.load("Img/vomis/vomiD_1.png")
        self.imageD_2 = pygame.image.load("Img/vomis/vomiD_2.png")
        self.imageD_3 = pygame.image.load("Img/vomis/vomiD_3.png")
        self.image_solD = pygame.image.load("Img/vomis/vomiD_sol.png")

        self.imageG_0 = pygame.image.load("Img/vomis/vomiG_0.png")
        self.imageG_1 = pygame.image.load("Img/vomis/vomiG_1.png")
        self.imageG_2 = pygame.image.load("Img/vomis/vomiG_2.png")
        self.imageG_3 = pygame.image.load("Img/vomis/vomiG_3.png") 
        self.image_solG = pygame.image.load("Img/vomis/vomiG_sol.png")

        self.imageF_0 = pygame.image.load("Img/vomis/vomiF_0.png")
        self.imageF_1 = pygame.image.load("Img/vomis/vomiF_1.png")
        self.imageF_2 = pygame.image.load("Img/vomis/vomiF_2.png")
        self.imageF_3 = pygame.image.load("Img/vomis/vomiF_3.png") 
        self.image_solF = pygame.image.load("Img/vomis/vomiF_sol.png")

        self.image = pygame.image.load("Img/vomis/vomi_vide.png")
        self.image = pygame.transform.scale(self.image,(60,60)).convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.x = self.player.rect.x
        self.rect.y = self.player.rect.y 
        self.rect.w = 80
        self.rect.h = 160
        self.x_blit = 0    #variable declage blit sur x (affichage uniquement)
        self.y_blit = 0
        self.rect_blit = [self.rect.x + self.x_blit,self.rect.y,self.rect.w,self.rect.h]   #Rectangle pour blit decalé / hitbox
        self.y_real = self.player.y_real 

        #Variable 
        self.time_debut_vomis = self.player.game.time
        
    def remove(self):
        #suprrime le vomis
        self.game.salle.salle_all_vomis.remove(self)
        self.game.salle.salle_all_sprites.remove(self)

    def move(self):
        #Update l'image du vomis en fonction du temps , block le joueru en eat vomis , gere la hit box
        self.vomis_duree = self.player.game.time - self.time_debut_vomis
        if(self.player.etat == 1 and self.vomis_duree < 0.2 ):
            #gere le vomis a droite
            self.rect.x = self.player.rect.x + 35
            self.rect.y = self.player.rect.y + 0
            self.player.etat_vomis = 1 #player entrain de vomir 1
            self.image = self.imageD_0
        elif(self.player.etat == 1 and self.vomis_duree < 0.4 ):
            self.player.etat_vomis = 1 
            self.image = self.imageD_1
        elif(self.player.etat == 1 and self.vomis_duree < 0.6 ):
            self.player.etat_vomis = 1 
            self.image = self.imageD_2
        elif(self.player.etat == 1 and self.vomis_duree < 0.8 ):
            self.player.etat_vomis = 1 
            self.image = self.imageD_3
        elif(self.player.etat == 1 and self.vomis_duree < 1 ):  #repasse en etat non vomis
            self.player.etat_vomis = 0
            self.remove()
            self.game.salle.salle_all_vomis_sol.add(self)
            self.image = self.image_solD
            self.rect.x = self.player.rect.x + 100
            self.rect.y = self.player.rect.y + 160
            self.rect.w = 45
            self.rect.h = 40
            self.x_blit = -55   #variable declage blit sur x (affichage uniquement)
            self.y_blit = -160
            self.y_real = self.player.y_real

        elif(self.player.etat == 2 and self.vomis_duree < 0.2 ):
            #gere le vomis a gauche
            self.rect.x = self.player.rect.x - 75
            self.rect.y = self.player.rect.y + 0
            self.player.etat_vomis = 1 #player entrain de vomir 1
            self.image = self.imageG_0
        elif(self.player.etat == 2 and self.vomis_duree < 0.4 ):
            self.player.etat_vomis = 1 
            self.image = self.imageG_1
        elif(self.player.etat == 2 and self.vomis_duree < 0.6 ):
            self.player.etat_vomis = 1 
            self.image = self.imageG_2
        elif(self.player.etat == 2 and self.vomis_duree < 0.8 ):
            self.player.etat_vomis = 1 
            self.image = self.imageG_3
        elif(self.player.etat == 2 and self.vomis_duree < 1 ):  #repasse en etat non vomis
            self.player.etat_vomis = 0
            self.remove()
            self.game.salle.salle_all_vomis_sol.add(self)
            self.image = self.image_solG
            self.rect.x = self.player.rect.x - 75
            self.rect.y = self.player.rect.y + 160
            self.rect.w = 45
            self.rect.h = 40
            self.x_blit = 0   #variable declage blit sur x (affichage uniquement)
            self.y_blit = -160
            self.y_real = self.player.y_real

        elif(self.player.etat in (0,3) and self.vomis_duree < 0.1 ):
            #gere le vomis devant
            self.rect.x = self.player.rect.x - 17
            self.rect.y = self.player.rect.y + 20
            self.y_real = self.player.y_real
            self.player.etat_vomis = 1 #player entrain de vomir 1
            self.image = self.imageF_0
        elif(self.player.etat in (0,3) and self.vomis_duree < 0.4):
            self.player.etat_vomis = 1 
            self.image = self.imageF_1
            self.y_real = self.player.y_real
        elif(self.player.etat in (0,3) and self.vomis_duree < 0.6 ):
            self.player.etat_vomis = 1 
            self.image = self.imageF_2
            self.y_real = self.player.y_real
        elif(self.player.etat in (0,3) and self.vomis_duree < 0.8 ):
            self.player.etat_vomis = 1 
            self.image = self.imageF_3
            self.y_real = self.player.y_real
        elif(self.player.etat in (0,3) and self.vomis_duree < 1 ):  #repasse en etat non vomis
            self.player.etat_vomis = 0
            self.remove()
            self.game.salle.salle_all_vomis_sol.add(self)
            self.image = self.image_solF
            self.rect.x = self.player.rect.x - 0
            self.rect.y = self.player.rect.y + 20
            self.rect.w = 60
            self.rect.h = 200
            self.x_blit = - 17   #variable declage blit sur x (affichage uniquement)
            self.y_blit = 0
            self.y_real = self.player.y_real

        if (self.player.etat == 1 or self.player.etat == 2):
            self.image = pygame.transform.scale(self.image,(100,200))

        if (self.player.etat == 0 or self.player.etat == 3):
            self.image = pygame.transform.scale(self.image,(100,200))

        if(self.vomis_duree > 4 ):
            #Si l'animation est encore la on la suprime
            self.remove()
            self.player.etat_vomis = 0

        for monster in (self.player.game.check_collision_group(self, self.game.salle.salle_all_monster)):
            #Si on touche un monstre , on update
            self.remove()
            self.player.etat_vomis = 0
            monster.dans_vomi = 1
            if (monster.taunt == 0):
                monster.taunt = 1
            monster.monster_dans_vomis()
            
    def sol_colide(self):
        #si le vomis au sol touche un monstre , on update  
        for monster in (self.player.game.check_collision_group(self, self.game.salle.salle_all_monster)):
            monster.dans_vomi = 1
            if (monster.taunt == 0):
                monster.taunt = 1
            monster.monster_dans_vomis()


