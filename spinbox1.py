import tkinter as tk
from tkinter import messagebox
ventana = tk.Tk()
ventana.title("Ejemplo spinbox")
ventana.configure(bg="#c4f6ff")
ventana.geometry("400x200")

def mostrarEdad():
    tk.messagebox.showinfo("Edad",f"La edad seleccionada es :{spin.get()}")

def mostrarGenero():
    tk.messagebox.showinfo("Genero",f"El genero seleccionado es :{genero.get()}")


#Spinbox de numeros del al 10 para edad
labelEdad=tk.Label(ventana, text="Edad",bg="#c4f6ff")
labelEdad.grid(row=0,column=0,padx=5,pady=5,sticky="w")
spin= tk.Spinbox(ventana,from_=1,to=10)
spin.grid(row=0,column=1,padx=10,pady=10)
boton=tk.Button(ventana,text="Obtener valor",command=mostrarEdad)
boton.grid(row=1,column=0,padx=10,pady=10)
#Genero
labelGenero=tk.Label(ventana,text="Genero",bg="#c4f6ff")
labelGenero.grid(row=2,column=0,padx=5,pady=5,sticky="w")
#Spinbox de texto para genero
genero=tk.Spinbox(ventana,values=("Masculino","Femenino","Otro"))
genero.grid(row=2,column=1,padx=10,pady=10)
botonGenero=tk.Button(ventana,text="Obtener Genero",command=mostrarGenero)
botonGenero.grid(row=3,column=0,padx=10,pady=10)
ventana.mainloop()