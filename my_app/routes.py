from flask import render_template, redirect, url_for, request, flash
from my_app import app, db   
from my_app.models import Product, Barcode, Categoria
from my_app.forms import ProductForm



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

        return redirect(url_for('nuevo_producto', product_id=product_id))

    return render_template("index.html", product_id=product_id)





@app.route('/productos/<int:product_id>', methods=['GET', 'POST'])
def nuevo_producto(product_id):
    form = ProductForm()

    print(f'este es la id en la ruta de producto: {product_id}')

    if form.validate_on_submit():
        # Crea un nuevo Producto y lo asocia a la categoría y al barcode
        producto = Product(
        brand=form.brand.data,
        description=form.description.data,
        size=form.size.data,
        price=form.price.data,
        categoria=form.categoria_nombre.data,
        ean=product_id
        )
        # Agrega el nuevo producto y barcode a la base de datos
        db.session.add(producto)
        db.session.commit()
        
        flash('El producto ha sido creado exitosamente!', 'success')
        
    elif request.method == 'GET':
        print(f'este es el producto id {product_id}')
    
        form.ean.data = product_id
        
        
        
    return render_template('nuevo_producto.html', form=form, product_id=product_id)
