import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import plotly.graph_objects as go
import PIL 
import io
import plotly.io as pio

COLOR = ["blue", "red", "green", "gray", "orange"]


def world_map(dict_df, case_type, word_pic):
    world = gpd.read_file(word_pic)

    world.replace("Brunei Darussalam", "Brunei", inplace=True)
    world.replace("Cape Verde", "Cabo Verde", inplace=True)
    world.replace("Congo", "Congo (Brazzaville)", inplace=True)
    world.replace("Democratic Republic of the Congo", "Congo (Kinshasa)", inplace=True)
    world.replace("Czech Republic", "Czechia", inplace=True)
    world.replace("Swaziland", "Eswatini", inplace=True)
    world.replace("Iran (Islamic Republic of)", "Iran", inplace=True)
    world.replace("Korea, Republic of", "Korea, South", inplace=True)
    world.replace("Libyan Arab Jamahiriya", "Libya", inplace=True)
    world.replace("Republic of Moldova", "Moldova", inplace=True)
    world.replace("Syrian Arab Republic", "Syria", inplace=True)
    world.replace("Taiwan", "Taiwan*", inplace=True)
    world.replace("United States", "US", inplace=True)
    world.replace("United Republic of Tanzania", "Tanzania", inplace=True)
    world.replace("The former Yugoslav Republic of Macedonia", "North Macedonia", inplace=True)
    world.replace("Lao People's Democratic Republic", "Laos", inplace=True)
    world.replace("Palestine", "West Bank and Gaza", inplace=True)
    world.replace("Holy See (Vatican City)", "Holy See", inplace=True)
    world.replace("Viet Nam", "Vietnam", inplace=True)

    merge = world.join(dict_df[case_type], on="NAME", how="right")
    image_frame = []

    for dates in merge.columns.to_list()[2:10]:
        ax = merge.plot(column=dates, cmap="OrRd", figsize=(15, 5), scheme="user_defined",
                        classification_kwds={"bins": [10, 100, 1000, 10000, 100000, 1000000, 10000000]},
                        legend=True, edgecolor="black", linewidth=0.6)
        ax.set_title(f"Total {case_type} Covid19 Cases:   {dates}", fontdict={"fontsize": 20}, pad=12.5)
        ax.set_axis_off()
        ax.get_legend().set_bbox_to_anchor((0.18, 0.6))

        img = ax.get_figure()

        plt.close()
        f = io.BytesIO()
        img.savefig(f, format="png")
        f.seek(0)
        image_frame.append(PIL.Image.open(f))

    image_frame[0].save("Image/" + case_type + ".gif", format="GIF", append_images=image_frame[1:],
                        save_all=True, duration=4, loop=0)


def world_cases(dict_df):
    # TO DO: visualiser l’évolution du nombre cumulé des cas confirmés, rétablis, morts, actifs et fermés dans le monde.
    # Étape 1: Créer une figure en utilisant la bibliothèque plotly.graph_objects

    # Étape 2: Pour chacune des clés du dictionnaire dict_df visualiser l’évolution du nombre cumulé
    fig = go.Figure()
    for index, key in enumerate(dict_df):
        fig.add_trace(go.Scatter(name=key, x=dict_df[key].columns, y=dict_df[key].sum(),
                      mode="lines", line=dict(width=5, color=COLOR[index])))
    fig.update_layout(xaxis=dict(dtick="M1"))
    fig.update_layout(title='Worldwide COVID-19 Cases', xaxis_tickfont_size=14, yaxis=dict(title='Number of Cases'),
                      legend=dict(y=0.99, x=0.01), legend_orientation="h")
    fig.show()
    pio.write_image(fig, 'Image/fig_04.png', width=1000, height=500)


def daily_plot_countries(dict_df, countries):
    # TO DO: visualiser l’évolution journalière du nombre cumulé des cas confirmés, morts, actifs et fermés pour un
    # certains nombres de pays sélectionner.
    # Étape 1: Créer des subfigure de 2 lignes et 2 colonnes de dimension 17*10

    # Étape 2: Pour chacune des clés du dictionnaire dict_df visualiser l’évolution du nombre de cas pour chaque
    # Pays de countries

    # Étape 3: Pour chaque pays de countries afficher un petit sommaire du nombre total des cas confirmés, morts,
    # actifs et fermés
    cases = ["Confirmed", "Deaths", "Active", "Closed"]
    fig, axs = plt.subplots(2, 2, figsize=(17, 10))
    for index, case in enumerate(cases):
        i, j = index // 2, index % 2
        axs[i, j].set_title(f"Daily increase in {case} cases")
        axs[i, j].set_ylabel("Number Of Cases")
        axes = [axs[0, 0], axs[0, 1], axs[1, 0], axs[1, 1]]
        dict_df[cases[index]].plot(y=countries, ax=axes[index], use_index=True, linewidth=4)
        axs[i, j].legend(loc="upper left")

    for country in countries:
        print('\n\n' + '\033[1m' + f"{country} Covid_19 Statistics:" + '\033[0m')

        for case in dict_df:
            print(f"Total number of {case} cases : {dict_df[case][country][-1]}")

    fig.show()
    plt.savefig('Image/fig_05.png', dpi=600, format='png')


def week_of_year(df):
    # TO DO: grouper les clés du dictionnaire dict_df par numéro de semaine
    # Étape 1: ajouter une colonne "WeekofYear" a la base de données df
	# https://www.geeksforgeeks.org/python-pandas-datetimeindex-weekofyear/

    # TO DO: créer une nouvelle base de données week_df avec les mêmes colonnes que df

    # Étape 2: Pour toutes les semaines de la base de données calculer la somme des cas de cette semaine pour remplir
    # la base de données week_df
    # Exemple:
    # Jour 1: 10 cas ==> semaine 1
    # Jour 2: 30 cas ==> semaine 1
    # Jour 3: 40 cas ==> semaine 1
    # Jour 4: 20 cas ==> semaine 1
    # Jour 5: 50 cas ==> semaine 1
    # Jour 6: 80 cas ==> semaine 1
    # Jour 7: 70 cas ==> semaine 1
    # ==> semaine 1: 300 cas

    # Étape 3: regrouper la base de données week_df par "WeekofYear"
    df = df - df.shift(fill_value=0)
    df.insert(len(df.columns), "WeekofYear", df.index.isocalendar().week)
    week_df = df.groupby("WeekofYear").sum()
    return week_df.head(-1)


def weekly_bar(dict_df, country):
    # TO DO: visualiser l’évolution hebdomadaire des cas confirmés, morts, actifs et fermés pour un de pays.
    # Étape 1: Pour l'ensemble des clés du dictionnaire dict_df regrouper les bases de donner par "WeekofYear" pensez a
    # utiliser la fonction week_of_year implémenter précédemment.

    # Étape 2: Créer des subfigure de 2 lignes et 2 colonnes de dimension 15*10

    # Étape 3: Pour chacune des clés du dictionnaire dict_df visualiser l’évolution hebdomadaire

    cases = ["Confirmed", "Deaths"]
    week_df = {key: week_of_year(item) for key, item in dict_df.items()}
    fig, axs = plt.subplots(2, 1, figsize=(15, 10))
    for index, case in enumerate(cases):
        sns.barplot(x=week_df[case].index, y=week_df[case][country], ax=axs[index])
        axs[index].set_xlabel(f'Year Week Number')
        axs[index].set_ylabel(f'Number Of {case} Cases')
        axs[index].set_title(f'Didtribution plot for {case} cases in {country}')
        axs[index].xaxis.set_major_locator(ticker.IndexLocator(base=5, offset=0.4))
        axs[index].xaxis.set_major_formatter(ticker.FuncFormatter(lambda x: int(x)))
    fig.show()
    plt.savefig('Image/fig_06.png', dpi=600, format='png')
