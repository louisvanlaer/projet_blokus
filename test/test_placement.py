from .test_plateau import creer_plateau

def placement_piece(plateau, piece, position, joueur=1):
    """
    Tente de placer une pièce sur le plateau.
    Retourne True si le placement est valide, sinon False.

    """
    x, y = position
    lignes_plateau = len(plateau)
    colonnes_plateau = len(plateau[0])

    # Vérification des collisions et des limites
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j] == 1:  # Partie active de la pièce
                # Vérifier les limites du plateau
                if x + i >= lignes_plateau or y + j >= colonnes_plateau:
                    return False  # Dépassement des limites
                # Vérifier si la case est déjà occupée
                if plateau[x + i][y + j] != 0:
                    return False  # Collision détectée

    # Placement de la pièce si tout est valide
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j] == 1:
                plateau[x + i][y + j] = 1  # Placement réussi

    return True


def test_placement_valide():
    print("=== Test Placement Valide ===")
    plateau = creer_plateau(5)  # Crée un plateau 5x5
    piece = [
        [1, 1],
        [0, 1]
    ]
    position = (2, 2)

    result = placement_piece(plateau, piece, position)
    print("Placement valide :", result)
    for ligne in plateau:
        print(ligne)
    assert result == True, "Le placement valide a échoué."


def test_collision():
    print("\n=== Test Collision ===")
    plateau = creer_plateau(5)  # Crée un plateau 5x5
    piece1 = [
        [1, 1],
        [0, 1]
    ]
    piece2 = [
        [1, 1],
        [1, 0]
    ]
    # Place la première pièce
    placement_piece(plateau, piece1, (2, 2))

    # Tente de placer la deuxième pièce à la même position
    result = placement_piece(plateau, piece2, (2, 2))
    print("Collision détectée :", not result)
    for ligne in plateau:
        print(ligne)
    assert result == False, "La collision n'a pas été détectée."


def test_depassement_limites():
    print("\n=== Test Dépassement des Limites ===")
    plateau = creer_plateau(5)  # Crée un plateau 5x5
    piece = [
        [1, 1],
        [0, 1]
    ]
    position = (4, 4)  # Position qui dépasse les limites du plateau

    result = placement_piece(plateau, piece, position)
    print("Dépassement des limites détecté :", not result)
    for ligne in plateau:
        print(ligne)
    assert result == False, "Le dépassement des limites n'a pas été détecté."


if __name__ == "__main__":
    # Exécution de tous les tests
    test_placement_valide()
    test_collision()
    test_depassement_limites()
    print("\nTous les tests ont été exécutés avec succès.")



