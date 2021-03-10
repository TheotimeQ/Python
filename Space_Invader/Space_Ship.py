#Importation Librairies
from tkinter import NW,PhotoImage,Canvas
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename

# Mes fonctions
from Affichage import *
from Laser import *

#Class SpaceShip
#Class qui stock les données du SpaceShip (Joueur)
class SpaceShip:
    def __init__(self,Class_Screen):
        self.x = Class_Screen.Windows_Largeur/2
        self.y = Class_Screen.Windows_Hauteur*0.86
        self.Largeur = 60
        self.Hauteur = 80
    
        self.xSpeed = 3

        self.image = Image.open("IMG\Ship.png") 
        self.img_copy= self.image.copy()
        self.image = self.img_copy.resize((self.Largeur, self.Hauteur))
        self.image_Ship = ImageTk.PhotoImage(self.image)

        self.Laser_Liste = []
        self.Max_Laser = 5

    #Place le Vaisseau du joueur
    def Place_SpaceShip(self,Class_Screen):
        self.Ship = Class_Screen.Fond.create_image(0,0, anchor = NW, image= self.image_Ship)
        Class_Screen.Fond.coords(self.Ship, self.x, self.y)

    def Moove_SpaceShip(self,Class_Screen):
        Class_Screen.Fond.coords(self.Ship, self.x, self.y)

    def Clear_Laser(self,Jeux):
        while(len(self.Laser_Liste) != 0 ):
            for Laser in self.Laser_Liste :
                Jeux.Fond.delete(Laser.Laser)
                self.Laser_Liste.remove(Laser)

    def Create_Laser(self,Class_Screen):
        if( len(self.Laser_Liste) < self.Max_Laser ):
            self.Laser_Liste.append(Laser(Class_Screen,self.x + self.Largeur/2 ,self.y - 3))

    def Moove_Laser(self,Jeux):
        for Laser in self.Laser_Liste :
            Laser.y -= Laser.ySpeed_Player
            Jeux.Screen.Fond.coords(Laser.Laser, Laser.x ,Laser.y , Laser.x + Laser.Largeur ,  Laser.y + Laser.Hauteur)
            if(Laser.y < -5):
                Jeux.Fond.delete(Laser.Laser)
                self.Laser_Liste.remove(Laser)


    



