from web.Function.data import data, pd, plt, objectToDataframe

# AGAIN

#
# Il vous est demandé de faire un programme et des instructions pour
# *répondre aux questions suivantes

# 5.1 Quel pays compte le plus grand nombre de joueurs ?
#     *Que pouvez-vous conclure de la valeur globale ?
def highestNumberOfPlayersByNationality():
    nationalityDataframe = pd.value_counts(data['Nationality'])
    maxNbOfPlayer = nationalityDataframe[nationalityDataframe == nationalityDataframe.max()]

    return objectToDataframe({
        'name': maxNbOfPlayer.index.values[0],
        'value': maxNbOfPlayer.values[0]
    })

# 5.2 Quelle est la différence entre les countplots et les distplots ?
#     *Quand utilisons-nous l'une ou l'autre ?
def compareCountplotAndDisplot(dataframe):
    return "countplot nous permet d'observer \
            les données regrouper par colonne ou Categorie. \
            distplot nous permet par contre de grouper par effectif"
