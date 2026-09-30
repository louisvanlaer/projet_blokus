# Spécifications Fonctionnelles - Jeu Blokus

## 1. Introduction

Le jeu Blokus est un jeu de plateau stratégique où 2 à 4 joueurs placent des pièces de formes différentes sur un plateau. L'objectif est de placer un maximum de pièces en respectant des règles spécifiques. Ce document décrit les spécifications fonctionnelles de l'application pour jouer au Blokus. Les spécifications se concentrent sur les interactions utilisateur et les fonctions abstraites sans entrer dans les détails techniques de l'implémentation.

---

## 2. Fonctions de base

### 2.1 Afficher l’état courant du plateau
#### Description
Cette fonction permet à l’utilisateur de visualiser le plateau de jeu à tout moment.

#### Entrées
- Aucun paramètre direct. La fonction est appelée automatiquement après chaque coup joué ou sur demande du joueur.

#### Sorties
- Représentation graphique ou textuelle du plateau :
  - Les cellules vides sont représentées par un caractère ou une couleur spécifique.
  - Les pièces des différents joueurs sont identifiées par des couleurs ou des symboles distincts (par exemple, J1 pour Joueur 1, J2 pour Joueur 2, etc.).

#### Dynamique
- **Initiative** : L’application affiche automatiquement le plateau après chaque action.
- **Cas d’erreur** : Aucun cas d’erreur prévu pour cette fonction.

---

### 2.2 Jouer et contrôler un coup
#### Description
Permet à un joueur de placer une pièce sur le plateau en respectant les règles du jeu.

#### Entrées
- Coordonnées de la cellule où placer la pièce (exemple : `A1`).
- Identifiant de la pièce à placer.
- Orientation de la pièce (par exemple, rotation ou symétrie).

#### Sorties
- Si le placement est valide : mise à jour du plateau.
- Si le placement est invalide : message d’erreur décrivant la raison (par exemple : "Placement interdit, la pièce n'est pas adjacente à une pièce existante").

#### Dynamique
- **Initiative** : Le joueur active cette fonction en indiquant son choix.
- **Cas d’erreur** :
  - La cellule est occupée.
  - La pièce ne respecte pas les règles de placement (par exemple : non-adjacence à une pièce du joueur).
  - Le joueur tente de jouer une pièce déjà placée.

---

### 2.3 Détecter la fin de partie
#### Description
Détermine si la partie est terminée pour un ou plusieurs joueurs.

#### Entrées
- Aucun paramètre direct. Cette fonction est appelée automatiquement après chaque coup.

#### Sorties
- Indication que la partie est terminée pour un joueur ou tous les joueurs.
- Classement des joueurs à la fin de la partie.

#### Dynamique
- **Initiative** : L’application détecte automatiquement la fin de partie.
- **Cas d’erreur** : Aucun cas d’erreur prévu pour cette fonction.

---

## 3. Fonction additionnelle n° 1 : Sauvegarder et charger une partie

### 3.1 Sauvegarder une partie
#### Description
Permet de sauvegarder l’état courant du jeu pour pouvoir reprendre plus tard.

#### Entrées
- Nom du fichier pour la sauvegarde.

#### Sorties
- Fichier contenant les données du plateau, les pièces restantes, et le joueur actif.

#### Dynamique
- **Initiative** : Le joueur demande explicitement la sauvegarde.
- **Cas d’erreur** :
  - Échec de l’écriture dans le fichier (par exemple : espace disque insuffisant).

---

### 3.2 Charger une partie
#### Description
Permet de charger une partie précédemment sauvegardée.

#### Entrées
- Nom du fichier de sauvegarde.

#### Sorties
- État du jeu restauré.

#### Dynamique
- **Initiative** : Le joueur choisit de charger une partie.
- **Cas d’erreur** :
  - Fichier introuvable.
  - Fichier corrompu ou incompatible.

---

## 4. Fonction additionnelle n° 2 : Historique des coups

### 4.1 Afficher l’historique des coups
#### Description
Permet aux joueurs de consulter les actions réalisées depuis le début de la partie.

#### Entrées
- Aucun paramètre direct.

#### Sorties
- Liste des coups joués dans l’ordre chronologique.

#### Dynamique
- **Initiative** : Le joueur active cette fonction via un menu.
- **Cas d’erreur** : Aucun cas d’erreur prévu.

---


