def est_connexion_diagonale(plateau, x, y):
    """
    Vérifie si la case (x, y) est connectée en diagonale à une autre case contenant une pièce (valeur != 0).
    Retourne True si une connexion diagonale existe, sinon False.
    """
    diagonales = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dx, dy in diagonales:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(plateau) and 0 <= ny < len(plateau[0]):
            if plateau[nx][ny] == 1:  # Vérifie uniquement la présence d'une pièce
                return True
    return False

def test_est_connexion_diagonale():
    """
    Test pour vérifier la connexion diagonale d'une pièce.
    """
    plateau = [
        [0, 1],  # (0,1) contient une pièce
        [0, 0]   # (1,0) devrait détecter une connexion diagonale avec (0,1)
    ]

    # Vérifie qu'une pièce placée en diagonale est détectée correctement
    assert est_connexion_diagonale(plateau, 1, 0) == True, "Erreur : Connexion diagonale non détectée"

    # Vérifie qu'une pièce placée ailleurs ne crée pas de connexion diagonale
    assert est_connexion_diagonale(plateau, 0, 0) == False, "Erreur : Connexion diagonale incorrectement détectée"

    print("Test simplifié de connexion diagonale réussi !")
