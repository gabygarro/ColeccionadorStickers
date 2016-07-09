from abrirSobres import *

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


def coleccionar(main, username, album, colorDeFondo, celdasLibres, carpetaPostales):
    main.withdraw()
    pygame.init()
    listaPostales=read(open('album_'+username+'.txt','r'))
    sobresAbiertos=int(listaPostales[len(listaPostales)-1])
    hora=int(listaPostales[len(listaPostales)-2])
    print(hora)
    listaPostales=listaPostales[:len(listaPostales)-2]

    listaRepetidas=read(open('repetidas_'+username+'.txt','r'))

    
    # print('listaPostales: '+str(listaPostales))

    # temporal:
    

    pag=0
    pagina=album[pag]

    paginas=len(album)
    filas=len(album[0])
    columnas=len(album[0][0])
    nombre=album[1]

    ANCHO=150#dimensiones fijas de las postales
    ALTO=175
    MARGEN=10

    #dimensiones de la pantalla:
    if columnas*(ANCHO+MARGEN)+20<(ANCHO+MARGEN)*3+20:
        anchoPantalla=(ANCHO+MARGEN)*3+20
    else:
        anchoPantalla=columnas*(ANCHO+MARGEN)+20
    altoPantalla=filas*(ALTO+MARGEN)+110

    #converitr la matriz album de unosy 0's a una con objetos 
    #cada objeto es una postal
    album=matrizObjetosPostal(listaPostales, album)


    pantalla=pygame.display.set_mode((anchoPantalla,altoPantalla))
    pygame.display.set_caption(str(os.path.basename(os.getcwd())))

    GRIS=(197,197,197)
    NEGRO= (0,0,0)
    BLANCO= ( 255, 255, 255)
    
    
    clock=pygame.time.Clock()#reloj del ciclo
    
    barraInferior=pygame.Surface([anchoPantalla,90])
    barraInferior.fill((255,255,255))
    
    
    # TextoColor=fuentePeq.render('Color',1,(255,255,255))
    #Colorear la pantalla
    if colorDeFondo==None: 
        colorDeFondo=(0,0,0)
    pantalla.fill(colorDeFondo)


    fuente=pygame.font.SysFont('Times',25)
    fuentePeq=pygame.font.SysFont('Times',19)


    #muestra mensaje
    mensaje=fuentePeq.render('Utilice las flechas del teclado para desplazarse por las paginas',1,(0,0,0))

    
    boton=pygame.Surface((130,30))
    colorDeFondoInverso=(abs(255-colorDeFondo[0]),abs(255-colorDeFondo[1]),abs(255-colorDeFondo[2]))
    boton.fill(colorDeFondoInverso)

    nuevasPostales=fuentePeq.render('Nuevas Postales',1,colorDeFondo)
    
    

    terminado=False#regula el ciclo principal del juego
    # loop del juego

    while not terminado:
        pagina=album[pag]
        keys=pygame.key.get_pressed()
        #cantida de celdas para bloquear que quedan
        b=pantalla.blit(boton,(anchoPantalla-131,altoPantalla-70))

        for event in pygame.event.get():
            if event.type==QUIT:
                terminado=True
                os.chdir(os.path.dirname(os.getcwd()))
                os.chdir(os.path.dirname(os.getcwd()))
                pygame.quit()
                sys.exit()

            elif keys[pygame.K_LEFT] and pag>0:
                pag-=1     
            elif keys[pygame.K_RIGHT] and pag<paginas-1 :
                pag+=1
            elif keys[pygame.K_UP]:
                pag=paginas-1
            elif keys[pygame.K_DOWN]:
                pag=0  
            elif event.type==MOUSEBUTTONDOWN:         
                 if b.collidepoint(pygame.mouse.get_pos()):
                    if sobresAbiertos<3:
                        et=[]
                        for i in range(1,5):
                            numPos=str(random.randint(1,celdasLibres))
                            if numPos not in listaPostales:
                                listaPostales.append(numPos)
                                hora=tiempoSegundos(time.strftime("%H:%M:%S"))
                                guardarPostales('album_'+username+'.txt',listaPostales,hora,str(sobresAbiertos))
                            else:
                                listaRepetidas.append(numPos)
                                guardarPostales('repetidas_'+username+'.txt', listaRepetidas,None,None)
                            et.append(fuentePeq.render(numPos,1,colorDeFondoInverso))
                            for Pag in album: 
                                for fila in Pag:
                                    for postal in fila:
                                        if postal!=1:
                                            if postal.nombre==numPos:
                                                postal.adquirida()
                           
                        sobresAbiertos+=1
                    else:
                        if abs(tiempoSegundos(time.strftime("%H:%M:%S"))-hora)>=43200:
                            sobresAbiertos=0
                        else:
                            message.showinfo(master=main, title='Ya no mas',message='Ya no puede abrir mas sobres. Tiene que esperar al menos doce horas. Trate de tener paciencia')
                    
        
        #ciclo para mostrar las postales donde van

        for fila in range(filas):
            yPostal=(MARGEN+ALTO)*fila+MARGEN
            for columna in range(columnas):
                xPostal=(MARGEN+ANCHO)*columna+MARGEN
                pos=pagina[fila][columna]
                if pos!=1:
                    if pos.estado==1:
                        img=pygame.image.load(carpetaPostales+'/'+pos.nombre+'.gif')
                        pantalla.blit(img,(xPostal, yPostal))
                    else:
                        numero=fuentePeq.render(pos.nombre,1,(255,255,255))
                        pygame.draw.rect(pantalla,GRIS,(xPostal,yPostal,ANCHO,ALTO),0)
                        pantalla.blit(numero,(xPostal+ANCHO//2,yPostal+ALTO//2))
                else:
                    pygame.draw.rect(pantalla,colorDeFondo,(xPostal,yPostal,ANCHO,ALTO),0)

        

        numeroPag=fuente.render(str(pag+1),1,(0,0,0))
        
        
        pantalla.blit(barraInferior,(0, altoPantalla-50))
        pantalla.blit(numeroPag, (anchoPantalla-30, altoPantalla-25))
        pantalla.blit(mensaje, (0, altoPantalla-20))
        # pygame.draw.line(pantalla,colorDeFondoInverso,(columnas*(ANCHO+MARGEN)+MARGEN,0),(columnas*(ANCHO+MARGEN)+MARGEN,altoPantalla),2)
        if sobresAbiertos==1:
            pass
        boton.blit(nuevasPostales,(5,1))
        pygame.display.update()  
        clock.tick(10)