import pandas as pd


def load_df(add_death_df, add_confirmed_df, add_recovered_df, add_summary_df):
    # TO DO: Lire les bases de données à partir des liens URL reçus en paramètres
    return [pd.read_csv(add_death_df), pd.read_csv(add_confirmed_df),
            pd.read_csv(add_recovered_df), pd.read_csv(add_summary_df)]


def summary_add_col(df, col, value):
    # TO DO: Ajouter une colonne à la base de données df reçue en paramètre (deux lignes)
    # le nom et la valeur de cette colonne se trouvent respectivement dans les variables col et value.
    df.insert(len(df.columns), col, value)
    return df


def summary_extract_col(df, cols):
    # TO DO: Extraire les colonnes reçues en paramètre désirer de la base de données df (une seul ligne)
    return df[cols]


def summary_by_country(df):
    # TO DO: Grouper le DataFrame par Country_Region (une seule ligne). Utiliser la méthode groupby()
    return df.groupby("Country_Region").sum()


def creat_dict_df(death_df, confirmed_df, recovered_df):
    # TODO: Créer un dictionnaire avec des bases de données reçues en paramètre (une seule ligne)
    return {"Deaths": death_df, "Confirmed": confirmed_df, "Recovered": recovered_df}


def dict_remove_col(dict_df, cols):
    # TO DO: Supprimer des colonnes cols du dictionnaire dict_df (une seule ligne) 
    # les colonnes doivent être supprimées de l’ensemble des clés du dictionnaire
    return {name: data_frame.drop(columns=cols) for name, data_frame in dict_df.items()}


def dict_by_country(dict_df):
    # TO DO: Grouper le dictionnaire dict_df par Country/Region pour toutes les clés du dictionnaire
    # et changer les colonnes en datetime, utiliser le lien suivant pour plus d'information
    # https://pandas.pydata.org/pandas-docs/version/0.20/generated/pandas.to_datetime.html
    new_dict = {}
    for name, data_frame in dict_df.items():
        new_dict[name] = data_frame.groupby("Country/Region").sum()
        new_dict[name].columns = pd.to_datetime(new_dict[name].columns)  # , errors='ignore').date

    return new_dict


def dict_add_key(dict_df):
    # TO DO: Ajouter les clés Active case et Closed Case a votre dictionnaire de DataFrame
    # les cles du dictionnaire doivent être triés comme suit:{"Confirmed", "Deaths", "Active", "Closed", "Recovered"}
    dict_df['Closed'] = dict_df["Deaths"] + dict_df["Recovered"]
    dict_df['Active'] = dict_df["Confirmed"] - dict_df["Closed"]
    return {key: dict_df[key] for key in ["Confirmed", "Deaths", "Active", "Closed", "Recovered"]}


def dict_by_day(dict_df):
    # TO DO: Grouper le dictionnaire de DataFrame par date (une seule ligne)
    # Utiliser le lien suivant:
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.transpose.html
    return {key: dataframe.T for key, dataframe in dict_df.items()}


def basic_inf_summary(summary_df):
    # TO DO: Afficher les informations suivantes: Somme des nombres de cas confirmé,
    # active, fermée, mort et rétabli dans le monde.
    order = ["Confirmed", "Recovered", "Deaths", "Active", "Closed"]
    sum_df = summary_df.sum()
    print("\n\n" + '\033[1m' + 'Basic Information:' + '\033[0m')
    for case in order:
        print(f"Total number of {case} cases around the world {sum_df[case]}")
