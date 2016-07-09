
from creador import *
from editor import *
from definitivo import *

def definitivo(menu):
    try:
        menu.withdraw()
        listaDir=os.listdir('Coleccionadores')#lista de directorios y archivos dentro de la carpeta "Coleccionadores"
        if listaDir==[]:#si no hay nada-->No hay coleccionadores
            messagebox.showerror(master=menu, title='No hay coleccionadores', message='No has creado ningun coleccionador')
        else:
            folder=tkdir.askdirectory(master=menu,initialdir='Coleccionadores',title='Entre a la carpeta del coleccionador y haga clic en OK', )
            guardarComoDefinitivo(folder, menu)
    except:
        menu.deiconify()
    
def crear(menu):
    menu.withdraw()
    creador(menu)
    menu.destroy()
    #menu.deiconify()


def editar(menu):
    menu.withdraw()
    listaDir=os.listdir('Coleccionadores')#lista de directorios y archivos dentro de la carpeta "Coleccionadores"
    if listaDir==[]:#si no hay nada-->No hay coleccionadores
        messagebox.showerror(master=menu, title='No hay coleccionadores', message='No has creado ningun coleccionador')
    else:
        folder=tkdir.askdirectory(master=menu,initialdir='Coleccionadores',title='Entre a la carpeta del coleccionador y haga clic en OK', )
        editor(folder, listaDir, menu)
    #menu.deiconify()
        
    

    
def menuEC(vent):
    vent.destroy()
    menu=tk.Tk()
    #crear(menu)
    menu.resizable(width=False, height=False)
    menu.config(bg='white')
    menu.geometry('400x400')
    menu.title('Menu de Coleccionadores')
    
    tk.Label(menu, text='Escoja una accion a realizar', font=('Comic Sans','10'), bg='white').place(x=1,y=1)
    tk.Button(menu, bg='#6AC8E7',text='Crear album nuevo',font=('Comic Sans','10'),fg='black', command=lambda:creador(menu)).place(x=1, y=65)
    tk.Button(menu, bg='#3AAACF',text='Editar un album existente',font=('Comic Sans','10'),fg='black',command=lambda:editar(menu)).place(x=1, y=100)
    tk.Button(menu, bg='#3A6ACF',text='Guardar un album como definitivo',font=('Comic Sans','10'),fg='black',command=lambda:definitivo(menu)).place(x=1, y=135)
    tk.Button(menu, text='Jugar', bg='#7fdfE7', command=lambda:juego()).place(x=1, y=30)
    
    menu.mainloop()

#menuEC()
