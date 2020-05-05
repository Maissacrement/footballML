# Initialisation de pandas, seaborn et matplotlib.pylot.
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import io

print("1.1 Initialisation l'environnement pandas, seaborn et matplotlib.pylot.")

#Init
knn=KNeighborsClassifier()

def writeAResponse(df, filename):
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    with open(filename, "w", encoding="utf-8") as f:
        f.write(s)

"""
    @params:
        - data: Dataframe
    return:
        - tab : Pandas.Series
"""
def typeAndAttributeOfDataframe(data):
    # afficher les types et attributs de la variable data
    #info = data.info()
    #print(data[0:2]._data)
    #writeAResponse(data, "csv/df_info.txt")
    labels, contents = [], []
    for label, content in data.items():
        labels.append(label)
        contents.append(content.dtype)

    labels[0] = 'Index'
    tab = pd.Series(contents, index=labels)

    #print(tab)
    #print(data.info())

    return tab


"""
    @params:
        - dataframe: Dataframe
        - *categorieName: String
    return:
        - tab : Pandas.Series
"""
def dataGraphByCategorie(dataframe, *categorieName):
    categories = []
    value = None
    if(len(categorieName) > 0):
        for arg in categorieName:
            categories.append(arg)

        value = dataframe[0:][categories]
    else:
        value = dataframe[0:][categorieName]

    print(value)

    return value

def data():
    plt.figure(figsize=(20,7))
    #countplot
    #set_xticklabeks,

def valeurGlobal(overallDataframe):
    # Utilisez pandas pour obtenir la moyenne, la médiane,
    # l'écart-type et la plage de la valeur globale.
    return {
        'max': overallDataframe.max().values[0],
        'moy': overallDataframe.mean().values[0],
        'ecartType': overallDataframe.std().values[0]
    }

def cleanSymboleToNumber(table, *labels):
    dot = None

    for label in labels:
        dot = table[table[label].str.contains('.')]
        dot.replace(['$'],['0'],inplace=True, regex=True)
        dot.replace(['\.'],[''],inplace=True, regex=True)
        dot.replace(['€','K', 'M'],['','000', '000000'],inplace=True, regex=True)

    return dot

def valuesAsWage(knn, wage=10000):
    x = np.array([[wage]]) # 2D Array

    return knn.predict(x)

def main():
    # 1
    # Importation du CSV et initialisation de la variable data
    data = pd.read_csv('./web/csv/data.csv')

    # 2 

    dataframeResume = typeAndAttributeOfDataframe(data)
    #print(dataframeResume)
    table = dataGraphByCategorie(data,'Overall')
    table.dropna()

    # 4
    print("Valeur gloabl: ", valeurGlobal(table))
    sns.distplot(table)
    #plt.gca().set(title='Frequency Histogram', ylabel='Frequency');
    #sns.set();
    #table.plot(kind='hist')
    #sns.distplot(table[0:], bins=table, kde=True, hist=True)
    #plt.show()
    #print(table)

    # 5
    # 5.1 Quel pays compte le plus grand nombre de joueurs ?
    #     *Que pouvez-vous conclure de la valeur globale ?
    plt.figure(figsize=(20,7))
    nationalityDataframe = pd.value_counts(data['Nationality'])
    maxNbOfPlayer = nationalityDataframe[nationalityDataframe == nationalityDataframe.max()]
    print('5.1 Le pays avec le plus grand nombre de joueur est',
        maxNbOfPlayer.index.values[0] , 'avec',
        maxNbOfPlayer.values[0], 'joueurs'
    )

    #6
    po = data[data["Nationality"].isin(["England", "France", "Italy", "Spain", "Brazil", "Argentina", "Germany"])]
    po.FontSize = 10
    #po = data[data["Nationality"].isin(['Germany'])]
    #print('test: ', po['Nationality'])

    # Quel est le pays qui possède le plus fort potentiel ? Les paramètres des instructions peuvent être Nationality, Potentiel et Countries?
    #Countries n'existe pas? Country ≈ Nationality

    #sns.countplot(x="Nationality", data=po)
    potential = pd.value_counts(data['Potential'])
    #print(potential)
    #print(len(potential.values))
    #print(data["Nationality"].values)

    langs = data["Nationality"][1:]
    potentials = data["Potential"][1:]
    #data['Nationality'].plot.bar(y=potentials)
    p = sns.barplot(x="Nationality", y="Potential", data=po)
    p.set_xticklabels(p.get_xticklabels(), rotation=0, fontsize='large', horizontalalignment='right')

    # 7
    # Utilisez la fonction Scatter pour dessiner le diagramme de dispersion du potentiel par rapport
    # au pays du joueur pour les pays choisis : France, Italie, Espagne, Brésil, Argentine, Argentine, Allemagne, Angleterre

    plt.figure(figsize=(20, 7)) # New window
    plt.scatter(x="Nationality", y="Potential", data=po)#,hue=['France','Spain','England','Italy','Brazil','Argentina','Germany'])
    #RegularPolyCollection( rotation=90, horizontalalignment="right", fontweight='bold',fontsize='medium')
    #plt.title('Scatter plot')
    plt.show()

    #  Lorsque vous utilisez l'apprentissage supervisé pour résoudre un problème, nous introduisons des fonctions
    # *dans un algorithme d'apprentissage automatique. Cet algorithme apprend à prédire le bon résultat à partir
    # *de ces caractéristiques.

    #You must create a learning model from the analyses and the given file.

    # Q: Vous devez créer un modèle d'apprentissage à partir des analyses et du fichier donné pour apprendre à
    #   *trouver le prix et valeur des joueurs.
    table = dataGraphByCategorie(data, 'Value', 'Wage')

    # Data cleaning
    table.dropna()
    cleanedTab = cleanSymboleToNumber(table, 'Value', 'Wage')
    #print('cleaned: ', cleanedTab)

    #prix
    y1= cleanedTab['Value']
    x1= cleanedTab.drop('Value', axis=1)

    #model
    knn.fit(x1, y1)
    score = knn.score(x1, y1) # estimate

    # first learning
    knn.predict(x1)

    print('fiabilité', score)
    salaire_test = 251483
    print('ML: le prix du joueur pour un salaire de', salaire_test, 'euros sera de', valuesAsWage(knn, salaire_test)[0],'euros')

if __name__ == '__main__': main()
