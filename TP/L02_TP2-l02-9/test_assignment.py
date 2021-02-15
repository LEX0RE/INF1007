import math
import numpy as np
import os
import sys
import json
from mock import patch
from exercice1 import exercice1 as ex1
from exercice2 import exercice2 as ex2
from exercice3 import exercice3 as ex3
import exercice4 as ex4
from exercice5 import multiplierMatrices as multiplierMatrice
from exercice6 import createVocabulary as creerVocabulaire
import _thread
import threading
import unittest


# Timeout
def exit_function():
    _thread.interrupt_main()


def timeout(s):
    def outer(fn):
        def inner(*args, **kwargs):
            timer = threading.Timer(s, exit_function)
            timer.start()
            try:
                result = fn(*args, **kwargs)
            finally:
                timer.cancel()
            return result

        return inner

    return outer


class TestExercice1(unittest.TestCase):
    CONST_SIZE = 1000

    def test_tri_dix_elements(self):
        array = np.random.randint(-100, 100, 10)
        print(ex1(array))
        print(np.sort(array))
        isEqual = np.array_equal(np.sort(array), ex1(array))
        self.assertTrue(isEqual)

    def test_tri_complet(self):
        array = np.random.randint(-100, 100, self.CONST_SIZE)
        isEqual = np.array_equal(np.sort(array), ex1(array))
        self.assertTrue(isEqual)


class TestExercice2(unittest.TestCase):
    def test_paranthese_bien_1(self):
        self.assertEqual(ex2("()"), "(.)")

    def test_paranthese_bien_2(self):
        self.assertEqual(ex2("(()())"), "((.)(.))")

    def test_paranthese_bien_3(self):
        self.assertEqual(ex2("(())((()))()"), "((.))(((.)))(.)")

    def test_paranthese_bien_4(self):
        self.assertEqual(ex2("((((((()))))))"), "(((((((.)))))))")

    def test_non_parenthese_1(self):
        value_returned = str(ex2("(((")).lower()
        self.assertIn("corr", value_returned)

    def test_non_parenthese_2(self):
        value_returned = str(ex2(")))")).lower()
        self.assertIn("corr", value_returned)

    def test_non_parenthese_3(self):
        value_returned = str(ex2("((())")).lower()
        self.assertIn("corr", value_returned)

    def test_non_parenthese_4(self):
        value_returned = str(ex2("(()))")).lower()
        self.assertIn("corr", value_returned)


class TestExercice3(unittest.TestCase):
    CONST_GRAVITE = 9.81
    CONST_HAUTEUR = 100.5
    MAX_DIFF = 2  # si les etudiants font h > 0.01 ou h >= 0.01 on ne penalise pas

    def test_rebond_faible(self):
        self.generique_test(self.CONST_HAUTEUR, 0.2)

    def test_rebond_fort(self):
        self.generique_test(self.CONST_HAUTEUR, 0.7)

    def generique_test(self, hauteur_initiale, coefficient_rebond):
        nb_rebonds_attendu = self.verification(hauteur_initiale, coefficient_rebond)
        nb_rebonds_test = ex3(hauteur_initiale, coefficient_rebond)

        diff = abs(nb_rebonds_attendu - nb_rebonds_test)
        self.assertTrue(diff <= self.MAX_DIFF)

    def verification(self, hauteur_initiale, coefficient_rebond):
        h = hauteur_initiale
        nb_rebonds = 0
        while h > 0.01:
            v = math.sqrt(2 * self.CONST_GRAVITE * h)
            v *= coefficient_rebond
            h = v * v / (2 * self.CONST_GRAVITE)
            nb_rebonds += 1
        return nb_rebonds


class TestExercice4(unittest.TestCase):
    # 355 / 113 is a good approximation of PI so 355 / 133*4 is a good approx of PI/4
    IN_CIRCLE = 355 * 2
    ITERATIONS = 452 * 2
    counter = 1

    @timeout(1)
    def executerTest(self, fonction, nom_fonction):
        try:
            fonction()
        except KeyboardInterrupt:
            self.fail(
                f'L\'appel fonction {nom_fonction} ne se termine pas --> Verifiez vos boucles')
        except AssertionError as e:
            raise e

    def mockedRandom(self):
        if self.counter <= self.IN_CIRCLE:
            value = 0.5  # inside circle
        else:
            value = 0.0  # outside circle
        self.counter += 1
        return value

    def executer_pi(self):
        with patch('__main__.ex4.random', self.mockedRandom):
            self.assertAlmostEqual(ex4.exercice4()[0], 3.141, delta=0.001)

    def test_pie_is_well_aproximed(self):
        self.executerTest(self.executer_pi, "Approximer Pi")


class TestExercice5(unittest.TestCase):
    A = ([[1, 2], [1, 5]])
    B = ([[1, 2], [1, 6], [3, 8]])
    C = ([[1], [6]])

    def test_multyply_matrice_with_uncompatible_size_1(self):
        isEqual = np.array_equal(multiplierMatrice(self.A, self.B), [[0.0, 0.0], [0.0, 0.0]])
        self.assertTrue(isEqual)

    def test_multyply_matrice_with_uncompatible_size_2(self):
        isEqual = np.array_equal(multiplierMatrice(self.C, self.A), [[0.0, 0.0], [0.0, 0.0]])
        self.assertTrue(isEqual)

    def test_multyply_matrice_with_compatible_size_1(self):
        isEqual = np.array_equal(multiplierMatrice(self.B, self.A), [[3, 12], [7, 32], [11, 46]])
        self.assertTrue(isEqual)

    def test_multyply_matrice_with_compatible_size_2(self):
        isEqual = np.array_equal(multiplierMatrice(self.A, self.C), [[13], [31]])
        self.assertTrue(isEqual)


class TestExercice6(unittest.TestCase):

    @timeout(1)
    def executerTest(self, fonction, nom_fonction):
        try:
            fonction()
        except KeyboardInterrupt:
            self.fail(
                f'L\'appel fonction {nom_fonction} ne se termine pas --> Verifiez vos boucles')
        except AssertionError as e:
            raise e

    @staticmethod
    def create_new_vocab():
        new_mails = [{
            "mail": {
                "From": "GP@paris.com",
                "Date": "2004-08-15",
                "Body": [
                    "famili",
                    "subito",
                    "uncl",
                    "new",
                    "joint"
                ],
                "Spam": "true"
            }
        },
            {
                "mail": {
                    "From": "farmer@paris.com",
                    "Date": "2000-09-15",
                    "Body": [
                        "pleas",
                        "practition",
                        "new",
                        "marino",
                        "enrononlin",
                        "success",
                        "use"
                    ],
                    "Spam": "false"
                }
            },
            {
                "mail": {
                    "From": "kitchen@paris.com",
                    "Date": "2001-12-10",
                    "Body": [
                        "use",
                        "joint",
                        "success",
                        "portfolio",
                        "offic",
                        "use",
                        "america",
                        "tel",
                        "user"
                    ],
                    "Spam": "false"
                }
            },
            {
                "mail": {
                    "From": "SA_and_HP@paris.com",
                    "Date": "2005-07-18",
                    "Body": [
                        "guatemala",
                        "subito",
                        "postcard",
                        "famili",
                        "portfolio",
                        "electromagnet",
                        "subito",
                        "user"
                    ],
                    "Spam": "true"
                }
            }]
        with open('mails.json', 'w') as fp:
            json.dump(new_mails, fp, indent=4)

    def setUp(self):
        self.create_new_vocab()
        self.spam_ham_words = ["portfolio", "new", "user", "joint"]

        self.spam_words = {"subito": 0.23076923076923078, "guatemala": 0.07692307692307693,
                           "electromagnet": 0.07692307692307693}

        self.ham_words = {"practition": 0.0625, "marino": 0.0625}
        self.executerTest(creerVocabulaire, "Creer Vocabulaire")
        self.emails = {}
        with open("results.json") as json_data:
            self.emails = json.load(json_data)

        self.principal_keys = self.emails.keys()
        self.spam_dict = {}
        self.ham_dict = {}
        for element in self.principal_keys:
            if 'spam' in element.lower():
                self.spam_dict = self.emails[element]
            if 'ham' in element.lower():
                self.ham_dict = self.emails[element]

    def principal_keys_are_in_the_dict(self):
        ham_key = False
        spam_key = False
        for element in self.principal_keys:
            if 'ham' in element.lower():
                ham_key = True
            if 'spam' in element.lower():
                spam_key = True
        return ham_key and spam_key

    def spam_keys_are_in_dict(self):
        if not self.principal_keys_are_in_the_dict():
            return False
        spam_keys = self.spam_dict.keys()
        for element in self.spam_ham_words + list(self.spam_words.keys()):
            if element not in spam_keys:
                return False
        return True

    def ham_keys_are_in_dict(self):
        if not self.principal_keys_are_in_the_dict():
            return False
        ham_keys = self.ham_dict.keys()
        for element in self.spam_ham_words + list(self.ham_words.keys()):
            if element not in ham_keys:
                return False
        return True

    def test_principal_keys_are_in_dict(self):
        self.assertTrue(self.principal_keys_are_in_the_dict())

    def test_spam_keys_are_in_dict(self):
        self.assertTrue(self.spam_keys_are_in_dict())

    def test_ham_keys_are_in_dict(self):
        self.assertTrue(self.ham_keys_are_in_dict())

    def test_spam_keys_should_not_be_in_ham_dict(self):
        if not self.principal_keys_are_in_the_dict():
            self.assertTrue(False)
            return
        ham_keys = self.ham_dict.keys()
        for element in self.spam_words:
            key_not_exist = element not in ham_keys
            key_give_0_prop = False
            if element in ham_keys:
                key_give_0_prop = self.ham_dict[element] == 0
            self.assertTrue(key_give_0_prop or key_not_exist)

    def test_ham_keys_should_not_be_in_spam_dict(self):
        if not self.principal_keys_are_in_the_dict():
            self.assertTrue(False)
            return
        spam_keys = self.spam_dict.keys()
        for element in self.ham_words:
            key_not_exist = element not in spam_keys
            key_give_0_prop = False
            if element in spam_keys:
                key_give_0_prop = self.spam_dict[element] == 0
            self.assertTrue(key_give_0_prop or key_not_exist)

    def test_spam_prob_are_correct(self):
        if not self.spam_keys_are_in_dict():
            self.assertTrue(False)
            return
        for element in self.spam_words:
            self.assertAlmostEqual(self.spam_dict[element], self.spam_words[element], places=9)

    def test_ham_prob_are_correct(self):
        if not self.ham_keys_are_in_dict():
            self.assertTrue(False)
            return
        for element in self.ham_words:
            self.assertAlmostEqual(self.ham_dict[element], self.ham_words[element], places=9)


if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)
