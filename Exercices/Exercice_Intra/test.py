"""
def iterator(min, max):
    number = 0
    for i in range(min, max, 2):
        number += 1
        for j in range(max * 3):
            number += 1
            if j % 3 == 0:
                continue
    print(number)

iterator(2, 6)
"""
def iterate(min, max):
    compteur = 0
    for i in range(min, max, 2):
        for j in range(max * 3):
            compteur += 1
            if j % 3 == 0:
                break
    return compteur

print(iterate(2, 6))