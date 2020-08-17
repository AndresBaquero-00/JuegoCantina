from .Creador import *
from .Productos.Cerveza import *

class CreadorCerveza(Creador):

    def factoryMethod(self):
        return Cerveza()