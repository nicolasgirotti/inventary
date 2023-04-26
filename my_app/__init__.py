from flask import Flask, render_template, request, url_for
from urllib.parse import urlparse, parse_qs
from flask_sqlalchemy import SQLAlchemy



# Instancia de app
app = Flask(__name__)

# Configuracion de llave secreta, necesaria para enviar datos cifrados
app.config['SECRET_KEY'] ='12345'

# Configuracion de base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.sqlite'
# Eliminar datos en terminal innecesarios
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instancia de base de datos
db = SQLAlchemy()

from my_app import routes

