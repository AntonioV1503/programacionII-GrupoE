import tkinter as tk
from tkinter import messagebox
ventana = tk.Tk()
ventana.title("Ejemplo ListBox")
sintomasLabel=tk.Label(ventana,text="Sintomas")
sintomasLabel.grid(row=0,column=0,padx=5,pady=5,sticky="w")
#Crear ListBox
lista=tk.Listbox(ventana,selectmode=tk.SINGLE)
lista.insert(1,"Dolor de cabeza")
lista.insert(2,"Fiebre")
lista.insert(3,"Tos")
lista.insert(4,"Fatiga")
lista.insert(5,"Dificultad al respirar")
lista.grid(row=0,column=1,pady=10,sticky="we")
#Boton para mostrar seleccion
def mostrar():
    seleccionado=lista.get(lista.curselection())
    tk.messagebox.showinfo("Seleccion",f"Has elegido: {seleccionado}")
boton=tk.Button(ventana,text="Mostrar seleccion",command=mostrar)
boton.grid(row=1,column=0,padx=10,pady=10)
ventana.mainloop()