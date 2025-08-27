import tkinter as tk
from tkinter import messagebox
ventana = tk.Tk()
ventana.title("Ejemplo spinbox")
ventana.configure(bg="#49aabb")
ventana.geometry("400x200")

def mostrarEdad():
    tk.messagebox.showinfo("Edad",f"La edad seleccionada es :{spin.get()}")

#Spinbox de numeros del al 10 para edad
labelEdad=tk.Label(ventana, text="Edad",bg="#49aabb")
labelEdad.grid(row=0,column=0,padx=5,pady=5,sticky="w")
spin= tk.Spinbox(ventana,from_=1,to=10)
spin.grid(row=0,column=1,padx=10,pady=10)
boton=tk.Button(ventana,text="Obtener valor",command=mostrarEdad)
boton.grid(row=1,column=0,padx=10,pady=10)
ventana.mainloop()