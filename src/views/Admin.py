import AdminModal
from Interfaz import Interfaz
from tkinter import*
from Almacen import  E_TipoUsuario

class Admin(AdminModal.AdminModal):

    def content(self, miframe, raiz):
        botonenvio= Button(miframe, text="Preguntas para estudiantes", command= lambda: self.mostrar_ventana_modal(E_TipoUsuario.ESTUDIANTE))
        botonenvio.grid(row=0, column=0, sticky="e", padx=10, pady=10)
        botonenvio= Button(miframe, text="Preguntas para docentes", command= lambda: self.mostrar_ventana_modal(E_TipoUsuario.DOCENTE))
        botonenvio.grid(row=1, column=0, sticky="e", padx=10, pady=10)

        botonenvio= Button(raiz, text="Cerrar sesión", command=self.cerrar_sesion)
        botonenvio.pack(padx=10, pady=5)