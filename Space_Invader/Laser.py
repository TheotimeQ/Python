#Importation Librairies
from tkinter import Canvas

# Mes fonctions

#Class Laser
#Class qui stock les données des lasers
class Laser:
    def __init__(self,Class_Screen,x,y):
        self.x = x
        self.y = y
        self.Largeur = 5
        self.Hauteur = 10
        self.ySpeed_Monster = 2
        self.ySpeed_Player = 5 
        self.Laser = Class_Screen.Fond.create_rectangle(x, y, x + self.Largeur, y + self.Hauteur , fill='White')


        
        