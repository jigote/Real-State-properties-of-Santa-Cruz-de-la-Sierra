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
    return render_template('index.html')









