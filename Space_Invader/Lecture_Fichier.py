#Toutes les fonctions qui lisent dans des fichier

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