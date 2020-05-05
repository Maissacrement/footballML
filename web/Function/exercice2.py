from web.Function.data import data

# 2
# Créer une page de vue des données en html. Vous pouvez limiter
# *votre page à quelques lignes

# Nous allons ici recuperer la données a insérer sur notre page html
def getData():
    # Filtered data
    return data.drop(data.columns[0], axis=1)

#renderCsvToHTML()
