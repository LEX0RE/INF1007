def exercice1(tableau):
    #TODO: trier le tableau
    for i in range(len(tableau)):
        for j in range(i + 1, len(tableau)):
            if tableau[j] < tableau[i]:
                temp = tableau[i]
                tableau[i] = tableau[j]
                tableau[j] = temp
    return tableau

if __name__ == '__main__':
    #Voici un exemple de tableau à trier:
    tableau_a_trier = [2,4,6,4,6,7,8,9,7,5,4,3]

    resultat = exercice1(tableau_a_trier)
    print(resultat)