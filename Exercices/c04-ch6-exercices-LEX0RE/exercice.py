#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values = []
        while len(values) < 10:
            values.append(input("Entrer une seule valeur :"))
    values.sort()

    print(values)
    return values


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        words = [input() for i in range(2)]
    return sorted(words[0]) == sorted(words[1])


def contains_doubles(items: list) -> bool:
    for i in range(len(items)):
        if items[i] in items[i + 1:]:
            return True
    return False


def best_grades(student_grades: dict) -> dict:
    best = dict()
    for key, value in student_grades.items():
        if len(best) == 0 or (sum(value) / len(value)) > list(best.values())[0]:
            best = {key:sum(value) / len(value)}
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return best


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    frequency = dict()
    for key in sentence:
        frequency[key] = sentence.count(key)
    sorted_keys = sorted(frequency, key=frequency.__getitem__, reverse=True)
    for key in sorted_keys:
        if sentence.count(key) >= 5:
            print(f"Le caractère {key} revient {frequency[key]} fois")
    return frequency


def get_recipes():
    key = input("Entrer le nom de la recette : ")
    item = input("Entrer la liste d'item séparés par des espaces : ")
    list_items = item.split()
    recipe_book = {key: list_items}
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    return recipe_book


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    key = input("Entrer le nom de la recette à regarder : ")
    if key in ingredients:
        print(ingredients[key])
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    print(anagrams())

    my_list = [2, 2, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
