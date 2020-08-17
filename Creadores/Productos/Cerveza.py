import pygame
from .Producto import *
from .Iteradores.IteradorCerveza import *

class Cerveza(Producto):

    cervezas = []

    #Crea todas las propiedades de la cerveza
    def crear(self, barra):
        #Se crea la cerveza de acuerdo la barra en la que va a ser servida
        self.barra = barra
        if(barra == 0):
            self.x = 210
            self.y = 0
            self.temp = -10
        elif(barra == 1):
            self.x = 215
            self.y = 40
            self.temp = -20
        elif(barra == 2):
            self.x = 220
            self.y = 87
            self.temp = -40
        elif(barra == 3):
            self.x = 223
            self.y = 140
            self.temp = -60
        else:
            self.x = -100
            self.y = 0

        #Sprites de la cerveza y el vaso
        self.cerveza = pygame.image.load("Imagenes/Cerveza/Cerveza.png")
        self.roto = pygame.image.load("Imagenes/Cerveza/Roto.png")

        self.gameOver = False

    #Movimiento de la cerveza
    def mover(self, num):
        self.x -= num

    #Retorna la barra en la que entró el cliente
    def getBarra(self):
        return self.barra

    #Retorna un iterador para controlar las cervezas
    def getIterador(self):
        cerveza = Cerveza()
        cerveza.crear(0)
        return IteradorCerveza(cerveza)

    #Retorna la posicion en X de la barra
    def getPosX(self):
        return self.x

    #Dibuja la cerveza en pantalla
    def dibujar(self, pantalla):
        if(self.x > self.temp):
            pantalla.blit(self.cerveza, (self.x, self.y))
            self.gameOver = False
        else:
            self.gameOver = True

        if(self.gameOver):
            pantalla.blit(self.roto, (self.x, self.y))

    #Retorna un valor booleano en caso de que la cerveza se rompa
    def getGameOver(self):
        return self.gameOver

    #Clona la cerveza
    def clone(self, barra):
        cerveza = Cerveza()
        cerveza.crear(barra)
        self.cervezas.append(cerveza)

    def eliminar(self):
        for i in range(len(self.cervezas)):
            self.cervezas.pop()