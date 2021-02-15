"""
Affectation multiple
Convertion avec int()
structure de donnée qui contient des élément unique
str.join()
str.index() et str.find()
fonction native pour obtenir indice du caractère et caractère

"""

"""
def ma_fonction(parametre=None):
    if parametre and parametre.upper() == "TEST":
        return "Le test fonctionne"
    else:
        return "Banane"

print(ma_fonction())
"""

"""
def some_function(some_list=["a", "b", "d", "c"]):
    some_list = sorted(some_list)
    compteur = 8
    while some_list:
        some_list = some_list.pop()
        compteur -= 2
 
    return len(some_list), compteur

print(some_function())
"""

#Pourquoi on peut pas utiliser des listes comme clés de dictionnaire

"""
import math

def distance(point1, point2):
    if len(point1) == len(point2):
        return (round(math.sqrt(sum(((point1[index] - point2[index]) ** 2) for index in range(len(point1)))) * 1000) / 1000)

print(distance([0.3, -2.0, 1.1, 9.9], [0, 1, 1, 22.3]))
print(distance([0.3, -2.0, 1.1, 9.9], [0, 1, 1, 22.3]))
"""

"""
def solution(s):
    # Compléter la fonction
    resultat = 0
    part = ""
    letters = set(s)
    condition = False
    for i in s:
        condition = True
        part += i
        for i in letters:
            if i not in part:
                condition = False
        if s.count(part) > resultat and condition == True:
            resultat = s.count(part)
    return resultat

print(solution("abcabcabcabc"))
print(solution("abccbaabccba"))
print(solution("fffff"))
print(solution("aaaab"))
"""
"""
def fonction(nombre):
    result = []
    for i in range(nombre - 22, nombre + 22):
        if i <= 0:
            continue
        elif i % 7 == 0:
            result.append(i)
    while len(result) > 3:
        diff = [abs(nombre - i) for i in result]
        numero = [num for num in range(len(diff)) if max(diff) == diff[num]][0]
        result.pop(numero)
    return result

print(fonction(7))
"""