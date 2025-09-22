#Importacion de librerias
import tkinter as tk
from tkinter import ttk,messagebox

#Funcion guardar archivo doctores
def guardar_en_archivo_doc():
    with open("doctoresRegistro.txt", "w", encoding="utf-8") as archivo:
        for doctores in doctores_data:
            archivo.write(
                f"{doctores['Nombre']}|{doctores['Especialidad']}|{doctores['Años de experiencia']}|"
                f"{doctores['Genero']}|{doctores['Hospital']}\n"
            )

def cargar_desde_archivo_doctores():
    try:
        with open("doctoresRegistro.txt","r",encoding="utf-8") as archivo:
            doctores_data.clear()
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==5:
                    doctores={
                    "Nombre":datos[0],
                    "Especialidad":datos[1],
                    "Años de experiencia":datos[2],
                    "Genero":datos[3],
                    "Hospital":datos[4]
                }
                    doctores_data.append(doctores)
        cargar_treeviewD()
    except FileNotFoundError:
        open("doctoresRegistro.txt","w",encoding="utf-8").close()

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


#Lista vacia de doctores
doctores_data=[]
#Funcion Registrar doctores
def registrarDoctor():
    #Crear un diccionario con los datos ingresados
    doctor={
        "Nombre":nombreD.get(),
        "Especialidad":combo.get(),
        "Años de experiencia":spin.get(),
        "Genero":genero.get(),
        "Hospital":comboh.get()
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
                item["Años de experiencia"],
                item["Genero"],
                item["Hospital"]
            )
        )

#Crear ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Doctores")
ventana_principal.geometry("800x600")
#Crear contenedor notebook (pestañas)
pestañas=ttk.Notebook(ventana_principal)
#Crear frame doctores
frame_doctores=ttk.Frame(pestañas)
pestañas.add(frame_doctores,text="Doctores")
#Mostrar las pestañas en la ventana
pestañas.pack(expand=True,fill="both")
#Doctores
Titulo=tk.Label(frame_doctores,text="REGISTRO DE DOCTORES",font=30)
Titulo.grid(row=0,column=1)
#Nombre
labelNombreD=tk.Label(frame_doctores,text="Nombre:")
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
#Años de experiencia
labelEdadD=tk.Label(frame_doctores, text="Años de experiencia:",)
labelEdadD.grid(row=3,column=0,padx=5,pady=5,sticky="e")
spin= tk.Spinbox(frame_doctores,from_=1,to=120)
spin.grid(row=3,column=1,padx=5,pady=5,sticky="w")
#Genero
labelGenero=tk.Label(frame_doctores,text="Genero:")
labelGenero.grid(row=4,column=0,padx=5,pady=5,sticky="e")
genero=tk.StringVar()
genero.set("Masculino") #Valor por defecto
radioMasculino=ttk.Radiobutton(frame_doctores,text="Masculino",variable=genero,value="Masculino")
radioMasculino.grid(row=4,column=1,padx=5,pady=5,sticky="w")
radioFemenino=ttk.Radiobutton(frame_doctores,text="Femenino",variable=genero,value="Femenino")
radioFemenino.grid(row=5,column=1,padx=5,pady=5,sticky="w")
#Hospital
etiquetah=tk.Label(frame_doctores,text="Hospital:")
etiquetah.grid(row=6,column=0,padx=5,pady=5,sticky="e")
#Crear Combobox
opcionesh=["Publico","Privado"]
comboh=ttk.Combobox(frame_doctores,values=opcionesh,state="readonly")
comboh.current(0) #Seleccionar la primera opcion por defecto
comboh.grid(row=6,column=1,padx=5,pady=5,sticky="W")
#Frame para los botones
btn_frameD=tk.Frame(frame_doctores)
btn_frameD.grid(row=7,column=0,columnspan=2,pady=5,sticky="e")
#Boton registrar
btn_registrarD=tk.Button(btn_frameD,text="Registrar",command=registrarDoctor,bg="#34fa1a")
btn_registrarD.grid(row=0,column=0,padx=5)
#Boton eliminar
btn_eliminarD=tk.Button(btn_frameD,text="Eliminar",command=eliminardoctor,bg="#ff0404")
btn_eliminarD.grid(row=0,column=1,padx=5)
treeviewD=ttk.Treeview(frame_doctores,columns=("Nombre","Especialidad","Años de experiencia","Genero","Hospital"),show="headings")
#Encabezados
treeviewD.heading("Nombre",text="Nombre Completo")
treeviewD.heading("Especialidad",text="Especialidad")
treeviewD.heading("Años de experiencia",text="Años de experiencia")
treeviewD.heading("Genero",text="Genero")
treeviewD.heading("Hospital",text="Hospital")
#Definir anchos de columnas
treeviewD.column("Nombre",width=120)
treeviewD.column("Especialidad",width=120)
treeviewD.column("Años de experiencia",width=200,anchor="center")
treeviewD.column("Genero",width=80,anchor="center")
treeviewD.column("Hospital",width=80,anchor="center")
#Ubicar el Treeview en la cuadricula
treeviewD.grid(row=8,column=0,columnspan=2,sticky="w",padx=5,pady=10)
#ScrollBar vertical
scroll_yd=ttk.Scrollbar(frame_doctores,orient="vertical",command=treeviewD.yview)
treeviewD.configure(yscrollcommand=scroll_yd.set)
scroll_yd.grid(row=8,column=2,sticky="ns")
cargar_desde_archivo_doctores()
ventana_principal.mainloop()