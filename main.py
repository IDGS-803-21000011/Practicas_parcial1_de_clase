from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("formulario.html")

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

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

if __name__ == "__main__":
    app.run(debug=True)