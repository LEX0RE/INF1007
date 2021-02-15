from vehicule import Vehicule
from dictionnaire_modeles import roues_dict, chassis_dict, moteurs_dict
from roue import Roue
from chassis import Chassis
from moteur import Moteur


class Amphibie(Vehicule):

    def __init__(self, nom: str, position_dep: list):
        roues = [Roue(roues_dict['moto'], 5, 0.01, 2000)]
        moteur = Moteur(moteurs_dict['auto'], 50, 12)
        chassis = Chassis(chassis_dict['camion'], 100, 0.1, 0.9)
        super().__init__(nom, position_dep, roues, moteur, chassis)
        
    def celebrer(self):
        return "Victoire de l'Amphibie"