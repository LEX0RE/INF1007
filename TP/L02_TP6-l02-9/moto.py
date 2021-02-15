from vehicule import Vehicule
from dictionnaire_modeles import roues_dict, chassis_dict, moteurs_dict
from roue import Roue
from chassis import Chassis
from moteur import Moteur


# PARTIE 2 - TODO
class Moto(Vehicule):

    def __init__(self, nom: str, position_dep: list):
        roues = [Roue(roues_dict['moto'], 10, 0.02, 320)] * 2
        moteur = Moteur(moteurs_dict['moto'], 82, 9.3)
        chassis = Chassis(chassis_dict['moto'], 100, 0.6, 0.6)
        super().__init__(nom, position_dep, roues, moteur, chassis)

    def celebrer(self):
        return "Victoire de la Moto"
