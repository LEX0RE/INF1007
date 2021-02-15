# Définissez et implémentez ici la liste des fonctions de tests responsables des tests de chacune des fonctions de
# logique.py

import logique
import constantes as c


def tester_demarrer_jeu_matrice_5x5():
    sauvegarde = c.TAILLE_GRILLE
    c.TAILLE_GRILLE = 5
    nombre_zero_attendue = (c.TAILLE_GRILLE ** 2) - c.NOMBRE_CASE_INITIAL
    nombre_zero = 0

    matrice = logique.demarrer_jeu()
    for ligne in matrice:
        nombre_zero += ligne.count(0)

    c.TAILLE_GRILLE = sauvegarde
    return nombre_zero == nombre_zero_attendue


def tester_demarrer_jeu_matrice_0x0():
    sauvegarde = c.TAILLE_GRILLE
    c.TAILLE_GRILLE = 0

    matrice_attendue = []
    matrice = logique.demarrer_jeu()

    c.TAILLE_GRILLE = sauvegarde

    return matrice == matrice_attendue


def tester_initialiser_nouvelle_matrice_5x5():
    matrice_attendue = [[0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0]]

    sauvegarde = c.TAILLE_GRILLE
    c.TAILLE_GRILLE = 5
    matrice = logique.initialiser_nouvelle_matrice()
    c.TAILLE_GRILLE = sauvegarde

    return matrice == matrice_attendue


def tester_initialiser_nouvelle_matrice_0x0():
    matrice_attendue = []

    sauvegarde = c.TAILLE_GRILLE
    c.TAILLE_GRILLE = 0
    matrice = logique.initialiser_nouvelle_matrice()
    c.TAILLE_GRILLE = sauvegarde

    return matrice == matrice_attendue


def tester_ajouter_nouveau_2_ou_4_matrice_pleine():
    matrice = [[2, 2, 2, 2],
               [2, 2, 2, 2],
               [2, 2, 2, 2],
               [2, 2, 2, 2]]
    matrice_attendue = [[2, 2, 2, 2],
                        [2, 2, 2, 2],
                        [2, 2, 2, 2],
                        [2, 2, 2, 2]]

    return logique.ajouter_nouveau_2_ou_4(matrice) == matrice_attendue


def tester_ajouter_nouveau_2_ou_4_possible():
    matrice = [[2, 2, 2, 2],
               [2, 2, 2, 2],
               [2, 2, 2, 2],
               [2, 2, 2, 0]]
    matrice_attendue_2 = [[2, 2, 2, 2],
                          [2, 2, 2, 2],
                          [2, 2, 2, 2],
                          [2, 2, 2, 2]]
    matrice_attendue_4 = [[2, 2, 2, 2],
                          [2, 2, 2, 2],
                          [2, 2, 2, 2],
                          [2, 2, 2, 4]]

    resultat_1 = logique.ajouter_nouveau_2_ou_4(matrice) == matrice_attendue_2
    resultat_2 = logique.ajouter_nouveau_2_ou_4(matrice) == matrice_attendue_4

    return resultat_1 or resultat_2


def tester_fusion_possible_matrice_vide():
    matrice = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
    resultat_attendu = False

    return logique.fusion_possible(matrice) == resultat_attendu


def tester_fusion_possible_case_separee():
    matrice = [[2, 0, 0, 2],
               [4, 0, 0, 4],
               [2, 0, 0, 2],
               [4, 4, 4, 4]]
    resultat_attendu = True

    return logique.fusion_possible(matrice) == resultat_attendu


def tester_get_etat_jeu_courant_deux_conditions():
    matrice = [[4, 2, 4,             2],
               [2, 4, 2,             4],
               [4, 2, 4,             2],
               [2, 4, 2, c.CASE_FINALE]]
    resultat_attendu = c.ETAT_VICTOIRE

    return logique.get_etat_jeu_courant(matrice) == resultat_attendu


def tester_get_etat_jeu_courant_matrice_vide():
    matrice = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
    resultat_attendu = c.ETAT_PARTIE_EN_COURS

    return logique.get_etat_jeu_courant(matrice) == resultat_attendu


def tester_comprimer_matrice_vide():
    matrice = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
    resultat_attendu = ([[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]], False)

    return logique.comprimer(matrice) == resultat_attendu


def tester_comprimer_matrice_pleine():
    matrice = [[2, 2, 2, 2],
               [2, 2, 2, 2],
               [2, 2, 2, 2],
               [2, 2, 2, 2]]
    resultat_attendu = ([[2, 2, 2, 2],
                         [2, 2, 2, 2],
                         [2, 2, 2, 2],
                         [2, 2, 2, 2]], False)

    return logique.comprimer(matrice) == resultat_attendu


def tester_fusionner_cases_identiques():
    matrice = [[4, 4, 4, 4],
               [4, 4, 4, 4],
               [4, 4, 4, 4],
               [4, 4, 4, 4]]
    resultat_attendu = ([[8, 0, 8, 0],
                        [8, 0, 8, 0],
                        [8, 0, 8, 0],
                        [8, 0, 8, 0]], True)

    return logique.fusionner(matrice) == resultat_attendu


def tester_fusionner_distantes():
    matrice = [[4, 0, 0, 4],
               [4, 0, 0, 4],
               [4, 0, 0, 4],
               [4, 0, 0, 4]]
    resultat_attendu = ([[4, 0, 0, 4],
                         [4, 0, 0, 4],
                         [4, 0, 0, 4],
                         [4, 0, 0, 4]], False)

    return logique.fusionner(matrice) == resultat_attendu


def tester_inverser_matrice_pleine():
    matrice = [[1,   2,  3,  4],
               [5,   6,  7,  8],
               [9,  10, 11, 12],
               [13, 14, 15, 16]]
    matrice_attendu = [[4,   3,  2,  1],
                       [8,   7,  6,  5],
                       [12, 11, 10,  9],
                       [16, 15, 14, 13]]

    return logique.inverser(matrice) == matrice_attendu


def tester_inverser_matrice_identite():
    matrice = [[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]]
    matrice_attendu = [[0, 0, 0, 1],
                       [0, 0, 1, 0],
                       [0, 1, 0, 0],
                       [1, 0, 0, 0]]

    return logique.inverser(matrice) == matrice_attendu


def tester_transposer_matrice_identite():
    matrice = [[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]]
    resultat_attendu = [[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]]

    return logique.transposer(matrice) == resultat_attendu


def tester_transposer_matrice_pleine():
    matrice = [[1, 2, 3, 4],
               [1, 2, 3, 4],
               [1, 2, 3, 4],
               [1, 2, 3, 4]]
    resultat_attendu = [[1, 1, 1, 1],
                        [2, 2, 2, 2],
                        [3, 3, 3, 3],
                        [4, 4, 4, 4]]

    return logique.transposer(matrice) == resultat_attendu


def tester_faire_translation_gauche_impossible():
    matrice = [[1, 2, 3, 4],
               [1, 0, 0, 0],
               [1, 0, 0, 0],
               [1, 2, 3, 4]]
    resultat_attendu = ([[1, 2, 3, 4],
                         [1, 0, 0, 0],
                         [1, 0, 0, 0],
                         [1, 2, 3, 4]], False)

    return logique.faire_translation_gauche(matrice) == resultat_attendu


def tester_faire_translation_gauche_maximum():
    matrice = [[0, 0, 1, 2],
               [0, 0, 1, 2],
               [0, 0, 1, 2],
               [0, 0, 1, 2]]
    resultat_attendu = ([[1, 2, 0, 0],
                         [1, 2, 0, 0],
                         [1, 2, 0, 0],
                         [1, 2, 0, 0]], True)

    return logique.faire_translation_gauche(matrice) == resultat_attendu


def tester_faire_translation_droite_impossible():
    matrice = [[4, 3, 2, 1],
               [0, 0, 0, 1],
               [0, 0, 0, 1],
               [4, 3, 2, 1]]
    resultat_attendu = ([[4, 3, 2, 1],
                         [0, 0, 0, 1],
                         [0, 0, 0, 1],
                         [4, 3, 2, 1]], False)

    return logique.faire_translation_droite(matrice) == resultat_attendu


def tester_faire_translation_droite_maximum():
    matrice = [[1, 2, 0, 0],
               [1, 2, 0, 0],
               [1, 2, 0, 0],
               [1, 2, 0, 0]]
    resultat_attendu = ([[0, 0, 1, 2],
                         [0, 0, 1, 2],
                         [0, 0, 1, 2],
                         [0, 0, 1, 2]], True)

    return logique.faire_translation_droite(matrice) == resultat_attendu


def tester_faire_translation_haut_impossible():
    matrice = [[1, 1, 1, 1],
               [2, 0, 0, 2],
               [3, 0, 0, 3],
               [4, 0, 0, 4]]
    resultat_attendu = ([[1, 1, 1, 1],
                         [2, 0, 0, 2],
                         [3, 0, 0, 3],
                         [4, 0, 0, 4]], False)

    return logique.faire_translation_haut(matrice) == resultat_attendu


def tester_faire_translation_haut_maximum():
    matrice = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [1, 1, 1, 1],
               [2, 2, 2, 2]]
    resultat_attendu = ([[1, 1, 1, 1],
                         [2, 2, 2, 2],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]], True)

    return logique.faire_translation_haut(matrice) == resultat_attendu


def tester_faire_translation_bas_impossible():
    matrice = [[4, 0, 0, 4],
               [3, 0, 0, 3],
               [2, 0, 0, 2],
               [1, 1, 1, 1]]
    resultat_attendu = ([[4, 0, 0, 4],
                         [3, 0, 0, 3],
                         [2, 0, 0, 2],
                         [1, 1, 1, 1]], False)

    return logique.faire_translation_bas(matrice) == resultat_attendu


def tester_faire_translation_bas_maximum():
    matrice = [[1, 1, 1, 1],
               [2, 2, 2, 2],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
    resultat_attendu = ([[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [1, 1, 1, 1],
                         [2, 2, 2, 2]], True)

    return logique.faire_translation_bas(matrice) == resultat_attendu


def ecrire_resultat_test(test, resultat):
    reussite_ou_echec = ("Échec", "Réussite")[resultat]
    print(test + "..." + reussite_ou_echec)


if __name__ == '__main__':
    print("\n" + logique.demarrer_jeu.__name__ + ":")
    ecrire_resultat_test(tester_demarrer_jeu_matrice_5x5.__name__,
                         tester_demarrer_jeu_matrice_5x5())

    ecrire_resultat_test(tester_demarrer_jeu_matrice_0x0.__name__,
                         tester_demarrer_jeu_matrice_0x0())

    print("\n" + logique.initialiser_nouvelle_matrice.__name__ + ":")
    ecrire_resultat_test(tester_initialiser_nouvelle_matrice_5x5.__name__,
                         tester_initialiser_nouvelle_matrice_5x5())

    ecrire_resultat_test(tester_initialiser_nouvelle_matrice_0x0.__name__,
                         tester_initialiser_nouvelle_matrice_0x0())

    print("\n" + logique.ajouter_nouveau_2_ou_4.__name__ + ":")
    ecrire_resultat_test(tester_ajouter_nouveau_2_ou_4_matrice_pleine.__name__,
                         tester_ajouter_nouveau_2_ou_4_matrice_pleine())

    ecrire_resultat_test(tester_ajouter_nouveau_2_ou_4_possible.__name__,
                         tester_ajouter_nouveau_2_ou_4_possible())

    print("\n" + logique.fusion_possible.__name__ + ":")
    ecrire_resultat_test(tester_fusion_possible_matrice_vide.__name__,
                         tester_fusion_possible_matrice_vide())

    ecrire_resultat_test(tester_fusion_possible_case_separee.__name__,
                         tester_fusion_possible_case_separee())

    print("\n" + logique.get_etat_jeu_courant.__name__ + ":")
    ecrire_resultat_test(tester_get_etat_jeu_courant_deux_conditions.__name__,
                         tester_get_etat_jeu_courant_deux_conditions())

    ecrire_resultat_test(tester_get_etat_jeu_courant_matrice_vide.__name__,
                         tester_get_etat_jeu_courant_matrice_vide())

    print("\n" + logique.comprimer.__name__ + ":")
    ecrire_resultat_test(tester_comprimer_matrice_vide.__name__,
                         tester_comprimer_matrice_vide())

    ecrire_resultat_test(tester_comprimer_matrice_pleine.__name__,
                         tester_comprimer_matrice_pleine())

    print("\n" + logique.fusionner.__name__ + ":")
    ecrire_resultat_test(tester_fusionner_cases_identiques.__name__,
                         tester_fusionner_cases_identiques())

    ecrire_resultat_test(tester_fusionner_distantes.__name__,
                         tester_fusionner_distantes())

    print("\n" + logique.inverser.__name__ + ":")
    ecrire_resultat_test(tester_inverser_matrice_pleine.__name__,
                         tester_inverser_matrice_pleine())

    ecrire_resultat_test(tester_inverser_matrice_identite.__name__,
                         tester_inverser_matrice_identite())

    print("\n" + logique.transposer.__name__ + ":")
    ecrire_resultat_test(tester_transposer_matrice_identite.__name__,
                         tester_transposer_matrice_identite())

    ecrire_resultat_test(tester_transposer_matrice_pleine.__name__,
                         tester_transposer_matrice_pleine())

    print("\n" + logique.faire_translation_gauche.__name__ + ":")
    ecrire_resultat_test(tester_faire_translation_gauche_impossible.__name__,
                         tester_faire_translation_gauche_impossible())

    ecrire_resultat_test(tester_faire_translation_gauche_maximum.__name__,
                         tester_faire_translation_gauche_maximum())

    print("\n" + logique.faire_translation_droite.__name__ + ":")
    ecrire_resultat_test(tester_faire_translation_droite_impossible.__name__,
                         tester_faire_translation_droite_impossible())

    ecrire_resultat_test(tester_faire_translation_droite_maximum.__name__,
                         tester_faire_translation_droite_maximum())

    print("\n" + logique.faire_translation_haut.__name__ + ":")
    ecrire_resultat_test(tester_faire_translation_haut_impossible.__name__,
                         tester_faire_translation_haut_impossible())

    ecrire_resultat_test(tester_faire_translation_haut_maximum.__name__,
                         tester_faire_translation_haut_maximum())

    print("\n" + logique.faire_translation_bas.__name__ + ":")
    ecrire_resultat_test(tester_faire_translation_bas_impossible.__name__,
                         tester_faire_translation_bas_impossible())

    ecrire_resultat_test(tester_faire_translation_bas_maximum.__name__,
                         tester_faire_translation_bas_maximum())
