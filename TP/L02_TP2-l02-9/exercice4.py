import math
from random import random



def exercice4():

    #TODO: Approximer PI selon l'enonce.
    nombreIn = 0
    approximationPi = 0
    nIterations = 0
    while abs(math.pi - approximationPi) > 0.0001:
        x = (random() * 2) - 1
        y = (random() * 2) - 1
        if ((x ** 2) + (y ** 2)) < 1:
            nombreIn += 1
        nIterations += 1
        approximationPi = (nombreIn / nIterations) * 4
    approximationPi = math.trunc(approximationPi * 1000) / 1000 # Car demandé de mettre seulement que 3 chiffres décimaux lorsque demandé sur Team
    return (approximationPi, nIterations)



if __name__ == '__main__':
    tuple = exercice4()
    print("Approximation de pi = {:.3f}, en {} iterations".format(tuple[0], tuple[1]))