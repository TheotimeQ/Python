#Jeux du pendu dans la console - FINI 

# Bibliotheque 
# Rien

# Mes fonctions 
from MyFunction import *

# Variable 
Fichier_Mots = "Rendu\Console\Mots.txt"
Fichier_Score = "Rendu\Console\Scores.txt"

# Choisit Entre Jouer / Ajouter / Regarder les mots / regarder les scores
# Rien --> Rien
def main():
    print('Jeux du pendu :')
    print('1 - Jouer  :')
    print('2 - Ajouter un mots')
    print('3 - Regarder les mots')
    print('4 - Afficher les scores')
    Choix = input("Votre choix : ")

    if Choix == "1" :
        print("C'est parti!")
        Pendu_Console(Fichier_Mots)

    elif Choix == "2" :
        Mots_Ajout = input("Taper le mots à ajouter : ")
        if Check_mot_fichier(Mots_Ajout,Fichier_Mots):
            print("Le mots existe deja")
        else : 
            Ajout_mot_fichier(Mots_Ajout,Fichier_Mots)
            Mots_ranger(Fichier_Mots)
            print("Le mots : "+ Mots_Ajout +" a été ajouté")
            main()

    elif Choix == "3" :
        Print_mot_fichier(Fichier_Mots)
        main()

    elif Choix == "4":
        Afficher_Scores(Fichier_Score)
    
# Print tous les mots du fichier
# Fichier --> Rien
def Print_mot_fichier(Fichier):
    print("Voici la liste des mots : ")
    print("\n")
    with open(Fichier, 'r') as Tout_les_mots :
        lines = Tout_les_mots.readlines()
        for line in lines :
            print(line)
        Tout_les_mots.close()

# Affiche le mots correctement dans la console en fonction des lettres qui ont etait proposées
# Mots , Lettre proposée --> Rien
def Afficher_mots(Mots,Lettres):
    Affichage = []
    for Lettre_mots in Mots :
        if Lettre_mots in Lettres :
            Affichage.append(Lettre_mots + " ")
        else :
            Affichage.append("_ ")
    Affichage[0] = Mots[0] + " "
    print("".join(Affichage))

# Affiche les scores contenue dans le fichier 
# Fichier --> Rien
def Afficher_Scores(Fichier):
    with open(Fichier, 'r') as Tout_les_Scores :
        lignes = Tout_les_Scores.readlines()
        for line in lignes :
            print("".join(list(line)[0:-1]))
        Tout_les_Scores.close()

# Affiche le pendu 
# Nombre d'essai raté --> Rien
def Afficher_Pendu(Nb_Raté):
    Pendu = [ [" _________"," |/    |"," |     O"," |   _/|\_"," |     |    "," |    / \   "," |\  |   |  "," |_\________"],
              [" |_\________"," |\       "," |       "," |         "," |   "," |     " , " |/    " , " _________"] ]
    
    if Nb_Raté == 8 :
        for To_Print in Pendu[0]:
            print(To_Print)
    else :
        for k in range(Nb_Raté-1, -1, -1):
            print(Pendu[1][k])

# _________  8
# |/    |    7
# |          6
# |          5
# |          4
# |          3
# |\         2
# |_\________1

# Demare le jeux
# Fichier --> Rien
def Pendu_Console(fichier):
    Nb_Vie = 8
    Gagner = False
    Mots = Choix_mots(fichier)
    Mots_liste = list(Mots)
    Taille_mots = len(Mots)
    Lettres_prop_juste = [Mots_liste[0]]
    Lettres_prop_fausse = []
    print("\n")
    print("Trouver le mots suivant :")
    print("\n")
    Afficher_mots(Mots,Lettres_prop_juste)
    print("\n")
    while ( len(Lettres_prop_fausse) < Nb_Vie and Gagner == False) :
        Nouvelle_Lettre = input("A quelle lettre penssez vous ? : ")
        while (Nouvelle_Lettre in Lettres_prop_juste or Nouvelle_Lettre in Lettres_prop_fausse):
            print("Vous avez deja entré cette lettre....")
            Nouvelle_Lettre = input("Nouvelle nouvelle lettre ? : ")
        print("\n")
        [Lettres_prop_juste,Lettres_prop_fausse,Gagner] = update_pendu(Nouvelle_Lettre,Lettres_prop_juste,Lettres_prop_fausse,Mots)
        print("Lettre juste :" , Lettres_prop_juste)
        print("Lettre Fausse :" ,Lettres_prop_fausse)
        print("\n")
        Afficher_Pendu(len(Lettres_prop_fausse))
        print("\n")
        Afficher_mots(Mots,Lettres_prop_juste)
        print("\n")

    if Gagner == True :
        Score = len(Mots) * (Nb_Vie - len(Lettres_prop_fausse)) * 100 
        print(" Et c'est gagnnnnnnéééééé")
        print("\n")
        Ajout_Score(Score,Fichier_Score)
        Trier_Scores(Fichier_Score)
        Afficher_Scores(Fichier_Score)
        print("\n")
        print("Rejouer ?")
        print("\n")
        main()

    else :
        print(" Et c'est perduuuuuuuu")
        print("\n")
        Trier_Scores(Fichier_Score)
        Afficher_Scores(Fichier_Score)
        print("\n")
        print("Rejouer ?")
        print("\n")
        main()

main()

