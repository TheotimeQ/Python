#Jeux du pendu dans la console - Pas fini 

# Bibliotheque 
from tkinter import Tk,Label,Button,Entry,NW,PhotoImage,StringVar,Place,Text,Canvas,Message
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from datetime import datetime

# Mes fonctions 
from MyFunction import *
from ClassPendu import *

# Variable 
Fichier_Mots = "Rendu\Pendu\TK\Mots.txt"
Fichier_Scores = "Rendu\Pendu\TK\Score.txt"

# Lance le programe
# Rien --> Rien
def main():
    Window = Tk() 

    Game = Pendu(Window)

    Window.title("Jeux du Pendu")
    Window.overrideredirect(True)
    Window.geometry("{0}x{1}+0+0".format(Game.Windows_Largeur, Game.Windows_Hauteur))

    Fond = Canvas(Game.Window, width=Game.Windows_Largeur+10, height=Game.Windows_Hauteur+10, bg='gray22')
    Fond.place(x = -10, y = -10)

    Titre = Label(Window, text='Jeux du pendu ! ',font=("Courier", 30)).pack(padx = 0 , pady = 20)

    Btn_Jouer = Button(Window, text ="Jouer", command = lambda: jouer(Game) )
    Placer(Game,Btn_Jouer,0.08,0.2,0.15,0.1)

    Btn_Score = Button(Window, text ="Afficher les scores", command = lambda: afficher_droite(Game,Fichier_Scores) )
    Placer(Game,Btn_Score,0.08,0.4,0.15,0.1)

    New_Mot = StringVar()
    New_Mot.set("Entrez un mot")
    Ety_Add = Entry(Window, textvariable = New_Mot ,bd = 2)
    Placer(Game,Ety_Add,0.25,0.6,0.15,0.1)

    Lbl_Add = Button(Window, text ="Ajouter le mot", command = lambda: ajouter_mot(New_Mot.get()) )
    Placer(Game,Lbl_Add,0.08,0.6,0.15,0.1)

    Btn_Regarder = Button(Window, text ="Afficher les mots", command = lambda: afficher_droite(Game,Fichier_Mots) )
    Placer(Game,Btn_Regarder,0.08,0.8,0.15,0.1)
    
    Btn_Quit = Button(Window, text ="Quitter", command = Window.destroy )
    Btn_Quit.place(x = 10, y = 10, height = 25, width = 75)

    Window.mainloop()

#Demare le jeux
#Class Game --> Rien
def jouer(Game):
    Fond = Canvas(Game.Window, width=Game.Windows_Largeur+10, height=Game.Windows_Hauteur+10, bg='gray22')
    Fond.place(x = -10, y = -10)

    Btn_Quit = Button(Game.Window, text ="Quitter", command = Game.Window.destroy )
    Btn_Quit.place(x = 10, y = 10, height = 25, width = 75)
    
    Lbl_instruc = Label(Game.Window, text = "Trouvez le mot suivant : ")
    Placer(Game,Lbl_instruc,0.1,0.5,0.15,0.05)

    update_mot(Game)                #affiche le mot correctement
    afficher_wrong_good(Game)       #Affiche les mauvaise et bonne lettre deja rentré
    Ask_Lettre(Game)                #Demande un lettre

#Affiche de quoi demander une lettre et la stock dans la class Pendu
#Game --> Rien
def Ask_Lettre(Game):
    Game.New_Lettre_entry = StringVar()
    Game.New_Lettre_entry.set("")
    Game.Ety_Lettre = Entry(Game.Window, textvariable = Game.New_Lettre_entry ,bd = 2)
    Placer(Game,Game.Ety_Lettre,0.25,0.8,0.02,0.05)

    Lbl_Add = Label(Game.Window, text ="A quelle lettre penssez vous ? ")
    Placer(Game,Lbl_Add,0.1,0.8,0.12,0.05)

    Afficher_Pendu(Game)
    Btn_Add = Button(Game.Window, text ="Valider (Ou pressez Entrée)" , command = lambda: Add_lettre(Game,Game.New_Lettre_entry.get()))
    Game.Window.bind('<Return>', lambda event: Enter(event,Game))
    Placer(Game,Btn_Add,0.3,0.8,0.15,0.05)

#Action avec touche entrée
def Enter(event,Game):
    Add_lettre(Game,Game.New_Lettre_entry.get())
    
#Verifie si la lettre et bonne et l'ajoute au mots / Nous fais gagner , perdre
#Class , Lettre --> Rien
def Add_lettre(Game,Lettre):
    Game.New_Lettre = Lettre
    print(Lettre)

    if ( len(Game.Lettres_prop_fausse) < Game.Nb_Vie and Game.Gagner == False) :
        if (Game.New_Lettre == ""):
            affiche_message(Game,"Veuillez rentrer une lettre")

        elif (Game.New_Lettre in Game.Lettres_prop_juste or Game.New_Lettre in Game.Lettres_prop_fausse):
            affiche_message(Game,"Vous avez deja entré cette lettre....")

        else :
            affiche_message(Game,"Vous avez rentré : " + Game.New_Lettre)
            [Game.Lettres_prop_juste,Game.Lettres_prop_fausse,Game.Gagner] = update_pendu(Game.New_Lettre,Game.Lettres_prop_juste,Game.Lettres_prop_fausse,Game.Mots)
            Game.New_Lettre = "" 
            afficher_wrong_good(Game)
            update_mot(Game)
            Afficher_Pendu(Game)
    
    if Game.Gagner == True :
        Fond = Canvas(Game.Window, width=Game.Windows_Largeur+10, height=Game.Windows_Hauteur+10, bg='gray22')
        Fond.place(x = -10, y = -10)
        Lbl_Win1 = Label(Game.Window, text ="C'est gagnéeeeeee! ")
        print("Gagné")
        Placer(Game,Lbl_Win1,0.2,0.6,0.12,0.05)
        score(Game)
         
    elif (len(Game.Lettres_prop_fausse) >= Game.Nb_Vie ):
        Fond = Canvas(Game.Window, width=Game.Windows_Largeur+10, height=Game.Windows_Hauteur+10, bg='gray22')
        Fond.place(x = -10, y = -10)
        Lbl_Win2 = Label(Game.Window, text ="C'est perddduuuu! C'etait : "+ Game.Mots)
        Placer(Game,Lbl_Win2,0.2,0.6,0.20,0.05)
        print("Perdu")
        score(Game)

    else: 
        Game.New_Lettre_entry = StringVar()
        Game.New_Lettre_entry.set("")
        Game.Ety_Lettre = Entry(Game.Window, textvariable = Game.New_Lettre_entry ,bd = 2)
        Placer(Game,Game.Ety_Lettre,0.25,0.8,0.02,0.05)

#Affiche le pendu comme il faut sur la droite
#Class --> Rien
def Afficher_Pendu(Game):
    Image_nb = len(Game.Lettres_prop_fausse)
    Game.canvas = Canvas(Game.Window, width = 860, height = 860) 
    Game.canvas.create_image(0,0, anchor = NW, image= Game.photo[Image_nb])
    Placer(Game,Game.canvas,0.5,0.025,0.5,0.95)

#Affiche bouton pour relancer partie
#Class --> Rien
def rejouer(Game):
    Lbl_Rej = Button(Game.Window, text ="Rejouer" , command = main)
    Placer(Game,Lbl_Rej,0.15,0.6,0.2,0.1)

#Reinitialise la fenettre et affiche les scores a droite
#Class --> Rien
def score(Game):

    Btn_Quit = Button(Game.Window, text ="Quitter", command = Game.Window.destroy )
    Btn_Quit.place(x = 10, y = 10, height = 25, width = 75)

    Psudo = StringVar()
    Psudo.set("")

    Ety_Psu = Entry(Game.Window, textvariable = Psudo ,bd = 2)
    Placer(Game,Ety_Psu,0.2,0.2,0.1,0.05)

    Lbl_Psu = Label(Game.Window, text ="Votre psudo ?")
    Placer(Game,Lbl_Psu,0.1,0.2,0.1,0.05)

    Lbl_Psu_val = Button(Game.Window, text ="Valider" , command = lambda: Add_Psu(Game,Ety_Psu.get()))
    Placer(Game,Lbl_Psu_val,0.3,0.2,0.1,0.05)

    afficher_droite(Game,Fichier_Scores)
    ##Trier_Scores(Fichier_Scores)

#Affiche le nouveau score et les anciens et ajoute le nouveau au fichier, demande à rejouer
#Game , psudo --> Rien
def Add_Psu(Game,Psu):
    Game.Psudo = Psu
    Score = len(Game.Mots) * (Game.Nb_Vie - len(Game.Lettres_prop_fausse)) * 100 

    Lbl_Score = Label(Game.Window, text ="Votre score : " + str(Score) ,font=("Courier", 10))
    Placer(Game,Lbl_Score,0.15,0.4,0.2,0.1)

    with open(Fichier_Scores, 'a') as Tout_les_Scores :
        Date = "".join(list(str(datetime.now())[0:-7]))
        Score = str(Score)
        Tout_les_Scores.write("    " + Score + "  |  " + Game.Psudo + "  |  " + Date + "\n") 
        Tout_les_Scores.close()

    afficher_droite(Game,Fichier_Scores)
    rejouer(Game)

#Affiche les lettres justes et fausses deja validées
#Class --> Rien
def afficher_wrong_good(Game):
    Lbl_juste = Label(Game.Window, text = "Lettres justes : " + ' '.join(Game.Lettres_prop_juste))
    Placer(Game,Lbl_juste,0.1,0.1,0.2,0.05)
    Lbl_fausse = Label(Game.Window, text = "Lettres fausses : " + ' '.join(Game.Lettres_prop_fausse))
    Placer(Game,Lbl_fausse,0.1,0.2,0.2,0.05)

#Afficher le mots inconnue
#Class --> Rien
def update_mot(Game):
    Lbl_instruc = Label(Game.Window, text = Mots_unknow(Game.Mots,Game.Lettres_prop_juste) ,font=("Courier", 15))
    Lbl_instruc.place(x = 40 , y = 125, height = 50, width = 150)
    Placer(Game,Lbl_instruc,0.15,0.6,0.2,0.07)

#Ajoute un mots dans le fichier mots
# Mots --> Rien
def ajouter_mot(mot):
    Ajout_mot_fichier(mot,Fichier_Mots)
    Mots_ranger(Fichier_Mots)
    messagebox.showinfo(title="Ajout mot", message="Le mots " + mot + " a bien été ajouté")

#Affiche un message en bas de l'ecrant
#Class , Message ---> Rien
def affiche_message(Game,Message):
    Lbl_Mess = Label(Game.Window, text = Message)
    Placer(Game,Lbl_Mess,0.15,0.9,0.2,0.07)

#Affiche le contenu d'un fichier sur la droite de la fenettre
#Class , Fichier ---> Rien
def afficher_droite(Game,Fichier):
    Liste_mots = fichier_to_string(Fichier)
    affichage(Game,Liste_mots)

#Affiche un message sur la droite de la fenettre
#Class , Message ---> Rien
def affichage(Game,message):
    Affichage = Text(Game.Window, wrap='word')
    Placer(Game,Affichage,0.5,0.15,0.4,0.8)
    Affichage.insert('1.0', message)

#Renvoi le contenu d'un fichier dans une chaine de caractere coupé par /n a chaque ligne
#Fichier --> Chaine de caractere
def fichier_to_string(Fichier):
    with open(Fichier, 'r') as Fichier_Data :
        lines = Fichier_Data.readlines()
        Liste_lines = ""
        for line in lines :
            Liste_lines += line + "\n"
        Fichier_Data.close()
    return Liste_lines

#Place un element proportionellement à la taille de la fenettre et lui donne une taille 
#Classe , element , placement %x , %y , taille : %x , %y 
def Placer(Game,element,x_place,y_place,x_taille,y_taille):
    element.place(x = Game.Windows_Largeur*x_place , y = Game.Windows_Hauteur*y_place , height = Game.Windows_Hauteur*y_taille, width = Game.Windows_Largeur*x_taille)

main()
