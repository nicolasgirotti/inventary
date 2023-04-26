from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length





class ProductForm(FlaskForm):
    brand = StringField('Marca', validators=[DataRequired()])
    description = StringField('Descripción', validators=[DataRequired()])
    size = StringField('Tamaño')
    price = DecimalField('Precio', validators=[DataRequired()])
    categoria_nombre = StringField('Nombre de categoría', validators=[DataRequired()])
    ean = IntegerField('EAN', validators=[DataRequired()])
    submit = SubmitField('Registrar producto')