import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='', static_url_path='')

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def landingpage():
    heading="Hola muundoo!!"
    return render_template("landingpage.html", heading=heading)

@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        return "Querida usuario, querido usuario, por favor ingrese sus datos"
    else:
        name = request.form.get("name")
        return render_template('users.html', name=name)

@app.route("/nido")
def nido():
    return render_template("nido.html")

@app.route("/smartstudio")
def smartstudio():
    return render_template("smartstudio.html")

@app.route("/trii")
def triii():
    return render_template("triii.html")

@app.route("/portofino")
def portofino():
    return render_template("portofino.html")

@app.route("/torrepremium")
def torrepremium():
    return render_template("torrepremium.html")

@app.route("/torreszen")
def torreszen():
    return render_template("torreszen.html")

@app.route("/skyLux")
def skyLux():
    return render_template("skyLux.html")

@app.route("/skyPalmeto")
def skyPalmeto():
    return render_template("skyPalmeto.html")

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if session.get("ambientes") is None:
        session["ambientes"] = []
    if request.method == "POST":
        ambiente = request.form.get("ambiente")
        session["ambientes"].append(ambiente)

    return render_template('Tour_para_subir/registro.html', ambientes=session["ambientes"])

@app.route("/tour_nido")
def tour_nido():
    return render_template('Tour_para_subir/index.html')


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == "GET":
        return "Pidale al usuario que vuelva a enviar el formulario"
    else:
        name = request.form.get("name")
        return render_template('dashboard.html', name=name)

@app.route("/index")
def index():
    departamentos = db.execute("SELECT * FROM departamentos").fetchall()
    return render_template('index.html', departamentos=departamentos)

@app.route("/book", methods=["POST"])
def book():
    """"registra una visita"""

    #obtener informacion 
    name = request.form.get("name")
    try:
        departamento_id = int(request.form.get("departamento_id"))
    except ValueError:
        return render_template("error.html", message="Numero de departamento inválido")

    if db.execute("SELECT * FROM departamentos WHERE id = :id", {"id": departamento_id}).rowcount == 0:
        return render_template("error.html", message="No hay tal departamento con ese id")
    db.execute("INSERT INTO visitantes (nombre, departamento_id) VALUES (:nombre, :departamento_id)", 
            {"nombre":name, "departamento_id":departamento_id})
    db.commit()
    return render_template("success.html")

@app.route("/book2", methods=["GET", "POST"])
def book2():
    """"llenó el formulario"""

    if request.method == "GET":
        return "Querida usuaria, querido usuario, porfavor ingrese todos los datos de la casilla anterior"
   
    #obtener informacion 
    name = request.form.get("name")
    lastName = request.form.get("lastName")
    cellphone = request.form.get("cellphone")
    email = request.form.get("email")

    db.execute("INSERT INTO form_info (lastName, name, cellphone, email) VALUES (:lastName, :name, :cellphone, :email)", 
            {"name":name, "lastName":lastName, "cellphone":cellphone, "email":email})
    db.commit()
    return render_template("success.html")


@app.route("/departamentos")
def departamentos():
    """Lista de todos los departamentos"""
    departamentos = db.execute("SELECT * FROM departamentos").fetchall()
    return render_template("departamentos.html", departamentos=departamentos)
  
@app.route("/departamentos/<int:departamento_id>")
def departamento(departamento_id):
    """ Lista de detalles sobre ese departamento. """

    #Me aseguro de que el departamento existe.
    departamento = db.execute("SELECT * FROM departamentos WHERE id = :id", {"id":departamento_id}).fetchone()
    if departamento is None:
        return render_template("error.html", message="No hay tal vuelo.")
    #obtener todos los pasajeros
    visitantes = db.execute("SELECT name FROM visitantes WHERE departamento_id = :departamento_id", 
                            {"departamento_id": departamento_id}).fetchall()
    return render_template("dashboard.html", departamento=departamento, visitantes=visitantes)










