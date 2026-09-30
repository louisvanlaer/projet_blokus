
# Cahier de Tests de Validation - Jeu Blokus

## Cahier de Tests de Validation

### Définition
Un test de validation est un type de test réalisé du point de vue de l’utilisateur. Il se concentre sur la **fonctionnalité globale** de l’application, telle qu’elle est perçue par l’utilisateur final.

#### Objectifs principaux :
1. **Tester une fonction utilisateur complète** : Chaque test de validation est associé à une fonction utilisateur décrite dans les spécifications fonctionnelles. Par exemple, "Afficher l’état courant du plateau" ou "Détecter la fin de partie".
2. **Simuler les interactions utilisateur** : Les tests reproduisent les actions de l’utilisateur pour vérifier si l’application répond correctement dans des scénarios réels.
3. **Évaluer la qualité perçue** : Ces tests permettent d’estimer si l’expérience utilisateur est fluide et conforme aux attentes.

---

### Motivation
Les tests de validation permettent de garantir que :
1. Les fonctionnalités décrites dans les spécifications fonctionnelles sont correctement implémentées.
2. L’application respecte les règles et offre une expérience utilisateur fluide.
3. Les bugs ou comportements inattendus sont identifiés et corrigés avant la mise en production.

---

## Exemples

## Test 1.1 : Affichage initial

**But** : Vérifier que le plateau est vide et correctement affiché au lancement du jeu.  

**Entrée utilisateur** : Commande pour démarrer une nouvelle partie.  

**Sortie attendue** :  
- Plateau vide avec les coins réservés pour chaque joueur.  
- Les cellules vides sont représentées par un caractère ou une couleur spécifique.  

**Critères de réussite** :  
- Plateau bien formaté.  
- Les coins réservés sont visibles.  

---

## Test 2.1 : Placement valide  

**But** : Vérifier que le joueur peut placer une pièce en respectant les règles du jeu.  

**Entrée utilisateur** : Coordonnées (A1), identifiant de la pièce (L), et orientation.  

**Sortie attendue** :  
- La pièce est placée sur le plateau.  
- Le tour passe au joueur suivant.  

**Critères de réussite** :  
- Placement de la pièce valide.  
- Tour du joueur suivant indiqué.  

---


## Test 2.2 : Détection des collisions  

**But** : Vérifier qu’une collision est correctement détectée lorsqu’une pièce est placée sur une case occupée.  

**Entrée utilisateur** : Deux pièces sont placées aux mêmes coordonnées.  

**Sortie attendue** :  
- Message d'erreur : "Coup invalide : collision détectée."  
- La première pièce reste en place.  

**Critères de réussite** :  
- Collision détectée.  
- Plateau reste inchangé après l'erreur.  

---

## Test 2.3 : Dépassement des limites  

**But** : Empêcher le joueur de placer une pièce en dehors des limites du plateau.  

**Entrée utilisateur** : Coordonnées qui dépassent les bords du plateau.  

**Sortie attendue** :  
- Message d’erreur : "Coup invalide : dépassement des limites."  
- Plateau inchangé.  

**Critères de réussite** :  
- Message d’erreur affiché.  
- Le plateau reste inchangé.  

---

## Test 2.4 : Gestion des pièces invalides  

**But** : Vérifier que seules les pièces valides sont acceptées (1 à 5 cases).  

**Entrée utilisateur** : Taille de pièce invalide (par exemple 6 cases ou plus).  

**Sortie attendue** :  
- Message d’erreur : "Taille de pièce invalide. Veuillez entrer une taille entre 1 et 5."  

**Critères de réussite** :  
- Message d’erreur affiché.  
- Aucune pièce n’est placée sur le plateau.  


### A0
```
| Test                     | Description                          | Version | Résultat |
|--------------------------|--------------------------------------|---------|----------|
| test_afficher_plateau    | Affiche un plateau vide correctement | A0      | OK       |
| test_placement_valide    | Place une pièce correctement         | A0      | OK       |
| test_collision           | Détecte une collision de pièces      | A0      | OK       |
| test_depassement_limites | Détecte un dépassement de plateau    | A0      | OK       |
| test_placement_erreur    | Gestion des pièces invalides         | A0      | OK       |

```

### **Fonction de base : Détecter la fin de partie**
5. **Test 3.1 : Fin de partie pour un joueur**
   - **But :** Vérifier que le jeu détecte qu’un joueur ne peut plus jouer.
   - **Entrée utilisateur :** Le joueur 2 n’a plus de mouvements possibles.
   - **Sortie attendue :** 
     - Message : "Joueur 2 ne peut plus jouer."
     - Les autres joueurs continuent.

6. **Test 3.2 : Fin de partie complète**
   - **But :** Vérifier que le jeu se termine lorsque plus aucun joueur ne peut jouer.
   - **Entrée utilisateur :** Aucun mouvement possible pour tous les joueurs.
   - **Sortie attendue :** 
     - Message : "Fin du jeu. Gagnant : Joueur X."
     - Affichage du classement final.

### **Fonction additionnelle : Sauvegarder une partie**
7. **Test 4.1 : Sauvegarde réussie**
   - **But :** Vérifier que l’état courant du jeu peut être sauvegardé.
   - **Entrée utilisateur :** Nom du fichier pour la sauvegarde.
   - **Sortie attendue :** 
     - Fichier de sauvegarde créé.
     - Confirmation : "Sauvegarde réussie."

8. **Test 4.2 : Échec de sauvegarde - espace disque insuffisant**
   - **But :** Vérifier la gestion d’un échec de sauvegarde.
   - **Entrée utilisateur :** Nom du fichier pour la sauvegarde.
   - **Sortie attendue :** 
     - Message d’erreur : "Erreur : espace disque insuffisant."
     - État du jeu inchangé.

### **Fonction additionnelle : Charger une partie**
9. **Test 5.1 : Chargement réussi**
   - **But :** Vérifier que l’état d’une partie précédemment sauvegardée peut être restauré.
   - **Entrée utilisateur :** Nom du fichier de sauvegarde valide.
   - **Sortie attendue :** 
     - État du jeu restauré.
     - Message : "Partie chargée avec succès."

10. **Test 5.2 : Échec de chargement - fichier introuvable**
    - **But :** Vérifier la gestion d’un fichier inexistant.
    - **Entrée utilisateur :** Nom d’un fichier qui n’existe pas.
    - **Sortie attendue :** 
      - Message d’erreur : "Erreur : fichier introuvable."
      - État du jeu inchangé.

### **Fonction additionnelle : Historique des coups**
11. **Test 6.1 : Historique complet**
    - **But :** Vérifier que tous les coups joués sont listés dans l’ordre chronologique.
    - **Entrée utilisateur :** Commande pour afficher l’historique.
    - **Sortie attendue :** 
      - Liste des coups depuis le début de la partie.
      - Affichage dans l’ordre chronologique.

---

## Forme
Le cahier de tests de validation doit suivre la structure suivante pour chaque test :
1. **Numéro de test :** Identifiant unique (par ex. : `2.1` pour la fonction Jouer un coup).
2. **But :** Objectif du test.
3. **Entrée utilisateur :** Données ou actions nécessaires pour exécuter le test.
4. **Sortie attendue :** Résultat attendu si le test est réussi.
5. **Critères de réussite :** Conditions nécessaires pour valider le test.
