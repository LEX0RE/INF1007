#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.linspace(-1.3, 2.5, 64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    return [(np.linalg.norm(c), np.arctan2(c[1], c[0])) for c in cartesian_coordinates]


def find_closest_index(values: np.ndarray, number: float) -> int:
    return np.abs(values - number).argmin()


def create_graph() -> None:
    x = np.linspace(-1, 1, 250)
    y = (x ** 2) * np.sin(1 / (x ** 2)) + x
    plt.scatter(x, y, label="scatter")
    plt.plot(x, y, label="line", color="r")
    plt.ylabel('y')
    plt.ylabel('x')
    plt.xlim((-1, 1))
    plt.title("y = x² * sin(1/x²) + x")
    plt.legend()
    plt.show()


def monte_carlo(iteration: int=5000) -> float:
    x_inside_dots = []
    y_inside_dots = []
    x_outside_dots = []
    y_outside_dots = []
    for i in range(iteration):
        x = np.random.random()
        y = np.random.random()
        if np.linalg.norm((x, y)) < 1:
            x_inside_dots.append(x)
            y_inside_dots.append(y)
        else:
            x_outside_dots.append(x)
            y_outside_dots.append(y)
    
    plt.scatter(x_inside_dots, y_inside_dots, label="inside dot")
    plt.scatter(x_outside_dots, y_outside_dots, label="outside dot")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

    return ((len(x_inside_dots)) / iteration) * 4


def integrate_and_plot() -> tuple:
    result_inf = integrate.quad(lambda x: np.exp(-x ** 2), -np.inf, np.inf)

    x = np.arange(-4, 4, 0.1)
    y = [integrate.quad(lambda x: np.exp(-x ** 2), 0, value)[0] for value in x]
    
    plt.plot(x, y, label="Fonction")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    return result_inf

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(linear_values())
    print(coordinate_conversion(np.array([(0, 0), (10, 10)])))
    print(find_closest_index(np.array([0, 5, 10, 12, 8]), 10.5))
    create_graph()
    print(monte_carlo())
    integrate_and_plot()
    pass
