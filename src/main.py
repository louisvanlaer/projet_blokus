COINS = [(0, 0), (0, 19), (19, 0), (19, 19)]
"""Liste des coins du plateau où les joueurs doivent placer leur première pièce."""

def creer_plateau(taille=20):
    """
    Crée une grille de jeu Blokus vide de taille `taille x taille`.

    Args:
        taille (int): La taille du plateau, par défaut 20x20.

    Returns:
        list: Une matrice de taille `taille x taille` remplie de zéros.
    """
    return [[0 for _ in range(taille)] for _ in range(taille)]

def afficher_plateau(plateau):
    """
    Affiche l'état actuel du plateau de jeu dans la console.

    Args:
        plateau (list): La matrice représentant le plateau du jeu.
    """
    print("\nÉtat du plateau :")
    for ligne in plateau:
        print(" ".join(str(case) if case != 0 else "-" for case in ligne))
    print()


def afficher_piece(piece):
    """
    Affiche une pièce donnée dans la console.

    Args:
        piece (list): La matrice représentant la pièce du jeu.
    """
    for ligne in piece:
        print(" ".join(str(case) if case != 0 else "." for case in ligne))
    print()
    
def transformer_piece(piece, rotation=0, miroir_h=False, miroir_v=False):
    """
    Vérifie si la pièce est connectée à une autre pièce du même joueur par un coin.

    Args:
        plateau (list): Le plateau de jeu.
        piece (list): La pièce à placer.
        position (tuple): Coordonnées (x, y) sur le plateau.
        joueur (int): Numéro du joueur.

    Returns:
        bool: True si la pièce touche une autre du même joueur par un coin, sinon False.
    """
    for _ in range(rotation // 90):
        piece = [list(reversed(col)) for col in zip(*piece)]

    if miroir_h:
        piece = [list(reversed(ligne)) for ligne in piece]

    if miroir_v:
        piece = list(reversed(piece))

    return piece

def est_connexion_diagonale(plateau, piece, position, joueur):
    """
    Vérifie si la pièce est connectée à une autre pièce du même joueur par un coin.

    Args:
        plateau (list): Le plateau de jeu.
        piece (list): La pièce à placer.
        position (tuple): Coordonnées (x, y) sur le plateau.
        joueur (int): Numéro du joueur.

    Returns:
        bool: True si la pièce touche une autre du même joueur par un coin, sinon False.
    """
    x, y = position
    directions_diagonales = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j] == 1:
                for dx, dy in directions_diagonales:
                    nx, ny = x + i + dx, y + j + dy
                    if 0 <= nx < len(plateau) and 0 <= ny < len(plateau[0]) and plateau[nx][ny] == joueur:
                        return True
    return False

def est_adjacent(plateau, piece, position, joueur):
    """
    Vérifie si la pièce est adjacente à une autre du même joueur (interdit dans les règles de Blokus).

    Args:
        plateau (list): Le plateau de jeu.
        piece (list): La pièce à placer.
        position (tuple): Coordonnées (x, y) sur le plateau.
        joueur (int): Numéro du joueur.

    Returns:
        bool: True si la pièce est adjacente, sinon False.
    """
    x, y = position
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j] == 1:
                for dx, dy in directions:
                    nx, ny = x + i + dx, y + j + dy
                    if 0 <= nx < len(plateau) and 0 <= ny < len(plateau[0]) and plateau[nx][ny] == joueur:
                        return True
    return False

def placement_piece(plateau, piece, position, joueur, premiere_piece_place,placement_reel):
    # Gère le placement d'une piece sur le plateau en respectant les règles.
    if not isinstance(piece, list) or not all(isinstance(row, list) for row in piece):
        raise TypeError("La piece doit être une liste de listes.")

    listes_erreurs = {
        0 : "",
        1 : "Erreur : Placement en dehors du plateau.",
        2 : "Erreur : La premiere piece doit être placee dans l'un des coins du plateau.",
        3 : "Erreur : Les pieces doivent se toucher en diagonale.",
        4 : "Erreur : Vous ne pouvez pas placer une piece sur une autre deja existante.",
        5 : "Erreur : Vous ne pouvez pas placer une piece a cote d'une de vos autres pieces"
    }

    x, y = position
    lignes_plateau, colonnes_plateau = len(plateau), len(plateau[0])
    
    code_erreur=0

    #Verification du placement à l intérieur du plateau
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j] == 1:
                if x + i >= lignes_plateau or y + j >= colonnes_plateau:
                    code_erreur=1
                    if placement_reel == 1:
                        print(f"Code erreur {code_erreur} : {listes_erreurs[code_erreur]}")
                    return False

    
    #Verification que les pièces ne se superposent pas
    if premiere_piece_place[joueur]:
        for i in range(len(piece)):
            for j in range(len(piece[i])):
                if piece[i][j] == 1 and plateau[x + i][y + j] != 0:
                    code_erreur=4
                    if placement_reel == 1:
                        print(f"Code erreur {code_erreur} : {listes_erreurs[code_erreur]}")
                    return False    
                
    #Verification si les pièces se touchent bien par une diagonale                
    if premiere_piece_place[joueur]:
        if not est_connexion_diagonale(plateau, piece, position, joueur):
            code_erreur=3
            if placement_reel == 1:
                print(f"Code erreur {code_erreur} : {listes_erreurs[code_erreur]}")
            return False
            
    #Verification si les pieces sont adjacentes                
    if premiere_piece_place[joueur]:
        if est_adjacent(plateau, piece, position, joueur):
            code_erreur=5
            if placement_reel == 1:
                print(f"Code erreur {code_erreur} : {listes_erreurs[code_erreur]}")
            return False
    
    #Verification de la pose de la premiere piece dans un coin
    if not premiere_piece_place[joueur]:
        premiere_valide = False  # Variable pour vérifier si une case est dans un coin
        for i in range(len(piece)):
            for j in range(len(piece[i])):
                position2 = (x + i, y + j)
                if piece[i][j] == 1 and position2 in COINS:
                    premiere_valide = True  # Au moins une case est dans un coin
        if premiere_valide:
            premiere_piece_place[joueur] = True
        else:
            code_erreur=2
            if placement_reel == 1:
                print(f"Code erreur {code_erreur} : {listes_erreurs[code_erreur]}")
            return False

    #Pose des pieces
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j] == 1:
                plateau[x + i][y + j] = joueur
    return True

def generer_pieces():
    """
    Génère les 21 pièces prédéfinies du jeu Blokus.

    Returns:
        dict: Un dictionnaire contenant les pièces prédéfinies.
    """
    pieces = {
        "Monomino (1 carre)": [[1]],
        "Domino (2 carres)": [[1, 1]],
        "Tromino en L": [[1, 0], [1, 1]],
        "Tromino en ligne": [[1, 1, 1]],
        "Tetromino carre": [[1, 1], [1, 1]],
        "Tetromino en T": [[0, 1, 0], [1, 1, 1]],
        "Tetromino en L": [[1, 0, 0], [1, 1, 1]],
        "Tetromino en Z": [[1, 1, 0], [0, 1, 1]],
        "Tetromino en ligne": [[1, 1, 1, 1]],
        "Pentomino en T": [[1, 1, 1], [0, 1, 0], [0, 1, 0]],
        "Pentomino en V": [[1, 0, 0], [1, 0, 0], [1, 1, 1]],
        "Pentomino en Z": [[1, 1, 0], [0, 1, 0], [0, 1, 1]],
        "Pentomino en U": [[1, 0, 1], [1, 1, 1]],
        "Pentomino en W": [[1, 0, 0], [1, 1, 0], [0, 1, 1]],
        "Pentomino en L": [[1, 0, 0, 0], [1, 1, 1, 1]],
        "Pentomino en P": [[1, 1, 0], [1, 1, 1,]],
        "Pentomino en F": [[0, 1, 1], [1, 1, 0], [0, 1, 0]],
        "Pentomino en Y": [[0, 1, 0, 0], [1, 1, 1, 1]],
        "Pentomino en X": [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
        "Pentomino en N": [[1, 1, 0, 0], [0, 1, 1, 1]],
        "Pentomino en I": [[1, 1, 1, 1, 1]]
    }
    return pieces

def initialiser_pieces_joueurs():
    """
    Initialise les pièces disponibles pour chaque joueur.

    Returns:
        dict: Un dictionnaire contenant les pièces pour chaque joueur.
    """
    pieces_joueur_1 = generer_pieces()
    pieces_joueur_2 = generer_pieces()
    return {1: pieces_joueur_1, 2: pieces_joueur_2}

def jouer_tour(plateau, joueur, nom_piece, position, joueur_actuel, premiere_piece_place, pieces_restantes):
    """
    Gère le tour de jeu d'un joueur spécifique.

    Args:
        plateau (list): Le plateau de jeu.
        joueur (int): Le numéro du joueur actuel.
        nom_piece (str): Le nom de la pièce choisie.
        position (tuple): Les coordonnées (x, y) pour le placement.
        joueur_actuel (int): Le joueur en cours de jeu.
        premiere_piece_place (dict): Indicateur de placement des premières pièces.
        pieces_restantes (dict): Pièces restantes des joueurs.
    """
    if joueur != joueur_actuel:
        print(f"Erreur : Ce n'est pas le tour du joueur {joueur}.")
        return False

    if nom_piece not in pieces_restantes[joueur]:
        print("Erreur : La piece choisie n'est plus disponible.")
        return False

    piece = pieces_restantes[joueur][nom_piece]

    if placement_piece(plateau, piece, position, joueur, premiere_piece_place,1):
        print(f"Joueur {joueur} : piece placee avec succès.")
        del pieces_restantes[joueur][nom_piece]
        return True
    else:
        return False

def peut_jouer(plateau, pieces_restantes, joueur, premiere_piece_place):
    """
    Vérifie si le joueur peut encore placer au moins une pièce sur le plateau.

    Args:
        plateau (list): Le plateau de jeu.
        pieces_restantes (dict): Pièces restantes des joueurs.
        joueur (int): Le numéro du joueur.
        premiere_piece_place (dict): Indicateur de placement des premières pièces.

    Returns:
        bool: True si le joueur peut encore jouer, sinon False.
    """
    for nom_piece, piece in pieces_restantes[joueur].items():
        for x in range(len(plateau)):
            for y in range(len(plateau[0])):
                if placement_piece(plateau, piece, (x, y), joueur, premiere_piece_place.copy(),0):
                    retirer_piece(plateau, piece, (x, y))  # Retirer la piece après test
                    return True
    return False

def retirer_piece(plateau, piece, position):
    """
    Retire une pièce du plateau après un placement de test.

    Args:
        plateau (list): Le plateau de jeu.
        piece (list): La pièce à retirer.
        position (tuple): Coordonnées (x, y) de la pièce à retirer.
    """
    x, y = position
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j] == 1:
                plateau[x + i][y + j] = 0

def partie_terminee(plateau, pieces_restantes, premiere_piece_place):
    """
    Vérifie si la partie est terminée en s'assurant qu'aucun joueur ne peut plus jouer.

    Args:
        plateau (list): Le plateau de jeu.
        pieces_restantes (dict): Pièces restantes des joueurs.
        premiere_piece_place (dict): Indicateur de placement des premières pièces.

    Returns:
        bool: True si la partie est terminée, sinon False.
    """
    for joueur in pieces_restantes:
        if pieces_restantes[joueur] and peut_jouer(plateau, pieces_restantes, joueur, premiere_piece_place):
            return False  # Si un joueur peut encore jouer, la partie continue
    return True  # Aucun joueur ne peut jouer, la partie est terminée



def main():
    """
    Fonction principale qui gère l'exécution du jeu Blokus.
    Elle demande le nombre de joueurs, initialise le plateau et gère les tours de jeu.
    La partie se termine lorsqu'aucun joueur ne peut plus poser de pièce.
    """
    plateau = creer_plateau(20)
    afficher_plateau(plateau)
    pieces_restantes = initialiser_pieces_joueurs()
    joueurs = [1, 2]
    joueur_actuel = joueurs[0]
    premiere_piece_place = {1: False, 2: False}
    ascii_art = """

///** ██████╗ ██╗      ██████╗ ██╗  ██╗██╗   ██╗███████╗ **|||
///** ██╔══██ ██║     ██╔═══██╗██║ ██╔╝██║   ██║██╔════╝ **|||
///*  ███████ ██║     ██║   ██║█████╔╝ ██║   ██║███████╗  *|||
//*   ██╔══██ ██║     ██║   ██║██╔═██╗ ██║   ██║╚════██║   *||
/*    ██████╗╝███████╗╚██████╔╝██║  ██╗╚██████╔╝███████║    *|
*     ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝     *
"""
    print(ascii_art)
    while True:
        try:
            nombre_joueurs = int(input("Combien de joueurs veulent s'amuser à jouer à Blokus ? "))
            # Vérification si le nombre est entre 2 et 4 inclus
            if not (2 <= nombre_joueurs <= 4):
                print("Erreur : Veuillez entrer un nombre entre 2 et 4.")
                continue
            break
        except ValueError:  
            print("Erreur : Veuillez entrer un nombre valide (entre 2 et 4).")

    print(f"C'est parti pour {nombre_joueurs} joueurs !")

    # Fonction principale qui gère la partie de Blokus.
    plateau = creer_plateau(20)
    afficher_plateau(plateau)
    pieces_restantes = {i: generer_pieces() for i in range(1, nombre_joueurs + 1)}
    joueurs = list(range(1, nombre_joueurs+1))
    print (f"{joueurs}")
    joueur_actuel = joueurs[0]
    premiere_piece_place = {i: False for i in range(1, nombre_joueurs+1)}
    
    print (f"{premiere_piece_place}")

    while not partie_terminee(plateau, pieces_restantes, premiere_piece_place):
        print(f"\nJoueur {joueur_actuel}, c'est votre tour !")
        print("\npieces disponibles :")
        for i, nom_piece in enumerate(pieces_restantes[joueur_actuel].keys()):
            print(f"{i + 1}. {nom_piece}")# Sélection de la piece
            afficher_piece(pieces_restantes[joueur_actuel][nom_piece])
        while True:
            try:
                choix = int(input(f"\nJoueur {joueur_actuel} Choisissez une piece (entrez le numéro ou -1 pour quitter) : "))
                if choix == -1:
                    print("Partie interrompue. Merci d'avoir joué !")
                    return
                nom_piece_choisie = list(pieces_restantes[joueur_actuel].keys())[choix - 1]
                break
            except (ValueError, IndexError):
                print("Choix invalide. Veuillez entrer un numéro valide.")

        print("\nVous avez choisi la piece :")
        afficher_piece(pieces_restantes[joueur_actuel][nom_piece_choisie])

        # Transformation de la piece
        while True:
            rotation = input("Voulez-vous tourner la piece ? (0, 90, 180, 270) : ")
            if rotation in ['0', '90', '180', '270']:
                pieces_restantes[joueur_actuel][nom_piece_choisie] = transformer_piece(
                    pieces_restantes[joueur_actuel][nom_piece_choisie],
                    int(rotation)
                )
                print("\nLa piece après rotation :")
                afficher_piece(pieces_restantes[joueur_actuel][nom_piece_choisie])
                break
            else:
                print("Rotation invalide. Veuillez entrer 0, 90, 180 ou 270.")

        # Retournement horizontal
        retour_h = input("Retourner horizontalement ? (o/n) : ").lower()
        if retour_h == 'o':
            pieces_restantes[joueur_actuel][nom_piece_choisie] = transformer_piece(
                pieces_restantes[joueur_actuel][nom_piece_choisie],
                miroir_h=True
            )
            print("\nLa piece après retournement horizontal :")
            afficher_piece(pieces_restantes[joueur_actuel][nom_piece_choisie])

        # Retournement vertical
        retour_v = input("Retourner verticalement ? (o/n) : ").lower()
        if retour_v == 'o':
            pieces_restantes[joueur_actuel][nom_piece_choisie] = transformer_piece(
                pieces_restantes[joueur_actuel][nom_piece_choisie],
                miroir_v=True
            )
            print("\nLa piece après retournement vertical :")
            afficher_piece(pieces_restantes[joueur_actuel][nom_piece_choisie])

        # Placement de la piece
        while True:
            try:
                x = int(input("Entrez la position X : "))
                y = int(input("Entrez la position Y : "))
                position = (x, y)
                if jouer_tour(plateau, joueur_actuel, nom_piece_choisie, position, joueur_actuel, premiere_piece_place, pieces_restantes):
                    print("piece placee avec succès ! Voici le plateau mis à jour :")
                    afficher_plateau(plateau)
                    break
                else:
                   print("Position invalide")
            except ValueError:
                print("Position invalide. Veuillez entrer des coordonnées valides (X et Y).")

        # Changer de joueur
        joueur_actuel = joueurs[(joueurs.index(joueur_actuel) + 1) % len(joueurs)]

    print("Fin de la partie.")

if __name__ == "__main__":
    main()

