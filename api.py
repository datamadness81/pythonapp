import flask
from flask import render_template, jsonify
import os
import random
import linecache

app = flask.Flask(__name__)
app.config["DEBUG"] = True

DATA_FILE = "data.txt"
randfile = open(DATA_FILE, "w")
nums = 4096

for i in range(nums):
    line = str(random.uniform(-4096, 4096)) + "\n"
    randfile.write(line)
randfile.close()

diccOperaciones = {
    'linea1': 0,
    'linea2': 0,
    'valorLinea1': 0,
    'valorLinea2': 0,
    'zresult': 0
}


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/suma/<int:num1>/<int:num2>', methods=['GET'])
def suma(num1, num2):
    if ((int(num1) > 4096) or (int(num2) > 4096)):
        return '''<h1>Uno o mas numeros fuera de rango, por favor modifique</h1>'''
    elif num2 == 0 or num1 == 0:
        return '''<h1>No es posible asignar una linea 0 al listado de numeros</h1>'''
    else:
        diccOperaciones["linea1"] = num1
        diccOperaciones["linea2"] = num2
        if os.path.exists(DATA_FILE):
            line_numbers = [num1, num2]
        listSuma = []
        for i in range(len(line_numbers)):
            x = float(linecache.getline(
                DATA_FILE, line_numbers[i]).strip())
            listSuma.append(x)
        diccOperaciones["valorLinea1"] = listSuma[0]
        diccOperaciones["valorLinea2"] = listSuma[1]
        diccOperaciones["zresult"] = sum(listSuma)
        return jsonify(diccOperaciones)


@app.route('/resta/<int:num1>/<int:num2>', methods=['GET'])
def resta(num1, num2):
    if ((int(num1) > 4096) or (int(num2) > 4096)):
        return '''<h1>Uno o mas numeros fuera de rango, por favor modifique</h1>'''
    elif num2 == 0 or num1 == 0:
        return '''<h1>No es posible asignar una linea 0 al listado de numeros</h1>'''
    else:
        diccOperaciones["linea1"] = num1
        diccOperaciones["linea2"] = num2
        if os.path.exists(DATA_FILE):
            line_numbers = [num1, num2]
        listResta = []
        for i in range(len(line_numbers)):
            x = float(linecache.getline(
                DATA_FILE, line_numbers[i]).strip())
            listResta.append(x)
        diccOperaciones["valorLinea1"] = listResta[0]
        diccOperaciones["valorLinea2"] = listResta[1]
        diccOperaciones["zresult"] = listResta[0] - listResta[1]
        return jsonify(diccOperaciones)


@app.route('/multi/<int:num1>/<int:num2>', methods=['GET'])
def multi(num1, num2):
    if ((int(num1) > 4096) or (int(num2) > 4096)):
        return '''<h1>Uno o mas numeros fuera de rango, por favor modifique</h1>'''
    elif num2 == 0 or num1 == 0:
        return '''<h1>No es posible asignar una linea 0 al listado de numeros</h1>'''
    else:
        diccOperaciones["linea1"] = num1
        diccOperaciones["linea2"] = num2
        if os.path.exists(DATA_FILE):
            line_numbers = [num1, num2]
        listMulti = []
        for i in range(len(line_numbers)):
            x = float(linecache.getline(
                DATA_FILE, line_numbers[i]).strip())
            listMulti.append(x)
        diccOperaciones["valorLinea1"] = listMulti[0]
        diccOperaciones["valorLinea2"] = listMulti[1]
        diccOperaciones["zresult"] = listMulti[0] * listMulti[1]
        return jsonify(diccOperaciones)


@app.route('/div/<int:num1>/<int:num2>', methods=['GET'])
def division(num1, num2):
    if ((int(num1) > 4096) or (int(num2) > 4096)):
        return '''<h1>Uno o mas numeros fuera de rango, por favor modifique</h1>'''
    elif num2 == 0 or num1 == 0:
        return '''<h1>No es posible asignar una linea 0 al listado de numeros</h1>'''
    else:
        diccOperaciones["linea1"] = num1
        diccOperaciones["linea2"] = num2
        if os.path.exists(DATA_FILE):
            line_numbers = [num1, num2]
        listDiv = []
        for i in range(len(line_numbers)):
            x = float(linecache.getline(
                DATA_FILE, line_numbers[i]).strip())
            listDiv.append(x)
        diccOperaciones["valorLinea1"] = listDiv[0]
        diccOperaciones["valorLinea2"] = listDiv[1]
        diccOperaciones["zresult"] = listDiv[0] / listDiv[1]
        return jsonify(diccOperaciones)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8081)
