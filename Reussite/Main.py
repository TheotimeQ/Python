#----------------------------------------------

#noms, prénoms et groupe

#----------------------------------------------
#Bibliotheques utilisées
import os
import random
import numpy as np
import matplotlib.pyplot as plt
from turtle import *
#--------------------------------------------
#Programme pour tester les fonctions : (F5 pour le lancer)

def test():
    print("1 :  carte_to_chaine")
    print("2:  afficher_reussite")
    print("3 :  init_pioche_fichier")
    print("4 :  ecrire_fichier_reussite")
    print("5 :  init_pioche_alea")
    print("6 :  alliance")
    print("7 :  saut_si_possible")
    print("8 :  une_etape_reussite")
    print("9 :  reussite_mode_auto")
    print("10 :  reussite_mode_manuel")
    print("11 :  lance_reussite")
    print("12 :  res_multi_simulation")
    print("13 :  statistiques_nb_tas")
    print("14 :  Graphique_proba")
    print("15 :  reussite_avec_affichage turtle")
    Choix = int(input("Entrez votre choix: "))
    print("\n")   

    if(Choix == 1):
        Dictio = {}
        Dictio["Valeur"] = "3"
        Dictio["Couleur"] = "C"
        print(carte_to_chaine(Dictio))

    if(Choix == 2):
        L = [{'Valeur': '3', 'Couleur': 'P'},{'Valeur': '8', 'Couleur': 'P'},{'Valeur': 'V', 'Couleur': 'K'},{'Valeur': 'V', 'Couleur': 'P'},{'Valeur': '10', 'Couleur': 'T'},{'Valeur': '4', 'Couleur': 'P'},{'Valeur': '8', 'Couleur': 'T'},{'Valeur': 'V', 'Couleur': 'K'}]
        print(afficher_reussite(L))

    if(Choix == 3):
        print(init_pioche_fichier("data_init"))

    if(Choix == 4):
        L = [{'Valeur': '3', 'Couleur': 'P'},{'Valeur': '8', 'Couleur': 'P'},{'Valeur': 'V', 'Couleur': 'K'},{'Valeur': 'V', 'Couleur': 'P'},{'Valeur': '10', 'Couleur': 'T'},{'Valeur': '4', 'Couleur': 'P'},{'Valeur': '8', 'Couleur': 'T'},{'Valeur': 'V', 'Couleur': 'K'}]
        ecrire_fichier_reussite("Test",L)
        print("Fichier créé")

    if(Choix == 5):
        print(init_pioche_alea(52))

    if(Choix == 6):
        print(alliance({'Valeur': 'V', 'Couleur': 'D'},{'Valeur': 'V', 'Couleur': 'C'}))

    if(Choix == 7):
        L = [{'Valeur': '3', 'Couleur': 'P'},{'Valeur': '8', 'Couleur': 'P'},{'Valeur': 'V', 'Couleur': 'K'},{'Valeur': 'V', 'Couleur': 'P'},{'Valeur': '10', 'Couleur': 'T'},{'Valeur': '4', 'Couleur': 'P'},{'Valeur': '8', 'Couleur': 'T'},{'Valeur': 'V', 'Couleur': 'K'}]
        print(saut_si_possible(L,2))

    if(Choix == 8):
        Pioche = init_pioche_alea(32)
        L = [{'Valeur': '3', 'Couleur': 'P'},{'Valeur': '8', 'Couleur': 'P'},{'Valeur': 'V', 'Couleur': 'K'},{'Valeur': 'V', 'Couleur': 'P'},{'Valeur': '10', 'Couleur': 'T'},{'Valeur': '4', 'Couleur': 'P'},{'Valeur': '8', 'Couleur': 'T'},{'Valeur': 'V', 'Couleur': 'K'}]
        une_etape_reussite(L,P,True)

    if(Choix == 9):
        Pioche = init_pioche_alea(32)
        reussite_mode_auto(Pioche,True)

    if(Choix == 10):
        Pioche = init_pioche_alea(32)
        reussite_mode_manuel(Pioche,2)

    if(Choix == 11):
        print(lance_reussite("auto",32,False,2))
        
    if(Choix == 12):
        print(res_multi_simulation(15,32))

    if(Choix == 13):
        statistiques_nb_tas(2000,32)

    if(Choix == 14):
        Graphique_proba(3000,32)

    if(Choix == 15):
        reussite_avec_affichage(32,2)
        
    print("\n")   
    test()
    return


#--------------------------------------------
#Arguments : Dictionaire modelisant une carte
#Return : Chaine de caracteres du type  : "3♡"

def carte_to_chaine(Dict):
    Val = Dict["Valeur"]
    Coul = Dict["Couleur"]
    if len(Val)<2:
        A = " "+ Val
    else :
        A = Val
    if Coul == "P":
            A = A + chr(9824)
    if Coul == "C":
            A = A + chr(9825)
    if Coul == "K":
            A = A + chr(9826)
    if Coul == "T":
            A = A + chr(9827)
    return (A)

#----------------------------------------------------
#Arguments : Suite de dictionaire modelisant les cartes
#Return : Chaine de caracteres du type  : "3♠  8♠  V♢  V♠ 10♣  4♠  8♣  V♢"

def afficher_reussite(Suite):
    Long = len(Suite)
    A = ""
    for k in range(Long):
        A = A + " " + carte_to_chaine(Suite[k])
    return(A + "\n" + "\n")

#----------------------------------------------------
#Arguments : Nom du fichier a lire
#Return : Suite de dictionaire modelisant les cartes stockées dans le fichier

def init_pioche_fichier(Nom_Fichier):
    Fichier = open(Nom_Fichier + ".txt", "r")
    Cartes = Fichier.read()
    Fichier.close
    Long = len(Cartes)
    k = 0
    L = []
    Val = "0"
    Coul = "0"
    while(k != Long-1):
        if(Cartes[k] == "-"):
            Coul = Cartes[k+1]
            if(Cartes[k-2] == " "):
                Val = Cartes[k-1]
            else:
                Val = Cartes[k-2] + Cartes[k-1]
            L.append({'Valeur': Val, 'Couleur': Coul})
        k += 1
    return(L)
    
#----------------------------------------------------
#Arguments : Nom du fichier à créer  + Liste de carte a stocker dans le fichier
#Return : Rien

def ecrire_fichier_reussite(Nom_fichier,Pioche):
    Fichier = open(Nom_fichier + ".txt", "w")
    for k in range(len(Pioche)):
        Fichier.write(Pioche[k]["Valeur"]+"-"+Pioche[k]["Couleur"]+" ")
    Fichier.close
    return
        
#----------------------------------------------------
#Arguments : Nombre de carte de la pioche à creer 
#Return : Liste de dictionaires modelisants les cartes de la pioche

def init_pioche_alea(nb_cartes = 32):
    if(nb_cartes == 32):
        A = init_pioche_fichier("init_pioche_32")   #On vas recuperer la liste de carte stocker dans un fichier
    if(nb_cartes == 52):
        A = init_pioche_fichier("init_pioche_52")
    random.shuffle(A)
    return(A)
    
#-----------------------------------------------------
#Arguments : Deux dictionaire modelisant deux cartes
#Return :True / False si les cartes forme une alliance ou non

def alliance(carte1,carte2):
    if(carte1["Valeur"] == carte2["Valeur"] or carte1["Couleur"] == carte2["Couleur"]):
        return(True)
    else:
        return(False)
    
#-----------------------------------------------------
#Arguments : Liste des cartes visible sur les tas + numero du tas a faire sauter
#Return :True / False si le le tas a sauté et modifie la liste de tas si le tas a sauté
    
def saut_si_possible(liste_tas,num_tas):
    Nb_tas = len(liste_tas)
    Carte_Droite = liste_tas[num_tas + 1]
    Carte_Gauche = liste_tas[num_tas - 1]
    if(alliance(Carte_Droite,Carte_Gauche) == True):
        for k in range(num_tas , Nb_tas):
            liste_tas[k-1] = liste_tas[k]
        liste_tas.pop()
        return(True)
    return(False)

#-----------------------------------------------------
#Arguments : Liste des cartes visible sur les tas + liste cartes pioche + True/False si on veut afficher ou pas
#Return :Rien mais liste_tas a été modifiée

def une_etape_reussite(liste_tas,pioche,affiche=False):
    
    if(affiche==True):
        print(afficher_reussite(liste_tas))
    
    liste_tas.append(pioche[0])
    pioche.pop(0)
    
    if(affiche==True):
        print(afficher_reussite(liste_tas))
        
    Nb_tas = len(liste_tas)
    
    if(saut_si_possible(liste_tas,Nb_tas - 2)==True):  
        Changement = 1
        if(affiche==True):
            print(afficher_reussite(liste_tas))
        Nb_tas = len(liste_tas)
        
        while(Changement == 1):
            k = 1
            Changement = 0
            while(k < Nb_tas - 1  and Changement == 0):       
                if(saut_si_possible(liste_tas,k)==True):
                    if(affiche==True):
                        print(afficher_reussite(liste_tas))
                    Changement = 1
                else:
                    Changement = 0
                Nb_tas = len(liste_tas)
                k = k + 1
    return

#------------------------------------------------------
#Arguments : liste cartes pioche + True/False si on veut afficher ou pas
#Return :Return la liste des tas a la fin de la reussite automatique

def reussite_mode_auto(Pioche,affiche=False):
    Pioche_Copie = list(Pioche)
    Nb_cartes_pioche = len(Pioche_Copie)
    liste_tas = []
    
    if(affiche==True):
            print(afficher_reussite(Pioche))
            
    for k in range(0,3):
        liste_tas.append(Pioche_Copie[0])
        Pioche_Copie.pop(0)
        if(affiche==True):
            print(afficher_reussite(liste_tas))
    
    while(Nb_cartes_pioche != 0):  
        une_etape_reussite(liste_tas,Pioche_Copie,affiche)
        Nb_cartes_pioche = len(Pioche_Copie)
    return(liste_tas)

#-----------------------------------------------------
#Arguments : liste cartes pioche + nombre de tas max pour gagner
#Return :Return la liste des tas a la fin de la reussite manuel

def reussite_mode_manuel(Pioche,nb_tas_max=2):
    
    Pioche_Copie = list(Pioche)
    Nb_cartes_pioche = len(Pioche_Copie)
    liste_tas = []
    
    print("Pioche :",Nb_cartes_pioche,"cartes \n")    
    print("P : Piocher | S : Faire un saut  | F : Finir la reussite | Q : Abandonner ")
    Choix = input("Entrez votre choix: ")
    
    while(Choix in ("P","S","F","Q")):
        
        if(Choix == "Q" and Nb_cartes_pioche != 0):
            while(Nb_cartes_pioche != 0):
                liste_tas.append(Pioche_Copie[0])
                Pioche_Copie.pop(0)
                Nb_cartes_pioche = len(Pioche_Copie)
                Nb_tas = len(liste_tas)
                print(afficher_reussite(liste_tas))

        if(Choix == "P" and Nb_cartes_pioche != 0):
            liste_tas.append(Pioche_Copie[0])
            Pioche_Copie.pop(0)
            Nb_cartes_pioche = len(Pioche_Copie)
            Nb_tas = len(liste_tas)
            print(" \n")
            print(afficher_reussite(liste_tas))

        if(Choix == "S"):
            Num_tas_saut= int(input("Entrez le numero du tas :"))
            Num_tas_saut = Num_tas_saut - 1
            Nb_cartes_pioche = len(Pioche_Copie)
            Nb_tas = len(liste_tas)
            if(Num_tas_saut != 0 and Num_tas_saut != Nb_tas - 1 and Num_tas_saut < Nb_tas - 1):
                if(saut_si_possible(liste_tas,Num_tas_saut) == True):
                    print("Saut effectué ")
                    print(afficher_reussite(liste_tas))
                    Nb_cartes_pioche = len(Pioche_Copie)
                    Nb_tas = len(liste_tas)
                else :
                    print("Saut impossible ")
                    print(afficher_reussite(liste_tas))
            else:
                print("Saut impossible ")
                print(afficher_reussite(liste_tas))
                    
        if(Choix == "F"):
            Nb_cartes_pioche = len(Pioche_Copie)
            Nb_tas = len(liste_tas)
            while(Nb_tas < 3 and Nb_cartes_pioche !=0):
                liste_tas.append(Pioche_Copie[0])
                Pioche_Copie.pop(0)
                print(afficher_reussite(liste_tas))
                Nb_cartes_pioche = len(Pioche_Copie)
                Nb_tas = len(liste_tas)
            while(Nb_cartes_pioche != 0):  
                une_etape_reussite(liste_tas,Pioche_Copie,True)
                Nb_cartes_pioche = len(Pioche_Copie)
                
        Nb_tas = len(liste_tas)        
        Nb_cartes_pioche = len(Pioche_Copie)
        
        if(Nb_cartes_pioche == 0):
            if(Nb_tas <= nb_tas_max):
                print("C'est gagné!! :D ")
                return(liste_tas)
        if(Nb_cartes_pioche == 0):
            if(Nb_tas > nb_tas_max):
                print("Perdu :( ")
                return(liste_tas)
                
        print("Pioche :",Nb_cartes_pioche,"cartes \n")    
        print("P : Piocher | S : Faire un saut  | F : Finir la reussite | Q : Abandonner ")
        Choix= input("Entrez votre choix: ")
    return(liste_tas)
    
#-----------------------------------------------------
#Arguments : mode + nb de cartes de la pioche , True/False - Affichage , Nb de tas max pour gagner
#Return :Return la liste des tas a la fin de la reussite

def lance_reussite(mode,nb_cartes=32,affiche=False,nb_tas_max=2):
    if(nb_cartes != 32 and nb_cartes != 52):
        return("Nombre de cartes invalide")
    if(mode != "manuel" and mode != "auto"):
        return("Mode invalide")
    Pioche = init_pioche_alea(nb_cartes)
    if(mode == "auto"):
        liste_tas = reussite_mode_auto(Pioche,affiche)
    if(mode =="manuel"):
        liste_tas = reussite_mode_manuel(Pioche,nb_tas_max)
    return(liste_tas)
        
#-----------------------------------------------------
#Arguments : nombre de simulation a faire , nombre de carte de la pioche pour chaque simulation
#Return :Return la liste des nombre de tas à la fin de chaque simulation

def res_multi_simulation(nb_sim,nb_cartes=32):
    L = []
    for k in range(nb_sim):
        Pioche = init_pioche_alea(nb_cartes)
        L.append(len(lance_reussite("auto",nb_cartes,affiche=False)))
    return(L)

#------------------------------------------------------
#Arguments : nombre de simulation a faire , nombre de carte de la pioche pour chaque simulation
#Return :Rien , mais affiche  la moyenne , le max et le min des nombre de tas

def statistiques_nb_tas(nb_sim,nb_cartes=32):
    L = res_multi_simulation(nb_sim,nb_cartes)
    Maximum = L[0]
    Minimum = L[0]
    Moyenne = 0
    for i in L:
        if(i >= Maximum):
            Maximum = i
        if(i <= Minimum):
            Minimum = i
        Moyenne = Moyenne + i
    Moyenne = Moyenne / len(L)
    print("Moyenne :",Moyenne)
    print("Minimum :",Minimum)
    print("Maximum :",Maximum)
    return

#-----------------------------------------------------
#Arguments : nombre de simulation a faire , nombre de carte de la pioche pour chaque simulation
#Return :Rien , mais affiche un graphe avec la proba de gagner la partie en ordonée , et le nombre de tas max pour gagner en abscisse

def Graphique_proba(Nb_sim,Nb_cartes=32):
    Proba = []
    Nb_tas = [ k for k in range(2,33) ]
    L = res_multi_simulation(Nb_sim,Nb_cartes)
    for k in range(2,33):
        Nb_gagne = 0
        for i in L:
            if(i <= k) :
                Nb_gagne += 1
        Proba.append(Nb_gagne/Nb_sim)
    print(Nb_tas)
    print(Proba)
    plt.plot(Nb_tas, Proba)
    plt.show()
    return
        
#-----------------------------------------------------
#Arguments : nombre de carte de la pioche , tas max pour gagner
#Return :Rien , mais lance une partie en mode manuel avec affichage turtle
def reussite_avec_affichage(Nb_cartes=32,Nb_tas_max=2):
    fenetre = Screen()
    setup(width=1400,height=250)
    valeurs  = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'D', 'R', 'A']
    couleurs = ['P', 'C', 'K', 'T']
    carte = {}
    for c in couleurs:
        for v in valeurs:
            fichier = "imgs/carte-" + v + '-' + c + '.gif'
            carte[c, v] = fichier
            fenetre.register_shape( fichier )

    Pioche = init_pioche_alea(Nb_cartes)
    reussite_mode_manuel_turtle(Pioche,carte,Nb_tas_max)
    goto(0,0)
    write("Cliquez dans la fenêtre pour terminer.", align='center')
    exitonclick()
    return

#-----------------------------------------------------
#Adaptation de : reussite_mode_manuel pour utiliser turtle 
def reussite_mode_manuel_turtle(Pioche,carte,nb_tas_max=2):
    
    Pioche_Copie = list(Pioche)
    Nb_cartes_pioche = len(Pioche_Copie)
    liste_tas = []
    tampons = {}
    
    print("Pioche :",Nb_cartes_pioche,"cartes \n")    
    print("P : Piocher | S : Faire un saut  | F : Finir la reussite | Q : Abandonner ")
    Choix= input("Entrez votre choix: ")
    
    while(Choix in ("P","S","F","Q")):
        
        if(Choix == "Q" and Nb_cartes_pioche != 0):
            while(Nb_cartes_pioche != 0):
                liste_tas.append(Pioche_Copie[0])
                Pioche_Copie.pop(0)
                Nb_cartes_pioche = len(Pioche_Copie)
                Nb_tas = len(liste_tas)
                tampons = afficher_reussite_turtle(liste_tas,carte,tampons)

        if(Choix == "P" and Nb_cartes_pioche != 0):
            liste_tas.append(Pioche_Copie[0])
            Pioche_Copie.pop(0)
            Nb_cartes_pioche = len(Pioche_Copie)
            Nb_tas = len(liste_tas)
            print(" \n")
            tampons = afficher_reussite_turtle(liste_tas,carte,tampons)

        if(Choix == "S"):
            Num_tas_saut= int(input("Entrez le numero du tas :"))
            Num_tas_saut = Num_tas_saut - 1
            Nb_cartes_pioche = len(Pioche_Copie)
            Nb_tas = len(liste_tas)
            if(Num_tas_saut != 0 and Num_tas_saut != Nb_tas - 1 and Num_tas_saut < Nb_tas - 1):
                if(saut_si_possible(liste_tas,Num_tas_saut) == True):
                    print("Saut effectué ")
                    reset()
                    tampons = afficher_reussite_turtle(liste_tas,carte,tampons)
                    Nb_cartes_pioche = len(Pioche_Copie)
                    Nb_tas = len(liste_tas)
                else :
                    print("Saut impossible ")
                    tampons = afficher_reussite_turtle(liste_tas,carte,tampons)
            else:
                print("Saut impossible ")
                tampons = afficher_reussite_turtle(liste_tas,carte,tampons)
                    
        if(Choix == "F"):
            Nb_cartes_pioche = len(Pioche_Copie)
            Nb_tas = len(liste_tas)
            while(Nb_tas < 3 and Nb_cartes_pioche !=0):
                liste_tas.append(Pioche_Copie[0])
                Pioche_Copie.pop(0)
                tampons = afficher_reussite_turtle(liste_tas,carte,tampons)
                Nb_cartes_pioche = len(Pioche_Copie)
                Nb_tas = len(liste_tas)
            while(Nb_cartes_pioche != 0):  
                une_etape_reussite(liste_tas,Pioche_Copie,True)
                Nb_cartes_pioche = len(Pioche_Copie)
                
        Nb_tas = len(liste_tas)        
        Nb_cartes_pioche = len(Pioche_Copie)
        
        if(Nb_cartes_pioche == 0):
            if(Nb_tas <= nb_tas_max):
                print("C'est gagné!! :D ")
                return(liste_tas)
        if(Nb_cartes_pioche == 0):
            if(Nb_tas > nb_tas_max):
                print("Perdu :( ")
                return(liste_tas)
                
        print("Pioche :",Nb_cartes_pioche,"cartes \n")    
        print("P : Piocher | S : Faire un saut  | F : Finir la reussite | Q : Abandonner ")
        Choix= input("Entrez votre choix: ")
    return(liste_tas)
    
#-----------------------------------------------------
#Adaptation de afficher_reussite pour utiliser turtle 
def afficher_reussite_turtle(Suite,carte,tampons):
    fenetre = Screen()
    setup(width=1400,height=250)
    dos = "imgs/carte-dos.gif"
    fenetre.register_shape( dos )
    xinit = -600
    yinit =  0
    largeur_carte = 69
    hauteur_carte = 100
    separation = 5
    up()
    speed(15)
    x = xinit
    y = yinit
    k = 0
        
    tampons = {}
    for i in Suite :
        C = i["Couleur"]
        V = i["Valeur"]
        shape( dos )
        goto (x, y)
        shape( carte[C,V] )
        tampons[C, V] = stamp()
        x = x + largeur_carte + separation
        #y = y - hauteur_carte - separation
        hideturtle()

    return(tampons)

#----------------------------------------------------
#print(carte_to_chaine(Dictio))
#afficher_reussite(L)
#init_pioche_fichier("data_init")
#ecrire_fichier_reussite("Nom_fichier",L)
#init_pioche_alea(52)
#alliance({'Valeur': 'V', 'Couleur': 'D'},{'Valeur': 'V', 'Couleur': 'C'})
#print(saut_si_possible(L,2))
#une_etape_reussite(L,P,True)
#reussite_mode_auto(Pioche,True)
#reussite_mode_manuel(Pioche,2)
#print(lance_reussite("auto",32,False,2))
#print(res_multi_simulation(15,32))
#statistiques_nb_tas(5000,32)
#Graphique_proba(4000,32)
#reussite_avec_affichage(32,2)
#--------------------------------------------------

test()










