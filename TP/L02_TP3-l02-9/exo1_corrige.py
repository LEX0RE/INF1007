# TODO
def lire_fichier():
    chemin = "./"
    nom = "listeDeNombres.txt"

    # Ouvrir le fichier en mode de lecture à l'aide d'un context manager
    with open(chemin + nom, 'r') as f:
        #Lire les lignes du fichier dans un tableau de lignes
        tableauDeLignes = f.readlines()

    # Faire une tableau de tableau (contenu) contenant les séquences de nombres (transformées de string à int)
    contenu = [[int(val) for val in lignes.split()] for lignes in tableauDeLignes[0:]]

    return contenu

# TODO
def sauvegarder_sequences_triees(chemin, nom, sequencesTriees):
    # Ouvrir le fichier en mode écriture à l'aide d'un context manager
    with open(chemin + nom, "w") as f:

        # Pour toutes les séquences triées de nombres
        for sequence in sequencesTriees:
            
            # Pour tous les nombres dans la séquence
            for nombre in sequence:
                # Écrire le nombre séparé d'un espace 
                f.write(str(nombre) + " ")

            # Changer de ligne
            f.write("\n")

# TODO
def fusionner(gauche, droite):
    # Si le premier tableau (gauche) est vide, alors rien n'a besoin d'être fusionné. 
    # Retourner le deuxième tableau (droite) comme étant le résultat
    if len(gauche) == 0:
        return droite

    # Si le deuxième tableau (droite) est vide, alors rien n'a besoin d'être fusionné. 
    # Retourner le premier tableau (gauche) comme étant le résultat
    if len(droite) == 0:
        return gauche

    resultat = []
    indexGauche = indexDroite = 0

    # Parcourir les deux tableaux (droite et gauche) jusqu'à ce que tous les éléments
    # soient ajoutés au tableau resultat
    while len(resultat) < len(gauche) + len(droite):
        # Les éléments doivent être triés pour être ajouté au tableau résultat.
        # Il faut donc décider de soit prendre le prochain élément du tableau
        # droite ou soit du tableau gauche
        if gauche[indexGauche] <= droite[indexDroite]:
            resultat.append(gauche[indexGauche])
            indexGauche += 1
        else:
            resultat.append(droite[indexDroite])
            indexDroite += 1

        # Si la fin de n'importe lequel des deux tableaux est atteinte,
        # ajouter directement tous les éléments restants de l'autre tableau
        # au tableau résultat, et terminer la boucle.
        if indexDroite == len(droite):
            resultat += gauche[indexGauche:]
            break

        if indexGauche == len(gauche):
            resultat += droite[indexDroite:]
            break

    return resultat

# TODO
def tri_fusion(sequenceDeNombre):
    # Si le tableau (sequenceDeNombre) contient moins de 2 éléments, retourner directement le tableau
    # comme étant le résultat de la fonction
    if len(sequenceDeNombre) < 2:
        return sequenceDeNombre

    # Trouver l'indice de l'élément milieu du tableau
    milieuSequence = len(sequenceDeNombre) // 2

    # Trier le tableau en séparant récursivement le tableau en 2 parties égales
    # qui seront triées et finalement fusionnées ensemble dans le résultat final
    # INDICE: Passer à chaque paramètres de la fonction fusionner la fonction tri_fusion
    # avec une partie (gauche ou droite) de la séquence de nombre
    return fusionner(
        gauche=tri_fusion(sequenceDeNombre[:milieuSequence]),
        droite=tri_fusion(sequenceDeNombre[milieuSequence:]))

# NE PAS TOUCHER, C'EST UNE FONCTION DE TEST POUR VOUS AIDER À VALIDER VOS RÉSULTATS
def tester_resultat(sequencesATrier, sequencesTriees):
    bonResultats = 0

    for indice in range(len(sequencesTriees)):
        test = sequencesATrier[indice][:] 
        test.sort() # C'est facile le Python ! 
        if (test == sequencesTriees[indice]): 
            bonResultats += 1

    return bonResultats == len(sequencesATrier)

# NE PAS TOUCHER AU MAIN
if __name__ == '__main__':
    sequencesATrier = lire_fichier()

    print("Les séquences à trier sont: ")
    print(sequencesATrier)

    sequencesTriees = []

    for sequence in sequencesATrier:
        sequencesTriees.append(tri_fusion(sequence))

    print("Les séquences triées sont: ")
    print(sequencesTriees)

    estBon = testerResulta_r(sequencesATrier, sequencesTriees)

    if estBon:
        print("Bravo, le tri est bon !")  
    else:
        print("Oups, le tri ne fonctionne pas")
    
    sauvegarder_sequences_triees("./", "resultats.txt", sequencesTriees)
