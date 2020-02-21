import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
#Ventana1
ventana = tk.Tk()
ventana.geometry("700x400")
ventana.title("Sistema Escolar")

def imprimir_todo():
    listo = True
    listo2 = True
    val3 = True
    val4 = True
    aux2 = opcion.get()
    if aux2 == 0:
        val3 = False
    if aux2 == 1:
        texradio = 'Soltero'
    if aux2 == 2:
        texradio = 'Viudo'
    if aux2 == 3:
        texradio = 'Casado'
    if aux2 == 4:
        texradio = 'Divorciado'
    if aux2 == 5:
        texradio = 'Es complicado'

    tex2 = 'Te gusta:\n'
    if var1.get() == 1:
        tex2 += chk.cget("text")+'\n'
    if var2.get() == 1:
        tex2 += chk2.cget("text")+'\n'
    if var3.get() == 1:
        tex2 += chk3.cget("text")+'\n'
    if var4.get() == 1:
        tex2 += chk4.cget("text")+'\n'
    if var5.get() == 1:
        tex2 += chk5.cget("text")+'\n'
    
    if var1.get() == 0 and var2.get() == 0 and var3.get() == 0 and var4.get() == 0 and var5.get() == 0:
        val4 = False

    if  val4 == False or val3 == False:
        listo = False
   

    if(preguntar_nombre.get() == '' or preguntar_AP.get() == '' or preguntar_Materno.get() == '' 
    or preguntar_Direccion.get() == '' or Sel_Colonia.get() == ''
    or Ciudad.get() == '' or Municipio.get() == ''): 
        listo2 = False

    if(listo == False or listo2 == False):
        mBox.showinfo('Error','Faltan Datos por completar!!')
    else:
        mBox.showinfo('Datos Personales',preguntar_nombre.get()+'\n'+preguntar_AP.get()+'\n'+preguntar_Materno.get()+
        '\n'+preguntar_Direccion.get()+'\n'+Colonia.get()+'\n'+Ciudad.get()+'\n'+Municipio.get()+'\n'+'Preferencias'+tex2+'\nEstas:\n'+texradio+'\nMeta en la vida:\n'+objetivo.get())
        

        
def funcion_caja_mensaje():
    mBox.showinfo('Acerca de','App de Daniel Caballero')     


def funcion_salir():
    ventana.quit()
    ventana.destroy()
    exit()


def funcion_click2():
    val = True
    val2 = True
    aux = opcion.get()
    if aux == 0:
        val = False
    if aux == 1:
        texradio = 'Soltero'
    if aux == 2:
        texradio = 'Viudo'
    if aux == 3:
        texradio = 'Casado'
    if aux == 4:
        texradio = 'Divorciado'
    if aux == 5:
        texradio = 'Es complicado'

    tex = 'Te gusta:\n'
    if var1.get() == 1:
        tex += chk.cget("text")+'\n'
    if var2.get() == 1:
        tex += chk2.cget("text")+'\n'
    if var3.get() == 1:
        tex += chk3.cget("text")+'\n'
    if var4.get() == 1:
        tex += chk4.cget("text")+'\n'
    if var5.get() == 1:
        tex += chk5.cget("text")+'\n'
    
    if var1.get() == 0 and var2.get() == 0 and var3.get() == 0 and var4.get() == 0 and var5.get() == 0:
        val2 = False

    if  val2 == False or val == False:
        accion2.config(text = "Faltan opciones :(")
    else:   
        mBox.showinfo('Preferencias',tex+'\nEstas:\n'+texradio+'\nMeta en la vida:\n'+objetivo.get())
    
    
def funcion_click():
    
    if(preguntar_nombre.get() == '' or preguntar_AP.get() == '' or preguntar_Materno.get() == '' 
    or preguntar_Direccion.get() == '' or Sel_Colonia.get() == ''
    or Ciudad.get() == '' or Municipio.get() == ''): 
        accion.configure(text="Faltan Campos :(")
    else:
        mBox.showinfo('Datos Personales',preguntar_nombre.get()+'\n'+preguntar_AP.get()+'\n'+preguntar_Materno.get()+
        '\n'+preguntar_Direccion.get()+'\n'+Colonia.get()+'\n'+Ciudad.get()+'\n'+Municipio.get())
        accion.configure(text="LISTO!!")
        

 
    
           


#Barra de Menu
barra_menu = Menu(ventana)
ventana.config(menu = barra_menu)
opciones_menu = Menu(barra_menu)
opciones_menu.add_command(label = "Imprimir", command = imprimir_todo)
opciones_menu.add_command(label = "Salir", command = funcion_salir)
barra_menu.add_cascade(label = "Sistema", menu = opciones_menu)
opciones_menu = Menu(barra_menu)
opciones_menu.add_command(label = "Acerca de", command = funcion_caja_mensaje)
barra_menu.add_cascade(label = "Ayuda", menu = opciones_menu)

#Pestañas
tabControl = ttk.Notebook(ventana)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text = 'Datos Personales')
tabControl.pack(expand = 1, fill = "both")
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text = 'Preferencias')

#Nombre
ttk.Label(tab1, text= "Nombre"). grid(column=0, row=0)
nombre= tk.StringVar()
preguntar_nombre = ttk.Entry(tab1, width=20, textvariable=nombre)
preguntar_nombre.grid(column=1, row=0)

     
#Apellido Paterno
ttk.Label(tab1, text= "Apellido_Paterno").grid(column=0, row=1)
Apellido_Paterno= tk.StringVar()
preguntar_AP = ttk.Entry(tab1, width=20, textvariable=Apellido_Paterno)
preguntar_AP.grid(column=1, row=1)
#Apellido_Materno
ttk.Label(tab1, text= "Apellido_Materno").grid(column=0, row=2)
Apellido_Materno= tk.StringVar()
preguntar_Materno = ttk.Entry(tab1, width=20, textvariable=Apellido_Materno)
preguntar_Materno.grid(column=1, row=2)
#Direccion
ttk.Label(tab1, text= "Direccion").grid(column=0, row=3)
Direccion= tk.StringVar()
preguntar_Direccion = ttk.Entry(tab1, width=20, textvariable=Direccion)
preguntar_Direccion.grid(column=1, row=3)
#Colonia_Lista
ttk.Label(tab1, text= "Colonia").grid(column=0, row=4)
Colonia=tk.StringVar()
Sel_Colonia = ttk.Combobox(tab1, width=12, textvariable=Colonia)
Sel_Colonia['values'] = ('MorelosSur','LaMora','Santiaguito','Centro')
Sel_Colonia.grid(column=1, row=4)
#Ciudad
ttk.Label(tab1, text="Ciudad").grid(column=0, row=5)
Ciudad=tk.StringVar()
Sel_Ciudad = ttk.Combobox(tab1, width=12, textvariable=Ciudad)
Sel_Ciudad['values'] = ('Morelia','Ciudad de Mexico','Guadalajara','Queretaro')
Sel_Ciudad.grid(column=1, row=5)
#Municipio
ttk.Label(tab1, text="Municipio").grid(column=0, row=6)
Municipio=tk.StringVar()
Sel_Municipio = ttk.Combobox(tab1, width=12, textvariable=Municipio)
Sel_Municipio['values'] = ('Zinapecuaro','Querendaro','Indaparapeo','Alvaro Obregon')
Sel_Municipio.grid(column=1, row=6)
#Boton_Registrar
accion=ttk.Button(tab1,text="Imprimir", command=funcion_click)
accion.grid(column=1, row=13)
accion2=ttk.Button(tab2,text="Imprimir", command=funcion_click2)
accion2.grid(column=2, row=13)
#CheckButtons
ttk.Label(tab2, text= "Pasatiempos"). grid(column=1, row=7)
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
chk = tk.Checkbutton(tab2, text="Futbol", variable=var1)
chk.grid(column=0, row=8)
chk2 = tk.Checkbutton(tab2, text="Basketball", variable=var2)
chk2.grid(column=1,row=8)
chk3 = tk.Checkbutton(tab2, text="Musica", variable=var3)
chk3.grid(column=2,row=8)
chk4 = tk.Checkbutton(tab2, text="Programar", variable=var4)
chk4.grid(column=3,row=8)
chk5 = tk.Checkbutton(tab2, text="Leer", variable=var5)
chk5.grid(column=4,row=8)

#RadioButtons
ttk.Label(tab2, text= "Estado"). grid(column=1, row=9)
opcion = tk.IntVar()
texradio = ''
radio1 = tk.Radiobutton(tab2, text= "Soltero", variable= opcion, value=1)
radio1.grid(column=0,row=10)
radio2 = tk.Radiobutton(tab2, text= "Viudo", variable= opcion, value=2)
radio2.grid(column=1,row=10)
radio3 = tk.Radiobutton(tab2, text= "Casado", variable= opcion, value=3)
radio3.grid(column=2,row=10)
radio4 = tk.Radiobutton(tab2, text= "Divorciado", variable= opcion, value=4)
radio4.grid(column=3,row=10)
radio5 = tk.Radiobutton(tab2, text= "Es complicado", variable= opcion, value=5)
radio5.grid(column=4,row=10)
#Objetivo de la vida
ttk.Label(tab2, text = "Objetivo de la vida").grid(column = 0, row = 11)
objetivo = tk.StringVar()
preguntar_objetivo = ttk.Entry(tab2, width = 20, textvariable = objetivo)
preguntar_objetivo.grid(column = 1, row=11)


ventana.mainloop() 
