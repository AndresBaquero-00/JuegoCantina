import pygame
from pygame import *
from Creadores.Creador import *
from Creadores.CreadorCantinero import *
from Creadores.CreadorCerveza import *
from Creadores.CreadorCliente import *
from Creadores.Productos.Iteradores.IteradorCliente import *
from CheckPoint.Caretaker import *
from CheckPoint.Nivel import *

class Juego:
    creador = None
    #Permite que los personajes no hagan funciones si alguna tecla se mantiene pulsada
    pressed = False

    #Define el numero del nivel y si el jugador pasa de nivel
    nivel = False
    numNivel = 0

    #Estado que define si el jugador perdió el juego
    gameOver = True
    perderNivel = False

    #CheckPoint
    checkpoint = Caretaker()

    #Iteradores
    iteradorCliente = None
    iteradorCerveza = None

    #Puntos del juego
    puntos = 0

    def crearCerveza(self):
        #Crea las cervezas
        self.creador = CreadorCerveza()
        cerveza = self.creador.crearProducto()
        cerveza.crear(0)
        self.iteradorCerveza = cerveza.getIterador()
        return cerveza

    def crearCliente(self):
        #Crea los clientes
        self.creador = CreadorCliente()
        cliente = self.creador.crearProducto()
        cliente.crear(0, 0)
        self.iteradorCliente = cliente.getIterador()
        return cliente

    def crearCantinero(self):
        #Crea el cantinero
        self.creador = CreadorCantinero()
        cantinero = self.creador.crearProducto()
        cantinero.crear()
        return cantinero

    def hacerInicio(self):
        #Inicia pygame
        self.taberna = pygame.image.load("Cantina.png")
        self.inicio = pygame.image.load("Inicio.jpg")

    def sumarPuntos(self):
        self.puntos += 1