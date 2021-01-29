#Fonctions annexes 

# Bibliotheque 
import random 
from datetime import datetime
from time import strftime

# Regarde si le mots est present dans le fichier
# Mots , Fichier --> True / False
def Check_mot_fichier(Mots_Ajout,Fichier):
    with open(Fichier, 'r') as Tout_les_mots :
        lignes = Tout_les_mots.readlines()
        for line in lignes :
            if Mots_Ajout in line :
                Tout_les_mots.close()
                return True
        Tout_les_mots.close()
        return False

# Ajoute le mots dans le fichier
# Mots , Fichier --> Rien
def Ajout_mot_fichier(Mots_Ajout,Fichier):
    with open(Fichier, 'a') as Tout_les_mots :
        Tout_les_mots.write(Mots_Ajout + "\n") 
        Tout_les_mots.close()

# Choisit un mots dans le fichier
# Fichier --> Mots
def Choix_mots(Fichier):
    with open(Fichier, 'r') as Tout_les_mots :
        lines = Tout_les_mots.readlines()
        x = random.randint(1,len(lines))  #Genere un nombre random 
        Mots = lines[x]
    Tout_les_mots.close()
    return Mots[0:-1]

#Mets le mots sous le format "O _ _ _ i _ _"
#Mots correct , lettre juste --> Mots formaté
def Mots_unknow(Mots,Lettres):
    Affichage = []
    for Lettre_mots in Mots :
        if Lettre_mots in Lettres :
            Affichage.append(Lettre_mots + " ")
        else :
            Affichage.append("_ ")
    Affichage[0] = Mots[0] + " "
    return("".join(Affichage))

# Regarde si la lettre donnee et bonne ou non , update vie / gagner
# Nouvelle letttre Lettre proposée juste , lettre proposée fause , Mots
# --> 
# Lettre proposée juste , lettre proposée fause , gagner 
def update_pendu(New_Lettre,Lettre_Juste,Lettre_Fausse,Mots):
    Gagner = True
    if New_Lettre in Mots : 
        Lettre_Juste.append(New_Lettre)
    else :
        Lettre_Fausse.append(New_Lettre)

    for Lettre in Mots :
        if Lettre not in Lettre_Juste :
            Gagner = False
    
    return Lettre_Juste,Lettre_Fausse,Gagner

#Range les mots par taille puis ordre alphabetique dans le fichier
# Fichier --> Rien
def Mots_ranger(Fichier="Pendu\Mots.txt"):
    Mes_mots = []
    Matrice_mots = [ [] for k in range (0,28) ] #ligne n rempli de mots de n lettres
    with open(Fichier, 'r') as Tout_les_mots :  #recupere tous les mots
        lignes = Tout_les_mots.readlines()
        for line in lignes :
            Mes_mots.append("".join(list(line)[0:-1])) #On suprime le \n ( au final inutile )
        Tout_les_mots.close()

    for Mots in Mes_mots :                #On trie les mots par taille
        n = len(Mots)
        Matrice_mots[n].append(Mots)

    for k in range (0,len(Matrice_mots)) : #Trie par ordre alphabetique
        Matrice_mots[k].sort()
        
    with open(Fichier, 'w') as Fichier : #On ecrase le fichier existant      
        for line in Matrice_mots : #On reecris
            for mots in line :
                Fichier.write(mots + "\n") 
        Fichier.close()

# Ajoute le score au fichier des scores :
# Fichier , Score --> Rien
def Ajout_Score(Score, Fichier = "Pendu\Scores.txt"):
    with open(Fichier, 'a') as Tout_les_Scores :
        Name = input("Rentrez votre psudo : ")
        Date = "".join(list(str(datetime.now())[0:-7]))
        Score = str(Score)
        print("Votre score :")
        print(Score + "  |  " + Name + "  |  " + Date + "\n")
        Tout_les_Scores.write(Score + "  |  " + Name + "  |  " + Date + "\n") 
        Tout_les_Scores.close()

#Fonction qui trie le ficher score en fonction de la date ou du score .... A faire plus tard
def Trier_Scores(Fichier = "Pendu\Scores.txt"):
    #Recupeere seulement premier chiffre ligne , puis sotck la ligne....
    #map(int,list(str(n2_int)))
    return 