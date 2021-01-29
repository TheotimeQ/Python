import pygame
from game_code import Game

#initialisation jeux
pygame.init()
pygame.font.init()
game = Game()
game.running = True

while (game.running ==  True):

    if (game.pause == False):

        #mise a jour du temps
        game.clock.tick()
        game.time_update()
        #Update tout les sprite (check colision + mouvement)
        for vomis in game.salle.salle_all_vomis:
            #On avance l'animation du vomis
            vomis.move()
        
        for bouteille in game.salle.salle_all_bouteilles:
            #on regarde si le joueur est sur une bouteille
            bouteille.check_bouteille() 

        for coffre in game.salle.salle_all_coffres:
            #on regarde si le joueur est sur un coffre
            coffre.check_coffre() 

        for monster in game.salle.salle_all_monster:
            #on fait avancer les monstres et leur tete
            monster.forward()
            monster.monster_set_type()
            monster.tete.tete_update()

        for vomis in game.salle.salle_all_vomis_sol:
            #on regarde si les monstre sont en collision avec un vomis
            vomis.sol_colide()

        for objet in game.player.object_list:
            #on actualise les objets
            objet.objet_set_type()

        game.salle.salle_changement()

        if (game.player.alcool_lvl <= 0 ):
            print("Perdu")
            game.running = False
    
        #affichage
        game.affichage.affichage_update(8)
        #deplacement player
        game.deplacement()
        #recupere evenements clavier
        game.evenements()

        print(game.player.rect.x,game.player.rect.y,game.player.y_real)

    if (game.pause == True):
        game.affichage.affichage_pause()
        game.evenements()

    if (game.restart == True):
        game.restart = False
        game.running = False
        pygame.quit()
        pygame.init()
        pygame.font.init()
        game = Game()
        ame.running = True
    
            


            


