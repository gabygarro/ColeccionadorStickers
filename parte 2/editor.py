import os
import pygame
import sys
from pygame.locals import *
import Tkinter as tk
import tkMessageBox as messagebox
import tkColorChooser as tkcolor
import shutil

pygame.init()

def read(f):#lee un archivo de texto y lo convierte en una lista(caad renglon es un elemento)
    List=[]#Esto se agrega para no tener una lista de usuarios inicialmente vacia
    string=''
    line=f.readline()#comienza en la primera linea
    while line!='':
        for letter in line:
            if letter!='\n':
                string+=letter
        List.append(string)
        line=f.readline()
        string=''
    return List
    
def crearPaginas(paginas, filas, columnas):
    colec=[]
    for i in range(paginas):
        colec.append([])
        for j in range(filas):
            colec[i].append([])
            for k in range(columnas):
                colec[i][j].append(0)
    return colec

def count(elem, m):
    """funcion para contar la cantidad de 1's (celdas
    bloqueadas dentro del coleccionadore"""
    c=0
    for i in m:
        for j in i:
            for k in j:
                if k==elem:
                    c+=1
    return c
def guardar(album, colorDeFondo):
    albumPy=open('album.py','w')
    albumPy.write('album='+str(album)+'\n'+'colorDeFondo='+str(colorDeFondo))
    albumPy=open('album.py','r')
    
def despliegue(nombre,paginas,filas,columnas,folderImagenes,colorDeFondo,menu,album):
    messagebox.showinfo(message='Cada cambio que haga se guarda de modo automatico')
    pygame.init()    
    pag=0
    pagina=album[pag]
    ANCHO=150#dimensiones fijas de las postales
    ALTO=175
    MARGEN=10
    anchoPantalla=columnas*(ANCHO+MARGEN)+10#tamano de la pantalla de acuerdo a la cantidad de postales
    if anchoPantalla<250:
        anchoPantalla=250#en caso de que sea solo una celda las etiquetas de texto no calzarian bien
    altoPantalla=filas*(ALTO+MARGEN)+100
    pantalla=pygame.display.set_mode((anchoPantalla,altoPantalla))
    pygame.display.set_caption(str(nombre))

    #se definen las dimensiones de las celdas
    #colores
    GRIS=(197,197,197)
    NEGRO= (0,0,0)
    BLANCO= ( 255, 255, 255)
    
    terminado=False#regula el ciclo principal del juego

    clock=pygame.time.Clock()#reloj del ciclo
    
    barraInferior=pygame.Surface([anchoPantalla,100])
    barraInferior.fill((0,0,0))
    
    
    
    fuente=pygame.font.SysFont('Times',40)
    fuentePeq=pygame.font.SysFont('Times',19)
    
    mensaje=fuentePeq.render('Utilice las flechas del teclado',1,(255,255,255))
    mensaje2=fuentePeq.render('para desplazarse por las paginas',1,(255,255,255))

    colorSurf=pygame.Surface([100,50])
    TextoColor=fuentePeq.render('Color',1,(255,255,255))
    
    """loop del juego"""
    while not terminado:
        
        bloqueadas=count(1, album)#cuenta la cantidad de celdas bloqueadas
        keys=pygame.key.get_pressed()
        #cantida de celdas para bloquear que quedan
        quedan=fuentePeq.render('Puede bloquear '+str(filas*columnas*paginas-70-bloqueadas),1,(255,255,255))
        
        try: #si el usuario cierra la ventana de elegir color sin seleccionar ningun color
            pantalla.fill(colorDeFondo)
            colorSurf.fill(colorDeFondo)
        except:
            pass
        
        for event in pygame.event.get():
            if event.type==QUIT:
                terminado=True
                os.chdir(os.path.dirname(os.getcwd()))
                os.chdir(os.path.dirname(os.getcwd()))
                pygame.quit()
                return album
                sys.exit()
       
            elif event.type==MOUSEBUTTONDOWN:
                posicion=pygame.mouse.get_pos()
                try: #en casi de que el usuario haga algo invaldo, el juego no se cae asi como asi
                    
                    #posiciones en la cuadricula
                    columna=posicion[0]//(ANCHO+MARGEN)
                    fila=posicion[1]//(ALTO+MARGEN)
                    
                    if pagina[fila][columna]==0:
                         
                         if (filas*columnas*paginas)-bloqueadas>70:
                            pagina[fila][columna]=1
                         else:
                           
                            messagebox.showerror(master=menu, title='Pare',message='Ya, ya no puede bloquear mas. No siga')
                    else:
                        pagina[fila][columna]=0
                    guardar(album, colorDeFondo)
                    
                except:
                    columna=posicion[0]
                    fila=posicion[1]
                    if columna>=(anchoPantalla-100) and fila>=(altoPantalla-100):
                        colorDeFondo=tkcolor.askcolor(title='Color de fondo')[0]
                        print(colorDeFondo)
                        guardar(album, colorDeFondo)
            elif keys[pygame.K_LEFT] and pag>0:
                pag-=1
                
            elif keys[pygame.K_RIGHT] and pag<paginas-1 :
                pag+=1
            elif keys[pygame.K_UP]:
                pag=paginas-1
            elif keys[pygame.K_DOWN]:
                pag=0
                      
                          
            pagina=album[pag]
            


            for fila in range(filas):
                for columna in range(columnas):
                    color=BLANCO
                    if pagina[fila][columna]==1:
                        color=GRIS
                    pygame.draw.rect(pantalla,color,
                                 [(MARGEN+ANCHO)*columna+MARGEN,
                          (MARGEN+ALTO)*fila+MARGEN,
                          ANCHO,ALTO],0)
            numero=fuente.render(str(pag+1),1,(255,255,255))
            
            pantalla.blit(barraInferior,(0, anchoPantalla-90))
            pantalla.blit(numero,(anchoPantalla//2-50,altoPantalla-50))
            pantalla.blit(mensaje,(5,altoPantalla-90))
            pantalla.blit(mensaje2,(5,altoPantalla-70))
            pantalla.blit(colorSurf,(anchoPantalla-100,altoPantalla-50))
            pantalla.blit(TextoColor,(anchoPantalla-90,altoPantalla-40))
            pantalla.blit(quedan,(7,altoPantalla-25))
            pygame.display.update()  
            clock.tick(100)


def getMatriz(nombre, menu):
        shutil.copy('Coleccionadores/'+str(nombre)+'/album.py','album.py')#crea una copia del archivo album en la carpeta donde estan los modulos
        from album import album,colorDeFondo
        return album,colorDeFondo
    


def editor(folder, listaDir, menu):
        nombre=os.path.split(folder)[1]
        album,colorDeFondo=getMatriz(nombre, menu)
        os.chdir(folder)
        configs=open('configs','r')
        configs=read(configs)
        
        bloqueado=int(configs[0])
        nombre=configs[1]
        paginas=int(configs[2])
        filas=int(configs[3])
        columnas=int(configs[4])
        folderImagenes=configs[5]
        if not bloqueado:
            album=despliegue(nombre,paginas,filas,columnas,folderImagenes,colorDeFondo,menu,album)
        else:
            messagebox.showinfo(title='No se puede editar', message='Este album ya es definitivo, y por eso no se puede modificar. Sorry')
        menu.deiconify()
        
        
        
        



pygame.quit()
