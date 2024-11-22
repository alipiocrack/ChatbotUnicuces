from Interfaz import Interfaz
from tkinter import*
import Almacen
from Almacen import Almacen, E_TipoUsuario
import tkinter.messagebox as messagebox


class AdminModal(Interfaz):

    def mostrar_ventana_modal(self, tipo : E_TipoUsuario):
        self.ventana_modal = Toplevel(cursor="hand2")
        self.ventana_modal.title(f"Gestionar preguntas de {tipo.value}")

        row = 0
        options = None

        match  tipo:
            case E_TipoUsuario.ESTUDIANTE:
                options = Almacen.Preguntas_estudiante
            case E_TipoUsuario.DOCENTE:
                options = Almacen.Preguntas_docente

        cuadroPregunta= self.CrearText(row,1)
        cuadroRespuesta= self.CrearText(row,2)

        self.CrearButton(row, 3, "Agregar", self.Editar(tipo, "", cuadroPregunta, cuadroRespuesta, options))
        row += 1
        for pregunta, respuesta in options.items():
            cuadroPregunta= self.CrearText(row,1, pregunta)
            cuadroRespuesta= self.CrearText(row,2, respuesta)

            self.CrearButton(row, 3, "Editar", self.Editar(tipo, pregunta, cuadroPregunta, cuadroRespuesta, options))
            self.CrearButton(row, 4, "Eliminar", self.Eliminar(tipo, pregunta, options))
            row += 1

        if(row==0):
            self.ventana_modal.geometry("300x50")
            etiqueta = Label(self.ventana_modal, text="No hay preguntas")
            etiqueta.pack()

        boton_cerrar = Button(self.ventana_modal, text="Cerrar", command=self.ventana_modal.destroy)
        boton_cerrar.grid(row=row+1, sticky="e", padx=10, pady=10)

    def CrearText(self, row, column, text = "") -> Text:
        cuadro = Text(self.ventana_modal, width=250, height=3, state="normal")
        cuadro.grid(row=row, column=column)
        cuadro.config(fg="black", width=50)
        cuadro.insert(self.location, text)
        return cuadro

    def CrearButton(self, row, column, text, action) -> Button:
        boton= Button(self.ventana_modal, text=text, command= action)
        boton.grid(row=row, column=column, sticky="e", padx=10, pady=10)
        return boton

    def Eliminar(self, tipo, pregunta, options: dict[str,str]):
        def eliminar_pregunta():
            if messagebox.askyesno("Confirmar Eliminación", f"¿Está seguro que desea eliminar la pregunta: '{pregunta}'?", parent=self.ventana_modal):
                options.pop(pregunta, None)
                self.Refrescar(tipo)
        return eliminar_pregunta

    def Editar(self, tipo, preguntaOriginal ,pregunta, respuesta, options: dict[str,str]):
        def editar_pregunta():
            pr = pregunta.get("1.0", "end-1c")
            rs = respuesta.get("1.0", "end-1c")
            if pr.strip() != "" and rs.strip() != "":
                options.pop(preguntaOriginal, None)
                options[pr] = rs
                self.Refrescar(tipo)
            else:
                messagebox.showerror("Error", "No se puede agregar una pregunta o respuesta vacía", parent=self.ventana_modal)
        return editar_pregunta

    def Refrescar(self, tipo):
        self.ventana_modal.destroy()
        self.mostrar_ventana_modal(tipo)
