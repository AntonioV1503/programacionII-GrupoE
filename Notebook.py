#Importacion de librerias
import tkinter as tk
from tkinter import ttk,messagebox
#Crear ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("500x700")
#Crear contenedor notebook (pestañas)
pestañas=ttk.Notebook(ventana_principal)
#Crear frames (uno por pestaña)
frame_pacientes=ttk.Frame(pestañas)
#Agregar pestañas al notebook
pestañas.add(frame_pacientes,text="Pacientes")
#Crear frame doctores
frame_doctores=ttk.Frame(pestañas)
pestañas.add(frame_doctores,text="Doctores")
#Mostrar las pestañas en la ventana
pestañas.pack(expand=True,fill="both")
#Nombre
labelNombre=tk.Label(frame_pacientes,text="Nombre Completo:")
labelNombre.grid(row=0,column=0,padx=5,pady=5,sticky="w")
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0,column=1,padx=5,pady=5,sticky="w")
#Fecha de nacimiento
labelFechaN=tk.Label(frame_pacientes,text="Fecha de Nacimiento:")
labelFechaN.grid(row=1,column=0,padx=5,pady=5,sticky="w")
fechaN=tk.Entry(frame_pacientes)
fechaN.grid(row=1,column=1,padx=5,pady=5,sticky="w")
#Edad (Readonly)
labelEdad=tk.Label(frame_pacientes,text="Edad:")
labelEdad.grid(row=2,column=0,padx=5,pady=5,sticky="w")
edadP=tk.Entry(frame_pacientes,state="readonly")
edadP.grid(row=2,column=1,padx=5,pady=5,sticky="w")
#Genero
labelGenero=tk.Label(frame_pacientes,text="Genero:")
labelGenero.grid(row=3,column=0,padx=5,pady=5,sticky="w")
genero=tk.StringVar()
genero.set("Masculino") #Valor por defecto
radioMasculino=ttk.Radiobutton(frame_pacientes,text="Masculino",variable=genero,value="Masculino")
radioMasculino.grid(row=3,column=1,padx=5,pady=5,sticky="w")
radioFemenino=ttk.Radiobutton(frame_pacientes,text="Femenino",variable=genero,value="Femenino")
radioFemenino.grid(row=4,column=1,padx=5,pady=5,sticky="w")
#Grupo sanguineo
labelGrupoSanguineo=tk.Label(frame_pacientes,text="Grupo Sanguineo:")
labelGrupoSanguineo.grid(row=5,column=0,padx=5,pady=5,sticky="w")
entryGrupoSanguineo=tk.Entry(frame_pacientes)
entryGrupoSanguineo.grid(row=5,column=1,padx=5,pady=5,sticky="w")
#Tipo de seguro
labelTipoSeguro=tk.Label(frame_pacientes,text="Tipo de Seguro:")
labelTipoSeguro.grid(row=6,column=0,padx=5,pady=5,sticky="w")
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico") #Valor por defecto
comboTipoSeguro=ttk.Combobox(frame_pacientes,values=["Publico","Privado","Ninguno"],textvariable=tipo_seguro,state="readonly")
comboTipoSeguro.grid(row=6,column=1,padx=5,pady=5,sticky="w")
#Centro Medico
labelCentroMedico=tk.Label(frame_pacientes,text="Centro de salud:")
labelCentroMedico.grid(row=7,column=0,padx=5,pady=5,sticky="w")
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central")#Valor por defecto
comboCentroMedico=ttk.Combobox(frame_pacientes,values=["Hospital Central","Clinica Norte","Centro Sur"],textvariable=centro_medico,state="readonly")
comboCentroMedico.grid(row=7,column=1,padx=5,pady=5,sticky="w")
ventana_principal.mainloop()
