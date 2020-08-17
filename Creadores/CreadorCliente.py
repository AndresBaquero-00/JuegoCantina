from .Creador import *
from .Productos.Cliente import *

class CreadorCliente(Creador):

    def factoryMethod(self):
        return Cliente()