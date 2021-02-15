import math

constanteGravitationnelle = 9.81
def exercice3(hauteurInitiale, coefficientDeRebond):
    #TODO: faites vos calculs et mettez le resultat dans la variable 'nombreDeRebonds'
    h_im1 = hauteurInitiale
    nombreDeRebonds = 0
    while h_im1 > 0.01:
        v_im1 = math.sqrt(2 * constanteGravitationnelle * h_im1)
        v_i = v_im1 * coefficientDeRebond
        h_i = (v_i ** 2) / (2 * constanteGravitationnelle)
        nombreDeRebonds += 1
        h_im1 = h_i

    return nombreDeRebonds

if __name__ == '__main__':
    hauteurInitiale = float(input("Quelle est la hauteur initiale: "))
    coefficientDeRebond = float(input("Quel est le coefficient de rebond(entre 0 et 1 exclus [0:1[ ): "))
    print(exercice3(hauteurInitiale, coefficientDeRebond))



