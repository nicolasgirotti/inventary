from flask import render_template, redirect, url_for, request
from my_app import app, db   
from my_app.models import Product, Barcode, Categoria



# Ruta para leer codigo y mostrar codigo de producto
@app.route("/", methods=['GET', 'POST'])
def index():

    # Get url
    url = request.url
    print(f"esta es la url {url}")

    # Condicional que verifica si la url tiene un codigo de producto
    if 'content' not in url:
        product_id = ''
    else:
        product_id = url.split("content=")[1].split("&")[0]
        print(f"esta es id {product_id}")

    return render_template("index.html", product_id=product_id)



