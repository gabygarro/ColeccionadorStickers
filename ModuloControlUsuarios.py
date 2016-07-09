# -*- coding: utf-8 -*-

from ModuloEdicionColeccionadores import *
from ModuloJuego import *

if 'usuarios.txt' not in carpetas:#variable carpetas es importada de otro modulo
    f=open('usuarios.txt','w')
    
f=open('usuarios.txt','r')


global usersList
usersList=read(f)
def Jugar(username, ventSeleccion):
    #esta funcion llama al modulo de uso de los coleccionadores
    ventSeleccion.destroy()
    jugar(username)


def verify(usersList, usernameEntry, passwordEntry, logWin):#verifica si el usuario concuerda con la contraseña
    password=passwordEntry.get()#"obtiene nombre de usuario"
    username=usernameEntry.get()#obtiene contraseña
    encontrado=False#esto es para saber si ya se encontro el nombredeuusario%contrasena que concuerdan con lo dado por el usuario
    for user in usersList: 
        if encontrado==False:#mientras no se haya encontrado
            if user==username+'%'+password:#los concatena y los compara con el usuario%contraseña en la usersList
                encontrado=True#reoporta que lo encontro
                logWin.destroy()#destruye la ventana de ingreso
                ventSeleccion=tk.Tk()
                ventSeleccion.config(bg='white')
                ventSeleccion.geometry('150x150+0+0')
                tk.Button(ventSeleccion, text='Crear y editar albumes', bg='#0fff0a', command=lambda:menuEC(ventSeleccion)).pack()
                tk.Button(ventSeleccion, text='Usar los albumes', bg='yellow', command=lambda:Jugar(username, ventSeleccion)).pack()#llama a esta funcion en el modulo de ediciond e coleccionadores
    if encontrado==False:#si al terminar el ciclo for no se encontro el usuario
        messagebox.showerror(master=None, message='usuario y contraseña no concuerdan')
    
def pantalla():#creay la ventana con entradas para nombre de usuario y contraseñas (se usa p' registro y para acceso)
    logWin=tk.Tk()
    logWin.geometry('300x150+0+0')
    logWin.config(bg='white')
    tk.Label(logWin,bg='white',text='username').grid(column=1,row=1)
    usernameEntry=tk.Entry(logWin)#entrada usuario
    usernameEntry.grid(column=2, row=1)
    logWin.resizable(width=False, height=False)
    passwordLabel=tk.Label(logWin,bg='white', text='contrasena').grid(column=1, row=2)
    passwordEntry=tk.Entry(logWin, show='*')#Entry contrasena
    passwordEntry.grid(column=2, row=2)
    def gotomenu():
        logWin.destroy()
        principalMenu()
    a=tk.Button(logWin,text='Menu', bg='red', fg='white',takefocus=0, command=lambda:gotomenu())
    a.grid(column=1, row=4)
    return (logWin,usernameEntry, passwordEntry,a)#esto
    
def login(usersList):
    principal.destroy()
    ventana=pantalla()
    username=ventana[1]
    password=ventana[2]
    ventana[3].grid(row=3, column=1)
    ventana=ventana[0]
    ventana.title('Ventana de ingreso')
    enterButton=tk.Button(ventana, text='Entrar', bg="blue", fg="white",
              command=lambda:verify(usersList,username, password, ventana))#boton de entrada
    enterButton.grid(column=2, row=3)
    
def clonar(m):
    nm=[]
    for i in range( len (m) ):
        nm.append ( m[i][:])
    return nm

def listaNombres(usersList):
    lisNom=clonar(usersList)
    pos=0
    for user in lisNom:
        
        lisNom[pos]=user[:user.index('%')]
        
        pos+=1
    return lisNom
    

def createUser(ventana, username, password, password2):#crear nuevo usuario
    global usersList
    lisNom=listaNombres(usersList)#obtiene solo los nombres de usuario (sin contraseña) a aprtir de la lisra de usuarios 
    username=username.get()#obtiene el texto escrito en la entrada de username
    pas=password.get()#obtiene la contraseña
    pas2=password2.get()#obtiene la verificacione de contrasenña
    terminado=False
    if username in lisNom:#ya el nombre de usuario esta escogido y no pueden haber repetidos
        print('usuario ya usado')#imprime a la terminal. borrar luego
        messagebox.showerror(title='Usuario ya existente', message='El username '+str(username)+' ya existe')
        terminado=True
        return False
    """Este ciclo es el encargado de crear el usuario si comple con las condidiones de no tener nombre o contraseña
    vacios; y que la contraseña y la contraseña de verificacion sean iguales"""
    while terminado==False:
        if username=='' :#si el username escogido es vacio
            messagebox.showerror(parent=ventana,title=' Username Invalido', message='El nombre de usuario es invalido')
            terminado=True
        elif  pas=='':#si la contraseña es vacia
            messagebox.showerror(parent=ventana,title='Contraseña Invalida', message='La contraseña es invalida')
            terminado=True
        elif pas==pas2:
            f=open('usuarios.txt','a')
            f.write(username+'%'+pas+'\n')
            f=open('usuarios.txt','r')
            usersList=read(f)#vuelve a leer usersList,a hora con el nuevo usuario creado
            messagebox.showinfo(parent=ventana,title='Registro completo', message='El usuario ha sido creado con exito')
            ventana.destroy()
            principal.deiconify()
            terminado=True#mata el ciclo
        else:
            messagebox.showerror(parent=ventana,title='error', message='Las contrasenas no coinciden')
            terminado=True

            
    
def sign(usersList):#funcion para sign up de nuevos usuarios
    principal.destroy()
    ventana=pantalla()
    username=ventana[1]
    password=ventana[2]
    ventana=ventana[0]
    ventana.title('Ventana de registro')
    password2=tk.Entry(ventana, show='*')
    password2.grid(column=2, row=3)#repetir contrasena
    tk.Label(ventana, text='repita la contraseña', bg='#fff').grid(row=3, column=1)
    tk.Button(ventana, text='Crear usuario', bg='#ffff00', command=lambda:createUser(ventana, username, password, password2)).grid(column=2, row=4)
    username.focus_set()

def principalMenu():
    print('ModuloControlUsuarios_principalMenu()')
    global principal
    principal=tk.Tk()
    principal.resizable(width=False, height=False)
    try:
        ventana.destroy()
    except:
        None
    principal.geometry('200x100+0+0')
    principal.config(bg='white')
    principal.title('Menu')
    
    pick=tk.Label(principal, text='Seleccione una accion a realizar:', bg='#fff').grid(row=1, column=1)
    
    logButton=tk.Button(principal, text='Acceder',bg="#00ff0f",bd=0,fg="black",
                  command=lambda:login(usersList))
    logButton.place(x=5, y=20)
    
    signButton=tk.Button(principal, text='Registrarse', bg="#000fff", fg="white",
                  command=lambda:sign(usersList))
    signButton.place(x=5, y=50)

    
    principal.mainloop()

    

principalMenu()

