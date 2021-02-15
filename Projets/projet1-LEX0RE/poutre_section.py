import math

# Initialisation des variables
F = 10000  # en N
E = 210  # en GPa = 10^3 N/mm^2
L = 100  # en mm

# poutre rectangulaire
b = 10  # en mm
h = 20  # en mm

# poutre carrée
a = 15  # en mm

# poutre ronde
d = 5  # en mm

# poutre creuse
D = 15  # en mm
d = 5  # en mm


# Calcul de la section optimale

E *= (10 ** 3) # convertion en N/mm²

solution = None
section = ["rectangulaire", "carrée", "ronde", "creuse"]
I = []
delta_max = []

I.append((b * (h ** 3)) / 12) # rectangulaire
I.append((a ** 4) / 12) # carrée
I.append((math.pi * (d ** 4)) / 64) # ronde
I.append((math.pi * ((D ** 4) - (d ** 4))) / 64) # creuse

for i in I:
    delta_max.append(((F * (L ** 3)) / (3 * E * i)))

for i in range(len(delta_max)):
    if delta_max[i] == min(delta_max):
        solution = i
    print(F"Déformation {section[i]} :", delta_max[i])

print(F"Le type de section minimisant la déformation maximale est {section[solution]}, avec une déformation de {delta_max[solution]} mm")
