# Jeu de reverso en ligne de commande
# Ecrit avec Python

grille = [[0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0]] # Grille du jeu. Ici, une case ayant pour valeur 0 veut dire qu'elle est vide. Si elle a pour valeur 1, alors le joueur 1 y a placé un pion, et si elle a pour valeur 2, alors le joueur 2 y a placé un pion.
          

def recupererSymbole(joueur):
    "Récupérer le symbole d'un joueur"
    if joueur == 1: # Si c'est le joueur 1 qui est donné en paramètre
        return "a" # On retourne la lettre "a" comme son symbole
    
    if joueur == 2: # Si c'est le joueur 2 qui est donné en paramètre
        return "b" # On retourne la lettre "b" comme son symbole
    

def afficherGrille():
    "Afficher la grille du jeu"
    for ligne in range(len(grille)): # Pour chaque ligne de la grille
        for colonne in grille[ligne]: # Pour chaque colonne de la ligne actuelle
            if ligne == 0 or ligne == 5: # Si on est à la première ou à la dernière ligne de la grille
                print("-", end = " ") 

            

            if ligne > 0 and ligne < 5: # Tant qu'on est ni à la première ni à la dernière ligne
                print("|", end =" ")

        print() # On appelle print() pour faire un saut à la ligne



afficherGrille()
