#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    if (len(string) % 2):
        return 0
    return 1


def remove_third_char(string: str) -> str:
    string = string[0:2] + string[3:]
    return string


def replace_char(string: str, old_char: str, new_char: str) -> str:
    while string.find(old_char) != -1:
        pos = string.find(old_char)
        string = string[:pos] + new_char + string[pos + 1:]
    return string


def get_number_of_char(string: str, char: str) -> int:
    occurence = 0
    for x in string:
        if x == char:
            occurence += 1
    return occurence


def get_number_of_words(sentence: str, word: str) -> int:
    occurence = 0
    while sentence.find(word) != -1:
        sentence = sentence[sentence.find(word) + len(word):]
        occurence += 1
    return occurence


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello world! est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
