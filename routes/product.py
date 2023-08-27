from flask import Blueprint, render_template, request, url_for, redirect
# Crear una ruta con Blueprint
producto = Blueprint("producto", __name__)

@producto.route("/")
def index():
    return "Hello World!"
'''
@producto.route("product/:product_name")
def consultar_producto():
    if method == "GET":
        data = data.json()

        response = url[0]
'''



