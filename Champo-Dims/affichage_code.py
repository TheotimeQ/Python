import pygame
class Affichage:
    def __init__(self,game):
        #Initialisation de l'affichage
        self.game = game
        info = pygame.display.Info()
        icone = pygame.image.load("Img\icone.png") 
        pygame.display.set_caption("Les alcoDims anonyme")
        pygame.display.set_icon(icone)
        self.screen = pygame.display.set_mode((int(info.current_w*0.8),int(info.current_h*0.8)),pygame.FULLSCREEN)  
        self.screen_rect = self.screen.get_rect()
        print(self.screen_rect , info.current_w,info.current_h)

        self.image_button_quit = pygame.image.load("Img/button_quit.png")
        self.image_button_quit = pygame.transform.scale(self.image_button_quit,(300 , 50)).convert_alpha()
        self.quit_button_rect = self.image_button_quit.get_rect()
        self.quit_button_rect.x = int(self.screen_rect.w / 2 - 150)
        self.quit_button_rect.y = 500

        self.image_button_restart = pygame.image.load("Img/button_restart.png")
        self.image_button_restart = pygame.transform.scale(self.image_button_restart,(300 , 50)).convert_alpha()
        self.restart_button_rect = self.image_button_restart.get_rect()
        self.restart_button_rect.x = int(self.screen_rect.w / 2 - 150)
        self.restart_button_rect.y = 400

        self.image_button_play = pygame.image.load("Img/button_play.png")
        self.image_button_play = pygame.transform.scale(self.image_button_play,(300 , 50)).convert_alpha()
        self.play_button_rect = self.image_button_play.get_rect()
        self.play_button_rect.x = int(self.screen_rect.w / 2 - 150)
        self.play_button_rect.y = 300

        pygame.display.flip()  
        print("Affichage initialisé")
    
    def affichage_update(self,delay = 0):
        #Affiche tout les sprite , en tenant compte des differents plans
        self.game.player.modele_update()
        self.screen.blit(self.game.salle.image, (0,0))

        for mur in self.game.salle.salle_all_mur : 
            mur.rect_blit = [mur.rect.x,mur.rect.y,mur.rect.w,mur.rect.h]  
            #pygame.draw.rect(self.game.affichage.screen,(233, 122, 3),mur.rect_blit)
            mur.rect_blit = [mur.rect.x + mur.x_blit,mur.rect.y + mur.y_blit,mur.rect.w,mur.rect.h]
            self.screen.blit(mur.image,mur.rect_blit)

        vomis_rect_sequence = []
        for sprite in self.game.salle.salle_all_vomis_sol : 
            sprite.rect_blit = [sprite.rect.x,sprite.rect.y,sprite.rect.w,sprite.rect.h]  
            #pygame.draw.rect(self.game.affichage.screen,(233, 122, 3),sprite.rect_blit)
            sprite.rect_blit = [sprite.rect.x + sprite.x_blit,sprite.rect.y + sprite.y_blit,sprite.rect.w,sprite.rect.h]
            blit_arg = (sprite.image,sprite.rect_blit)
            vomis_rect_sequence.append(blit_arg)
        self.screen.blits((vomis_rect_sequence))

        L = []
        for sprite in self.game.salle.salle_all_sprites:
            #On fais une liste de nos sprite
            L.append(sprite)
        L = sorted(L, key=lambda sprite: sprite.y_real)
        #on les tri par y_real croissant

        sprite_rect_sequence = []
        for sprite in L : 
            sprite.rect_blit = [sprite.rect.x,sprite.rect.y,sprite.rect.w,sprite.rect.h]  
            #pygame.draw.rect(self.game.affichage.screen,(233, 122, 3),sprite.rect_blit)
            sprite.rect_blit = [sprite.rect.x + sprite.x_blit,sprite.rect.y + sprite.y_blit,sprite.rect.w,sprite.rect.h]
            blit_arg = (sprite.image,sprite.rect_blit)
            sprite_rect_sequence.append(blit_arg)
        self.screen.blits((sprite_rect_sequence))
        
        self.feuille_affiche()
        self.monster_health_bar()

        x_barre_objet = 220
        y_barre_objet = 20
        sprite_rect_sequence = []
        
        for objet in self.game.player.object_list:
            objet.rect_blit = [x_barre_objet,y_barre_objet, objet.rect.w, objet.rect.h] 
            x_barre_objet += objet.rect.w + 10
            blit_arg = (objet.image,objet.rect_blit)
            sprite_rect_sequence.append(blit_arg)
            
        self.screen.blits((sprite_rect_sequence))

        self.game.player.bar_bouteille_update(self.game.affichage.screen)
        self.game.player.bar_alcool_update(self.game.affichage.screen)

        self.game.framerate_update()
        pygame.time.wait(delay)
        pygame.display.flip()

    def affichage_pause(self):
        self.screen.blit(self.image_button_play,self.play_button_rect)
        self.screen.blit(self.image_button_quit,self.quit_button_rect)
        self.screen.blit(self.image_button_restart,self.restart_button_rect)
        pygame.display.flip()

    def feuille_affiche(self):
        self.type = self.game.player.feuille_lvl
        if (self.type == 20):
            self.image = pygame.image.load("Img/feuille/feuille_20.png")
            self.image = pygame.transform.scale(self.image,(90,90)).convert_alpha()
        elif (self.type == 19):
            self.image = pygame.image.load("Img/feuille/feuille_19.png")
            self.image = pygame.transform.scale(self.image,(90,90)).convert_alpha()
        elif (self.type == 18):
            self.image = pygame.image.load("Img/feuille/feuille_18.png")
            self.image = pygame.transform.scale(self.image,(90,90)).convert_alpha()
        elif (self.type == 17):
            self.image = pygame.image.load("Img/feuille/feuille_17.png")
            self.image = pygame.transform.scale(self.image,(90,90)).convert_alpha()
        elif (self.type == 16):
            self.image = pygame.image.load("Img/feuille/feuille_16.png")
            self.image = pygame.transform.scale(self.image,(90,90)).convert_alpha()
        elif (self.type == 15):
            self.image = pygame.image.load("Img/feuille/feuille_15.png")
            self.image = pygame.transform.scale(self.image,(90,90)).convert_alpha()
        elif (self.type == 14):
            self.image = pygame.image.load("Img/feuille/feuille_14.png")
            self.image = pygame.transform.scale(self.image,(90,90)).convert_alpha()
        elif (self.type == 13):
            self.image = pygame.image.load("Img/feuille/feuille_13.png")
            self.image = pygame.transform.scale(self.image,(90,90)).convert_alpha()
        elif (self.type == 12):
            self.image = pygame.image.load("Img/feuille/feuille_12.png")
            self.image = pygame.transform.scale(self.image,(90,90)).convert_alpha()
        elif (self.type == 11):
            self.image = pygame.image.load("Img/feuille/feuille_11.png")
            self.image = pygame.transform.scale(self.image,(90,90)).convert_alpha()
        elif (self.type == 10):
            self.image = pygame.image.load("Img/feuille/feuille_10.png")
            self.image = pygame.transform.scale(self.image,(90,90)).convert_alpha()
        elif (self.type == 9):
            self.image = pygame.image.load("Img/feuille/feuille_9.png")
            self.image = pygame.transform.scale(self.image,(90,90)).convert_alpha()
        elif (self.type == 8):
            self.image = pygame.image.load("Img/feuille/feuille_8.png")
            self.image = pygame.transform.scale(self.image,(90,90)).convert_alpha()
        elif (self.type == 7):
            self.image = pygame.image.load("Img/feuille/feuille_7.png")
            self.image = pygame.transform.scale(self.image,(90,90)).convert_alpha()
        elif (self.type == 6):
            self.image = pygame.image.load("Img/feuille/feuille_6.png")
            self.image = pygame.transform.scale(self.image,(90,90)).convert_alpha()
        elif (self.type == 5):
            self.image = pygame.image.load("Img/feuille/feuille_5.png")
            self.image = pygame.transform.scale(self.image,(90,90)).convert_alpha()
        elif (self.type == 4):
            self.image = pygame.image.load("Img/feuille/feuille_4.png")
            self.image = pygame.transform.scale(self.image,(90,90)).convert_alpha()
        elif (self.type == 3):
            self.image = pygame.image.load("Img/feuille/feuille_3.png")
            self.image = pygame.transform.scale(self.image,(90,90)).convert_alpha()
        elif (self.type == 2):
            self.image = pygame.image.load("Img/feuille/feuille_2.png")
            self.image = pygame.transform.scale(self.image,(90,90)).convert_alpha()
        elif (self.type == 1):
            self.image = pygame.image.load("Img/feuille/feuille_1.png")
            self.image = pygame.transform.scale(self.image,(90,90)).convert_alpha()
        elif (self.type == 0):
            self.image = pygame.image.load("Img/feuille/feuille_0.png")
            self.image = pygame.transform.scale(self.image,(90,90)).convert_alpha()
        elif (self.type == -1):
            self.image = pygame.image.load("Img/feuille/feuille_vide.png")
            self.image = pygame.transform.scale(self.image,(90,90)).convert_alpha()

        x_feuille = 120
        y_feuille = 20
        rect_blit = [x_feuille,y_feuille, 90, 90]   
        self.screen.blit(self.image,rect_blit)

    def monster_health_bar(self):
        for monster in self.game.salle.salle_all_monster :
            if (monster.monster_variante in (4,5,6)):
                monster.update_health_bare()
                pygame.draw.rect(self.game.affichage.screen,monster.health_bar_color_back,monster.health_bar_position_back)
                pygame.draw.rect(self.game.affichage.screen,monster.health_bar_color,monster.health_bar_position)


        





 
