# Jeu de reverso en ligne de commande
# Ecrit avec Python

grille = [[0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,0,0,0],
          [0,0,0,2,1,0]] # Grille du jeu. Ici, une case ayant pour valeur 0 veut dire qu'elle est vide. Si elle a pour valeur 1, alors le joueur 1 y a placé un pion, et si elle a pour valeur 2, alors le joueur 2 y a placé un pion.
          

def recupererSymbole(joueur):
    "Récupérer le symbole d'un joueur"
    if joueur == 1: # Si c'est le joueur 1 qui est donné en paramètre
        return "a" # On retourne la lettre "a" comme son symbole
    
    if joueur == 2: # Si c'est le joueur 2 qui est donné en paramètre
        return "b" # On retourne la lettre "b" comme son symbole
    

def afficherGrille():
    "Afficher la grille du jeu"
    for ligne in range(len(grille)): # Pour chaque ligne de la grille
        for colonne in grille[ligne] : # Pour chaque colonne de la ligne actuelle
            #print("Contenu de la case :", colonne)
            if ligne == 0 or ligne == 5: # Si on est à la première ou à la dernière ligne de la grille
                if colonne == 0: # Si aucun joueur n'a placé un pion dans une case de la ligne
                    print("-", end = " ") 
            

            else:
                if colonne == 0:
                    print("|", end = " ")


            if colonne != 0: # Si une colonne a une case dont la valeur est différente de 0, alors c'est qu'un joueur y a placé un pion
                    #print("Le contenu de la case vaut", colonne)
                    print(recupererSymbole(colonne), end= " ") # On affiche le symbole du joueur dans la grille de jeu



                
                    
                   

        print() # On appelle print() pour faire un saut à la ligne



def trouverLigneLibre(colonne):
    "Trouver la dernière ligne libre dans une colonne"
    for ligne in range(len(grille[colonne]) -1, -1, -1): # On parcoure chaque case de la colonne à l'envers de manière à trouver la dernière ligne libre
            if grille[ligne][colonne] == 0: # Si aucun pion n'a été placé sur la ligne
                 return ligne # On retourne la ligne libre

    return -1 # Si aucune ligne n'est libre, alors on retourne -1         



def demanderColonne(joueur):
     "Demander au joueur dans quelle colonne placer un jeton"
     try:
        colonne = int(input(f"Joueur {joueur}, indiquez dans quelle colonne placer un pion (peut être comprise entre 0 et 5):")) # Demander au joueur dans quelle colonne il faut placer un jeton
        if trouverLigneLibre(colonne) == -1: # Si aucune ligne n'est libre dans la colonne demandée
               print(f"La colonne n°{colonne} est entièrement occupée. Veuillez saisir une autre colonne :") # On indique au joueur que la colonne de son choix n'est plus libre
               demanderColonne(joueur) # Demander au joueur de saisir une autre colonne

        return colonne       
     

     except ValueError: 
          print("Le numéro de la colonne saisie est invalide. Veuillez ne saisir qu'un nombre entier.")
          colonne = int(input(f"Joueur {joueur}, indiquez dans quelle colonne placer un pion (peut être comprise entre 0 et 5):")) # Demander au joueur dans quelle colonne il faut placer un jeton
          if trouverLigneLibre(colonne) == -1: # Si aucune ligne n'est libre dans la colonne demandée
               print(f"La colonne n°{colonne} est entièrement occupée. Veuillez saisir une autre colonne :") # On indique au joueur que la colonne de son choix n'est plus libre
               demanderColonne(joueur) # Demander au joueur de saisir une autre colonne

          return colonne    


     except IndexError:
          print("Il n'y a aucune colonne correspondant au numéro que vous avez saisi. Veuillez saisir un numéro entre 0 et 5:")
          colonne = int(input(f"Joueur {joueur}, indiquez dans quelle colonne placer un pion (peut être comprise entre 0 et 5):")) # Demander au joueur dans quelle colonne il faut placer un jeton
          if trouverLigneLibre(colonne) == -1: # Si aucune ligne n'est libre dans la colonne demandée
               print(f"La colonne n°{colonne} est entièrement occupée. Veuillez saisir une autre colonne :") # On indique au joueur que la colonne de son choix n'est plus libre
               demanderColonne(joueur) # Demander au joueur de saisir une autre colonne

          return colonne     


def placerPion(joueur, colonne):
     "Placer le pion d'un joueur dans une colonne donnée"
     ligne_libre = trouverLigneLibre(colonne)
     grille[ligne_libre][colonne] = joueur
          
               
                              


while True:
     joueurs = [1,2]
     for joueur in joueurs:
          colonne = demanderColonne(joueur)
          placerPion(joueur, colonne)
          afficherGrille() 

                   
