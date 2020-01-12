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
    messages = db.execute("SELECT * FROM note").fetchall()
    #el .fetchall() corre el SQL query y me devuelve todos los resultados en una lista
    for message in messages:
        print(f"en el edificio {message.message} hubieron visitantes a {message.created_at} horas ")

if __name__=="__main__":
    main()