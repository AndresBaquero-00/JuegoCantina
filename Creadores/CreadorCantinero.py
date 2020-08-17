from .Creador import *
from .Productos.Cantinero import *


class CreadorCantinero(Creador):

    def factoryMethod(self):
        return Cantinero()