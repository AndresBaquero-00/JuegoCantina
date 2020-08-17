import pygame
from .Producto import *
from .Iteradores.IteradorCliente import *

class Cliente(Producto):
    clientes = []

    #Crea al cliente con sus propiedades
    def crear(self, barra, i):
        self.barra = barra
        if(barra == 0):
            self.x = 0 + 30*i
            self.y = 8
            self.temp = 0
        elif(barra == 1):
            self.x = -10 + 30*i
            self.y = 45
            self.temp = -10
        elif(barra == 2):
            self.x = -20 + 30*i
            self.y = 90
            self.temp = -20
        elif(barra == 3):
            self.x = -30 + 30*i
            self.y = 145
            self.temp = -30
        else:
            self.x = -100
            self.y = 8
            self.temp = -100

        self.tomar = False
        self.satisfecho = False
        self.cont = 0
        self.cliente = pygame.image.load("Imagenes/Cliente/Cliente.png")
        self.tomando = pygame.image.load("Imagenes/Cliente/Tomando.png")
        self.gameOver = False

    #Mueve al cliente
    def mover(self, num):
        self.x += num

    #Retorna la barra en la que entró el cliente
    def getBarra(self):
        return self.barra

    #Retorna la posicion en X de la barra
    def getPosX(self):
        return self.x

    def getTomar(self):
        return self.tomar

    def tomarCerveza(self, tomar):
        self.tomar = tomar

    def getIterador(self):
        cliente = Cliente()
        cliente.crear(0, 0)
        return IteradorCliente(cliente)
    
    #Dibuja al cliente
    def dibujar(self, pantalla):
        if(self.x < 210):
            if(not self.tomar):
                pantalla.blit(self.cliente, (self.x, self.y))
                self.gameOver = False
            else:
                pantalla.blit(self.tomando, (self.x, self.y-17))
                self.tomar = True
        else:
            self.gameOver = True

    def getGameOver(self):
        return self.gameOver

    #Clona al cliente
    def clone(self, barra, i):
        cliente = Cliente()
        cliente.crear(barra, i)
        self.clientes.append(cliente)

    def eliminar(self):
        for i in range(len(self.clientes)):
            self.clientes.pop()