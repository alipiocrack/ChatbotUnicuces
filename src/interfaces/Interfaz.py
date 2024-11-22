#importaciones
from abc import ABC, abstractmethod
from tkinter import*
import tkinter as tk
from tkinter import messagebox
import TipoUsuario


#creacion de ventana
class Interfaz(ABC):

    def __init__(self):
        self.raiz = None

    @abstractmethod
    def content(self, raiz, miframe):
        pass

    def init(self, x = "300"):
        self.location = tk.INSERT
        self.raiz = Tk()
        self.raiz.title("Chatbot Unicuces")
        self.raiz.resizable(False,False)
        self.raiz.iconbitmap("src/images/logo1.ico")
        self.raiz.geometry("800x500")
        self.raiz.config(bg = "blue")

        miframe= Frame(self.raiz, width="500", height="400")
        miframe.pack(fill="both", expand="true")
        miframe.config(bg="white")
        miframe.config(width="650", height="350")
        miframe.config(bd="35")
        miframe.config(relief="sunken")
        miframe.config(cursor="hand2")

        #implementacion de imagenes

        miImagen=PhotoImage(file="src/images/robot2.png")
        self.image = Label(miframe, image=miImagen)
        self.image.place(x=x, y="100")


        self.content(miframe, self.raiz)


        self.raiz.mainloop()

    def cerrar_sesion(self):
        if messagebox.askyesno("Cerrar sesión", "¿Estás seguro de que deseas cerrar sesión?"):
            self.volver()

    def volver(self):
            self.destroy()
            tipo = TipoUsuario.TipoUsuario()
            tipo.init()

    def destroy(self):
        self.raiz.destroy()

    def destroyImage(self):
        self.image.destroy()
