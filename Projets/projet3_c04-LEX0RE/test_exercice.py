import unittest
import exercice as ex


class TestExercice(unittest.TestCase):

    def setUp(self):
        self.negative = list(range(-10, 1))
        self.true_temp = list(range(1, 40))
        self.false_temp = list(range(40, 50))

    def test_proprietes_eau(self):
        for n in self.negative:
            self.assertIsNone(ex.proprietes_eau(n))
        for n in self.true_temp:
            self.assertIsNotNone(ex.proprietes_eau(n))
        for n in self.false_temp:
            self.assertIsNone(ex.proprietes_eau(n))

    def test_regime_stockes(self):
        dp, rho_p, rho_eau, mu = 1, 2, 3, 0
        self.assertIsNone(ex.regime_stockes(dp, rho_p, rho_eau, mu))
        mu = 4
        self.assertIsNotNone(ex.regime_stockes(dp, rho_p, rho_eau, mu))

    def test_regime_intermediaire(self):
        Rep, dp, rho_p, rho_eau, mu_eau = 1, 1, 1, 1, 1
        self.assertIsNotNone(ex.regime_intermediaire(Rep, dp, rho_p,
                                                     rho_eau, mu_eau))
        mu_eau = 0
        self.assertIsNone(ex.regime_intermediaire(Rep, dp, rho_p,
                                                  rho_eau, mu_eau))
        mu_eau = 1
        rho_eau = 0
        self.assertIsNone(ex.regime_intermediaire(Rep, dp, rho_p,
                                                  rho_eau, mu_eau))
        rho_eau = 1
        Rep = -1
        self.assertIsNone(ex.regime_intermediaire(Rep, dp, rho_p,
                                                  rho_eau, mu_eau))
        Rep = 1111
        self.assertIsNone(ex.regime_intermediaire(Rep, dp, rho_p,
                                                  rho_eau, mu_eau))
        Rep = 300
        self.assertIsNotNone(ex.regime_intermediaire(Rep, dp, rho_p,
                                                     rho_eau, mu_eau))

    def test_calcule_vitesse(self):
        rho_p = 2000
        dp = 1.0e-3
        t_eau = 14.3
        self.assertAlmostEqual(ex.calcule_vitesse(rho_p, dp, t_eau), 0.108, 0)
        dp = 0.00001
        self.assertIsNotNone(ex.calcule_vitesse(rho_p, dp, t_eau))
        t_eau = 0
        self.assertIsNone(ex.calcule_vitesse(rho_p, dp, t_eau))
        t_eau = 14.3


if __name__ == '__main__':
    unittest.main()
