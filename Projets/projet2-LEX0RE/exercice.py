import csv  

import random

def enregistrement(adresse_longue, code):
    """
    Cette fonction enregistre, dans un fichier text, la correspondance entre les adresses web longues et courtes.
    La fonction prend en paramètre l'adresse longue fournite par l'utilisateur et le code associé à cette adresse.
    La fonction vérifie au préalable si les adresses contiennent des espaces. Si c'est le cas, la fonction retourne False.
    Si l'enregistrement s'est bien déroulé, la fonction retourne True.
    """
    # Vérifie que les adresses ne contiennent pas d'espaces
    if ' ' in code:
        print('Erreur : le code fournie en paramètre contient un espace.')
        return False
    elif ' ' in adresse_longue:
        print('Erreur : l\'adresse longue fournie en paramètre contient un espace.')
        return False

    with open('data/database.csv', mode ='a', newline='\n') as f:  
        addresswriter = csv.writer(f, delimiter=' ')
        addresswriter.writerow([code, adresse_longue])
    
    return True

def chargement():
    """
    Cette fonction charge en mémoire le contenu de la base de données des adresses enregistrées.
    """
    # TODO: initialiser la structure de données vide
    donnees = dict()

    with open('data/database.csv', mode='r') as f:  
        addressreader = csv.reader(f, delimiter=' ')
        for row in addressreader:
            code, adresse_longue = row[0], row[1]
            adresse_courte = 'http://inf1007.polymtl.ca/' + code

            # TODO: enregistrer les adresses dans une structure de données appropriée
            donnees[code] = adresse_longue

    return donnees


def reduit(adresse_longue, personnalisation=None):
    """
    À partir de l'adresse passée en paramètre, cette fonction retourne une adresse réduite unique.
    L'adresse fournie en sortie du programme prend le préfixe http://inf1007.polymtl.ca/, 
    suivi par une chaîne de 8 caractères choisis aléatoirement parmi les suivantes :
    - des lettres minuscules ou majuscules
    - des chiffres
    - un tiret (-) ou un tiret bas (_)

    Alternativement, la fonction peut fournir une adresse personnalisée (ex: http://inf1007.polymtl.ca/projet2 ou http://inf1007.polymtl.ca/Benjamin),
    en passant le suffixe en paramètre (ex: personnalisation='Benjamin').

    Dans les deux cas de figure, la fonction doit retourner une adresse unique (qui n'existe donc pas encore dans la base de données). La base de données peut être chargée en mémoire à l'aide de la fonction "chargement()".
    Après avoir généré l'adresse courte, la fonction enregistre les deux adresses en utilisant la fonction "enregistrement()".
    Si le suffixe personnalisé fourni en paramètre existe déjà dans la base de données, la fonction doit retourner None. Sinon, elle retourne l'adresse courte.
    Si l'enregistrement dans la base de données n'a pas été réalisé, la fonction doit retourner None.
    """
    database = chargement()

    # TODO : implémenter la fonction
    if (personnalisation is None):
        code = ""
        possibility = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
        while code == "" or code in database:
            code = ""
            while len(code) < 8:
                symbol = possibility[random.randint(0, len(possibility) - 1)]
                code = code[:] + symbol
    elif personnalisation in database:
        return None
    else:
        code = personnalisation

    if enregistrement(adresse_longue, code) != True:
        return None
    else:
        return "http://inf1007.polymtl.ca/" + code
    

def allonge(adresse_courte):
    """
    Cette fonction returne l'adresse originale de l'adresse passée en paramètres.
    La fonction vérifie que l'adresse fournie en paramètre correspond à son système, donc qu'elle débute avec "http://inf1007.polymtl.ca/". Si ce n'est pas le cas, la fonctione retourne None.
    Si le code de l'adresse n'existe pas dans la base de données, la fonction retourne None.
    Si le code de l'adresse existe dans la base de données, la fonction retourne l'adresse originale.
    """
    database = chargement()

    # TODO : implémenter la fonction
    if adresse_courte is not None and adresse_courte.startswith("http://inf1007.polymtl.ca/") and adresse_courte[len("http://inf1007.polymtl.ca/"):] in database:
        return database[adresse_courte[len("http://inf1007.polymtl.ca/"):]]
    return None
