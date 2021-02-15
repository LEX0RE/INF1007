import _thread
import threading
import time

import exo1 as exo1_etudiant
import exo2 as exo2_etudiant
import exo2_corrige as exo2_corrige
import numpy as np
from random import randint
import unittest
import os
import sys
import copy


# Timeout
def exit_function():
    _thread.interrupt_main()


def timeout(s):
    def outer(fn):
        def inner(*args, **kwargs):
            timer = threading.Timer(s, exit_function)
            timer.start()
            try:
                result = fn(*args, **kwargs)
            finally:
                timer.cancel()
            return result

        return inner

    return outer


class TestTriFusion(unittest.TestCase):
    a_trier = []

    @timeout(2)
    def executer_test(self, fonction, nom_fonction):
        try:
            return fonction()
        except KeyboardInterrupt:
            self.fail(
                f'L\'appel fonction {nom_fonction} ne se termine pas --> Verifiez vos boucles')
        except AssertionError as e:
            raise e
        except:
            self.fail(
                f'Une exception a été levée lors de l\'appel fonction {nom_fonction}. Revérifier votre code.')

    def test_deja_trie(self):
        self.a_trier = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        tri_etudiant = self.executer_test(self.tri_fusion_etudiant, "tri_fusion")
        self.a_trier.sort()

        self.assertEqual(tri_etudiant, self.a_trier)

    def test_repetition(self):
        self.a_trier = [1, 1, 1, 1, 1, 1]

        tri_etudiant = self.executer_test(self.tri_fusion_etudiant, "tri_fusion")
        self.a_trier.sort()

        self.assertEqual(tri_etudiant, self.a_trier)

    def test_repetition2(self):
        self.a_trier = [1, 1, 1, 0, 1, 1]

        tri_etudiant = self.executer_test(self.tri_fusion_etudiant, "tri_fusion")
        self.a_trier.sort()

        self.assertEqual(tri_etudiant, self.a_trier)

    def test_negatif(self):
        self.a_trier = [-5, -2, 1, 456, -34, 0]

        tri_etudiant = self.executer_test(self.tri_fusion_etudiant, "tri_fusion")
        self.a_trier.sort()

        self.assertEqual(tri_etudiant, self.a_trier)

    def test_gros(self):
        self.a_trier = np.random.rand(500).tolist()

        tri_etudiant = self.executer_test(self.tri_fusion_etudiant, "tri_fusion")
        self.a_trier.sort()

        self.assertEqual(tri_etudiant, self.a_trier)

    def tri_fusion_etudiant(self):
        return exo1_etudiant.tri_fusion(self.a_trier)


class TestDijkstra(unittest.TestCase):
    poids = []
    distances = []
    predecesseurs = []
    noeuds = []
    element_plus_proche = None
    par_noeud = None

    @timeout(3)
    def executer_test(self, fonction, nom_fonction):
        try:
            return fonction()
        except KeyboardInterrupt:
            self.fail(
                f'L\'appel fonction {nom_fonction} ne se termine pas --> Verifiez vos boucles')
        except AssertionError as e:
            raise e

    #        except:
    #            self.fail(
    #                f'Une exception a été levée lors de l\'appel fonction {nom_fonction}. Revérifier votre code.')
    #            raise e

    def trouver_element_plus_proche_etudiant(self):
        self.element_plus_proche = exo2_etudiant.trouver_element_plus_proche(self.distances, self.noeuds)
        return self.element_plus_proche

    def mettre_a_jour_distances_etudiant(self):
        exo2_etudiant.mettre_a_jour_distances(self.poids, self.distances, self.predecesseurs, self.noeuds,
                                              self.par_noeud)

    def test_lire_poids(self):

        poids_attendus = exo2_corrige.lire_poids('poids.txt')

        self.assertEqual(exo2_etudiant.lire_poids("poids.txt"), poids_attendus)

    def test_initialiser(self):
        n_noeuds = 10
        noeud_initial = 2
        AUCUN = -1

        distances_attendues = [AUCUN] * n_noeuds
        distances_attendues[noeud_initial] = 0

        # TODO: - Les predecesseurs sont initialisés a -1.
        predecesseurs_attendus = [AUCUN] * n_noeuds
        predecesseurs_attendus[noeud_initial] = 0

        # TODO: - Noeuds doit etre initialise pour contenir toutes les valeurs de 0 a n_noeuds-1.
        noeuds_attendus = []
        for i in range(n_noeuds):
            noeuds_attendus.append(i)

        resultat_etudiant = exo2_etudiant.initialiser(noeud_initial, n_noeuds)
        resultat_etudiant[noeud_initial] = 0
        self.assertEqual((distances_attendues, predecesseurs_attendus, noeuds_attendus),
                         (resultat_etudiant[0], resultat_etudiant[1], resultat_etudiant[2]))

    def test_trouver_element_plus_proche(self):
        poids = exo2_corrige.lire_poids('poids.txt')
        n_noeuds = 8
        noeud_initial = 2
        AUCUN = -1

        self.distances, self.predecesseurs, noeuds = exo2_corrige.initialiser(noeud_initial, n_noeuds)

        element_attendu = exo2_corrige.trouver_element_plus_proche(self.distances, self.predecesseurs)

        self.assertEqual(element_attendu,
                         self.executer_test(self.trouver_element_plus_proche_etudiant, "trouver_element_plus_proche"))

    def test_mettre_a_jour_distances(self):
        self.poids = exo2_corrige.lire_poids('poids.txt')
        n_noeuds = 8
        noeud_initial = 2
        AUCUN = -1

        self.distances, self.predecesseurs, self.noeuds = exo2_corrige.initialiser(noeud_initial, n_noeuds)
        distances_attendues = copy.deepcopy(self.distances)
        predecesseurs_attendus = copy.deepcopy(self.predecesseurs)
        noeuds_attendus = copy.deepcopy(self.noeuds)

        # Réponse
        element_plus_proche_1 = exo2_corrige.trouver_element_plus_proche(self.distances, self.noeuds)
        exo2_corrige.mettre_a_jour_distances(self.poids, distances_attendues, predecesseurs_attendus, noeuds_attendus,
                                             element_plus_proche_1)
        element_plus_proche_2 = exo2_corrige.trouver_element_plus_proche(self.distances, self.noeuds)
        exo2_corrige.mettre_a_jour_distances(self.poids, distances_attendues, predecesseurs_attendus, noeuds_attendus,
                                             element_plus_proche_2)

        # Étudiant
        self.par_noeud = element_plus_proche_1
        self.executer_test(self.mettre_a_jour_distances_etudiant, "mettre_a_jour_distances")
        self.par_noeud = element_plus_proche_2
        self.executer_test(self.mettre_a_jour_distances_etudiant, "mettre_a_jour_distances")

        # exo2_etudiant.mettre_a_jour_distances(self.poids, self.distances, self.predecesseurs, self.noeuds, element_plus_proche_1)
        # exo2_etudiant.mettre_a_jour_distances(self.poids, self.distances, self.predecesseurs, self.noeuds, element_plus_proche_2)

        self.assertEqual((self.distances, self.predecesseurs, self.noeuds),
                         (distances_attendues, predecesseurs_attendus, noeuds_attendus))

    def test_predecesseurs_distances_final(self):
        self.poids = exo2_corrige.lire_poids('poids.txt')
        noeud_initial = 3
        AUCUN = -1
        self.distances, self.predecesseurs, self.noeuds = exo2_corrige.initialiser(noeud_initial, 8)
        predecesseurs_attendus = [1, 2, 7, 0, 7, 6, 3, 3]
        distances_attendues = [11, 10, 9, 0, 9, 8, 4, 7]

        start_time = time.time()
        timeout = 2
        while (self.noeuds):
            # Pour forcer un timeout si boucle infinie
            current_time = time.time()
            elapsed_time = current_time - start_time
            if elapsed_time > timeout:
                self.fail(
                    f'Les fonctions que vous avez defini pour dijkstra forcent une boucle infinie a l\'algorithme. Vos returns ou modifications de variables sont fautifs.')
                print(f'Les fonctions que vous avez defini pour dijkstra forcent une boucle infinie a l\'algorithme. Vos returns ou modifications de variables sont fautifs.')
                break

            # 	TODO: Trouver l'element le plus proche du noeud initial saisi par l'utilisateur.
            self.element_plus_proche = self.executer_test(self.trouver_element_plus_proche_etudiant,
                                                          "trouver_element_plus_proche")
            # exo2_etudiant.trouver_element_plus_proche(self.distances, self.noeuds)

            #   TODO: Si tous les chemins possibles ont été évalués (aucun prochain element a visiter), sortir de la boucle
            if (self.element_plus_proche == AUCUN):
                break

            # 	TODO: Mettre à jour les distances en vérifiant si c'est plus court de passer par le noeud le plus proche.
            # exo2_etudiant.mettre_a_jour_distances(self.poids, self.distances, self.predecesseurs, self.noeuds, element_plus_proche)
            self.par_noeud = self.element_plus_proche
            self.executer_test(self.mettre_a_jour_distances_etudiant, "mettre_a_jour_distances")

            # 	TODO: Retirer cet element le plus proche de l'ensemble noeuds.
            if self.element_plus_proche in self.noeuds:
                self.noeuds.remove(self.element_plus_proche)

            self.assertEqual((self.distances, self.predecesseurs), (distances_attendues, predecesseurs_attendus))


if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)
