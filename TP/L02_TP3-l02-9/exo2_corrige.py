import inspect

# region constantes

TAILLE_MAX = 32
AUCUN = -1  # Valeur utilisee lorsqu'il n'y a aucun chemin, aucun predecesseur, etc.  Pour utiliser une constante unique,


# il faut qu'elle ait une valeur invalide a la fois comme distance et comme numero de noeud.

# endregion

# region " Fonctions d'aide, Rien à modifier ici!""

# Indique si un element est dans l'ensemble.
def estDans(ensemble, element):
    for elem in ensemble:
        if elem == element:
            return True

    return False


def comparerTableaux(tableauA, tableauB):
    print(
        "Test a la ligne " + str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[len(tableauA) == len(tableauB)])

    estPareil = True
    for i in range(len(tableauA)):
        if tableauA[i] != tableauB[i]:
            estPareil = False

    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[estPareil])


def afficherTableau(nomTableau, tableau):
    print("Affichage tableau: " + nomTableau)

    for elem in tableau:
        print("{0:4}".format(elem), end=" ")
    print()


def afficherMatrice(nomMatrice, matrice):
    print("Affichage du contenu de la matrice: " + nomMatrice)
    for line in matrice:
        for elem in line:
            print("{0:4}".format(elem), end=" ")
        print()


# endregion

# region "Fonction à compléter"

# 1- Lit la matrice poids (distances entre les villes) a partir d'un fichier.
def lire_poids(nomFichier):
    # TODO: Lire le fichier et verifier que la lecture n'a pas fait d'erreur; affecter la valeur a ok selon s'il y a eu
    #      une erreur ou non et retourner la matrice lue.  La matrice retournée n'a pas d'importance s'il y a eu une erreur.
    #      Format du fichier: dimension sur une ligne puis les differents elements séparés par des "whitespaces".
    #
    # TODO Partie 2: Ajouter une couche de vérification des données en entrée. Vérifier que toutes les lignes de la matrice
    #                ont la même longeur et qu'il n'y a pas de valeurs incohérentes (autres que des entier positifs ou -1)
    with open(nomFichier, 'r') as f:
        listeDeLignes = f.readlines()

    matriceLue = [[int(val) for val in ligne.split()] for ligne in listeDeLignes[0:]] 
 
    if not all(len(ligne) == len(matriceLue[0]) for ligne in matriceLue[1:]): 
        print("La matrice n'est pas conforme (les lignes n'ont pas toutes la meme longueur. Fin du programme.") 
        exit() 
 
    if not all([x >=-1 for ligne in matriceLue for x in ligne]): 
        print("La matrice n'est pas conforme (valeurs doivent être -1 ou entier positif). Fin du programme") 
        exit() 

    return matriceLue


# 2- Initialise les structures pour appliquer l'algorithme de Dijkstra.
def initialiser(noeudInitial, nNoeuds):
    # TODO: Initialiser les tableaux distances, predecesseurs et noeuds, incluant leurs tailles.
    #       Tel qu'indique dans l'enonce:
    #       Les distances sont initialisees a -1 sauf pour le noeud initial qui est a 0.

    distances = [AUCUN] * nNoeuds
    distances[noeudInitial] = 0

    # TODO: - Les predecesseurs sont initialisés a -1.
    predecesseurs = [AUCUN] * nNoeuds
    predecesseurs[noeudInitial] = 0

    # TODO: - Noeuds doit etre initialise pour contenir toutes les valeurs de 0 a nNoeuds-1.
    noeuds = []
    for i in range(nNoeuds):
        noeuds.append(i)

    return distances, predecesseurs, noeuds


# 3 - Trouve l'élément le plus proche de l'élément initial, selon le tableau actuel des distances.
def trouver_element_plus_proche(distances, noeuds):
    # TODO: Pour chaque element de la liste de noeuds, vérifier lequel a la plus petite valeur dans les distances et
    #  retourner l 'indice de cet élément. distance_min = AUCUN
    distance_min = AUCUN

    for noeud in noeuds:
        if distances[noeud] is not AUCUN:
            if (distance_min is not AUCUN and distances[distance_min] > distances[
                noeud]) or distance_min is AUCUN:
                distance_min = noeud
    return distance_min


# 4 - Fait la mise à jour des distances et des predecesseurs si on permet de passer par parNoeud.
def mettre_a_jour_distances(poids, distances, predecesseurs, noeuds, parNoeud):
    # TODO: Pour chaque element de l'ensemble noeuds, vérifier si passer parNoeud pour y aller réduit la distance
    #       par rapport à celle actuellement dans le tableau distances; si c'est le cas, modifie la distance pour
    #       cette nouvelle valeur et change le prédécesseur de cet élément comme étant parNoeud.  Attention aux valeurs -1
    #       dans les poids et les distances.  Voir la description dans l'énoncé pour plus de détails.
    for noeud in noeuds:
        if AUCUN not in (poids[parNoeud][noeud], parNoeud):
            if distances[noeud] is AUCUN or (distances[noeud] > (poids[parNoeud][noeud] + distances[parNoeud])):
                distances[noeud] = poids[parNoeud][noeud] + distances[parNoeud]
                predecesseurs[noeud] = parNoeud
    return


# 5 - Retire un element d'une liste, la lsite considérée comme un ensemble (où l'ordre n'est pas important).
def retirerUnElementDeLensemble(ensemble, element):
    ensemble.remove(element)
    return


# 6- Affiche le plus court chemin, soit la liste des noeuds par lesquels il faut passer pour se rendre de la source
# a la destination.  Suppose que l'algorithme a deja ete applique pour calculer les tableaux de distances et predecesseurs.
def afficher_chemin_plus_proche(distances, predecesseurs, noeudSource, noeudDestination):
    # TODO: Afficher le chemin similairement à l'exemple de sortie suivant:
    #       Le chemin le plus court de 4 vers 7 est:
    #       4 -> 2 -> 5 -> 7
    #       de distance 10

    print("Le chemin le plus court de " + str(noeudSource) + " vers " + str(noeudDestination) + " est:")

    indice_courant = noeudDestination
    chemin = " " + str(noeudDestination)

    while indice_courant is not noeudSource:
        indice_courant = predecesseurs[indice_courant]
        chemin = " " + str(indice_courant) + " ->" + chemin

    if noeudDestination is noeudSource:
        chemin = str(noeudSource) + " ->"

    print(chemin)
    print("De distance " + str(distances[noeudDestination]))

    return


# endregion

# region "Fonctions de test - Rien à modifier pour vous ici!"

BON_SI_VRAI = ["ERREUR", "BON"]


def tester_trouveElementPlusProche():
    print("Test de trouve_element_plus_proche:")

    distances = [7, 2, -1, 5, 6]
    noeuds = [0, 1, 2, 3, 4]

    plusProche = trouver_element_plus_proche(distances, noeuds)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[plusProche == 1])

    noeuds = [0, 2, 3, 4]
    plusProche = trouver_element_plus_proche(distances, noeuds)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[plusProche == 3])


def tester_mettreAJourDistances():
    print("Test de mettre_a_jour_distances")
    poids = [[0, 4, 2, -1], [-1, 0, -1, 2], [1, 1, 0, 6], [-1, -1, -1, 0]]
    distances = [0, -1, -1, -1]
    predecesseurs = [-1, -1, -1, -1]

    noeuds = [0, 1, 2, 3]
    distancesAttendues = [0, 4, 2, -1]
    predecesseursAttendus = [-1, 0, 0, -1]
    mettre_a_jour_distances(poids, distances, predecesseurs, noeuds, 0)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : ")
    comparerTableaux(distances, distancesAttendues)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : ")
    comparerTableaux(predecesseurs, predecesseursAttendus)
    distances = distancesAttendues
    predecesseurs = predecesseursAttendus

    noeuds = [1, 2, 3]
    distancesAttendues = [0, 3, 2, 8]
    predecesseursAttendus = [-1, 2, 0, 2]

    mettre_a_jour_distances(poids, distances, predecesseurs, noeuds, 2)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : ")
    comparerTableaux(distances, distancesAttendues)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : ")
    comparerTableaux(predecesseurs, predecesseursAttendus)
    distances = distancesAttendues
    predecesseurs = predecesseursAttendus

    # Un etat impossible dans l'algorithme, mais ceci permet de verifier si mettre_a_jour_distances verifie seulement les elements de l'ensemble noeuds.
    distances[0] = 10
    noeuds = [1, 2, 3]
    mettre_a_jour_distances(poids, distances, predecesseurs, noeuds, 2)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[distances[0] == 10])


def tester_retirerUnElementDuTableau():
    print("Test de retirerUnElementDuTableau: ")
    ensemble = [5, 2, 3, 4, 1]
    ensembleSans2 = [1, 4, 3, 5]  # C'est un ensemble, l'ordre n'est pas important
    ensemble.remove(2)
    print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[
        len(ensemble) == len(ensembleSans2)])
    for elem in ensembleSans2:
        print("Test a la ligne " + str(inspect.currentframe().f_lineno) + " : " + BON_SI_VRAI[estDans(ensemble, elem)])


# endregion

if __name__ == '__main__':
    tester_trouveElementPlusProche()
    tester_mettreAJourDistances()
    tester_retirerUnElementDuTableau()
    print("Fin des tests")

    # TODO: Lire la matrice des poids � partir du fichier poids.txt.
    matriceLue = lire_poids("poids.txt")  # Devrait mettre une constante pour poids.txt

    afficherMatrice("matriceLue", matriceLue)

    # TODO: Demander a l'utilsateur l'indice du noeud source, avec validation de l'entree.
    while True:
        indiceNoeudSource = int(input("Quel est l'indice du noeud source? "))
        if indiceNoeudSource >= 0 and indiceNoeudSource < len(matriceLue):
            break

    # TODO: Intialiser les tableaux de distances, predecesseurs et noeuds.
    liste_distances, liste_predecesseurs, liste_noeuds = initialiser(indiceNoeudSource, len(matriceLue))

    # TODO: Tant qu'il reste des éléments dans l'ensemble noeuds:
    while (liste_noeuds):
        # 	TODO: Trouver l'element le plus proche du noeud initial saisi par l'utilisateur.
        element_plus_proche = trouver_element_plus_proche(liste_distances, liste_noeuds)

        #   TODO: Si tous les chemins possibles ont été évalués (aucun prochain element a visiter), sortir de la boucle
        if (element_plus_proche == AUCUN):
            break

        # 	TODO: Mettre à jour les distances en vérifiant si c'est plus court de passer par le noeud le plus proche.
        mettre_a_jour_distances(matriceLue, liste_distances, liste_predecesseurs, liste_noeuds, element_plus_proche)

        # 	TODO: Retirer cet element le plus proche de l'ensemble noeuds.
        if element_plus_proche in liste_noeuds:
            liste_noeuds.remove(element_plus_proche)

    # TODO: Afficher le contenu de distances.
    afficherTableau("Contenu de distances", liste_distances)

    # TODO: Afficher le contenu de predecesseurs.
    afficherTableau("Contenu de predecesseurs", liste_predecesseurs)

    # TODO: Demander a l'utilisateur un noeud destination different de la source, avec validation de l'entree (indiquer
    #       l'intervalle de sommet possible et si la valeur entrée est hors de celui-ci).
    while True:
        indiceNoeudDestination = int(input("Quel est l'indice du noeud destination? "))
        if indiceNoeudDestination >= 0 and indiceNoeudSource < len(
                matriceLue) and indiceNoeudSource != indiceNoeudDestination:
            break

    # TODO Partie 2: Valider si un chemin entre les deux sommet existe


    # TODO: Afficher la solution, soit le plus court chemin allant de la source vers la destination.
    afficher_chemin_plus_proche(liste_distances, liste_predecesseurs, indiceNoeudSource, indiceNoeudDestination)
