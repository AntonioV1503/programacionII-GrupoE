import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
#Crear ventana principal
ventana=tk.Tk()
ventana.title("Ejemplo Combobox")
ventana.configure(bg="#49aabb")
ventana.geometry("400x200")
#Etiqueta
etiqueta=tk.Label(ventana,text="Seleccione especialidad:")
etiqueta.grid(row=0,column=0,padx=10,pady=10,sticky="w")
#Crear Combobox
opciones=["Cardiologia","Neurologia","Pediatria","Dermatologia"]
combo=ttk.Combobox(ventana,values=opciones,state="readonly")
combo.current(0) #Seleccionar la primera opcion por defecto
combo.grid(row=0,column=1,padx=10,pady=10)
def mostrar():
    seleccion=combo.get()
    tk.messagebox.showinfo("Seleccion",f"Has elegido: {seleccion}")
#Boton para confirmar seleccion
boton=tk.Button(ventana,text="Aceptar",command=mostrar)
boton.grid(row=1,column=0,columnspan=2,pady=15)
ventana.mainloop()