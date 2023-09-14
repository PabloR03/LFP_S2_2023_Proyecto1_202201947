import tkinter as tk
from tkinter import Menu, messagebox, filedialog, scrolledtext
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import os

class ventana_principal:
    def __init__(self, root):
        #Variable Analizado
        self.archivo_analizado=True

        #Ventana Pricipal
        self.root = root
        self.root.title("Aplicacion Numérica Con Analizador Léxico - 202201947")
        self.root.geometry("1280x720")
        self.root.resizable(0,0)
        #Frame Botones Opciones
        opciones_frame = tk.Frame(root, bg="dodgerblue4")
        opciones_frame.pack(pady=5)
        opciones_frame.pack_propagate()
        opciones_frame.configure(width=1280, height=60)


        boton_archivo=tk.Menubutton(opciones_frame, text="ARCHIVO")        
        boton_archivo.place(x=20, y=10, width=140, height=40)

        opciones=Menu(boton_archivo,tearoff=0)
        boton_archivo["menu"]=opciones
        opciones.add_command(label="ABRIR", command=self.buscar_archivo)
        opciones.add_command(label="GUARDAR", command=self.guardar_archivo)
        opciones.add_command(label="GUARDAD COMO", command=self.guardar_como)
        opciones.add_command(label="SALIR", command=self.salir)

        boton_analizar=tk.Button(opciones_frame,text="ANALIZAR", command=self.analizar)
        boton_analizar.place(x=500, y=10, width=140, height=40)

        boton_errores=tk.Button(opciones_frame,text="ERRORES", command=self.errores)
        boton_errores.place(x=650,y=10, width=140, height=40)

        boton_reporte=tk.Button(opciones_frame,text="REPORTE", command=self.reporte)
        boton_reporte.place(x=800, y=10, width=140, height=40)

        boton_salir=tk.Button(opciones_frame,text="X", command=self.salir)
        boton_salir.place(x=1220, y=10, width=40, height=40)
        
        #Frame Cuadro De Texto
        cuadrotexto_frame=tk.Frame(root,bg="dodgerblue")
        self.cuadroTexto = scrolledtext.ScrolledText(cuadrotexto_frame, bg="White", width=110, height=33)
        self.cuadroTexto.place(x=55, y=30)
        cuadrotexto_frame.pack(pady=5)
        cuadrotexto_frame.pack_propagate()
        cuadrotexto_frame.configure(width=1000, height=600)
        

    def buscar_archivo(self):
        self.archivo_analizado=True
        texto_archivo = ""
        ruta = tk.Tk()
        ruta.withdraw()
        ruta.attributes('-topmost', True)
        try:
            self.ruta_seleccionada= nueva_ruta = filedialog.askopenfilename(filetypes=[("Archivos JSON", f"*.json")])
            with open(nueva_ruta, encoding="utf-8") as archivo_json:
                texto_archivo = archivo_json.read()
            self.texto = texto_archivo
            # Elimina contenido del cuadro
            self.cuadroTexto.delete(1.0, "end")
            # set contenido
            self.cuadroTexto.insert(1.0, self.texto)
            messagebox.showinfo("Abrir", "Archivo Cargado con exito")
        except:
            messagebox.showerror("Error", "No se ha seleccionado un archivo")
            return
    
    def guardar_archivo(self):
        try:
            # Tomar datos que esta en el cuadro de texto
            self.texto = self.cuadroTexto.get(1.0, "end")
            archivo = open(self.ruta_seleccionada, 'w', encoding="utf-8")
            archivo.write(self.texto)
            # mensaje de guardado
            messagebox.showinfo("Guardado", "Archivo guardado con exito")
        except:
            messagebox.showerror("Error", "No se ha seleccionado ningún archivo")
            return

    def guardar_como(self):
        try:
            # Tomar datos que esta en el cuadro de texto
            self.texto = self.cuadroTexto.get(1.0, "end")
            self.archivo_seleccionado = asksaveasfilename(filetypes=[("Archivos JSON", f"*.json")], defaultextension=[("Archivos JSON", f"*.json")], initialfile=" ")
            archivo = open(self.archivo_seleccionado, 'w', encoding="utf-8")
            archivo.write(self.texto)
            # mensaje de guardado
            messagebox.showinfo("Guardado", "Archivo guardado con exito")
        except:
            messagebox.showerror("Error", "No se ha seleccionado ningún archivo")
            return

    def salir(self):
        try:
            messagebox.showinfo("Salir", "Gracias por utilizar el programa")
            self.root.destroy()
        except:
            messagebox.showerror("Error", "Error")


    def analizar(self):

        messagebox.showinfo("Analisis completado","Analisis realizado con exito")



    def reporte(self):

        messagebox.showinfo("Guardado", "Archivo de errores generado con exito")


    def errores(self):
        messagebox.showinfo("Guardado", "Archivo de errores generado con exito")



if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = ventana_principal(root)
    root.mainloop()