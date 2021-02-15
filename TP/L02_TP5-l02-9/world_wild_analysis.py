import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio


def summary_analyse_data(df):
    # TO DO: plot the 10 countries with the highest number of confirmed, deaths, active, closed, recovered,
    # and mortality rate
    # Étape 1: Créer des subfigure de 3 lignes et 2 colonnes de dimension 15*15 en utilisant la bibliothèque matplotlib
    # https://matplotlib.org/3.1.0/gallery/subplots_axes_and_figures/subplots_demo.html

    # Étape 2:  dessiner sur chaque subplot les 10 pays les plus toucher par la Covid_19 selon le nombre de cas confirmés,
    # mort, actif, fermé et rétabli ainsi que le taux de mortalité en utilisant la bibliothèque seaborn.
    # https://seaborn.pydata.org/generated/seaborn.barplot.html
    fig, axs = plt.subplots(3, 2, figsize=(15, 15))
    for index, case in enumerate(df.columns):
        i, j = index // 2, index % 2
        data = df.nlargest(10, case)
        sns.barplot(x=case, y=data.index, data=data.head(10), ax=axs[i, j])
        axs[i, j].set_xlabel(f'Number of {case} cases')
        axs[i, j].set_title(f'Top 10 countries as per number of {case} cases')
    fig.tight_layout(pad=3.0)
    # fig.show()
    plt.savefig('Image/fig_01.png', dpi=600, format='png')


def summary_secteur(df):
    # TO DO: Plot le pourcentage mondial des cas confirmés par pays
    # Étape 1: Créer une base de données avec les pays qui ont un pourcentage de cas confirmé
    # supérieur ou égale à 2% des nombres de cas confirmé dans le monde.
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html

    # Étape 2: Créer une base de données avec les pays qui ont un pourcentage de cas confirmé
    # inférieur à 2% des nombres de cas confirmé dans le monde.
    # Cette base de données doit contenir une seule ligne représentant la somme de tous les cas
    # dans les pays ayant un pourcentage de cas confirmé inférieur à 2% dont le nom sera "Others"
    # https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/

    # Étape 3: Concaténer les deux bases de données créées précédemment
    # https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html

    # Étape 4: Dessiner le pourcentage mondial des cas confirmés par pays en utilisant la bibliothèque plotly.express
    # https://plotly.com/python/pie-charts/
    major = df.loc[df["Confirmed"] >= df["Confirmed"].sum() * 0.02]
    major = major[["Country_Region", "Confirmed"]]
    data = [["Others", df["Confirmed"].sum() - major["Confirmed"].sum()]]
    others = pd.DataFrame(data, columns=["Country_Region", "Confirmed"])
    result = pd.concat([major, others])
    labels, values = result["Country_Region"], result["Confirmed"]
    fig = px.pie(names=labels, values=values, hole=.4, color_discrete_sequence=px.colors.sequential.RdBu)
    fig.update_layout(title_text="Confirmed")
    fig.update_traces(textposition="inside")
    fig.show()
    pio.write_image(fig, 'Image/fig_02.png', width=1000, height=500)


def countries_bar(df, countries):
    # TO DO: plot pour certains pays le nombre de cas confirmés, morts, actifs, fermés et rétablis
    # Étape 1: soustraire les données des pays reçus en paramètre

    # Étape 2: TO DO: Retirer la colonne "Mortality_Rate"

    # Étape 3: Créer une figure en utilisant la bibliothèque plotly.graph_objects
    # https://plotly.com/python/subplots/
    data = df.loc[sorted(countries)]
    data = data.drop(columns="Mortality_Rate")
    fig = go.Figure()
    for case in data.columns:
        fig.add_trace(go.Bar(name=case, x=data.index, y=data[case]))

    fig.update_layout(yaxis=dict(title='Cases', titlefont_size=16, tickfont_size=14), xaxis_tickfont_size=14,
                      barmode='group', bargap=0.15, bargroupgap=0.1, legend=dict(x=0.01, y=0.99),
                      legend_orientation="h")
    fig.show()
    pio.write_image(fig, 'Image/fig_03.png', width=1000, height=500)
    
