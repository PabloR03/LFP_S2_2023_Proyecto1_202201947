import tkinter as tk
from tkinter import Menu
from tkinter import messagebox, filedialog, scrolledtext
from tkinter.filedialog import askopenfilename, asksaveasfilename
from matrix_Analizador import fun_instruccion, operar_, fun_genGrafico, fun_deleteL,  fun_Archivo_salida_errores, fun_deleteLE, fun_lGrafico
import os

class ventana_principal:
    def __init__(self, root):
        #ruta de archivo a analizar_Archivo
        self.archivo_analizado=True

        #datos de ventana principal
        self.root = root
        self.root.title("Aplicacion Numérica Con Analizador Léxico - 202201947")
        self.root.geometry("1280x720")
        self.root.resizable(0,0)
        #cuadro que contiene a los botones
        barra_de_opciones = tk.Frame(root, bg="dodgerblue4")
        barra_de_opciones.pack(pady=5)
        barra_de_opciones.pack_propagate()
        barra_de_opciones.configure(width=1280, height=60)

        #boton de menu (desplegable)
        boton_archivo=tk.Menubutton(barra_de_opciones, text="ARCHIVO")        
        boton_archivo.place(x=20, y=10, width=140, height=40)
            #op del menu
        op=Menu(boton_archivo,tearoff=0)
        boton_archivo["menu"]=op
        op.add_command(label="ABRIR", command=self.fun_bArchivo)
        op.add_command(label="GUARDAR", command=self.fun_gArchivo)
        op.add_command(label="GUARDAD COMO", command=self.fun_gcArchivo)


        # boton de analizar_Archivo
        boton_analizar=tk.Button(barra_de_opciones,text="ANALIZAR", command=self.analizar_Archivo)
        boton_analizar.place(x=500, y=10, width=140, height=40)
        #boton de salir
        boton_salir=tk.Button(barra_de_opciones,text="X", command=self.salir)
        boton_salir.place(x=1220, y=10, width=40, height=40)
        
        #cuadro De Texto
        cuadrotexto_frame=tk.Frame(root,bg="dodgerblue")
        self.cuadroTexto = scrolledtext.ScrolledText(cuadrotexto_frame, bg="White", width=110, height=33)
        self.cuadroTexto.place(x=55, y=30)
        cuadrotexto_frame.pack(pady=5)
        cuadrotexto_frame.pack_propagate()
        cuadrotexto_frame.configure(width=1000, height=600)
        
        #Def para buscar archivo tipo .json y abrirlo
    def fun_bArchivo(self):
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
            # Elimina contenido del textArea para cargar el archivo
            self.cuadroTexto.delete(1.0, "end")
            # Copia la informacion del contenido
            self.cuadroTexto.insert(1.0, self.texto)
            messagebox.showinfo("ABRIR ... ", "Archivo cargado, puede seguir editandolo en el panel de texto")
        except:
            messagebox.showerror("ERROR ... ", "Archivo no cargado, revise que haya seleccionado uno y que sea de tipo .Json")
            return
    
    #Def para guardar archivo que esta en el panel de texto
    def fun_gArchivo(self):
        try:
            # Tomar datos que esta en el cuadro de texto
            self.texto = self.cuadroTexto.get(1.0, "end")
            archivo = open(self.ruta_seleccionada, 'w', encoding="utf-8")
            archivo.write(self.texto)
            
            messagebox.showinfo("GUARDADO ... ", "Cambios Guardados, puede seguir en el analizador")
        except:
            messagebox.showerror("ERROR ... ", "Archivo no Guardado, revise la entrada")
            return

    def fun_gcArchivo(self):
        try:
            # Tomar datos que esta en el cuadro de texto
            self.texto = self.cuadroTexto.get(1.0, "end")
            self.archivo_seleccionado = asksaveasfilename(filetypes=[("Archivos JSON", f"*.json")], defaultextension=[("Archivos JSON", f"*.json")], initialfile=" ")
            archivo = open(self.archivo_seleccionado, 'w', encoding="utf-8")
            archivo.write(self.texto)
            
            messagebox.showinfo("GUARDADO ... ", "Cambios Guardados, puede seguir en el analizador")
        except:
            messagebox.showerror("ERROR ... ", "Archivo no Guardado, revise la entrada")
            return

    def salir(self):
        try:
            messagebox.showinfo("SALIDA ... ", "Cerrando programa, ;)")
            self.root.destroy()
        except:
            messagebox.showerror("ERROR ... ", "No se puede cerrar, revise la entrada")


    def analizar_Archivo(self):
        # variable para saber si ya se presiono el boton de analizar_Archivo
        # En caso de que despues de analizar_Archivo un arhivo se analice otro se limpian las listas
        
        
        try:
            #boton de errores
            boton_errores=tk.Button(text="ERRORES", command=self.errores)
            boton_errores.place(x=650,y=15, width=140, height=40)
            fun_deleteLE()
            fun_deleteL()
            fun_instruccion(self.texto)
            fun_lGrafico()
            operar_()
        except:
            messagebox.showerror("ERROR ... ", "Opcion " "Abrir Archivo" " no seleccionada ")
            return
        messagebox.showinfo("Exito","Archivo procesado con exito")

    def errores(self):
        #solo generar archivo de errores si ya se analizo el archivo
        if (self.archivo_analizado == False):
            messagebox.showerror("ERROR ... ", "Opcion " "Analizar no ha sido seleccionada" " ")
            return
        try:
            #boton de reporte
            boton_reporte=tk.Button(text="REPORTE", command=self.reporte)
            boton_reporte.place(x=800, y=15, width=140, height=40)
            fun_Archivo_salida_errores()
            messagebox.showinfo("Guardado", "Archivo de errores generado con exito, revise sus archivos")
        except:
            messagebox.showerror("ERROR ... ", "No se pudo generar Archivo de errores")
            return


    def reporte(self):
        #solo generar reporte si ya se analizo el archivo
        if (self.archivo_analizado == False):
            messagebox.showerror("ERROR ... ", "Opcion " "Analizar no ha sido seleccionada" " ")
            return
        
        try:
            fun_genGrafico(str("Reporte_diagrama_de_operaciones"))
            messagebox.showinfo("Guardado", "Archivo de reporte generado con exito")
        except:
            messagebox.showerror("ERROR ... ", "No se pudo generar Archivo de Reporte")
            return
        


if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = ventana_principal(root)
    root.mainloop()