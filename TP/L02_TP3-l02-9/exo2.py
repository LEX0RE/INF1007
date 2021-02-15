import inspect

# region constantes
#        Si nécessaire ajoutez vos constantes ici afin de ne pas utiliser de chiffres magiques dans le code

TAILLE_MAX = 32
AUCUN = -1  # Valeur utilisee lorsqu'il n'y a aucun chemin, aucun predecesseur, etc.  Pour utiliser une constante unique,
# il faut qu'elle ait une valeur invalide a la fois comme distance et comme numero de noeud.

# endregion

# region "Fonctions d'aide, Rien à modifier ici!"

# Indique si un element est dans l'ensemble.
def est_dans(ensemble, element):
    for elem in ensemble:
        if elem == element:
            return True

    return False


def comparer_tableaux(tableau_a, tableau_b):
    print(
        "Test a la ligne " + str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[len(tableau_a) == len(tableau_b)])

    est_pareil = True
    for i in range(len(tableau_a)):
        if tableau_a[i] != tableau_b[i]:
            est_pareil = False

    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[est_pareil])


def afficher_tableau(nom_tableau, tableau):
    print("Affichage tableau: " + nom_tableau)

    for elem in tableau:
        print("{0:4}".format(elem), end=" ")
    print()


def afficher_matrice(nom_matrice, matrice):
    print("Affichage du contenu de la matrice: " + nom_matrice)
    for line in matrice:
        for elem in line:
            print("{0:4}".format(elem), end=" ")
        print()


# endregion

# region "Fonction à compléter"

# 1- Lit la matrice poids (distances entre les villes) a partir d'un fichier. Retourne le contenu de la matrice lue
def lire_poids(nom_fichier):
    # TODO: Lire le fichier et verifier que la lecture n'a pas fait d'erreur;
    #  La matrice retournée n'a pas d'importance s'il y a eu une erreur.
    #
    # TODO : Ajouter une couche de vérification des données en entrée. Vérifier que toutes les lignes de la matrice
    #  ont la même longeur et qu'il n'y a pas de valeurs incohérentes (autres que des entier positifs ou -1). Si la
    #  matrice est non conforme, utilisez la fonction exit() pour terminer le programme après avoir notifié
    #  l'utilisateur.
    with open(nom_fichier, 'r') as f:
        matrice_lue = f.read().splitlines()
        valide = True
        longueur = 0
        
        for ligne in range(len(matrice_lue)):
            matrice_lue[ligne] = matrice_lue[ligne].split()

            if not longueur:
                longueur = len(matrice_lue[ligne])

            if len(matrice_lue[ligne]) != longueur:
                valide = False

            for index, chiffre in enumerate(matrice_lue[ligne]):
                if (chiffre < '0' or chiffre > '9') and chiffre != "-1":
                    valide = False
                    
                matrice_lue[ligne][index] = int(chiffre)
    
    if valide is False:
        print("Matrice non conforme")
        exit()
    return matrice_lue


# 2- Initialise les structures pour appliquer l'algorithme de Dijkstra.
def initialiser(noeud_initial, n_noeuds):
    # TODO: Initialiser et retourne les tableaux distances, predecesseurs et noeuds.
    #       Tel qu'indique dans l'enonce:
    #       Les distances sont initialisees a -1 sauf pour le noeud initial qui est a 0.
    # TODO: - Les predecesseurs sont initialisés a -1.
    # TODO: - Noeuds doit etre initialise pour contenir toutes les valeurs de 0 a nNoeuds-1.
    distances = [-1 for nombre in range(n_noeuds)]
    predecesseurs = distances[:]
    noeuds = {nombre for nombre in range(n_noeuds)}

    distances[int(noeud_initial)] = 0

    return distances, predecesseurs, noeuds


# 3 - Trouve et retourne l'élément le plus proche de l'élément initial, selon le tableau actuel des distances.
def trouver_element_plus_proche(distances, noeuds):
    # TODO: Pour chaque element de la liste de noeuds, vérifier lequel a la plus petite valeur dans les distances et
    #  retourner l 'indice de cet élément. distance_min = AUCUN
    noeud_plus_proche = -1

    for noeud in noeuds:
        if distances[noeud] + 1:
            if not noeud_plus_proche + 1 or \
               distances[noeud] < distances[noeud_plus_proche]:
                noeud_plus_proche = noeud

    return noeud_plus_proche


# 4 - Fait la mise à jour des distances et des predecesseurs si on permet de passer par par_noeud. Cette fonction ne
#     retourne rien elle modifie les paramètres référencés directement.
def mettre_a_jour_distances(poids, distances, predecesseurs, 
                            noeuds, par_noeud):
    # TODO: Pour chaque element de l'ensemble noeuds, vérifier si passer par_noeud pour y aller réduit la distance par
    #  rapport à celle actuellement dans le tableau distances; si c'est le cas, modifie la distance pour cette
    #  nouvelle valeur et change le prédécesseur de cet élément comme étant par_noeud.  Attention aux valeurs -1 dans
    #  les poids et les distances.  Voir la description dans l'énoncé pour plus de détails.

    # Simplification impossible en raison du maximum de 79 caractères
    for noeud in noeuds:
        if poids[par_noeud][noeud] + 1 and noeud != par_noeud:
            if not distances[noeud] + 1:
                distances[noeud] = poids[par_noeud][noeud] + \
                    distances[par_noeud]
                predecesseurs[noeud] = par_noeud
            elif distances[noeud] > poids[par_noeud][noeud] + \
                    distances[par_noeud]:
                if distances[par_noeud] + 1:
                    predecesseurs[noeud] = par_noeud
                    distances[noeud] = poids[par_noeud][noeud] + \
                        distances[par_noeud]


# 5- Affiche le plus court chemin, soit la liste des noeuds par lesquels il faut passer pour se rendre de la source a
# la destination. Suppose que l'algorithme a deja ete applique pour calculer les tableaux de distances et
# predecesseurs. Cette fonction ne retourne rien.
def afficher_chemin_plus_proche(distances, predecesseurs, noeud_source,
                                noeud_destination):
    # TODO: Afficher le chemin similairement à l'exemple de sortie suivant:
    #       Le chemin le plus court de 4 vers 7 est:
    #       4 -> 2 -> 5 -> 7
    #       de distance 10
    print(f"Le chemin le plus court de {noeud_source}", end="")
    print(f" vers {noeud_destination} est: ")
    parcours = [noeud_destination]
    noeud_sauvegarde = noeud_destination
    while noeud_sauvegarde != noeud_source:
        noeud_sauvegarde = predecesseurs[noeud_sauvegarde]
        parcours.append(noeud_sauvegarde)

    while len(parcours):
        print(parcours[len(parcours) - 1], end="")
        del parcours[len(parcours) - 1]
        if len(parcours):
            print(" -> ", end="")

    print(f"\nde distance {distances[noeud_destination]}")


# endregion

# region "Fonctions de test - Rien à modifier pour vous ici!"

BON_SI_VRAI = ["ERREUR", "BON"]


def tester_trouver_element_plus_proche():
    print("Test de trouve_element_plus_proche:")

    distances = [7, 2, -1, 5, 6]
    noeuds = [0, 1, 2, 3, 4]

    plus_proche = trouver_element_plus_proche(distances, noeuds)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[plus_proche == 1])

    noeuds = [0, 2, 3, 4]
    plus_proche = trouver_element_plus_proche(distances, noeuds)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[plus_proche == 3])


def tester_mettre_a_jour_distances():
    print("Test de mettre_a_jour_distances")
    poids = [[0, 4, 2, -1], [-1, 0, -1, 2], [1, 1, 0, 6], [-1, -1, -1, 0]]
    distances = [0, -1, -1, -1]
    predecesseurs = [-1, -1, -1, -1]

    noeuds = [0, 1, 2, 3]
    distances_attendues = [0, 4, 2, -1]
    predecesseurs_attendus = [-1, 0, 0, -1]
    mettre_a_jour_distances(poids, distances, predecesseurs, noeuds, 0)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : Deux sous tests")
    comparer_tableaux(distances, distances_attendues)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : Deux sous tests")
    comparer_tableaux(predecesseurs, predecesseurs_attendus)
    distances = distances_attendues
    predecesseurs = predecesseurs_attendus

    noeuds = [1, 2, 3]
    distances_attendues = [0, 3, 2, 8]
    predecesseurs_attendus = [-1, 2, 0, 2]

    mettre_a_jour_distances(poids, distances, predecesseurs, noeuds, 2)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : ")
    comparer_tableaux(distances, distances_attendues)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : ")
    comparer_tableaux(predecesseurs, predecesseurs_attendus)
    distances = distances_attendues
    predecesseurs = predecesseurs_attendus

    # Un etat impossible dans l'algorithme, mais ceci permet de verifier si mettreAJourDistances verifie seulement
    # les elements de l'ensemble noeuds.
    distances[0] = 10
    noeuds = [1, 2, 3]
    mettre_a_jour_distances(poids, distances, predecesseurs, noeuds, 2)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[distances[0] == 10])


# endregion

if __name__ == '__main__':
    tester_trouver_element_plus_proche()
    tester_mettre_a_jour_distances()
    print("Fin des tests")

    # TODO: Lire la matrice des poids à partir du fichier poids.txt et l'afficher dans le terminal.
    poids = lire_poids("./poids.txt")
    afficher_matrice("Matrice du fichier", poids)

    # TODO: Demander a l'utilsateur l'indice du noeud source, avec validation de l'entree.
    noeud_source = int(input("Veuillez indiquer l'indice du noeud source : "))

    if noeud_source > len(poids[0]) or noeud_source < 0:
        print("Noeud source invalide")
        exit()
    # TODO: Intialiser les tableaux de distances, predecesseurs et noeuds.
    distance, predecesseur, noeuds = initialiser(noeud_source, len(poids))

    # TODO: Tant qu'il reste des éléments dans l'ensemble noeuds:
    while len(noeuds):

        # 	TODO: Trouver l'element le plus proche du noeud initial saisi par l'utilisateur.
        noeud_plus_proche = trouver_element_plus_proche(distance, noeuds)

        #   TODO: Si tous les chemins possibles ont été évalués (aucun prochain element a visiter), sortir de la boucle
        if not noeud_plus_proche + 1:
            break

        # 	TODO: Mettre à jour les distances en vérifiant si c'est plus court de passer par le noeud le plus proche.
        mettre_a_jour_distances(poids, distance, predecesseur, noeuds,
                                noeud_plus_proche)

        # 	TODO: Retirer cet element le plus proche de l'ensemble noeuds.
        noeuds.remove(noeud_plus_proche)
    # TODO: Afficher le contenu de distances.
    afficher_tableau("Distance des noeuds", distance)

    # TODO: Afficher le contenu de predecesseurs.
    afficher_tableau("Prédecesseurs des noeuds", predecesseur)

    # TODO: Demander a l'utilisateur un noeud destination different de la source, avec validation de l'entree (indiquer
    #       l'intervalle de sommet possible et si la valeur entrée est hors de celui-ci).
    print("Veuillez indiquer un noeud destination ", end="")
    noeud_destination = int(input("différent de la source : "))

    if noeud_source == noeud_destination or noeud_destination > len(poids[0]):
        print("Noeud destination invalide")
        exit()

    # TODO: Valider si un chemin entre les deux sommet existe
    # TODO: Afficher la solution, soit le plus court chemin allant de la source vers la destination.
    if distance[noeud_destination] + 1:
        afficher_chemin_plus_proche(distance, predecesseur,
                                    noeud_source, noeud_destination)
    else:
        print("Destination impossible")
