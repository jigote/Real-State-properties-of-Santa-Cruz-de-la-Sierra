#lo mismo que list.py pero esta vez para seleccionar y mostrar los datos de la tabla "visitantes"
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
    visitantes = db.execute("SELECT * FROM visitantes").fetchall()
    #el .fetchall() corre el SQL query y me devuelve todos los resultados en una lista
    for visitante in visitantes:
        print(f"El visitante {visitante.nombre} estuvo en el departamento, {visitante.departamento_id} ")

if __name__=="__main__":
    main()