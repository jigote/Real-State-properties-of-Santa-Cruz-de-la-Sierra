import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, render_template

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
def index():
    heading="Hola muundoo!!"
    return render_template("index.html", heading=heading)

@app.route("/users")
def users():
    names = ["Alice", "Bob", "Charlie"]
    return render_template("users.html", names=names)

@app.route("/nido")
def nido():
    return render_template("nido.html")

@app.route("/smartstudio")
def smartstudio():
    return render_template("smartstudio.html")

@app.route("/trii")
def triii():
    return render_template("triii.html")

@app.route("/tour_nido")
def tour_nido():
    return render_template('Tour_para_subir/index.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/landingpage")
def landingpage():
    return render_template('landingpage.html')









