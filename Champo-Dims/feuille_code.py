import pygame
from objet_code import playerhitbox

class Feuille(pygame.sprite.Sprite):
    def __init__(self, game ,player,type,moove):
        #Initialise un vomis
        super().__init__()
        self.game = game
        self.player = player
        self.image = pygame.image.load("Img/feuille/feuille_vide.png")
        self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.player.rect.x + 20
        self.rect.y = self.player.rect.y + 40
        self.x_init = self.rect.x 
        self.y_init = self.rect.y + 25
        self.rect.w = 30
        self.rect.h = 30
        self.x_blit = 0   
        self.y_blit = 0
        self.rect_blit = [self.rect.x + self.x_blit,self.rect.y,self.rect.w,self.rect.h] 
        self.y_real = self.player.y_real 
        self.hitbox = playerhitbox(self.game)
        

        #Variable 
        self.velocity = 4
        self.type = type
        self.moove = moove     # 0: devant  1:deriere 2:droite 3:gauche
        self.feuille_lvl_update()
        self.angle = 0
        self.image_origine = self.image
        
    def remove(self):
        #suprrime le vomis
        self.game.salle.salle_all_feuille.remove(self)
        self.game.salle.salle_all_sprites.remove(self)

    def feuille_lvl_update(self):
        #update la note en fonction des objets du joueur
        if (self.type == 20):
            self.image = pygame.image.load("Img/feuille/feuille_20.png")
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()
        elif (self.type == 19):
            self.image = pygame.image.load("Img/feuille/feuille_19.png")
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()
        elif (self.type == 18):
            self.image = pygame.image.load("Img/feuille/feuille_18.png")
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()
        elif (self.type == 17):
            self.image = pygame.image.load("Img/feuille/feuille_17.png")
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()
        elif (self.type == 16):
            self.image = pygame.image.load("Img/feuille/feuille_16.png")
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()
        elif (self.type == 15):
            self.image = pygame.image.load("Img/feuille/feuille_15.png")
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()
        elif (self.type == 14):
            self.image = pygame.image.load("Img/feuille/feuille_14.png")
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()
        elif (self.type == 13):
            self.image = pygame.image.load("Img/feuille/feuille_13.png")
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()
        elif (self.type == 12):
            self.image = pygame.image.load("Img/feuille/feuille_12.png")
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()
        elif (self.type == 11):
            self.image = pygame.image.load("Img/feuille/feuille_11.png")
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()
        elif (self.type == 10):
            self.image = pygame.image.load("Img/feuille/feuille_10.png")
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()
        elif (self.type == 9):
            self.image = pygame.image.load("Img/feuille/feuille_9.png")
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()
        elif (self.type == 8):
            self.image = pygame.image.load("Img/feuille/feuille_8.png")
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()
        elif (self.type == 7):
            self.image = pygame.image.load("Img/feuille/feuille_7.png")
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()
        elif (self.type == 6):
            self.image = pygame.image.load("Img/feuille/feuille_6.png")
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()
        elif (self.type == 5):
            self.image = pygame.image.load("Img/feuille/feuille_5.png")
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()
        elif (self.type == 4):
            self.image = pygame.image.load("Img/feuille/feuille_4.png")
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()
        elif (self.type == 3):
            self.image = pygame.image.load("Img/feuille/feuille_3.png")
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()
        elif (self.type == 2):
            self.image = pygame.image.load("Img/feuille/feuille_2.png")
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()
        elif (self.type == 1):
            self.image = pygame.image.load("Img/feuille/feuille_1.png")
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()
        elif (self.type == 0):
            self.image = pygame.image.load("Img/feuille/feuille_0.png")
            self.image = pygame.transform.scale(self.image,(30,30)).convert_alpha()

    def forward(self):
        #fait bouger les feuille
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.image_origine,self.angle,1)
        if(self.moove == 3):
            self.rect.y += self.velocity
            self.y_real += self.velocity
            
        elif(self.moove == 0):
            self.rect.y -= self.velocity
            self.y_real -= self.velocity

        elif(self.moove == 1):
            self.rect.x += self.velocity

        elif(self.moove == 2):
            self.rect.x -= self.velocity

        self.hitbox.rect.x = self.rect.x
        self.hitbox.rect.y = self.y_real

        for monster in (self.player.game.check_collision_group(self, self.game.salle.salle_all_monster)):
            #Si on touche un monstre , on supprime la feuille et on enleve de la vie au monstre
            self.remove()
            if(monster.monster_variante in (4,5,6)):
                monster.health -= self.type
                if(monster.taunt == 0):
                    monster.taunt = 1

        if(self.rect.x > self.x_init + 500 or self.rect.x < self.x_init - 500 ):
            self.remove()

        elif(self.rect.y > self.y_init + 500 or self.rect.y < self.y_init - 500):
            self.remove()

        elif (self.y_real < self.game.salle.min_y or self.y_real > self.game.salle.max_y ):
            self.remove()

        if (self.game.check_collision_rect(self,self.game.salle.salle_all_mur)):
            print("rect colide")
            if(self.game.check_collision_mur(self.hitbox,self.game.salle.salle_all_mur)):
                print("mask colide")
                self.remove()

        

