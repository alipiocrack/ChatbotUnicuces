from Interfaz import Interfaz
from tkinter import*
import Menu as Menu
from Almacen import *
import Admin

class InfoUsuario(Interfaz):
    def content(self, miframe, raiz):

        nombreLabel= Label(miframe, text=Almacen.TipoUsuario.value, padx=10, pady=10 )
        nombreLabel.grid(row=0, column=0, sticky="e")

        cuadroNombre= Entry(miframe)
        cuadroNombre.grid(row=1, column=1)
        cuadroNombre.config(fg="black", justify="center")
        cuadroContrasena= Entry(miframe)
        cuadroContrasena.grid(row=2, column=1)
        cuadroContrasena.config(fg="black", justify="center")

        nombreLabel= Label(miframe, text="Nombre: ", padx=10, pady=10)
        nombreLabel.grid(row=1, column=0, sticky="e")
        contrasenaLabel= Label(miframe, text="Contrasena: ")
        contrasenaLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

        def codigoboton():

            nombre = cuadroNombre.get()
            contra = cuadroContrasena.get()

            usuarios = Almacen.Usuarios[Almacen.TipoUsuario]

            if  nombre in usuarios and usuarios[nombre] == contra:
                Almacen.Usuario =  UsuarioIngresado(nombre, contra)
                self.destroy()
                if(Almacen.TipoUsuario == E_TipoUsuario.ADMIN):
                    menu = Admin.Admin()
                else:
                    menu = Menu.Menu()
                menu.init("480")
            else:
                print("Usuario o contraseña incorrectos")
                cedulalabel= Label(miframe, text="Usuario o contraseña incorrectos")
                cedulalabel.grid(row=4, column=1, sticky="e", padx=10, pady=10, )


        botonenvio= Button(miframe, text="Enviar", command= codigoboton)
        botonenvio.grid(row=3, column=0, sticky="e", padx=10, pady=10)

        botonenvio= Button(raiz, text="Volver", command=self.volver)
        botonenvio.pack(padx=10, pady=5)