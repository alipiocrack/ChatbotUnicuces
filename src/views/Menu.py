from Interfaz import Interfaz
from tkinter import *

from Almacen import Almacen, E_TipoUsuario

class Menu(Interfaz):
    def content(self, raiz, miframe):
        milabel = Label(raiz, text=(f"Bienvenid@ {Almacen.Usuario.Nombre} al Chatbot de Unicuces"))
        milabel.place(x=450, y=50)

        self.milabel = Label()

        def codigoboton(pregunta, respuesta):
            def _codigoboton():
                self.destroyImage()
                self.milabel.destroy()
                self.milabel = Label(raiz, text=(respuesta), width=45,  wraplength=250)
                self.milabel.place(x=400, y=150)
            return  _codigoboton

        row = 0
        options = None

        match  Almacen.TipoUsuario:
            case E_TipoUsuario.ESTUDIANTE:
                options = Almacen.Preguntas_estudiante
            case E_TipoUsuario.DOCENTE:
                options = Almacen.Preguntas_docente

        for pregunta, respuesta in options.items():
            botonenvio = Button(raiz, text=pregunta, command=codigoboton(pregunta, respuesta))
            botonenvio.grid(row=row, column=0, sticky="e", padx=10, pady=10)
            row += 1

        botonenvio= Button(miframe, text="Cerrar sesión", command=self.cerrar_sesion)
        botonenvio.pack(padx=10, pady=5)



