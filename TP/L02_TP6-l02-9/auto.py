from vehicule import Vehicule
from dictionnaire_modeles import roues_dict, chassis_dict, moteurs_dict
from roue import Roue
from chassis import Chassis
from moteur import Moteur


# PARTIE 2 - TODO
class Auto(Vehicule):

    def __init__(self, nom: str, position_dep: list):
        roues = [Roue(roues_dict['auto'], 14, 0.015, 500)] * 4
        moteur = Moteur(moteurs_dict['auto'], 160, 8)
        chassis = Chassis(chassis_dict['auto'], 1205, 1.4, 0.3)
        super().__init__(nom, position_dep, roues, moteur, chassis)

    def celebrer(self):
        return "Victoire de l'Auto"