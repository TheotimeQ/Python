#Importation Librairies
from tkinter import Canvas

# Mes fonctions

#Class SpaceShip
#Class qui stock les données du SpaceShip (Joueur)
class Cube:
    def __init__(self,Class_Screen,n,i,j,jeux):
        self.Largeur = 20
        self.Hauteur = 20
        self.Alive = True
        self.x = int(Class_Screen.Windows_Largeur/jeux.Nb_Ilot)*n + int(Class_Screen.Windows_Largeur/jeux.Nb_Ilot)/2 - + j * self.Largeur 
        self.y = int(jeux.Ship.y - 50) - self.Hauteur*i
        self.Cube = Class_Screen.Fond.create_rectangle(self.x, self.y, self.x + self.Largeur, self.y + self.Hauteur , fill='White')

        
