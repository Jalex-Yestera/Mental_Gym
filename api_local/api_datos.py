#API

import os, sys
from flask import Flask, render_template, redirect, request, jsonify 
import json
import pandas as pd

# --------------------------
# $$$$$$$ API (FLASK GET) $$$$$$$$
# --------------------------

# Para obtener la url: ipconfig
# Para obtener los datos: url:6060/datos?cantidad=número entre 1 y 584
# Debe devolver el json con el número de refranes/datos que se indique como cantidad

app=Flask(__name__)

@app.route('/', methods=['GET'])
def default():
    return '''<h1>API DEL RETO TRIPULACIONES ALZHEIMER</h1>
<p>Para conseguir el json: url:6060/datos?cantidad=(cantidad de datos a devolver, máximo 585)</p>'''

@app.route('/datos', methods=['GET'])
def get_json():

    #cantidad=None

    def cargar_datos(num, csv, archivo):
        df=(pd.read_csv(csv,sep=";").T).sample(n=num, axis=1)
        df.to_json(archivo+".json")
        #datos=os.path.dirname(__file__)+"\\"+archivo+".json"
        datos=archivo+".json"
        with open (datos,"r") as json_file_readed:
            peticion=json.load(json_file_readed)
        return json.dumps(peticion)

    if "cantidad" in request.args:
        cant=int(request.args["cantidad"])
        return cargar_datos(num=cant, csv="refranes_manipulado.csv", archivo="refranes")
    else:
        return("Introduce la cantidad de datos que quieres")


# -------------------------------
# $$$$$$$ SERVIDOR FLASK $$$$$$$$
# -------------------------------

def main():
    
    print("STARTING PROCESS")
    print(os.path.dirname(__file__))
    

    settings_file = os.path.dirname(__file__) + "\\settings.json" # puede que esto sea sin barras
    with open(settings_file, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)

    SERVER_RUNNING = json_readed["server_running"]
    
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print("Server settings.json doesn't allow to start server. " + 
              "Please, allow it to run it.")
            
if __name__ == "__main__":
    main()