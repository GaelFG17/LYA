from flask import Flask, render_template, request, jsonify

import puzzle_lineal as pl
import Vuelos as vl
import DFSI
import DFS
import DFSR
import Dikstra as dk

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    result = ""
    estado_inicial = list(map(int, request.form['estado_inicial'].split(',')))
    solucion = list(map(int, request.form['solucion'].split(',')))
    pl.BFS(estado_inicial, solucion)
    result = pl.resul
    return jsonify(resultado=result)

@app.route('/vuelos', methods=['POST'])
def buscarV():
    result = ""
    estado_inicial = request.form['estado_inicial']
    solucion = request.form['solucion']
    vl.BuscarVuelos(estado_inicial, solucion)
    result = vl.resul
    return jsonify(resultado=result)

@app.route('/DFS', methods=['POST'])
def buscarDFS():
    result = ""
    estado_inicial = list(map(int, request.form['estado_inicial'].split(',')))
    solucion = list(map(int, request.form['solucion'].split(',')))
    DFS.DFS(estado_inicial, solucion)
    result = DFS.resul
    return jsonify(resultado=result)

@app.route('/DFSI', methods=['POST'])
def buscarDFSI():
    result = ""
    estado_inicial = request.form['estado_inicial']
    solucion = request.form['solucion']
    DFSI.DFSI(estado_inicial, solucion)
    result = DFSI.resul
    return jsonify(resultado=result)

@app.route('/DFSR', methods=['POST'])
def buscarDFSR():
    result = ""
    estado_inicial = list(map(int, request.form['estado_inicial'].split(',')))
    solucion = list(map(int, request.form['solucion'].split(',')))
    DFSR.DFSR(estado_inicial, solucion)
    result = DFSR.resul
    return jsonify(resultado=result)

@app.route('/DK', methods=['GET'])
def DK():
    result = ""
    result = dk.Dikstra()
    return jsonify(resultado=result)

if __name__ == "__main__":
    app.run(debug=True)