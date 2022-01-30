from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "topsecreto"



@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/registrarUsuario', methods=['POST'])
def registrarUsuario():

    session["name"] = request.form["name"]
    session["ubication"] = request.form["ubication"]
    session["language"] = request.form["language"]
    session["coment"] = request.form["coment"]

    return redirect('/dashboard')

@app.route('/dashboard', methods=['GET'])
def despliegaInformacion():
    return render_template("dashboard.html")

@app.route('/ingresar', methods=['POST'])
def ingresar():
    session['usuario'] = request.form["usuario"]

    if session['usuario'] == session["name"]:
        session['usuario'] == session["name"]
    else:
        return redirect('/') 
    return redirect('/dashboard')


if __name__=="__main__":
    app.run( debug=True )