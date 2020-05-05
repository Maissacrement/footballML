from web.Function.data import data, pd, plt, sns, dataGraphByCategorie
from web.Function.nationalityFilter import nationality

# AGAIN

# 6
# Utilisez la fonction barplot pour représenter la valeur potentielle par
# *rapport à la nationalité pour : French, Italie, Espagne, Brésil,
# *Argentine, Argentine, Allemagne, Angleterre

# Quel est le pays qui possède le plus fort potentiel ?
# *Les paramètres des instructions peuvent être Nationality,
# *Potentiel et Countries?
def genBarplotPotentialByNationality():
    potentialImgPath = "/static/images/potentialByNationality.png"
    labels=["Nationality", "Potential"]

    nationality.FontSize = 10
    barplot = sns.barplot(x=labels[0], y=labels[1], data=nationality)
    barplot.set_xticklabels(
        barplot.get_xticklabels(), rotation=15,
        fontsize='large', horizontalalignment='right'
    )
    fig = barplot.get_figure()
    fig.savefig("web" + potentialImgPath)

    return {
        'dataFrame': dataGraphByCategorie(nationality, labels[0], labels[1]),
        'imgLink': potentialImgPath
    }
