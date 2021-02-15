class Composante:

    def __init__(self, nom: str, poids: int):
        # PARTIE 1 - TODO
        self.__nom = nom
        self.__poids = poids

    @property
    def nom(self):
        return self.__nom

    @property
    def poids(self):
        return self.__poids