# Endpoint: /alumno/edad/genero
parametros: 
  edad(int)
  genero(string)

Respuesta

  [
  {
    "Nombre": "string",
    "Matricula": 0,
    "Edad": 0,
    "Facultad": "string",
    "Grado": "string",
    "Carrera": "string",
    "Genero": "string",
    "Correo": "string",
    "Promedio": 0,
    "Semestre": 0
  }
]

# Endpoint: /alumno/facultad/carrera/semestre
parametros: 
  facultad(string)
  carrera(string)
  semestre(int)

Respuesta:

[
  {
    "Nombre": "string",
    "Matricula": 0,
    "Edad": 0,
    "Facultad": "string",
    "Grado": "string",
    "Carrera": "string",
    "Genero": "string",
    "Correo": "string",
    "Promedio": 0,
    "Semestre": 0
  }
]

# Endpoint: /semestre/promedio/matricula
parametros
  semestre(int)
  promedio(number)
  matricula(int)

Respuesta:

  [
  {
    "Nombre": "string",
    "Matricula": 0,
    "Edad": 0,
    "Facultad": "string",
    "Grado": "string",
    "Carrera": "string",
    "Genero": "string",
    "Correo": "string",
    "Promedio": 0,
    "Semestre": 0
  }
]
