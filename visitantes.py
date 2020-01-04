#selecciono la tabla1 de datos de mi base de datos y mostrarlo usando codigo python
#luego le pido al usuario que ingrese el dato de tipo foreign key que busca
#me aseguro de que ese dato es valido de mi tabla1
#selecciono la tabla2 de mi base de datos y lo muestro usando codigo python
#imprimo la tabla con el foreign key que busca el usuario
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
    #lista de departamentos
    departamentos = db.execute("SELECT * FROM departamentos").fetchall()
    #el .fetchall() corre el SQL query y me devuelve todos los resultados en una lista
    for departamento in departamentos:
        print(f"Proyecto {departamento.edificio}")

    #Promt user que escoja un departamento.
    departamento_id = int(input("\nID del Departamento: "))
    departamento = db.execute("SELECT * FROM departamentos WHERE id = :id", {"id": departamento_id}).fetchone()
    
    #me aseguro de que esa foreign key es valida.
    if departamento is None:
        print("Error: No hay tenemos ese departamento")
        return

    #lista de visitantes
    visitantes = db.execute("SELECT nombre FROM visitantes WHERE departamento_id = :departamento_id", {"departamento_id": departamento_id}).fetchall()

    #imprimir Lista
    print("\nVisitantes:")
    for visitante in visitantes:
        print (f"El visitante {visitante.nombre} ")
    if len (visitantes) == 0:
        print ("No hay visitantes aún en este proyecto")

if __name__=="__main__":
    main()