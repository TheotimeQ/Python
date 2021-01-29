#Importation Librairies
from tkinter import Tk,Entry,NW,PhotoImage,Place,Canvas,NW,Label,Button
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

# Mes fonctions 
from Space_Ship import *
from Affichage import *
from Laser import *
from Monster import *
from Ilot import *

#Class Jeux
#Class qui stock les données du Jeux
class Jeux:
    #Initialise le jeux
    def __init__(self,Class_Screen):
        self.Start_Game(Class_Screen)
        self.key_press={"Left":False, "Right":False, "space":False}
        self.Bind()
        self.Next_Frame()

    #Bind les touches du clavier
    def Bind(self):
        for key in ["Left", "Right", "space"]:
            self.Screen.Window.bind('<KeyPress-%s>' %key,lambda event: self.press(event) )  
            self.Screen.Window.bind('<KeyRelease-%s>' %key, lambda event: self.release(event) )

    #Gere le movement du joueur
    def Move(self):
        if self.key_press["Left"]:
            self.Horizontal(self.Screen,-1)
        if self.key_press["Right"]:
            self.Horizontal(self.Screen,1)
        if self.key_press["space"]:
            self.key_press["space"] = False
            self.Ship.Create_Laser(self.Screen)

    #Mets a jour la liste des touches au "pressage de touches"
    def press(self,event):
        self.key_press[event.keysym] = True   

    #Mets a jour la liste des touches au "release touches"
    def release(self,event):
        self.key_press[event.keysym] = False

    #Deplace le vaisseau
    def Horizontal(self,Screen,sens):
        self.Ship.x += self.Ship.xSpeed * sens

    #Place les monstres , le vaisseau , et les ilots
    def Creation_Object(self,Class_Screen):
        self.Ship.Place_SpaceShip(Class_Screen)
        for j in range(0,self.Column):
            for i in range(0,self.Row):
                self.Monster[i][j] = (Monster(Class_Screen,i,j,self))
        print(self.Ilots)
        for n in range(0,self.Nb_Ilot):
            for j in range(0,self.Largeur_Ilot):
                for i in range(0,self.Hauteur_Ilot):
                    self.Ilots[n][i][j] = (Cube(Class_Screen,n,i,j,self))
                
    #Calcul la place restante a gauche et a droite des monstres pour qu'il aille toujours le plus pret du bord de l'ecrant
    def Calcul_Left_Right_Space(self):
        Max_Left = 0
        Max_Right = 0
        Found = False
        for j in range(0,self.Column):
            for i in range(0,self.Row):
                if(self.Monster[i][j].Alive == True and Found == False):
                    Max_Left = j
                    Found = True  
        Found = False
        for j in range(self.Column-1,-1,-1):
            for i in range(self.Row-1,-1,-1):
                if(self.Monster[i][j].Alive == True and Found == False):
                    Max_Right = j 
                    Found = True   
        self.Left_Space = Max_Left * int(self.Screen.Windows_Largeur/(self.Column + 1))
        self.Right_Space = (self.Column - Max_Right ) * int(self.Screen.Windows_Largeur/(self.Column + 1))

    #Detecte la collision Monstre / Laser et suprime le monstre et laser si collision
    def Detect_Collision_Monster(self,Laser_Liste):
        for Laser in Laser_Liste :
            for i, Monster_Line in enumerate(self.Monster) :
                for j, Monster in enumerate(Monster_Line) :
                    if (Monster.Alive == True):
                        if(Laser.x > Monster.x and Laser.x < Monster.x + Monster.Largeur and Laser.y > Monster.y and Laser.y < Monster.y + Monster.Hauteur):
                            self.Fond.delete(Laser.Laser)
                            self.Fond.delete(Monster.Monster)
                            self.Monster[i][j].Alive = False
                            Laser_Liste.remove(Laser)
                            self.Score += 10
                            Update_Top_Bar(self)

    #Detecte la collision Laser / Player
    def Detect_Collision_Player(self,Laser_Liste):
        for Laser in Laser_Liste :
            if(Laser.x > self.Ship.x and Laser.x < self.Ship.x + self.Ship.Largeur and Laser.y > self.Ship.y and Laser.y < self.Ship.y + self.Ship.Hauteur):
                self.Fond.delete(Laser.Laser)
                Laser_Liste.remove(Laser)
                self.Life -= 1
                Update_Top_Bar(self)
                if(self.Life <= 0):
                    self.Perdu = True

    #Detecte la collision Laser / Player
    def Detect_Collision_Cube(self,Laser_Liste_player,Laser_Liste_Monster,Ilot_Liste):
        for Ilot in Ilot_Liste :
            for Row in Ilot :
                for Cube in Row : 
                    if(Cube.Alive == True ):
                        for Laser in Laser_Liste_player :
                            if(Laser.x > Cube.x and Laser.x < Cube.x + Cube.Largeur and Laser.y > Cube.y and Laser.y < Cube.y + Cube.Hauteur):
                                self.Fond.delete(Laser.Laser)
                                Laser_Liste_player.remove(Laser)
                                self.Fond.delete(Cube.Cube)
                                Cube.Alive = False

                        for Laser in Laser_Liste_Monster :
                            if(Laser.x > Cube.x and Laser.x < Cube.x + Cube.Largeur and Laser.y > Cube.y and Laser.y < Cube.y + Cube.Hauteur):
                                self.Fond.delete(Laser.Laser)
                                Laser_Liste_Monster.remove(Laser)
                                self.Fond.delete(Cube.Cube)
                                Cube.Alive = False
        
    #Initialise/Reinitialise les variables du jeux
    def Start_Game(self,Class_Screen):
        self.Life = 3
        self.Perdu = False 
        self.Gagne = False
        self.Nb_Ilot = 4 
        self.Largeur_Ilot = 6
        self.Hauteur_Ilot = 4
        self.Ilots = [ [ [ [] for k in range(0,self.Largeur_Ilot) ] for k in range(0, self.Hauteur_Ilot)] for k in range(0,self.Nb_Ilot) ]
        self.Score = int()
        self.FrameRate = 80
        self.Screen = Class_Screen
        self.Fond = Class_Screen.Fond
        self.Screen.Screen_Destroy()
        self.Lbl_Score = Label(self.Screen.Window)
        Bouton_Quit(self.Screen.Window)
        self.Bouton_Rejouer(Class_Screen)
        Score(self)
        self.Ship = SpaceShip(Class_Screen)
        self.Column = 7
        self.Row = 3
        self.Monster= [ [ [] for k in range(0,self.Column) ] for k in range(0,self.Row)]
        self.Left_Space = int(Class_Screen.Windows_Largeur/(self.Column + 1))
        self.Right_Space = int(Class_Screen.Windows_Largeur/(self.Column + 1))
        self.Creation_Object(Class_Screen)
        self.Lbl_Perdu = Label(self.Screen.Window, text ="Perdu !")
        self.Lbl_Gagne = Label(self.Screen.Window, text ="Gagne !")
        self.Y_end = int(self.Ship.y - 50) - 20*self.Hauteur_Ilot
        Update_Top_Bar(self)
    
    #Check si le joueur a gagné
    def Check_Win(self):
        self.Gagne = True
        for Monster_Row in self.Monster : 
            for Monster in Monster_Row :
                if(Monster.Alive == True):
                    self.Gagne = False
        
    #Update tout ce qui dois etre update , et nous fais gagner / Perdre
    def Next_Frame(self):
        if(self.Perdu == False and self.Gagne == False):
            self.Check_Win()
            self.Calcul_Left_Right_Space()
            self.Move()
            for Monster_Row in self.Monster : 
                for Monster in Monster_Row :
                    self.Detect_Collision_Cube(self.Ship.Laser_Liste,Monster.Laser_Liste,self.Ilots)
                    Monster.Moove_Laser(self)
                    self.Detect_Collision_Player(Monster.Laser_Liste)
                    if (Monster.Alive == True):
                        Monster.Moove_Monster(self.Screen,self)
                        Monster.Create_Laser(self.Screen)
                        Monster.Check_y_Loose(self)
            
            self.Ship.Moove_Laser(self)
            self.Ship.Moove_SpaceShip(self.Screen)
            self.Detect_Collision_Monster(self.Ship.Laser_Liste)

        if(self.Perdu == True):
            self.Fond.delete(self.Ship.Ship)
            Placer(self.Screen,self.Lbl_Perdu,0.4,0.5,0.15,0.1)

        if(self.Gagne == True):
            self.Fond.delete(self.Ship.Ship)
            Placer(self.Screen,self.Lbl_Gagne,0.4,0.5,0.15,0.1)

        self.Screen.Window.after(int(1000/self.FrameRate),lambda: self.Next_Frame())

    #Place le bouton rejouer 
    def Bouton_Rejouer(self,Class_Screen):
        Btn_Rejouer = Button(self.Screen.Window, text ="Rejouer", command = lambda: self.Rejouer(Class_Screen) )
        Btn_Rejouer.place(x = 10, y = 45, height = 25, width = 75)

    #Relance le jeux et suprime les anciens elements
    def Rejouer(self,Class_Screen):
        if(self.Perdu == True):
            self.Lbl_Perdu.destroy()
        if(self.Gagne == True):
            self.Lbl_Gagne.destroy()
        for Monster_Row in self.Monster : 
            for Monster in Monster_Row :
                Monster.Clear_Laser(self)
        self.Ship.Clear_Laser(self)
        self.Start_Game(Class_Screen)





    





    