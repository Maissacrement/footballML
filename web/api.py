#web/api.py
import pandas as pd
from flask import Flask, send_from_directory, request, render_template
from web.Function.exercice2 import getData
from web.Function.exercice3 import renderTypeAndAttribute
from web.Function.exercice4 import dataframeByCategoriesAndQuantitative, statsByParams
from web.Function.exercice5 import highestNumberOfPlayersByNationality
from web.Function.exercice6 import genBarplotPotentialByNationality
from web.Function.exercice7 import genScatterPotentialByNationality
from web.Function.learning import learning, valuesAsWage
import webbrowser
import json
import time
import os
SECRET_PORT = os.getenv("PORT")

"""
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
"""

app = Flask(__name__)
app.config['PORT'] = os.environ.get('PORT')
root = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def hello_world():
    print('My secret port', app.config['PORT'])
    data = getData()
    return render_template('index.html', data=data, exo='exo3')

@app.route('/exo2')
def exo2():
    data = getData()
    return render_template('index.html', data=data, exo='exo2')

@app.route('/exo3')
def exo3():
    data = renderTypeAndAttribute()
    return render_template('index.html', data=data['dataFrame'], labels=data['labels'], exo='exo3')

# Need return img
@app.route('/exo4')
def exo4():
    # Quantitative data[1:]
    # Categories
    data = dataframeByCategoriesAndQuantitative()
    dataframeStats = statsByParams(data['dataFrame'])

    return render_template('index.html',
        link=data['imgLink'], data=data['dataFrame'],
        resume=dataframeStats, exo='exo4'
    )

@app.route('/exo5')
def exo5():
    # comp sns.distplot et countplot
    playersDataframe = highestNumberOfPlayersByNationality()
    return render_template('index.html',
        data=playersDataframe, exo='exo2'
    )

@app.route('/exo6')
def exo6():
    # comp sns.distplot et countplot
    data = genBarplotPotentialByNationality()
    resume  = statsByParams(data['dataFrame'])
    #return send_from_directory(root, 'templates/exo4.html')

    return render_template('index.html',
        link=data['imgLink'], resume=resume,
        data=data['dataFrame'], exo='exo4'
    )

@app.route('/exo7')
def exo7():
    data = genScatterPotentialByNationality()
    resume  = statsByParams(data['dataFrame'])
    #return send_from_directory(root, 'templates/exo4.html')

    return render_template('index.html',
        link=data['imgLink'], resume=resume,
        data=data['dataFrame'], exo='exo4'
    )

@app.route('/learning')
def learn():
    modele = learning()
    dataIndex = ['score', 'prediction']

    id = request.args.get('id', default = 1, type = int)
    data = [ [modele['fiabilite'], valuesAsWage(modele['knn'], id)[0]] ]
    resume = pd.DataFrame(data,columns=dataIndex)

    return render_template('index.html',
        link=modele['url'], data=modele['tab'],
        resume=resume, exo='exo4'
    )

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

def runWebBrowser():
    new = 2
    url = "http://0.0.0.0:" + str(SECRET_PORT) + "/exo2"
    webbrowser.open(url, new=new) # Open my web browser

def main():
    time.sleep(1)
    runWebBrowser()

main()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
