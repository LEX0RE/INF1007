from composante import Composante


# PARTIE 1 - TODO
class Moteur(Composante):

    def __init__(self, nom: str, poids: float, acceleration: float):
        self.__acceleration = acceleration
        super().__init__(nom, poids)
        
    @property
    def acceleration(self):
        return self.__acceleration