import exo1 as exo1_etudiant
import exo2 as exo2_etudiant
import exo2_corrige
import numpy as np
from random import randint
import unittest
import os
import sys
import copy

class TestTriFusion(unittest.TestCase):
    
    def test_deja_trie(self):
        a_trier = [0,1,2,3,4,5,6,7,8,9]

        tri_etudiant = exo1_etudiant.tri_fusion(a_trier)
        a_trier.sort()

        self.assertEqual(tri_etudiant, a_trier)

    def test_repetition(self):
        a_trier = [1,1,1,1,1,1]

        tri_etudiant = exo1_etudiant.tri_fusion(a_trier)
        a_trier.sort()

        self.assertEqual(tri_etudiant, a_trier)

    def test_repetition2(self):
        a_trier = [1,1,1,0,1,1]

        tri_etudiant = exo1_etudiant.tri_fusion(a_trier)
        a_trier.sort()

        self.assertEqual(tri_etudiant, a_trier)

    def test_negatif(self):
        a_trier = [-5, -2, 1, 456, -34, 0]

        tri_etudiant = exo1_etudiant.tri_fusion(a_trier)
        a_trier.sort()

        self.assertEqual(tri_etudiant, a_trier)

    def test_gros(self):
        a_trier = np.random.rand(500).tolist()

        tri_etudiant = exo1_etudiant.tri_fusion(a_trier)
        a_trier.sort()

        self.assertEqual(tri_etudiant, a_trier) 

class TestDijkstra(unittest.TestCase):
    def test_lire_poids(self):

        poids_attendus = exo2_corrige.lire_poids('poids.txt')    
        
        self.assertEqual(exo2_corrige.lire_poids("poids.txt"), poids_attendus)

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

        self.assertEqual((distances_attendues, predecesseurs_attendus, noeuds_attendus),(resultat_etudiant[0], resultat_etudiant[1], resultat_etudiant[2]))

    def test_trouver_element_plus_proche(self):
        poids = exo2_corrige.lire_poids('poids.txt')  
        n_noeuds = 8
        noeud_initial = 2
        AUCUN = -1

        distances, predecesseurs, noeuds = exo2_corrige.initialiser(noeud_initial, n_noeuds)

        element_attendu = exo2_corrige.trouver_element_plus_proche(distances, predecesseurs)
        
        self.assertEqual(element_attendu, exo2_etudiant.trouver_element_plus_proche(distances, predecesseurs))

    def test_mettre_a_jour_distances(self):
        poids = exo2_corrige.lire_poids('poids.txt')    
        n_noeuds = 8
        noeud_initial = 2
        AUCUN = -1

        distances, predecesseurs, noeuds = exo2_corrige.initialiser(noeud_initial, n_noeuds)
        distances_attendues = copy.deepcopy(distances)
        predecesseurs_attendus = copy.deepcopy(predecesseurs)
        noeuds_attendus = copy.deepcopy(noeuds)

        # Réponse
        element_plus_proche_1 = exo2_corrige.trouver_element_plus_proche(distances, noeuds)
        exo2_corrige.mettre_a_jour_distances(poids, distances_attendues, predecesseurs_attendus, noeuds_attendus, element_plus_proche_1)
        element_plus_proche_2 =  exo2_corrige.trouver_element_plus_proche(distances, noeuds)
        exo2_corrige.mettre_a_jour_distances(poids, distances_attendues, predecesseurs_attendus, noeuds_attendus, element_plus_proche_2)

        # Étudiant
        exo2_etudiant.mettre_a_jour_distances(poids, distances, predecesseurs, noeuds, element_plus_proche_1)
        exo2_etudiant.mettre_a_jour_distances(poids, distances, predecesseurs, noeuds, element_plus_proche_2)

        self.assertEqual((distances, predecesseurs, noeuds), (distances_attendues, predecesseurs_attendus, noeuds_attendus))


    def test_predecesseurs_distances_final(self):
        poids = exo2_corrige.lire_poids('poids.txt')  
        noeud_initial = 3
        AUCUN = -1
        distances, predecesseurs, noeuds = exo2_corrige.initialiser(noeud_initial, 8)
        predecesseurs_attendus = [3, 6, 6, 0, 7, 6, 3, 1]
        distances_attendues = [2, 6, 7, 0, 11, 8, 4, 9]

        while (noeuds):
            # 	TODO: Trouver l'element le plus proche du noeud initial saisi par l'utilisateur.
            element_plus_proche = exo2_etudiant.trouver_element_plus_proche(distances, noeuds)

            #   TODO: Si tous les chemins possibles ont été évalués (aucun prochain element a visiter), sortir de la boucle
            if (element_plus_proche == AUCUN):
                break

            # 	TODO: Mettre à jour les distances en vérifiant si c'est plus court de passer par le noeud le plus proche.
            exo2_etudiant.mettre_a_jour_distances(poids, distances, predecesseurs, noeuds, element_plus_proche)

            # 	TODO: Retirer cet element le plus proche de l'ensemble noeuds.
            if element_plus_proche in noeuds:
                noeuds.remove(element_plus_proche)
    
        self.assertEqual((distances, predecesseurs),(distances_attendues, predecesseurs_attendus))

if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)