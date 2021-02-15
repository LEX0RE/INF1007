import json

def createVocabulary():
    #les mails contient la structure de donnée présente dans mail.json
    with open("mails.json") as json_data:
        emails = json.load(json_data)

    #TODO: Affécté à la variable 'result' le résultat final
    SPAM = dict()
    HAM = dict()
    allSpam = 0
    allHam = 0
    for mail in emails:
        if mail["mail"]["Spam"] == "true":
            for word in mail["mail"]["Body"]:
                if word not in SPAM:
                    SPAM[word] = 0
                SPAM[word] += 1
                allSpam += 1
        else:
            for word in mail["mail"]["Body"]:
                if word not in HAM:
                    HAM[word] = 0
                HAM[word] += 1
                allHam += 1

    for key, value in SPAM.items():
        SPAM[key] = value / allSpam

    for key, value in HAM.items():
        HAM[key] = value / allHam

    result = {"Spam" : SPAM.copy(), "Ham" : HAM.copy()}
    with open('results.json', 'w') as fp:
        json.dump(result, fp, indent=4)

if __name__ == '__main__':
    createVocabulary()