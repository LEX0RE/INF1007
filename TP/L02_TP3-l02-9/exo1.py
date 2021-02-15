# TODO Fonction retournant les séquences à trier, lues à partir d'un fichier
def lire_fichier():
    chemin = "./"
    nom = "listeDeNombres.txt"

    # Ouvrir le fichier en mode de lecture à l'aide d'un context manager
    with open(chemin + nom, 'r') as f:
        # Lire les lignes du fichier dans un tableau de lignes
        contenu = f.read().splitlines()

    # Faire une tableau de tableau (contenu) contenant les séquences de nombres (transformées de string à int)
    for dimension in range(len(contenu)):
        contenu[dimension] = contenu[dimension].split()

        for index, chiffre in enumerate(contenu[dimension]):
            contenu[dimension][index] = int(chiffre)

    return contenu


# TODO Fonction écrivant les séquences triées dans un fichier spécifié
def sauvegarder_sequences_triees(chemin, nom, sequencesTriees):
    # Ouvrir le fichier en mode écriture à l'aide d'un context manager
    with open(chemin + nom, 'w') as f:

        # Pour toutes les séquences triées de nombres
        for sequence in sequencesTriees:

            # Pour tous les nombres dans la séquence
            for nombre in sequence:

                # Écrire le nombre suivi d'un espace
                f.write(str(nombre) + " ")

            # Changer de ligne
            f.write("\n")


def prendre_droite(resultat, droite):
    resultat.append(droite[0])
    del droite[0]


def prendre_gauche(resultat, gauche):
    resultat.append(gauche[0])
    del gauche[0]


# TODO Fonction servant à joindre les deux tableaux ensemble, avec les éléments en ordre croissant
def fusionner(gauche, droite):
    # Si le premier tableau (gauche) est vide, alors rien n'a besoin d'être fusionné. 
    # Retourner le deuxième tableau (droite) comme étant le résultat
    if not gauche or not len(gauche):
        return droite

    # Si le deuxième tableau (droite) est vide, alors rien n'a besoin d'être fusionné. 
    # Retourner le premier tableau (gauche) comme étant le résultat
    if not droite or not len(droite):
        return gauche

    resultat = []

    # Nous ne les utilisons pas
    # indexGauche = indexDroite = 0

    # Boucler jusqu'à ce que tous les éléments des deux tableaux (droite et gauche)
    # soient ajoutés au tableau resultat
    while len(droite) and len(gauche):

        # Les éléments doivent être triés pour être ajouté au tableau résultat.
        # Il faut donc décider de soit prendre le prochain élément du tableau
        # droite ou soit du tableau gauche
        if droite[0] < gauche[0]:
            prendre_droite(resultat, droite)
        else:
            prendre_gauche(resultat, gauche)
        
        # Si la fin de n'importe lequel des deux tableaux est atteinte,
        # ajouter directement tous les éléments restants de l'autre tableau
        # au tableau résultat, et terminer la boucle.
        while len(droite) and (gauche is None or not len(gauche)):
            prendre_droite(resultat, droite)

        while len(gauche) and (droite is None or not len(droite)):
            prendre_gauche(resultat, gauche)

    return resultat


# TODO Fonction d'entrée du tri fusion
def tri_fusion(sequenceDeNombre):
    # Si le tableau (sequenceDeNombre) contient moins de 2 éléments, retourner directement le tableau
    # comme étant le résultat de la fonction
    if len(sequenceDeNombre) < 2:
        return sequenceDeNombre

    # Trouver l'indice de l'élément milieu du tableau
    milieu = (len(sequenceDeNombre) // 2)

    # Trier le tableau en séparant récursivement le tableau en 2 parties égales
    # qui seront triées et finalement fusionnées ensemble dans le résultat final
    # INDICE: Passer à chaque paramètres de la fonction fusionner la fonction tri_fusion
    # avec une partie (gauche ou droite) de la séquence de nombre
    gauche = tri_fusion(sequenceDeNombre[:milieu])

    droite = tri_fusion(sequenceDeNombre[milieu:])

    return fusionner(gauche, droite)


# NE PAS TOUCHER, C'EST UNE FONCTION DE TEST POUR VOUS AIDER À VALIDER VOS RÉSULTATS
def tester_resultat(sequences_a_trier, sequences_triees):
    bon_resultats = 0

    for indice in range(len(sequences_triees)):
        test = sequences_a_trier[indice][:]
        test.sort() # C'est facile le Python ! 
        if (test == sequences_triees[indice]):
            bon_resultats += 1

    return bon_resultats == len(sequences_a_trier)

# NE PAS TOUCHER AU MAIN
if __name__ == '__main__':
    sequences_a_trier = lire_fichier()

    print("Les séquences à trier sont: ")
    print(sequences_a_trier)

    sequences_triees = []

    for sequence in sequences_a_trier:
        sequences_triees.append(tri_fusion(sequence))

    print("Les séquences triées sont: ")
    print(sequences_triees)

    est_bon = tester_resultat(sequences_a_trier, sequences_triees)

    if est_bon:
        print("Bravo, le tri est bon !")  
    else:
        print("Oups, le tri ne fonctionne pas")
    
    sauvegarder_sequences_triees("./", "resultats.txt", sequences_triees)
