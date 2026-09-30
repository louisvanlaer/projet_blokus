def creer_plateau(taille=20):
    """
    Crée un plateau vide de taille donnée.
    Par défaut, il crée un plateau 20x20.
    """
    return [[0 for _ in range(taille)] for _ in range(taille)]

def afficher_plateau(plateau):
    """
    Affiche le plateau en console.
    Les cases vides sont représentées par des points ('.').
    """
    for ligne in plateau:
        print(" ".join("." if case == 0 else str(case) for case in ligne))


# Tests unitaires
def test_creer_plateau():
    """
    Teste la fonction creer_plateau pour s'assurer qu'elle génère
    un plateau vide avec les dimensions correctes.
    """
    taille = 20
    plateau = creer_plateau(taille)

    # Vérifie la taille du plateau
    assert len(plateau) == taille, "Erreur : nombre de lignes incorrect"
    assert all(len(ligne) == taille for ligne in plateau), "Erreur : nombre de colonnes incorrect"
    assert all(cell == 0 for ligne in plateau for cell in ligne), "Erreur : les cases ne sont pas initialisées à 0"
    assert plateau is not None


def test_afficher_plateau():
    """
    Teste la fonction afficher_plateau.
    Vérifie que la fonction ne lève pas d'exception.
    """
    plateau = creer_plateau(5)  # Petit plateau pour simplifier l'affichage
    afficher_plateau(plateau)

