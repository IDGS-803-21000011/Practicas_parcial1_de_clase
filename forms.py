from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, FloatField

class DistanciaFrom(Form):
    x1 = FloatField('x1')
    x2 = FloatField('x2')
    y1 = FloatField('y1')
    y2 = FloatField('y2')