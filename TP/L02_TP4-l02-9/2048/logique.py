# logique.py est importé par gui.py
# Ce fichier consiste en la logique du jeu 2048

import random
import constantes as c


# TODO:
#  Initialisation du jeu
#  1. Dans une nouvelle matrice, ajouter deux fois (un 2 ou un 4)
def demarrer_jeu():
    matrice = initialiser_nouvelle_matrice()

    if len(matrice):
        for ajout in range(c.NOMBRE_CASE_INITIAL):
            matrice = ajouter_nouveau_2_ou_4(matrice)

    return matrice


# TODO:
#  Retourner une nouvelle matrice 4x4 remplie de 0
def initialiser_nouvelle_matrice():
    grille = []

    for ligne in range(c.TAILLE_GRILLE):
        grille.append([0 for colonne in range(c.TAILLE_GRILLE)])

    return grille


# TODO:
#  Ajout d'un 2 ou d'un 4 a la matrice du jeu avec des probabilités de: 90% 2 et 10% 4
#  dans un emplacement vide aléatoire de la matrice (emplacement == 0)
#  Modifie le paramètre grille et retourne la grille modifiée.
def ajouter_nouveau_2_ou_4(grille):

    # On test si on peut ajouter une case
    continuer = False
    for ligne in grille:
        if 0 in ligne:
            continuer = True
            break

    if not continuer:
        return grille

    ajout = c.CASE_INITIAL_UN

    # On suppose à la base que notre case sera deux et on détermine si
    # elle sera 4 selon les chances données
    if random.randint(1, c.CHANCE_TOTAL) <= c.CHANCE_CASE_QUATRE:
        ajout = c.CASE_INITIAL_DEUX

    max_random = c.TAILLE_GRILLE - 1

    position = (random.randint(0, max_random), random.randint(0, max_random))
    while grille[position[0]][position[1]] != 0:
        position = (random.randint(0, max_random),
                    random.randint(0, max_random))

    grille[position[0]][position[1]] = ajout

    return grille


# Regarde s'il y a un mouvement possible dans la grille donnée
def fusion_possible(grille) -> bool:
    for ligne in range(len(grille)):
        for colonne in range(len(grille)):
            if grille[ligne][colonne]:
                if colonne != c.TAILLE_GRILLE - 1:
                    if grille[ligne][colonne] == grille[ligne][colonne + 1]:
                        return True

                if ligne != c.TAILLE_GRILLE - 1:
                    if grille[ligne][colonne] == grille[ligne + 1][colonne]:
                        return True

    return False


# TODO:
#  Retourner l'état du jeu
#  Les valeurs retournées sont les états définis dans constantes.py (ETAT_x)
#  ex: return c.ETAT_VICTOIRE
#  1. Victoire
#    a) Si un élément de la matrice == 2048
#  2. Le jeu n'est pas fini
#    a) S'il y a au moins un élément == 0
#    b) OU S'il n'y a aucune cellule vide, MAIS qu'il y a un (ou des) mouvements possibles
#  3. Défaite
#    a) Les cas restants
def get_etat_jeu_courant(grille):
    for ligne in grille:
        if c.CASE_FINALE in ligne:
            return c.ETAT_VICTOIRE

    for ligne in grille:
        if 0 in ligne:
            return c.ETAT_PARTIE_EN_COURS

    if fusion_possible(grille):
        return c.ETAT_PARTIE_EN_COURS

    return c.ETAT_DEFAITE


# NOTE: Les fonctions suivantes sont pour le mouvement gauche seulement

# TODO:
#  Comprimer la matrice de jeu.
#  À effectuer après toutes les étapes avant et après le fusionnement des éléments
#    a) Initialiser une nouvelle matrice remplie de 0 initialement.
#    b) Bouger tous les éléments à son extrême gauche, lorsque possible
#        b.a) SEULEMENT possible lorsque l'élément à gauche == 0
#        b.b) PAS POSSIBLE si gauche != 0
#    c) Retourner la nouvelle matrice comprimée, avec un booléen indiquant s'il y a au moins eu
#       1 changement
def comprimer(matrice) -> tuple:
    resultat = initialiser_nouvelle_matrice()
    changement = False

    for index, ligne in enumerate(matrice):
        pointeur_resultat = 0

        for case in ligne:
            if case:
                if case != ligne[pointeur_resultat]:
                    changement = True

                resultat[index][pointeur_resultat] = case
                pointeur_resultat += 1

    return resultat, changement


# TODO:
#  Fusionner les éléments de la matrice après une compression
#  1) Si l'élément a la même valeur que le prochain élément dans la ligne
#     ET qu'ils sont non vides (!= 0)
#     ALORS doubler la valeur de l'élément courant ET vider l'élément suivant
#  2) Retourner la matrice fusionnée et un booléen indiquant s'il y a eu un changement
def fusionner(matrice) -> tuple:
    resultat = matrice[:]
    changement = False

    for ligne in range(len(resultat)):
        for colonne in range(len(resultat) - 1):
            if resultat[ligne][colonne]:
                if resultat[ligne][colonne] == resultat[ligne][colonne + 1]:
                    changement = True
                    resultat[ligne][colonne + 1] = 0
                    resultat[ligne][colonne] *= 2

    return resultat, changement


# TODO:
#  Inverser la matrice
#  1) Dans une nouvelle matrice,
#     inverser la séquence dans chaque ligne de la matrice
#  2) Retourner la nouvelle matrice
def inverser(matrice):
    nouvelle_matrice = initialiser_nouvelle_matrice()

    for index, ligne in enumerate(matrice):
        nouvelle_matrice[index] = ligne[::-1]

    return nouvelle_matrice


# TODO:
#  Transposer la matrice
#  1) Dans une nouvelle matrice,
#     Échanger les lignes avec les colonnes
#  2) Retourner la nouvelle matrice
def transposer(matrice):
    matrice_transpose = initialiser_nouvelle_matrice()

    for ligne in range(len(matrice)):
        matrice_transpose[ligne] = [rangee[ligne] for rangee in matrice]

    return matrice_transpose

# NOTE: Les fonctions suivantes servent à gérer un mouvement dans la matrice.


# TODO:
#  Bouger la matrice à gauche
#  1) Dans une nouvelle matrice
#    a) Comprimer la matrice
#    b) Fusionner la matrice
#    c) Recomprimer la matrice
#  2) Retourner la nouvelle matrice, ainsi qu'un booléen indiquant s'il y a eu un changement
def faire_translation_gauche(matrice) -> tuple:
    resultat = comprimer(matrice)
    changement = resultat[1]
    resultat = fusionner(resultat[0])
    changement = changement or resultat[1]
    resultat = comprimer(resultat[0])

    return resultat[0], changement or resultat[1]


# TODO:
#  Bouger la matrice à droite
#  1) Dans une nouvelle matrice
#    a) Inverser la matrice pour simuler un mouvement à gauche
#    b) Bouger la matrice à gauche
#    c) Re-inverser la matrice
#  2) Retourner la nouvelle matrice, ainsi qu'un booléen indiquant s'il y a eu un changement
def faire_translation_droite(matrice) -> tuple:
    resultat = (inverser(matrice), False)
    resultat = faire_translation_gauche(resultat[0])
    resultat = (inverser(resultat[0]), resultat[1])

    return resultat


# TODO:
#  Bouger la matrice en haut
#  1) Dans une nouvelle matrice
#    a) Transposer la matrice pour simuler un mouvement à gauche
#    b) Bouger la matrice à gauche
#    c) Re-transposer la matrice
#  2) Retourner la nouvelle matrice, ainsi qu'un booléen indiquant s'il y a eu un changement
def faire_translation_haut(matrice) -> tuple:
    resultat = (transposer(matrice), False)
    resultat = faire_translation_gauche(resultat[0])
    resultat = (transposer(resultat[0]), resultat[1])

    return resultat


# TODO:
#  Bouger la matrice en bas
#  1) Dans une nouvelle matrice
#    a) Transposer la matrice pour simuler un mouvement à droite
#    b) Bouger la matrice à droite
#    c) Re-transposer la matrice
#  2) Retourner la nouvelle matrice, ainsi qu'un booléen indiquant s'il y a eu un changement
def faire_translation_bas(matrice) -> tuple:
    resultat = (transposer(matrice), False)
    resultat = faire_translation_droite(resultat[0])
    resultat = (transposer(resultat[0]), resultat[1])

    return resultat
