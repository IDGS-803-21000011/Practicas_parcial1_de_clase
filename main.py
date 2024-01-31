from flask import Flask, render_template, request
import forms, math
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

if __name__ == "__main__":
    app.run(debug=True)