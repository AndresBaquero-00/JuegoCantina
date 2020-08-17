import pygame
from .Producto import *

class Cantinero(Producto):
    #Crea el cantinero con sus propiedades
    def crear(self):
        self.x = 257
        self.y = 17
        self.barra = 0
        self.vidas = 3

        self.cantinero = pygame.image.load("Imagenes/Cantinero/Cantinero.png")
        self.perder = pygame.image.load("Imagenes/Cantinero/Perdido.png")
        self.ganador = pygame.image.load("Imagenes/Cantinero/Ganador.png")

    #Mueve el cantinero por todo el bar
    def mover(self, dir):
        #Se mueve al cantinero de barra según la tecla oprimida
        if(dir == 0):
            self.barra = self.barra+1
        else:
            self.barra = self.barra-1
        
        #Se verifica que la barra en la que esté el cantinero no supere los limites
        if(self.barra > 3):
            self.barra = 0
        if(self.barra < 0):
            self.barra = 3
        
        #Se asigna la posición de acuerdo a la barra que se encuentre el cantinero
        if(self.barra == 0):
            #Primer barra
            self.x = 257
            self.y = 17
        elif(self.barra == 1):
            #Segunda barra
            self.x = 262
            self.y = 50
        elif(self.barra == 2):
            #Tercera barra
            self.x = 267
            self.y = 90
        elif(self.barra == 3):
            #Cuarta barra
            self.x = 275
            self.y = 145

    #Se dibuja el cantinero
    def dibujar(self, pantalla):
        pantalla.blit(self.cantinero, (self.x, self.y))

    #Se dibuja el cantinero
    def dibujarPerdido(self, pantalla):
        pantalla.blit(self.perder, (self.x, self.y))

    #Se dibuja el cantinero
    def dibujarGanador(self, pantalla):
        pantalla.blit(self.ganador, (self.x, self.y))

    def getBarra(self):
        return self.barra
   