#Toutes les fonctions qui gerent l'affichage

#Importation Librairies
from tkinter import Tk,Label,Button,Entry,NW,PhotoImage,StringVar,Place,Text,Canvas,Message

# Variable 
Fichier_Scores = "Rendu\Space_Invader\Scores\Scores.txt" # Ajouter la gestion du score cf pendu 

#Importation LIbrairies Perso
from Lecture_Fichier import *

#Place le bouton quitter
#Screen ---> Rien
def Bouton_Quit(Screen):
    Btn_Quit = Button(Screen, text ="Quitter", command = Screen.destroy )
    Btn_Quit.place(x = 10, y = 10, height = 25, width = 75)
    return Btn_Quit

#Place un bouton rejouer 
#Screen , Class de jeux --> Rien 
def Bouton_Rejouer(Screen,Jeux):
    Btn_Rejouer = Button(Screen, text ="Rejouer", command = lambda: Rejouer(Screen,Jeux) )
    Btn_Rejouer.place(x = 10, y = 45, height = 25, width = 75)
    return Btn_Rejouer

#Place un element proportionellement à la taille de la fenettre et lui donne une taille 
#Classe , element , placement %x , %y , taille : %x , %y 
def Placer(Class,element,x_place,y_place,x_taille,y_taille):
    element.place(x = Class.Windows_Largeur*x_place , y = Class.Windows_Hauteur*y_place , height = Class.Windows_Hauteur*y_taille, width = Class.Windows_Largeur*x_taille)

#Affiche les scores
#Class du screen --> Rien
def Afficher_Scores(Screen_Class):
    Fond = Canvas(Screen_Class.Window, width=Screen_Class.Windows_Largeur+10, height=Screen_Class.Windows_Hauteur+10, bg='gray9')
    Fond.place(x = -10, y = -10)
    Bouton_Quit(Screen_Class.Window)
    Scores = fichier_to_string(Fichier_Scores)
    Affichage = Text(Screen_Class.Window, wrap='word')
    Placer(Screen_Class,Affichage,0.05,0.30,0.90,0.65)
    Affichage.insert('2.0', Scores)

#Place la top barre au debut du jeux 
#Classe jeux --> Rien
def Score(Jeux):
    Jeux.Lbl_Score = Label(Jeux.Screen.Window,text="Votre score : {0}".format(Jeux.Score),font=("Cambria",20),bg="#5575a8",fg="white")
    Placer(Jeux.Screen,Jeux.Lbl_Score,0.1,0.005,0.80,0.05)

#Update les score et le nombre de vie
#Classe jeux --> Rien
def Update_Top_Bar(Jeux):
    Jeux.Lbl_Score.destroy
    Jeux.Lbl_Score = Label(Jeux.Screen.Window,text="Votre score : {0}         VIE : {1}".format(Jeux.Score,Jeux.Life),font=("Cambria",20),bg="#5575a8",fg="white")
    Placer(Jeux.Screen,Jeux.Lbl_Score,0.1,0.005,0.80,0.05)
