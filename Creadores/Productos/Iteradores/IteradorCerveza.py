from .Iterador import *

class IteradorCerveza(Iterador):
    
    def __init__(self, cerveza):
        self.cerveza = cerveza
        self.posicion = 0

    def primero(self):
        obj = None
        if(len(self.cerveza.cervezas) > 0):
            self.posicion = 0
            obj = self.cerveza.cervezas[0]
        return obj

    def siguiente(self):
        obj = None
        if((self.posicion) < len(self.cerveza.cervezas)):
            obj = self.cerveza.cervezas[self.posicion]
            self.posicion += 1
        return obj

    def hayMas(self):
        ok = False
        if((self.posicion) < len(self.cerveza.cervezas)):
            ok = True
        return ok

    def actual(self):
        obj = None
        if((self.posicion) < len(self.cerveza.cervezas)):
            obj = self.cerveza.cervezas[self.posicion]

        return obj


