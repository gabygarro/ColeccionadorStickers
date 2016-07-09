# -*- coding: utf-8 -*-
class Postal:
	def __init__(self, n):
		self.nombre=n
		self.estado=0

	def adquirida(self):
		self.estado=1


def matrizObjetosPostal(listaPostales, album):
	#funcion que convierte la matriz con 1's y 0's en una matriz llena de objetos Postal
	c=1
	pagina=0
	row=0
	pos=0
	
	for pag in album:
	    for fila in pag:
	        for postal in fila:
	            if postal==0:
	            	#los elementos 0 (celdas dispoibles del album) se cambian por objetos Postal
	                postal=Postal(str(c))
	                album[pagina][row][pos]=postal
	                
	                if str(c) in listaPostales:
	                	#si el usuario tiene esa postal entre la lista de las que posee
	
	                	postal.adquirida()
	                c+=1
	            pos+=1
	        pos=0
	        row+=1
	    pagina+=1
	    row=0

	"""
	for pag in album:
		for fila in pag:
			for postal in fila:
				if postal!=1:
					if postal.estado==1:
					print('tengo la número '+postal.nombre)
	print(album)
	"""
	print('transformado a matriz de objetos')
	return album
