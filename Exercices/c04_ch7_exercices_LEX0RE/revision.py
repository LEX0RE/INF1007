
def if_premier(nombre: int):
    for i in range(int(nombre / 2), 1, -1):
        if nombre % i == 0:
            return False
    return True    


def sequence_premier():
    chiffre = 2
    while True:
        yield chiffre
        chiffre += 1
        while not if_premier(chiffre):
            chiffre += 1


def sum_premier(nombre: int):
    total = 0
    for i, number in enumerate(sequence_premier()):
        if i < nombre:
            total += number
        else:
            return total




if __name__ == "__main__":
    print(sum_premier(50))
    gen = sequence_premier()
    for i in range(10):
        print(next(gen))