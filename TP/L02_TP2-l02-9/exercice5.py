def afficherMatrice(M):
    for i in range(len(M)):
        ligne = ['{}'.format(x) for x in M[i]]
        print(ligne, '\t')
    print('\n')


def matriceZero(nbLignes, nbColonnes):
    A = []
    #TODO: Remplir la matrice A de 0, selon les dimensions données
    colonne = [0 for c in range(nbColonnes)]
    A = [colonne[:] for l in range(nbLignes)]
    return A



def multiplierMatrices(A, B):

    #TODO: Si les matrices ne peuvent pas etre multipliées, affecter à C une matrice nulle [nbLignesA x nbColonnesB]
    C = matriceZero(len(A), len(B[0]))

    #TODO: Sinon faire la multiplication et mettre dans C le résultat
    if len(A[0]) == len(B):
        for row in range(len(A)):
            for column in range(len(B[0])):
                number = 0
                for index in range(len(B)):
                    number += A[row][index] * B[index][column]
                C[row][column] = number
    return C


if __name__ == '__main__':
    A = ([[1, 2], [1, 5]])
    B = ([[1, 2], [1, 6], [3, 8]])
    C = ([[1], [6]])
    afficherMatrice(multiplierMatrices(A, B))
    afficherMatrice(multiplierMatrices(B, A))
    afficherMatrice(multiplierMatrices(A, C))
    afficherMatrice(multiplierMatrices(B, C))