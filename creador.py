# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-
import Tkinter as tk
import tkMessageBox as messagebox
import os
import tkFileDialog as tkdir
from shutil import rmtree



carpetas=os.listdir(os.getcwd())#hace una lista con los directorios que estan dentro del directorio en que se encuentra el presente archivo
if 'Coleccionadores' not in carpetas:#Si nunca se ha creado un coleccionador y no existe la carpeta donde deben ser guardados. Si ya existe, apsa esta condicion
    os.mkdir('Coleccionadores')#la crea.


    
def crearColeccionador(paginas, filas, columnas):#crea una matriz de matrices
    colec=[]
    for i in range(paginas):
        colec.append([])
        for j in range(filas):
            colec[i].append([])
            for k in range(columnas):
                colec[i][j].append(0)
    return colec
        

def creaColeccionador(vent,name, pags, rows, columns, folder, menu):#funcion encargada de capturar los datos de entrda en la ventada de mas abajo
    try:
        carpeta=folder.get()
        nombre=name.get()#nombre del coleccionador
        paginas=int(pags.get())#cantidad de paginas, debe ser un numero entnero
        filas=int(rows.get())#cantidad de filas
        columnas=int(columns.get())#de columnas
        dimensionPagina=filas*columnas
        celdas=dimensionPagina*paginas#esta da la cantidad de celdas que va a tener el coleccionador, aun no se quitan las que se vzna  bloquear
        if 70<=celdas<=100:#rango de celdas permitidas
            if filas<=3 and columnas<=7:
                try:
                    os.chdir('Coleccionadores')
                    if not os.path.isdir(str(nombre)):#Si en la carpeta 'Coleccionadores' no existe un coleccionador con el nombre que se escogio
                            os.mkdir(str(nombre))#crea la carpeta con ese nombre para el nuevo coleccionador
                            os.chdir(str(nombre))#se mueve a esa carpeta para empezar a guardar las configuraciones del nuevo coleccionador en esa carpeta
                            config=open('configs','w')
                            config.write('0\n'+str(nombre)+'\n'+str(paginas)+'\n'+str(filas)+'\n'+str(columnas)+'\n'+str(carpeta))
                            album=open('album.py','w')
                            album.write('album='+str(crearColeccionador(paginas,filas,columnas))+'\n'+'colorDeFondo=(0,0,0)'+'\n'+'matrizPostales=[]')        
                            vent.destroy()
                            menu.deiconify()
                            os.chdir(os.path.dirname(os.getcwd()))
                            os.chdir(os.path.dirname(os.getcwd()))
                            messagebox.showinfo(master=None, message=str(nombre)+'se ha creado de manera satisfactoria :D')
                
                    else:#si ya existe, entonces solo queda informar que ya ese nombre ha sido escogido
                        messagebox.showerror(master=vent, title='Coleccionador ya existente',message='Ya existe un coleccionador con el nombre '+str(nombre))#informa que ya existe un coleccionador con ese nombre
                        os.chdir(os.path.dirname(os.getcwd()))##Se devuelve a la carpeta donde esta alojado este archivo
                except:
                    os.chdir(os.path.dirname(os.getcwd()))
                    if os.path.isdir(str(nombre)):
                        rmtree(str(nombre))
            else:
                messagebox.showerror(master=vent, title='Dimensiones incorrectas0',message='Las paginas deben tener un maximo de 3 filas y 7 columnas')                
        else:
            messagebox.showerror(master=vent, title='Cantidad inadecuada de celdas',message=str(celdas)+' postales no es una cantidad aceptable para el coleccionador. Debe haber entre 70 y100, mi vida.')
                
    except ValueError:
        messagebox.showerror(master=vent, title='Datos erroneos', message='Los datos ingresados son invalidos')


def escogerCarpeta(folder):#funcion para buscar la carpeta de almancenamiento de las imagenes
    #folder.set(tkdir.askDire
    carpeta=tkdir.askdirectory()#initialdir='/home/daniel')
    folder.set(carpeta)
    
def volver(vent, menu):#vuelve al menu de edicion de coleccionadores
    vent.destroy()
    menu.deiconify()
    

def creador(menu):      #esta duncion crea la ventana con las diferentes campos para insertar las oncfiguraciones del album
    vent=tk.Toplevel(master=menu)#es la ventanan la que se va a configurar el formato de el album (filas, columnas, cant paginas)
    vent.geometry('320x500')###configuraciones de la ventana
    vent.title('Creacion de nuevo coleccionador')
    color='#bbeee8'
    vent.config(bg=color)
    vent.resizable(width=None, height=None)###

    cordY=140
    #Entradas de losparametros para el coleccionador y las etiquetas correspondientes
    tk.Label(master=vent, text='Inserte las configuraciones del album',bg=color).place(x=5,y=10)
    tk.Label(master=vent, text='Nombre del coleccionador: ',bg=color).place(x=5,y=cordY)
    name=tk.Entry(master=vent)
    name.place(x=5,y=cordY+20)
    tk.Label(master=vent, text='Numero de paginas: ',bg=color).place(x=5,y=cordY+50)
    pags=tk.Entry(master=vent)
    pags.place(x=5,y=cordY+70)

    tk.Label(master=vent, text='Numero de filas por pagina: ',bg=color).place(x=5,y=cordY+100)
    rows=tk.Entry(master=vent)
    rows.place(x=5,y=cordY+120)

    tk.Label(master=vent, text='Numero de columnas por pagina: ',bg=color).place(x=5,y=cordY+150)
    columns=tk.Entry(master=vent)
    columns.place(x=5,y=cordY+170)

    tk.Label(master=vent, text='Carpeta donde estan las imagenes', bg=color).place(x=7, y=cordY+200)
    folder=tk.StringVar()
    tk.Label(master=vent, textvariable=folder, bg='#b5b5b5').place(x=7, y=cordY+220)
    tk.Button(master=vent, bg='#e9e9ab', text='Buscar directorio', command=lambda:escogerCarpeta(folder)).place(x=7, y=cordY+240)

    #etiqueta de especificaciones:
    tk.Label(master=vent, justify=tk.LEFT, text='Especificaciones: \n 1.Debe haber entre 70 y 100 postales. \n 2. La cantidad de postales debe coincidir \n      con la de la imagenes carpeta. \n 3. El máximo de filas es de 3.\n 4. El máximo de columnas es de 7.', bg='white').place(x=5, y=30)
    
    ##Boton para capturar datos de las entradas
    tk.Button(master=vent, text='Crear Coleccionador', bg='#ff9a47',command=lambda:creaColeccionador(vent,name, pags,rows, columns, folder, menu)).place(x=120,y=cordY+300)

    
    tk.Button(takefocus=0,master=vent,text='Volver',bg='#e08234',command=lambda:volver(vent, menu)).place(x=7,y=cordY+300)
    vent.mainloop()
#from ModuloEdicionColeccionadores import *
