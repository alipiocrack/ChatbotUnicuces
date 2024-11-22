from Interfaz import Interfaz
from tkinter import*

from Almacen import E_TipoUsuario
import InfoUsuario
from Almacen import Almacen

class TipoUsuario(Interfaz):
    def content(self, miframe, raiz):
        def codigoboton(tipo):
            Almacen.TipoUsuario = tipo
            self.destroy()
            infoUsuario = InfoUsuario.InfoUsuario()
            infoUsuario.init()

        botonenvio= Button(miframe, text="Administrador", command= lambda: codigoboton(E_TipoUsuario.ADMIN))
        botonenvio.grid(row=0, column=0, sticky="e", padx=10, pady=10)
        botonenvio= Button(miframe, text="Estudiante", command= lambda: codigoboton(E_TipoUsuario.ESTUDIANTE))
        botonenvio.grid(row=1, column=0, sticky="e", padx=10, pady=10)
        botonenvio= Button(miframe, text="Docente", command= lambda: codigoboton(E_TipoUsuario.DOCENTE))
        botonenvio.grid(row=2, column=0, sticky="e", padx=10, pady=10)