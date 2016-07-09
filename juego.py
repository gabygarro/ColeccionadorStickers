from temporal import *

def jugarColec(main, username):
    #try:
        if 'Coleccionadores' not in os.listdir(os.getcwd()) or ('Coleccionadores' in os.listdir(os.getcwd()) and os.listdir('Coleccionadores')==[]):
            message.showerror(master=main, message='No existen coleccionadores')
            return False
        else:
            folder=fdialog.askdirectory(master=main, initialdir='Coleccionadores', title='Entre en la carpeta del album que desea abrir y presione OK')
            shutil.copy(folder+'/album.py','album.py')
            from album import album
            from album import colorDeFondo
            try:
                os.remove('album.py')
                os.remove('album.pyc')
            except:
                pass
            os.chdir(folder)        

        
        celdasLibres=0
        for pag in album:
            for fila in pag:
                for columna in fila:
                    if columna==0:
                        celdasLibres+=1
        print('celdasLibres: '+str(celdasLibres))
        
        if 'album_'+username+'.txt' not in os.listdir(os.getcwd()):
            message.showerror(master=main, title='compre un album', message='Usted no posee un ejemplar de este album, consigase uno, si quiere.')
            os.chdir(os.path.dirname(os.getcwd()))
            os.chdir(os.path.dirname(os.getcwd()))
            
        else:
            configs=read(open('configs','r'))
            dirPostales=configs[5]
            carpetaPostales=os.path.basename(dirPostales)
            # print('carpeta: '+carpetaPostales)
            # print('listdir: '+str(os.listdir(os.getcwd())))
            if not carpetaPostales in os.listdir(os.getcwd()):
                cantPostales=len(os.listdir(dirPostales))
                if cantPostales==celdasLibres:
                    # print('se ha pasado')
                    shutil.copytree(dirPostales, carpetaPostales)
                    shutil.rmtree(dirPostales)
                    message.showinfo(master=main,message='Las carpeta de postales se ha movido a '+os.getcwd())

                else:
                    os.chdir(os.path.dirname(os.getcwd()))
                    os.chdir(os.path.dirname(os.getcwd()))
                    message.showerror(master=main, message='La carpeta de postales tiene '+str(cantPostales)+' archivos pero el coleccionador '+str(configs[1])+' tiene espacio para '+str(celdasLibres)+' imagenes')
            else:
                print(os.getcwd())
                print('llama a coleccionar')
                coleccionar(main, username, album, colorDeFondo, celdasLibres, carpetaPostales)


            
        