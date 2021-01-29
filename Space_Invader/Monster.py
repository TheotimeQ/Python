#Importation Librairies
from tkinter import NW,PhotoImage,Canvas
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import random as rnd

# Mes fonctions
from Affichage import *
from Laser import *

#Class Monster
#Class qui stock les données des montre
class Monster:
    def __init__(self,Class_Screen,i,j,Game):
        self.Row = i 
        self.Column = j 
        
        self.x = int(Class_Screen.Windows_Largeur/(Game.Column + 1))*j + (i%2)*int(Class_Screen.Windows_Largeur/(Game.Column + 1))/2
        self.y = int(Class_Screen.Windows_Hauteur*0.7/(Game.Row))*i + 20
        self.x_init = self.x

        self.Largeur = 100
        self.Hauteur = 100
        self.xSpeed = 2
        self.ySpeed = 10
        self.sens = 1
        self.number_aller_retour = 0
        self.Laser_Chance = 0.005
        self.Max_Laser = 2
        self.Alive = True
        self.image = Image.open("Rendu\Space_Invader\IMG\Monster.png") 
        self.img_copy= self.image.copy()
        self.image = self.img_copy.resize((self.Largeur, self.Hauteur))
        self.image_Ship = ImageTk.PhotoImage(self.image)
        self.Monster = Class_Screen.Fond.create_image(0,0, anchor = NW, image= self.image_Ship)
        Class_Screen.Fond.coords(self.Monster, self.x, self.y)

        self.Laser_Liste = []

    #Deplace le monstre
    def Moove_Monster(self,Class_Screen,Jeux):
        if(self.x > self.x_init + Jeux.Right_Space or self.x < self.x_init - Jeux.Left_Space):
            self.sens = -1*self.sens
            self.number_aller_retour += 1
        if(self.number_aller_retour == 2):
            self.y += self.ySpeed
            self.number_aller_retour = 0
        self.x += self.xSpeed * self.sens
        Class_Screen.Fond.coords(self.Monster, self.x, self.y)

    #Creer un laser depuis le monstre
    def Create_Laser(self,Class_Screen):
        if(rnd.random() < self.Laser_Chance and len(self.Laser_Liste) < self.Max_Laser ):
            self.Laser_Liste.append(Laser(Class_Screen,self.x + self.Largeur/2 ,self.y - 3))

    #Kill tout les lasers
    def Clear_Laser(self,Jeux):
        while(len(self.Laser_Liste) != 0 ): #Entrange , le for ne suffit pas a tout suprimer.... 
            for Laser in self.Laser_Liste :
                Jeux.Fond.delete(Laser.Laser)
                self.Laser_Liste.remove(Laser)

    #Deplace les laser
    def Moove_Laser(self,Jeux):
        for Laser in self.Laser_Liste :
            Laser.y += Laser.ySpeed_Monster
            Jeux.Screen.Fond.coords(Laser.Laser, Laser.x ,Laser.y , Laser.x + Laser.Largeur ,  Laser.y + Laser.Hauteur)
            if(Laser.y > Jeux.Screen.Windows_Hauteur + 5):
                Jeux.Fond.delete(Laser.Laser)
                self.Laser_Liste.remove(Laser)

    #Loose si monstre top bas
    def Check_y_Loose(self,Jeux):
        if(self.y + self.Hauteur >= Jeux.Y_end):
            Jeux.Perdu = True