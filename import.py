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
    f = open("departamentos.csv")
    reader = csv.reader(f)
    for edif, direc, duration in reader:
        db.execute("INSERT INTO departamentos (edificio, dirección, duración) VALUES (:edificio, :dirección, :duración)",
            {"edificio": edif, "dirección": direc, "duración": duration})
        print(f"añadì {edificio} con dirección {dirección} y duracion {duración}")
    db.commit()

if __name__ == '__main__':
    main()
