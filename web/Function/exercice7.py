from web.Function.data import data, pd, plt, sns, dataGraphByCategorie
from web.Function.nationalityFilter import nationality

# AGAIN

# 7
# Utilisez la fonction Scatter pour dessiner le diagramme de dispersion
# *du potentiel par rapport au pays du joueur pour les pays choisis :
# *France, Italie, Espagne, Brésil, Argentine, Argentine, Allemagne, Angleterre

def genScatterPotentialByNationality():
    potentialImgPath = "/static/images/scatterPotentialByNationality.png"
    labels=["Nationality", "Potential"]

    plt.figure(figsize=(20, 7)) # New window
    scatter = plt.scatter(x=labels[0], y=labels[1], data=nationality)
    fig = scatter.get_figure()
    fig.savefig("web" + potentialImgPath)

    return {
        'dataFrame': dataGraphByCategorie(nationality, labels[0], labels[1]),
        'imgLink': potentialImgPath
    }
