from flask import Flask, render_template, request
import forms, math
from io import open
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("layout.html")

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

@app.route("/cine")
def cine():
    return render_template("vistaCine.html")

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method == "POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        operacion=request.form.get("operacion")
        resultado = 0

        if operacion == "suma":
            resultado = int(num1) + int(num2)
        elif operacion == "resta":
            resultado = int(num1) - int(num2)
        elif operacion == "multiplicacion":
            resultado = int(num1) * int(num2)
        elif operacion == "division":
            resultado = int(num1) / int(num2)
        return "<h1>La multiplicacion es: {}</h1>".format(str(resultado))
    
@app.route("/resultadoCine", methods=["POST"])
def resultadoCine():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        boletos = request.form.get("boletos")
        tarjeta = request.form.get("tarjeta")
        compradores = request.form.get("compradores")
        resultado_multiplicacion = 0
        boletos_permitidos = int(compradores) * 7

        if not nombre or not boletos.isdigit():
            return "Error: Datos de entrada no válidos."

        boletos_enteros = int(boletos)
        if boletos_enteros > boletos_permitidos:
            resultado_multiplicacion = 0
        else: 
            if boletos_enteros > 5:
                if tarjeta == "si":
                    resultado_multiplicacion = (boletos_enteros * 12) - ((boletos_enteros * 12) * 0.15)
                    resultado_multiplicacion = resultado_multiplicacion - (resultado_multiplicacion * 0.10) 
                else:
                    resultado_multiplicacion = (boletos_enteros * 12) - ((boletos_enteros * 12) * 0.15)
            elif boletos_enteros == 3 or boletos_enteros == 4 or boletos_enteros == 5:
                if tarjeta == "si":
                    resultado_multiplicacion = (boletos_enteros * 12) - ((boletos_enteros * 12) * 0.10)
                    resultado_multiplicacion = resultado_multiplicacion - (resultado_multiplicacion * 0.10)
                else:
                    resultado_multiplicacion = (boletos_enteros * 12) - ((boletos_enteros * 12) * 0.10)
            else:
                if tarjeta == "si":
                    resultado_multiplicacion = (boletos_enteros * 12) * .10
                else: 
                    resultado_multiplicacion = boletos_enteros * 12
        return render_template("vistaCine.html", resultado=resultado_multiplicacion)

@app.route("/distancias", methods=["GET", "POST"])
def dist():
    dist_form = forms.DistanciaFrom(request.form)
    res = 0.0
    if request.method == "POST":
        x1 = dist_form.x1.data
        x2 = dist_form.x2.data
        y1 = dist_form.y1.data
        y2 = dist_form.y2.data
        res = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    return render_template("distancias.html", form=dist_form, resultado = res)

@app.route("/resistencias", methods=["GET", "POST"])
def resistencias():
    dist_form = forms.ResistenciaForm(request.form)
    v1 = 0
    v2 = 0
    v3 = 0
    t = 0
    h1 = ''
    h2 = ''
    h3 = ''
    tc = ''
    tolerancia = ''

    if request.method == "POST":
        banda1 = dist_form.banda1.data
        banda2 = dist_form.banda2.data
        banda3 = dist_form.banda3.data
        tolerancia = dist_form.tolerancia.data

        if banda1 == 'negro':
            v1 = '0'
            h1 = '#000000'
        elif banda1 == 'cafe':
            v1 = '1'
            h1 = '#804000'
        elif banda1 == 'rojo':
            v1 = '2'
            h1 = '#FF0000'
        elif banda1 == 'naranja':
            v1 = '3'
            h1 = '#ff8000'
        elif banda1 == 'amarillo':
            v1 = '4'
            h1 = '#FFFF00'
        elif banda1 == 'verde':
            v1 = '5'
            h1 = '#008000'
        elif banda1 == 'azul':
            v1 = '6'
            h1 = '#0000FF'
        elif banda1 == 'violeta':
            v1 = '7'
            h1 = '#6F00FF'
        elif banda1 == 'gris':
            v1 = '8'
            h1 = '#808080'
        elif banda1 == 'blanco':
            v1 = '9'
            h1 = '#FFFFFF'

        if banda2 == 'negro':
            v2 = '0'
            h2 = '#000000'
        elif banda2 == 'cafe':
            v2 = '1'
            h2 = '#804000'
        elif banda2 == 'rojo':
            v2 = '2'
            h2 = '#FF0000'
        elif banda2 == 'naranja':
            v2 = '3'
            h2 = '#ff8000'
        elif banda2 == 'amarillo':
            v2 = '4'
            h2 = '#FFFF00'
        elif banda2 == 'verde':
            v2 = '5'
            h2 = '#008000'
        elif banda2 == 'azul':
            v2 = '6'
            h2 = '#0000FF'
        elif banda2 == 'violeta':
            v2 = '7'
            h2 = '#6F00FF'
        elif banda2 == 'gris':
            v2 = '8'
            h2 = '#808080'
        elif banda2 == 'blanco':
            v2 = '9'
            h2 = '#FFFFFF'

        if banda3 == 'negro':
            v3 = 1
            h3 = '#000000'
        elif banda3 == 'cafe':
            v3 = 10
            h3 = '#804000'
        elif banda3 == 'rojo':
            v3 = 100
            h3 = '#FF0000'
        elif banda3 == 'naranja':
            v3 = 1000
            h3 = '#ff8000'
        elif banda3 == 'amarillo':
            v3 = 10000
            h3 = '#FFFF00'
        elif banda3 == 'verde':
            v3 = 100000
            h3 = '#008000'
        elif banda3 == 'azul':
            v3 = 1000000
            h3 = '#0000FF'
        elif banda3 == 'violeta':
            v3 = 10000000
            h3 = '#6F00FF'
        elif banda3 == 'gris':
            v3 = 100000000
            h3 = '#808080'
        elif banda3 == 'blanco':
            v3 = 1000000000
            h3 = '#FFFFFF'

    if tolerancia == 'dorado':
        t = .05
        tc = '#EABE3F'
    elif tolerancia == 'plata':
        t = .10
        tc = '#e3e4e5'

    valorStr = v1 + v2
    valorInt = int(valorStr)
    valor = valorInt * v3
    valorMaximo = valor + (valor * t)
    valorMinimo = valor - (valor * t)

    return render_template("resistencias.html", form=dist_form, valor=valor, valorMaximo=valorMaximo, valorMinimo=valorMinimo, h1=h1, h2=h2, h3=h3, tc=tc)

@app.route("/traductor", methods=["GET", "POST"])
def traductor():
    dist_form = forms.TraductorForm(request.form)
    dist_form2 = forms.BuscarPalabraForm(request.form)

    if request.method == 'POST' and dist_form.validate():
        campo_ingles = dist_form.campo_ingles.data
        campo_espanol = dist_form.campo_espanol.data

        archivo_texto = open('diccionario.txt','a')
        archivo_texto.write(f'\n{campo_ingles.lower()}: {campo_espanol.lower()}')
        archivo_texto.close()
        dist_form = forms.TraductorForm()

    return render_template("traductor.html", form=dist_form, form2=dist_form2)

@app.route("/buscar", methods=["GET", "POST"])
def buscar():
    dist_form = forms.TraductorForm(request.form)
    dist_form2 = forms.BuscarPalabraForm(request.form)
    archivo_texto = open('diccionario.txt', 'r')

    if request.method == 'POST' and dist_form2.validate():
        palabra = dist_form2.buscar_palabra.data.lower().strip()
        direccion = dist_form2.direccion_traduccion.data

        for linea in archivo_texto:
            if ':' in linea:
                palabra_dic, traduccion = linea.strip().split(':')
                if direccion == 'ingles_espanol':
                    if palabra_dic.strip().lower() == palabra:
                        return render_template("traductor.html", traduccion=traduccion.strip(), form=dist_form, form2=dist_form2)
                elif direccion == 'espanol_ingles':
                    if traduccion.strip().lower() == palabra:
                        return render_template("traductor.html", traduccion=palabra_dic.strip(), form=dist_form, form2=dist_form2)
    archivo_texto.close()
    return render_template("traductor.html", mensaje="La palabra no fue encontrada en el diccionario.", form=dist_form, form2=dist_form2)


if __name__ == "__main__":
    app.run(debug=True)

    # rcardielr@universidaddeleon.edu.mx