def est_adjacent(plateau, x, y):
    """
    Verifie si la case (x, y) est adjacente (haut, bas, gauche, droite) à une autre case contenant une piece.
    Retourne True si une connexion adjacente existe, sinon False.
    """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Haut, bas, gauche, droite uniquement
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(plateau) and 0 <= ny < len(plateau[0]):
            if plateau[nx][ny] == 1:
                return True  # Une case adjacente est trouvée
    return False
def test_est_adjacent():
    """
    Test pour verifier si les cases sont adjacentes ou non.
    """

    # Plateau où une pièce est placée sur (0,1), et on teste (0,0) (adjacent)
    plateau_adjacence = [
        [0, 1],  # (0,1) contient une pièce
        [0, 0]   # (0,0) est adjacent à (0,1), donc doit renvoyer True
    ]

    # Plateau où une pièce est placée en diagonale sur (0,1), et on teste (1,0) (diagonal)
    plateau_diagonale = [
        [0, 0],  
        [1, 0]   # (1,0) est en diagonale de (0,1), donc doit renvoyer False
    ]

    # Test adjacence (cas où les côtés se touchent, doit renvoyer True)
    assert est_adjacent(plateau_adjacence, 0, 0) == True, "Erreur : La fonction devrait renvoyer True pour une case adjacente"

    # Test non-adjacence (cas où les cases sont en diagonale, doit renvoyer False)
    assert est_adjacent(plateau_diagonale, 0, 1) == False, "Erreur : La fonction devrait renvoyer False, la piece est en diagonale"

    print("Test simplifie des cotes reussi : les cotes adjacents renvoient True, et les diagonales renvoient False.")
    


