#seleccionar datos de mi base de datos y mostrarlo usando codigo python
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")


# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


def main():
    departamentos = db.execute("SELECT edificio, duración FROM departamentos").fetchall()
    #el .fetchall() corre el SQL query y me devuelve todos los resultados en una lista
    for departamento in departamentos:
        print(f"en el edificio {departamento.edificio} hubieron visitantes, {departamento.duración} minutos ")

if __name__=="__main__":
    main()
