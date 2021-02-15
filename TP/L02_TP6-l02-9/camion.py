from vehicule import Vehicule
from dictionnaire_modeles import roues_dict, chassis_dict, moteurs_dict
from roue import Roue
from chassis import Chassis
from moteur import Moteur


# PARTIE 2 - TODO
class Camion(Vehicule):

    def __init__(self, nom: str, position_dep: list):
        roues = [Roue(roues_dict['camion'], 45.5, 0.01, 1820)] * 6
        moteur = Moteur(moteurs_dict['camion'], 455, 4)
        chassis = Chassis(chassis_dict['camion'], 8640, 5, 0.8)
        super().__init__(nom, position_dep, roues, moteur, chassis)
        
    def celebrer(self):
        return "Victoire du Camion"