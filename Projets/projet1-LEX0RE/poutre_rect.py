# Initialisation des variables

F = 10000  # en N
E = 210  # en GPa = 10^3 N/mm^2
L = 100  # en mm
b = 10  # en mm
h = 20  # en mm

# Calcul de l'inertie

E *= (10 ** 3) # convertion en N/mm²

I = (b * (h ** 3)) / 12

# Calcul de la déformation maximale

delta_max = ((F * (L ** 3)) / (3 * E * I))
print(F"La déformation maximale de la poutre est {delta_max} mm")

