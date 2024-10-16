from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quienes.html")
def quien():
    return render_template("quienes.html")

@app.route("/servicios.html")
def ser():
    return render_template("servicios.html")

@app.route("/entrada.html")
def entra():
    return render_template("entrada.html")

@app.route("/noticias.html")
def noti():
    return render_template("noticias.html")

@app.route("/contacto.html", methods = ['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        mensaje = request.form.get('mensaje')
        return render_template("salida.html", nombre = nombre, email = email, mensaje = mensaje)
    return render_template("contacto.html")

if __name__== "__main__":
    app.run(debug=True)