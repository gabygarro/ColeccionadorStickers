
from juego import *

def adquirir(main, username):
    #funcion para seleccionar el coleccionador que se quiere adquirir
    #try:
        if 'Coleccionadores' not in os.listdir(os.getcwd()) or ('Coleccionadores' in os.listdir(os.getcwd()) and os.listdir('Coleccionadores')==[]):
            message.showerror(master=main, message='No existen coleccionadores')
            return False
        else:
            os.chdir(fdialog.askdirectory(master=main, initialdir='Coleccionadores', title='Entre en la carpeta del album que desea y presione OK'))
            f=open('configs','r')
            configs=read(f)
        
        if configs[0]=='1':
            #ya el album fue guardado como definitivoiere
            if not 'album_'+username+'.txt' in os.listdir(os.getcwd()):
                albumUsuario=open('album_'+username+'.txt', 'w')
                albumUsuario.write('0'+'\n'+'1')
                albumUsuario.close()
                repetidasUsuario=open('repetidas_'+username+'.txt', 'w')
                repetidasUsuario.close()
                os.chdir(os.path.dirname(os.getcwd()))
                os.chdir(os.path.dirname(os.getcwd()))
                message.showinfo(master=main, message='Se ha adquirido el ejemplar con exito', title=':D')
                
            else:
                os.chdir(os.path.dirname(os.getcwd()))
                os.chdir(os.path.dirname(os.getcwd()))
                message.showerror(master=main, title='Ya tiene uno', message='Usted ya tiene un ejemplar de este coleccionador; y solo puede tener uno')
        else:
            os.chdir(os.path.dirname(os.getcwd()))
            os.chdir(os.path.dirname(os.getcwd()))
            message.showerror(master=main, title='Album aun es editable', message='El album aun no ha sido establecido como definitivo. Vaya al editor y establezcalo como definitivo')
            return False
    #except:
     #   pass
        
        
    

def jugar(username):
    #menu de juego, con los botones y labels
    bgColor='#fff'
    main=tk.Tk()
    main.geometry('300x300+0+0')
    main.config(bg=bgColor)
    main.title('Usar los albumes existentes')
    tk.Label(main,bg=bgColor, text='Usuario actual: '+username).place(x=2, y=3)
    tk.Label(main, bg=bgColor,text='Seleccione una opcion').place(x=2, y=30)
    tk.Button(main, fg='#fff',bg='#e50f5f', text='Adquirir un nuevo coleccionador', command=lambda:adquirir(main, username)).place(x=2, y=60)
    tk.Button(master=main, bg='#e1e1e1', text='Jugar con un coleccionador', command=lambda:jugarColec(main, username)).place(x=2, y=90)
    main.mainloop()
