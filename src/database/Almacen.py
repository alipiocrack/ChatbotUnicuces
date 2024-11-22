from enum import Enum

class E_TipoUsuario(Enum):
    NONE = "NONE"
    ADMIN = "ADMINISTRADOR"
    ESTUDIANTE = "ESTUDIANTE"
    DOCENTE = "DOCENTE"

class UsuarioIngresado:

    def __init__(self, nombre = "", contrasena = ""):
        self.Nombre = nombre
        self.Contrasena = contrasena

class  Almacen:

    TipoUsuario = E_TipoUsuario.NONE

    Usuario = UsuarioIngresado()

    Usuarios = {
        E_TipoUsuario.ADMIN: {
            "Admin": "123",
            "David": "321"},
        E_TipoUsuario.ESTUDIANTE: {
            "Jualian": "568",
            "Maria": "789"},
        E_TipoUsuario.DOCENTE: {
            "Mario": "159",
            "Lorena": "658"}
    }

    Preguntas_estudiante = {
        "¿Cuándo son los próximos parciales?": "Los próximos parciales serán en dos semanas.",
        "¿Cuándo son las inscripciones para la universidad?": "Las inscripciones están abiertas desde el 1 de marzo hasta el 30 de abril.",
        "¿Dónde puedo solicitar información sobre las carreras universitarias?": (
            "A través de la página web. Puedes acceder a la información en el siguiente enlace: "
            "https://www.universidad.edu.co"
        ),
        "¿Dónde está ubicada la sede en Cali?": "Está ubicada en la Cl. 14 Nte. #8N-35, Granada.",
    }

    Preguntas_docente = {
        "¿Cuándo son los próximos parciales?": "Los próximos parciales serán en dos semanas.",
        "¿Dónde puedo ingresar las notas de los estudiantes?": "A través de la plataforma SIAAF."
    }




