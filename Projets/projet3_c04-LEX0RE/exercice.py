import csv

# Variable globale
g = 9.80665  # m/s^2


def inter_lin(x: float, x1: float, y1: float, x2: float, y2: float) -> float:
    # Approximation des valeurs par interpolation linéaire
    if x2 - x1 != 0:
        return y1 + (x - x1) * ((y2 - y1) / (x2 - x1))
    return None


def nb_reynold(diametre_particule, vitesse_particule, rho_eau, mu_eau):
    # Obtient le nombre de Reynold
    if mu_eau:
        return (diametre_particule * vitesse_particule * rho_eau) / mu_eau
    return None


def trouver_deux_nb_min(liste: list):
    if type(liste) == list and len(liste) >= 2:
        nb1, nb2 = float("inf"), float('inf')
        for nombre in liste:
            if nombre <= nb1:
                nb1, nb2 = nombre, nb1
            elif nombre < nb2:
                nb2 = nombre

        return (nb1, nb2)

    return None


def proprietes_eau(temperature):
    # Extraction de la base de données
    base_de_donnee = []
    with open("./data/data.csv", "r", encoding="utf-8") as fichier_de_donnee:
        fichier_de_donnee.readline()
        base_de_donnee = fichier_de_donnee.read().splitlines()

        for index_ligne, ligne in enumerate(base_de_donnee):
            base_de_donnee[index_ligne] = ligne.split(",")

            for index_nombre, nombre in enumerate(base_de_donnee[index_ligne]):
                base_de_donnee[index_ligne][index_nombre] = float(nombre)

    # Calcul des propriétés de l'eau à une température donnée
    # 1. Trouve l'élément le plus proche
    diff = [data[0] for data in base_de_donnee]

    for index, nombre in enumerate(diff):
        diff[index] = abs(float(nombre) - temperature)

    minimum = trouver_deux_nb_min(diff)
    ref_1, ref_2 = None, None
    for index, nombre in enumerate(diff):
        if nombre == minimum[0] or nombre == minimum[1]:
            if ref_1 is None:
                ref_1 = base_de_donnee[index]
            elif ref_2 is None:
                ref_2 = base_de_donnee[index]

    # 2. Calcule la valeur intermédiaire par interpolation. On assume que la
    # température est toujours entre 0 et 40 inclusivement.
    if 0 < temperature < 40:
        rho = inter_lin(temperature, ref_1[0], ref_1[1], ref_2[0], ref_2[1])
        mu = inter_lin(temperature, ref_1[0], ref_1[2], ref_2[0], ref_2[2])
        return rho, mu
    else:
        return None


def regime_stockes(diametre_particule, rho_particule, rho_eau, mu_eau):
    # À compléter
    if mu_eau:
        dp = diametre_particule
        rho_p = rho_particule
        V = g * (dp ** 2) * (rho_p - rho_eau) / (mu_eau * 18)
        Rep = nb_reynold(dp, V, rho_eau, mu_eau)

        if Rep is None or not Rep:
            return None
        Cd = 24 / Rep

        if not Cd:
            return None
        return V, Cd, 24 / Cd
    return None


def regime_intermediaire(Rep, diametre_particule,
                         rho_particule, rho_eau, mu_eau):
    # À compléter
    if Rep and 0.3 < Rep <= 1000 and mu_eau and rho_eau:
        dp = diametre_particule
        rho_p = rho_particule
        Cd = (24 / Rep) * (1 + 0.14 * (Rep ** 0.7))
        if not Cd:
            return None

        V = (4 * g * dp * (rho_p - rho_eau) / (rho_eau * 3 * Cd)) ** (1/2)
        Rep = nb_reynold(dp, V, rho_eau, mu_eau)
        return V, Cd, Rep
    return None


def calcule_vitesse(rho_particule, diametre_particule, temperature_eau):
    dp = diametre_particule
    rho_p = rho_particule
    if proprietes_eau(temperature_eau) is None:
        return None

    rho_eau, mu_eau = proprietes_eau(temperature_eau)
    # À compléter
    print("\nRégime de Stockes")
    result = regime_stockes(dp, rho_p, rho_eau, mu_eau)

    if result is None:
        return None

    texte = "V={:.3f}, Cd={:.3f}, Rep={:.3f}"
    print(texte.format(result[0], result[1], result[2]))

    if result[2] >= 0.3:
        print("Régime intermédiaire")
        last_speed = None

        while last_speed is None or abs(last_speed - result[0]) > 0.001:
            last_speed = result[0]
            result = regime_intermediaire(result[2], dp,
                                          rho_p, rho_eau, mu_eau)

            if result is None:
                return None

            print(texte.format(result[0], result[1], result[2]))

    return result[0]


if __name__ == "__main__":
    rho_particule = 2000  # kg/m^3
    diametre_particule = 1.0e-3  # m

    temperature_eau = 14.3  # degres celsius

    vitesse_particule = calcule_vitesse(rho_particule, diametre_particule,
                                        temperature_eau)
