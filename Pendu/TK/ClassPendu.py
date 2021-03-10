#Jeux du pendu dans la console - Pas fini 

# Bibliotheque 
from tkinter import StringVar,Canvas
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from datetime import datetime

# Mes fonctions 
from MyFunction import *

# Variable 
Fichier_Mots = "TK\Mots.txt"
Fichier_Scores = "TK\Score.txt"

#Class Jeux
#Class qui stock toutes les données qui ont besoin d'etre transferées de fonction en fonction.... On envoie juste la class et le tour est joué
class Pendu:
    def __init__(self,Window):
        #Stock l'etat du jeux actuel
        self.Window = Window
        self.Nb_Vie = 8
        self.Gagner = False
        self.Mots = Choix_mots(Fichier_Mots)
        self.Mots_liste = list(self.Mots) #Mots choisi aleatoirement
        self.Taille_mots = len(self.Mots) #Si plus tard ajout choix difficulté
        self.Lettres_prop_juste = [self.Mots_liste[0]]
        self.Lettres_prop_fausse = []
        self.New_Lettre = ""    
        self.Ety_Lettre = ""    #On stockera un champs de saisie ici plus tard , pour permettre la remise a zero de ce champ de saisie 
        self.New_Lettre_entry = StringVar()
        self.Psudo = "noone"
        self.Windows_Largeur = self.Window.winfo_screenwidth()
        self.Windows_Hauteur = self.Window.winfo_screenheight()
        self.canvas = Canvas(self.Window)

        self.image = [Image.open("IMG\_" + str(k) + "_.png") for k in range(0,9) ]  #Recupere les images et les range dans une liste
        self.photo = [ImageTk.PhotoImage(self.image[k]) for k in range(0,9) ]
