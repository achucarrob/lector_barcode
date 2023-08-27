from flask import Flask, Blueprint, render_template, request, url_for, redirect

from app import data 
print(data)
# from routes.product import producto 

app = Flask(__name__)

# app.register_blueprint(producto)
# Crear una ruta con Blueprint
# producto = Blueprint("producto", __name__)

@app.route("/")
def index():
    return render_template('index.html')
'''
@app.route("product/:product_name")
def consultar_producto():
    if method == "GET":
        data = data.json()

        response = url[0]
'''