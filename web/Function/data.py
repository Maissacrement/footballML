import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy
import io

# 1
# Importation du CSV et initialisation de la variable data
data = pd.read_csv('./web/csv/data.csv')

"""
    @params:
        - data: Dataframe
    return:
        - tab : Pandas.Series
"""
def typeAndAttributeOfDataframe(df):
    # afficher les types et attributs de la variable data
    #info = data.info() # Print columns type
    labels, contents = [], []
    # df.items() me permet d'acceder aux colonnes et au type
    for label, content in df.items():
        labels.append(label)
        contents.append(content.dtype)

    labels[0] = 'Index'
    tab0 = pd.Series(contents, index=[numpy.arange(len(contents))])
    tab1 = pd.Series(labels, index=[numpy.arange(len(labels))])

    tab = pd.concat([tab0, tab1], axis=1)

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

    return value

"""
    @params:
        - dataframe: Dataframe
    return:
        - Obj : {
            'max': Float,
            'moy': Float,
            'ecartType': Float
        }
"""
def valeurGlobal(overallDataframe):
    # Utilisez pandas pour obtenir la moyenne, la médiane,
    # l'écart-type et la plage de la valeur globale.
    return {
        'max': overallDataframe.max().values[0],
        'moy': overallDataframe.mean().values[0],
        'ecartType': overallDataframe.std().values[0]
    }

def objectToDataframe(object, index=1):
    if(type(object) == int and index > 0):
        return pd.DataFrame(object, index=[x for x in range(index)])
    else:
        return pd.DataFrame(object, index=[x for x in range(1)])
