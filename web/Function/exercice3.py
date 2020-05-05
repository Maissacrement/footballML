from web.Function.data import data, pd, typeAndAttributeOfDataframe

# 3
# Donner l’instruction pour afficher les types et attributs de
# *la variable data crée en question 1.2.
def renderTypeAndAttribute():
    # create a pandas Series
    filteredSerie = typeAndAttributeOfDataframe(data)
    df = pd.DataFrame(filteredSerie)

    return {
        'dataFrame': df,
        'labels': ['Attributs', 'Type']
    }
