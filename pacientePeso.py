#Importacion de librerias
import tkinter as tk
from datetime import datetime
from tkinter import ttk,messagebox
#Funcion para enmascarar fecha
def enmascarar_fecha(texto):
    limpio=''.join(filter(str.isdigit,texto))
    formato_final=""
    if len(limpio)>8:
        limpio=limpio[:8]
    if len(limpio)>4:
        formato_final=f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio)>2:
        formato_final=f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final=limpio
    if fechaN.get()!=formato_final:
        fechaN.delete(0,tk.END)
        fechaN.insert(0,formato_final)
    if len(fechaN.get())==10:
        fecha_actual=datetime.now().date()
        fecha_nacimiento=datetime.strptime(fechaN.get(),'%d-%m-%Y').date()
        edad=fecha_actual.year-fecha_nacimiento.year 
        edadVar.set(edad)
    else:
        edadVar.set("")
    return True
#Funcion guardar archivo
def guardar_en_archivo():
    with open("pacientePeso.txt", "w", encoding="utf-8") as archivo:
        for paciente in paciente_data:
            archivo.write(
                f"{paciente['Nombre']}|{paciente['Fecha de Nacimiento']}|{paciente['Edad']}|"
                f"{paciente['Genero']}|{paciente['Grupo Sanguineo']}|{paciente['Tipo de Seguro']}|{paciente['Centro Medico']}|{paciente['Peso']}\n"
            )
#Funcion guardar archivo doctores
def guardar_en_archivo_doc():
    with open("doctores.txt", "w", encoding="utf-8") as archivo:
        for doctores in doctores_data:
            archivo.write(
                f"{doctores['Nombre']}|{doctores['Especialidad']}|{doctores['Edad']}|"
                f"{doctores['Telefono']}\n"
            )
#Cargar archivo
def cargar_desde_archivo_pacientes():
    try:
        with open("pacientePeso.txt","r",encoding="utf-8") as archivo:
            paciente_data.clear()
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==8:
                    paciente={
                    "Nombre":datos[0],
                    "Fecha de Nacimiento":datos[1],
                    "Edad":datos[2],
                    "Genero":datos[3],
                    "Grupo Sanguineo":datos[4],
                    "Tipo de Seguro":datos[5],
                    "Centro Medico":datos[6],
                    "Peso":datos[7]
                }
                    paciente_data.append(paciente)
        cargar_treeview()
    except FileNotFoundError:
        open("pacientePeso.txt","w",encoding="utf-8").close()
#Cargar archivo Doctores
def cargar_desde_archivo_doctores():
    try:
        with open("doctores.txt","r",encoding="utf-8") as archivo:
            doctores_data.clear()
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==4:
                    doctores={
                    "Nombre":datos[0],
                    "Especialidad":datos[1],
                    "Edad":datos[2],
                    "Telefono":datos[3],
                }
                    doctores_data.append(doctores)
        cargar_treeviewD()
    except FileNotFoundError:
        open("doctores.txt","w",encoding="utf-8").close()
#Funcion para eliminar paciente
def eliminarpaciente():
    seleccionado=treeview.selection()
    if seleccionado:
        indice=int(seleccionado[0])
        id_item=seleccionado[0]
        if messagebox.askyesno("Eliminar Paciente",f"¿Esta seguro de eliminar el paciente '{treeview.item(id_item,'values')[0]}'?"):
            del paciente_data[indice]
            guardar_en_archivo() #Guardar los cambios en el archivo
            cargar_treeview()
            messagebox.showinfo("Eliminar Paciente","Paciente eliminado exitosamente.")
    else: # este else es del if seleccionado
        messagebox.showwarning("Eliminar Paciente","No se ha seleccionado ningun paciente.")
        return
#Funcion para eliminar doctor
def eliminardoctor():
    seleccionado=treeviewD.selection()
    if seleccionado:
        indice=int(seleccionado[0])
        id_item=seleccionado[0]
        if messagebox.askyesno("Eliminar Doctor",f"¿Esta seguro de eliminar el doctor '{treeviewD.item(id_item,'values')[0]}'?"):
            del doctores_data[indice]
            guardar_en_archivo_doc() #Guardar los cambios en el archivo
            cargar_treeviewD()
            messagebox.showinfo("Eliminar Doctor","Doctor eliminado exitosamente.")
    else: # este else es del if seleccionado
        messagebox.showwarning("Eliminar Doctor","No se ha seleccionado ningun Doctor.")
        return
#Lista de pacientes (inicialmente vacia)
paciente_data=[]
#Funcion registrar paciente
def registrarPaciente():
    #Crear un diccionario con los datos ingresados
    paciente={
        "Nombre":nombreP.get(),
        "Fecha de Nacimiento":fechaN.get(),
        "Edad":edadVar.get(),
        "Genero":genero.get(),
        "Grupo Sanguineo":entryGrupoSanguineo.get(),
        "Tipo de Seguro":tipo_seguro.get(),
        "Centro Medico":centro_medico.get(),
        "Peso":entryPeso.get()
    }
    #Agregar paciente a la lista
    paciente_data.append(paciente)
    #Cargar al Treeview
    guardar_en_archivo()
    cargar_treeview()
def cargar_treeview():
    #Limpiar el TreeView
    for paciente in treeview.get_children():
        treeview.delete(paciente)
    #Insertar cada paciente
    for i,item in enumerate(paciente_data):
        treeview.insert(
            "","end",iid=str(i),
            values=(
                item["Nombre"],
                item["Fecha de Nacimiento"],
                item["Edad"],
                item["Genero"],
                item["Grupo Sanguineo"],
                item["Tipo de Seguro"],
                item["Centro Medico"],
                item["Peso"]
            )
        )
#Lista vacia de doctores
doctores_data=[]
#Funcion Registrar doctores
def registrarDoctor():
    #Crear un diccionario con los datos ingresados
    doctor={
        "Nombre":nombreD.get(),
        "Especialidad":combo.get(),
        "Edad":spin.get(),
        "Telefono":Telefono.get()
    }
    #Agregar doctor a la lista
    doctores_data.append(doctor)
    #Cargar al treeview de doctores
    cargar_treeviewD()
    guardar_en_archivo_doc()
def cargar_treeviewD():
    #Limpiar el TreeView
    for doctor in treeviewD.get_children():
        treeviewD.delete(doctor)
    #Insertar cada doctor
    for i,item in enumerate(doctores_data):
        treeviewD.insert(
            "","end",iid=str(i),
            values=(
                item["Nombre"],
                item["Especialidad"],
                item["Edad"],
                item["Telefono"]
            )
        )
#Evento al cambiar pestaña
def al_cambiar_pestaña(event):
    pestaña_activa=pestañas.index(pestañas.select())
    if pestaña_activa==0: #pacientes
        cargar_desde_archivo_pacientes()
    elif pestaña_activa==1: #Doctores
        cargar_desde_archivo_doctores()
#Crear ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("800x600")
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
#Llamando a la funcion enmascarar fecha
validacion_fecha=ventana_principal.register(enmascarar_fecha)
fechaN=ttk.Entry(frame_pacientes,validate="key",validatecommand=(validacion_fecha,'%P'))
fechaN.grid(row=1,column=1,padx=5,pady=5,sticky="w")
#Edad (Readonly)
labelEdad=tk.Label(frame_pacientes,text="Edad:")
labelEdad.grid(row=2,column=0,padx=5,pady=5,sticky="w")
edadVar=tk.StringVar()
edadP=ttk.Entry(frame_pacientes,textvariable=edadVar,state="readonly")
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
#Peso
labelPeso=tk.Label(frame_pacientes,text="Peso (Kg):")
labelPeso.grid(row=8,column=0,padx=5,pady=5,sticky="w")
entryPeso=tk.Entry(frame_pacientes)
entryPeso.grid(row=8,column=1,padx=5,pady=5,sticky="w")
#Frame para los botones
btn_frame=tk.Frame(frame_pacientes)
btn_frame.grid(row=10,column=0,columnspan=2,pady=5,sticky="w")
#Boton registrar
btn_registrar=tk.Button(btn_frame,text="Registrar",command=registrarPaciente)
btn_registrar.grid(row=0,column=0,padx=5)
#Boton eliminar
btn_eliminar=tk.Button(btn_frame,text="Eliminar",command=eliminarpaciente)
btn_eliminar.grid(row=0,column=1,padx=5)
#Crear TreeView para mostrar pacientes
treeview=ttk.Treeview(frame_pacientes,columns=("Nombre","FechaN","Edad","Genero","GrupoS","TipoS","CentroM","Peso"),show="headings")
#Definir encabezados
treeview.heading("Nombre",text="Nombre Completo")
treeview.heading("FechaN",text="Fecha Nacimiento")
treeview.heading("Edad",text="Edad")
treeview.heading("Genero",text="Genero")
treeview.heading("GrupoS",text="Grupo Sanguineo")
treeview.heading("TipoS",text="Tipo Seguro")
treeview.heading("CentroM",text="Centro Medico")
treeview.heading("Peso",text="Peso")
#Definir anchos de columnas
treeview.column("Nombre",width=120)
treeview.column("FechaN",width=120)
treeview.column("Edad",width=50,anchor="center")
treeview.column("Genero",width=70,anchor="center")
treeview.column("GrupoS",width=100,anchor="center")
treeview.column("TipoS",width=100,anchor="center")
treeview.column("CentroM",width=120,anchor="center")
treeview.column("Peso",width=70,anchor="center")
#Ubicar el Treeview en la cuadricula
treeview.grid(row=9,column=0,columnspan=2,sticky="nsew",padx=5,pady=10)
#ScrollBar vertical
scroll_y=ttk.Scrollbar(frame_pacientes,orient="vertical",command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=9,column=2,sticky="ns")
#Doctores
Titulo=tk.Label(frame_doctores,text="REGISTRO DE DOCTORES",font=30)
Titulo.grid(row=0,column=1)
#Nombre
labelNombreD=tk.Label(frame_doctores,text="Nombre Completo:")
labelNombreD.grid(row=1,column=0,padx=5,pady=5,sticky="e")
nombreD=tk.Entry(frame_doctores)
nombreD.grid(row=1,column=1,padx=5,pady=5,sticky="w")
#Especialidad
etiqueta=tk.Label(frame_doctores,text="Especialidad:")
etiqueta.grid(row=2,column=0,padx=5,pady=5,sticky="e")
#Crear Combobox
opciones=["Cardiologia","Neurologia","Pediatria","Traumatologia"]
combo=ttk.Combobox(frame_doctores,values=opciones,state="readonly")
combo.current(0) #Seleccionar la primera opcion por defecto
combo.grid(row=2,column=1,padx=5,pady=5,sticky="w")
#Edad
labelEdadD=tk.Label(frame_doctores, text="Edad",)
labelEdadD.grid(row=3,column=0,padx=5,pady=5,sticky="e")
spin= tk.Spinbox(frame_doctores,from_=1,to=120)
spin.grid(row=3,column=1,padx=5,pady=5,sticky="w")
#Telefono
labelTel=tk.Label(frame_doctores,text="Telefono:")
labelTel.grid(row=4,column=0,padx=5,pady=5,sticky="e")
Telefono=tk.Entry(frame_doctores)
Telefono.grid(row=4,column=1,padx=5,pady=5,sticky="w")
#Frame para los botones
btn_frameD=tk.Frame(frame_doctores)
btn_frameD.grid(row=5,column=0,columnspan=2,pady=5,sticky="e")
#Boton registrar
btn_registrarD=tk.Button(btn_frameD,text="Registrar",command=registrarDoctor,bg="#34fa1a")
btn_registrarD.grid(row=0,column=0,padx=5)
#Boton eliminar
btn_eliminarD=tk.Button(btn_frameD,text="Eliminar",command=eliminardoctor,bg="#ff0404")
btn_eliminarD.grid(row=0,column=1,padx=5)
treeviewD=ttk.Treeview(frame_doctores,columns=("Nombre","Especialidad","Edad","Telefono"),show="headings")
#Encabezados
treeviewD.heading("Nombre",text="Nombre Completo")
treeviewD.heading("Especialidad",text="Especialidad")
treeviewD.heading("Edad",text="Edad")
treeviewD.heading("Telefono",text="Telefono")
#Definir anchos de columnas
treeviewD.column("Nombre",width=120)
treeviewD.column("Especialidad",width=120)
treeviewD.column("Edad",width=50,anchor="center")
treeviewD.column("Telefono",width=60,anchor="center")
#Ubicar el Treeview en la cuadricula
treeviewD.grid(row=7,column=0,columnspan=2,sticky="w",padx=5,pady=10)
#ScrollBar vertical
scroll_yd=ttk.Scrollbar(frame_doctores,orient="vertical",command=treeviewD.yview)
treeviewD.configure(yscrollcommand=scroll_yd.set)
scroll_yd.grid(row=7,column=2,sticky="ns")
pestañas.bind("<<NotebookTabChanged>>",al_cambiar_pestaña)
cargar_desde_archivo_pacientes()
cargar_desde_archivo_doctores()
ventana_principal.mainloop()