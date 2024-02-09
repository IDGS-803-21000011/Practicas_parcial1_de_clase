from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, FloatField

class DistanciaFrom(Form):
    x1 = FloatField('x1')
    x2 = FloatField('x2')
    y1 = FloatField('y1')
    y2 = FloatField('y2')

class ResistenciaForm(Form):
    opcionesBandas = [
        ('negro', 'Negro'),
        ('cafe', 'Café'),
        ('rojo', 'Rojo'),
        ('naranja', 'Naranja'),
        ('amarillo', 'Amarillo'),
        ('verde', 'Verde'),
        ('azul', 'Azúl'),
        ('violeta', 'Violeta'),
        ('gris', 'Gris'),
        ('blanco', 'Blanco'),
    ]

    opcionesTolerancia = [
        ('dorado', 'Dorado'),
        ('plata', 'Plata')
    ]

    banda1 = SelectField('Color 1', choices=opcionesBandas)
    banda2 = SelectField('Color 2', choices=opcionesBandas)
    banda3 = SelectField('Color 3', choices=opcionesBandas)
    tolerancia = RadioField('Tolerancia', choices=opcionesTolerancia)