from chassis import Chassis
from moteur import Moteur
from roue import Roue

AIR_DENSITY = 1.2


class Vehicule:
    # PARTIE 2 - TODO
    def __init__(self, nom: str, position_dep: list, roues: list, moteur: Moteur, chassis: Chassis):
        self.__nom = nom
        self.__vitesse = [0, 0, 0]
        self.__position = position_dep[:]
        self.__roues = roues[:]
        self.__moteur = moteur
        self.__chassis = chassis


    def accelerer(self, temps_ecoule):
        force_totale = self.traction - self.friction - self.trainee
        acceleration = force_totale / self.poids
        self.vitesse[2] = self.vitesse[2] + acceleration * temps_ecoule
        self.position[2] = self.position[2] + self.vitesse[2] * temps_ecoule

    def celebrer(self):
        pass

    @property
    def nom(self):
        return self.__nom
        
    @property
    def roues(self):
        return self.__roues
        
    @property
    def moteur(self):
        return self.__moteur
        
    @property
    def chassis(self):
        return self.__chassis
        
    @property
    def position(self):
        return self.__position
        
    @property
    def vitesse(self):
        return self.__vitesse
        
    @property
    def poids(self):
        return self.__moteur.poids + self.__chassis.poids + sum(roue.poids for roue in self.__roues)
        
    @property
    def trainee(self):
        chassis_var = self.__chassis.coefficient_trainee * self.__chassis.aire_frontale
        return 1/2 * chassis_var * AIR_DENSITY * self.__vitesse[2] ** 2
        
    @property
    def traction(self):
        return self.poids * self.__moteur.acceleration
        
    @property
    def friction(self):
        return sum(roue.coefficient_friction * self.__vitesse[2] for roue in self.__roues)
        
    @property
    def acceleration(self):
        return (self.traction - self.trainee - self.friction) / self.poids
