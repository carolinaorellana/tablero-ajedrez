from aplicacion import app
from flask import render_template

@app.route('/')
def ajedrez_uno(columnas=8, filas=8, coloruno='purple', colordos='black'  ):
    return render_template('index.html', columnas=columnas, filas=filas,  coloruno=coloruno,colordos=colordos )  

@app.route('/<int:filas>')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def ajedrez_dos(columnas=8, filas=8, coloruno='purple', colordos='black'  ):
    return render_template('index.html', columnas=columnas, filas=filas,  coloruno=coloruno,colordos=colordos  ) 

@app.route('/<int:filas>/<int:columnas>')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def ajedrez_tres(columnas=8, filas=8, coloruno='peachpuff', colordos='navy' ):
    return render_template('index.html', columnas=columnas, filas=filas, coloruno=coloruno,colordos=colordos ) 


@app.route('/<int:filas>/<int:columnas>/<string:coloruno>')
def ajedrez_cuatro(columnas=8, filas=8, coloruno='peachpuff', colordos='navy'):
    return render_template('index.html', columnas=columnas, filas=filas, coloruno=coloruno,colordos=colordos ) 

@app.route('/<int:filas>/<int:columnas>/<string:coloruno>/<string:colordos>')
def ajedrez_cinco(columnas=8, filas=8, coloruno='peachpuff', colordos='navy'):
    return render_template('index.html', columnas=columnas, filas=filas, coloruno=coloruno,colordos=colordos ) 