from sqlalchemy import Numeric
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from flask_sqlalchemy import SQLAlchemy

from my_app import app, db


class Barcode(db.Model):
    # EAN es el codigo de barra de los productos en Argentina
    id = db.Column(db.Integer, primary_key=True)
    ean = db.Column(db.Integer)
    producto_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    size = db.Column(db.String(40))
    price = db.Column(Numeric(precision=8, scale=2))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    bar_code = db.relationship('Barcode', uselist=False, backref='producto')



class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    productos = db.relationship('Product', backref='categoria', lazy=True)



# Creacion de tablas en base de datos

db.init_app(app)
with app.app_context():
    db.create_all()


