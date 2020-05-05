from web.Function.data import data, pd, valeurGlobal, dataGraphByCategorie, sns

# AGAIN

# 4
# Utilisez la fonction distplot pour tracer l'histogramme de la
# *valeur globale. Essayez de jouer avec les paramètres hist, bins et kde.

# 4.1 Donnez deux exemples de données quantitatives et deux exemples de
#     *données catégorielles. Vous pouvez vous baser avec la colonne Overall
#     *par exemple du fichier data.cvs
def dataframeByCategoriesAndQuantitative():
    table0 = dataGraphByCategorie(data,'Overall')
    imgOverall = "/static/images/overall.png"

    table = table0.dropna()
    snsDistplot = sns.distplot(table)
    fig = snsDistplot.get_figure()
    fig.savefig("web" + imgOverall)

    return {
        'dataFrame': table,
        'imgLink': imgOverall
    }

# 4.2 Utilisez pandas pour obtenir la moyenne, la médiane, l'écart-type et la
#     *plage de la valeur globale.
def statsByParams(dataframe):
    stats = valeurGlobal(dataframe)
    return pd.DataFrame(stats, index=[0])
