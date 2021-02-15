from composante import Composante


# PARTIE 1 - TODO
class Chassis(Composante):

    def __init__(self, nom: str, poids: float, aire_frontale: int, coefficient_trainee: float):
        self.__aire_frontale = aire_frontale
        self.__coefficient_trainee = coefficient_trainee
        super().__init__(nom, poids)
        
    @property
    def aire_frontale(self):
        return self.__aire_frontale
        
    @property
    def coefficient_trainee(self):
        return self.__coefficient_trainee