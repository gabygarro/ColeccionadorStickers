"""este modulo edita el archivo de configuraciones
para establecer el album como definitivo"""
import os
from editor import read
from editor import messagebox

def listaArchivo(lista,nombre):#es como la inversa de read: convierte la lista en el archivo de texto
    configs=open(str(nombre),'w')
    for i in lista:
        
        configs.write(str(i)+'\n')
    #configs=open('configs','r')

    
def guardarComoDefinitivo(folder, menu):
    os.chdir(folder)
    
    configs=open('configs','r')
    a=read(configs)#lista con las configuraciones
    os.remove('configs')
    a[0]='1'
    listaArchivo(a,'configs')
    os.chdir(os.path.dirname(os.getcwd()))
    os.chdir(os.path.dirname(os.getcwd()))
    menu.deiconify()
