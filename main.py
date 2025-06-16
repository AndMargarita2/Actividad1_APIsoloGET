#importamos el framework fastapi a nuestro entorno 
from fastapi import FastAPI, HTTPException

#creamos un objeto a partir de la clase FastAPI
app= FastAPI()
#utilizamos la instacion funcion get del framework FastAPI
@app.get("/imprimir")
#creamos la funcion asincrona "imprimir"
async def imprimir():
        return "HOLA ESTUDIANTES"

#creamos la funcion asincrona con formato JSON 
@app.get("/Git")
async def imprimir():
    return {"Git_curso": "https://github.com/AndMargarita2?tab=repositories"}

#Documentacion con swagger

from pydantic import BaseModel
#creamos nuestra lista de entidades con los siguientes atributos
#{"id": 3, "Name": Andrea, "LastName": Maldonado, "Age": 23}
class User(BaseModel):
    id: int
    Name: str
    LastName: str
    Age: int

#creamos un objeto en forma de lista con difererntes usuarios
users_list = [
    User(id=1, Name="Andrea", LastName="Maldonado", Age=23),
    User(id=2, Name="Juan", LastName="Pérez", Age=30),
    User(id=3, Name="María", LastName="Gómez", Age=25),
]
#--get("/users")
@app.get("/usersclass/")
async def usersclass():
    return (users_list)


#----ACTIVIDAD 01------

from typing import List
import pandas as pd

# Definir el modelo Alumno para los datos del Excel
class Alumno(BaseModel):
    Nombre: str
    Matricula: int
    Edad: int
    Facultad: str
    Grado: str
    Carrera: str
    Genero: str
    Correo: str
    Promedio: float
    Semestre: int

# Cargar los datos del CSV al iniciar la app
try:
    df = pd.read_csv('registros.csv')
    alumnos_excel = [Alumno(**row) for row in df.to_dict(orient='records')]
except Exception as e:
    alumnos_excel = []
    print(f"Error al cargar el archivo CSV: {e}")


# Endpoint: /alumno/edad/genero
@app.get("/alumno/{Edad}/{Genero}", response_model=List[Alumno])
async def get_alumnos_by_edad_genero(Edad: int, Genero: str):
    result = [user for user in alumnos_excel if user.Edad == Edad and user.Genero.lower() == Genero.lower()]
    if not result:
        raise HTTPException(status_code=404, detail="No se encontraron alumnos con esa edad y género")
    return result

# Endpoint: /alumno/facultad/carrera/semestre
@app.get("/alumno/{Facultad}/{Carrera}/{Semestre}", response_model=List[Alumno])
async def get_alumnos_by_facultad_carrera_semestre(Facultad: str, Carrera: str, Semestre: int):
    print(f"Facultad recibida: '{Facultad}'")
    print(f"Carrera recibida: '{Carrera}'")
    print(f"Semestre recibido: '{Semestre}'")
    for user in alumnos_excel:
        print(f"Facultad en datos: '{user.Facultad}' | Carrera en datos: '{user.Carrera}' | Semestre en datos: '{user.Semestre}'")
    result = [user for user in alumnos_excel if user.Facultad.lower() == Facultad.lower() and user.Carrera.lower() == Carrera.lower() and user.Semestre == Semestre]
    if not result:
        raise HTTPException(status_code=404, detail="No se encontraron alumnos con esa facultad, carrera y semestre")
    return result

# Endpoint: /semestre/promedio/matricula
@app.get("/semestre/{Semestre}/{Promedio}/{Matricula}", response_model=List[Alumno])
async def get_alumnos_by_semestre_promedio_matricula(Semestre: int, Promedio: float, Matricula: str):
    result = [user for user in alumnos_excel if user.Semestre == Semestre and user.Promedio == Promedio and user.Matricula == Matricula]
    if not result:
        raise HTTPException(status_code=404, detail="No se encontraron alumnos con ese semestre, promedio y matrícula")
    return result


# Si necesitas lanzar un error 404, usa:
# raise HTTPException(status_code=404, detail="No encontrado")

#levantamos el server Uvicornuvicorn main:app --reload
#con uvicorn main:app --reload

#http..... /imprimir