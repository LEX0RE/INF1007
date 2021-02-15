def exercice2(expression):
    #TODO: retourner la valeur adéquate
    save = expression
    while expression.find('()') != -1:
        expression = expression.replace("()", "")
    if len(expression) > 0:
        return "Incorrect"
    else:
        save = save.replace("()","(.)")
        return save


if __name__ == '__main__':
        expression = input("veuillez entrer l'expression : ")
        print(exercice2(expression))