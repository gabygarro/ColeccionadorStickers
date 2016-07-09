import os
import pygame
import sys
from pygame.locals import *
import Tkinter as tk
import tkMessageBox as message
import tkColorChooser as tkcolor
import shutil
import tkFileDialog as fdialog
from Postal import *
import time
import random

def guardarPostales(nombre, lista, hora, sobres):
	archivo=open(nombre,'w')
	for postal in lista:
		archivo.write(str(postal)+'\n')
	if hora!=None:
		archivo.write(str(hora)+'\n')
	if sobres!=None:
		archivo.write(str(sobres))
	archivo.close()

def tiempoSegundos(string):
	return ((int(string[0:2])*60*60)+(int(string[3:5])*60)+int(string[6:8]))

