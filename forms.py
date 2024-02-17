from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, FloatField
from wtforms import validators

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

class TraductorForm(Form):
    campo_ingles = StringField('Palabra Inglés', [
        validators.DataRequired(message='El campo es requerido.'),
        validators.length(min=1, max=15, message='Ingresa una palabra válida.')
    ])
    campo_espanol = StringField('Palabra Español', [
        validators.DataRequired(message='El campo es requerido.'),
        validators.length(min=1, max=15, message='Ingresa una palabra válida.')
    ])

class BuscarPalabraForm(Form):
    buscar_palabra = StringField("Buscar palabra", [
        validators.DataRequired(message='El campo es requerido.'),
        validators.length(min=1, max=15, message='Ingresa una palabra válida.')
    ])
    direccion_traduccion = RadioField("Dirección de Traducción", choices=[('ingles_espanol', 'Inglés a Español'), ('espanol_ingles', 'Español a Inglés')], default='ingles_espanol')