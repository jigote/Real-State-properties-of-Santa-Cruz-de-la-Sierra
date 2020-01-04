import csv
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
    f = open("visitantes.csv")
    reader = csv.reader(f)
    for nomb, depar in reader:
        db.execute("INSERT INTO visitantes (nombre, departamento_id) VALUES (:nombre, :departamento_id)",
            {"nombre": nomb, "departamento_id": depar})
        print(f"añadì al visitante {nomb}, que visitó el departamento {depar}")
    db.commit()

if __name__ == '__main__':
    main()