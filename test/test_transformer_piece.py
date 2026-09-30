def creer_plateau(taille=20):
    # Crée une grille de taille x taille remplie de 0.
    return [[0 for _ in range(taille)] for _ in range(taille)]

def afficher_plateau(plateau):
    # Affiche l'état actuel du plateau de jeu dans la console.
    print("\nÉtat du plateau :")
    for ligne in plateau:
        print(" ".join(str(case) if case != 0 else "-" for case in ligne))
    print()

def afficher_piece(piece):
    # Affiche une pièce donnée dans la console.
    for ligne in piece:
        print(" ".join(str(case) if case != 0 else "." for case in ligne))
    print()

def transformer_piece(piece, rotation=0, miroir_h=False, miroir_v=False):
    # Transforme une pièce par rotation ou effet miroir.
    for _ in range(rotation // 90):
        piece = [list(reversed(col)) for col in zip(*piece)]

    if miroir_h:
        piece = [list(reversed(ligne)) for ligne in piece]

    if miroir_v:
        piece = list(reversed(piece))

    return piece

def test_transformer_piece():
    """
    Teste la fonction transformer_piece pour vérifier les rotations et miroirs.
    """
    piece = [[1, 0], [1, 0], [1, 1]]

    # Dictionnaire des transformations attendues
    transformations_attendues = {
        "rotation_90": ([[1, 1], [1, 0], [1, 0]], transformer_piece(piece, rotation=90)),
        "rotation_180": ([[1, 1], [0, 1], [0, 1]], transformer_piece(piece, rotation=180)),
        "rotation_270": ([[0, 1], [0, 1], [1, 1]], transformer_piece(piece, rotation=270)),
        "miroir_horizontal": ([[0, 1], [0, 1], [1, 1]], transformer_piece(piece, miroir_h=True)),
        "miroir_vertical": ([[1, 1], [1, 0], [1, 0]], transformer_piece(piece, miroir_v=True)),
    }

    for test, (expected, result) in transformations_attendues.items():
        assert result == expected, (
            f"Erreur : {test} incorrect\n"
            f"Attendu : {expected}\n"
            f"Obtenu  : {result}"
        )

    print("Tous les tests ont réussi avec succès !")

if __name__ == "__main__":
    test_transformer_piece()

