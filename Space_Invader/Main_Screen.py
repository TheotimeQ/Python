#Importation Librairies
from tkinter import Tk,Label,Button,Entry,NW,PhotoImage,StringVar,Place,Text,Canvas,Message

# Mes fonctions
from Affichage import *
from Game import *

#Class Main_Screen
#Class qui stock toutes les données qui ont besoin d'etre transferées de fonction en fonction.... On envoie juste la class et le tour est joué
class MainScreen:
    def __init__(self):
        self.Window = Tk()
        self.Windows_Largeur = self.Window.winfo_screenwidth()
        self.Windows_Hauteur = self.Window.winfo_screenheight()
        self.Widget = []
        self.Fond = Canvas(self.Window, width=self.Windows_Largeur+10, height=self.Windows_Hauteur+10, bg='gray10')
        self.Create_Main_Screen()
        
    def Create_Main_Screen(self):
        self.Window.title("Space Invader")
        self.Window.overrideredirect(True)
        self.Window.geometry("{0}x{1}+0+0".format(self.Windows_Largeur, self.Windows_Hauteur))
        self.Fond.pack(padx=0,pady=0)

        Titre = Label(self.Window, text='Space Invader! ',font=("Courier", 30))
        Placer(self,Titre,0.35,0.05,0.25,0.1)
        self.Widget.append(Titre)

        Btn_Jouer = Button(self.Window, text ="Jouer", command = lambda: Jeux(self) )
        Placer(self,Btn_Jouer,0.375,0.35,0.20,0.12)
        self.Widget.append(Btn_Jouer)

        Btn_Score = Button(self.Window, text ="Afficher les scores", command = lambda: Afficher_Scores(self) )
        Placer(self,Btn_Score,0.375,0.75,0.20,0.12)
        self.Widget.append(Btn_Score)

        Bouton_Quit(self.Window)

    def Screen_Destroy(self):
        for Element in self.Widget :
            Element.destroy()

