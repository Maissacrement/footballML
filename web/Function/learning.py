from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sns
from web.Function.data import data, pd, dataGraphByCategorie
import numpy as np

#Init
knn=KNeighborsClassifier()

def cleanSymboleToNumber(table, *labels):
    dot = None

    for label in labels:
        table = table[table[label] != '€0'] # Remove
        dot = table[table[label].str.contains('.')]
        dot.replace(['$'],['0'],inplace=True, regex=True)
        dot.replace(['\.'],[''],inplace=True, regex=True)
        dot.replace(['€','K', 'M'],['','000', '000000'],inplace=True, regex=True)

    return dot

def valuesAsWage(knn, wage=10000):
    x = np.array([[wage]]) # 2D Array

    return knn.predict(x)

def saveToPng(url, title, df):
    plt.figure(figsize=(20, 20)) # New window
    scatter = plt.scatter(x=df['Wage'].values, y=df['Value'].values, s=0.5, alpha=0.5)
    plt.xticks(
        rotation=90, horizontalalignment='right',
        fontweight=2, fontsize=8
    )
    plt.yticks(
        rotation=0,
        fontweight=2, fontsize=8
    )
    plt.tick_params(axis='x', pad=10)
    plt.tick_params(axis='y', pad=20)
    plt.title(title)

    fig = scatter.get_figure()
    fig.savefig("web" + url)


def learning():
    learningImgPath = "/static/images/learning.png"

    # Importé le csv avec pandas
    table = dataGraphByCategorie(data, 'Value', 'Wage')

    # Data cleaning
    table = table.dropna()
    cleanedTab = cleanSymboleToNumber(table, 'Value', 'Wage')
    saveToPng(
        learningImgPath, "IA",
        cleanedTab
    )
    #print('cleaned: ', cleanedTab)

    #prix
    y1= cleanedTab['Value']
    x1= cleanedTab.drop('Value', axis=1)

    #model
    knn.fit(x1, y1)
    score = knn.score(x1, y1) # estimate

    # first learning
    knn.predict(x1)

    return {
        'knn': knn,
        'tab': cleanedTab,
        'fiabilite': score,
        'url': learningImgPath
    }
