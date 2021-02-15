#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import pandas as pd
from sklearn.model_selection import train_test_split


# TODO: Définissez vos fonctions ici
def preprocess_data(data_path: str = "./data/winequality-white.csv") -> tuple:
    df = pd.read_csv(data_path, sep=";", header=0)
    y = df["quality"]
    x = df.drop(columns=["quality"])

    return train_test_split(x, y, test_size=0.1)


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    X_train, X_test, y_train, y_test = preprocess_data()
