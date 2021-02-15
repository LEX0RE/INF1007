#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
from math import pi
from turtle import *
import sys
import importlib
sys.path.insert(1, "D:\Python")
ch6 = __import__("c04-ch6-exercices-LEX0RE.exercice")
frequence = ch6.exercice.frequence

# TODO: Définissez vos fonction ici
def ellipsoide(a = 1, b = 1, c = 1, p = 1)->tuple:
    volume = (4/3) * pi * a * b * c
    return (volume, volume * p)

def rec_tree(dist=70, angle=35, size=7):
    if dist > 0 and size > 0:
        pensize(size)
        forward(dist)
        left(angle)
        rec_tree(dist - 10, angle - 5, size - 1)
        right(angle * 2)
        rec_tree(dist - 10, angle - 5, size - 1)
        left(angle)
        backward(dist)

def tree():
    setheading(90)
    color('green')
    begin_fill()
    rec_tree()
    end_fill()
    done()

def valide(chaine)->bool:
    for i in chaine:
        if i not in {"a", "g", "c", "t"}:
            return False
    return True

def saisie()->str:
    return str(input())

def proportion(chaine, sequence):
    proportion_value = chaine.count(sequence)
    proportion_value = round((proportion_value / len(chaine)) * 10000) /  100
    print(f"Il y a {proportion_value} % de {sequence}.")

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(ellipsoide(p = 3, a = 3, b = 45, c = 10))
    print((lambda sentence: sorted(frequence(sentence), key=frequence(sentence).__getitem__)[-1])("Ceci est uuuuuune phrase"))
    tree()
    chaine = saisie()
    if valide(chaine):
        proportion(chaine, saisie())
    else:
        print("Invalide")
    pass
