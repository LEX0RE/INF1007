"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""
	UNARMED_POWER = 20

	def __init__(self, name, power, min_level):
		self.__name = name
		self.power = power
		self.min_level = min_level

	@property
	def name(self):
		return self.__name


	@classmethod
	def make_unarmed(cls):
		return cls("Unarmed", cls.UNARMED_POWER, 1)


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""
	def __init__(self, name, max_hp, attack, defense, level):
		self.__name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.__weapon = None
		self.hp = max_hp

	@property
	def name(self):
		return self.__name
		
	@property
	def weapon(self):
		return self.__weapon
		
	@weapon.setter
	def weapon(self, val):
		if val is None:
			val = Weapon.make_unarmed()
		if val.min_level > self.level:
			raise ValueError(Weapon)
		self.__weapon = val

	@hp.setter
	def hp(self, val):
		self.__hp = utils.clamp(val, 0, self.max_hp)

	def compute_damage(self, other) -> int:
		crit = 1 + int(random.randint(1, 16) == 1)
		modifier = crit * random.randint(85, 100) / 100
		return (((((2 * self.level / 5) + 2) * self.weapon.power * self.attack / other.defense) / 50) + 2) * modifier


def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	print(attacker.name + " used " + attacker.weapon.name)
	defender.hp -= attacker.compute_damage(defender)
	print("  " + defender.name + " took " + str(int(attacker.compute_damage(defender))) + " dmg")


def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	print(c1.name + " starts a battle with " + c2.name)
	turn = 1
	while c1.hp > 0 or c2.hp > 0:
		deal_damage(c1, c2)
		c1, c2 = c2, c1
		turn += 1

	print(c2.name + "is sleeping with the fishes.")
	return turn

if __name__ == "__main__":
	c1 = Character("Äpik", 200, 150, 70, 70)
	c2 = Character("Gämmor", 250, 100, 120, 60)

	c1.weapon = Weapon("BFG", 100, 69)
	c2.weapon = Weapon("Deku Stick", 120, 1)

	turns = run_battle(c1, c2)
	print(f"The battle ended in {turns} turns.")