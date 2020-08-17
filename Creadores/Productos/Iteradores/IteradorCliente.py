from .Iterador import *

class IteradorCliente(Iterador):
    
    def __init__(self, cliente):
        self.cliente = cliente
        self.posicion = 0

    def primero(self):
        obj = None
        if(len(self.cliente.clientes) > 0):
            self.posicion = 0
            obj = self.cliente.clientes[0]
        return obj

    def siguiente(self):
        obj = None
        if((self.posicion) < len(self.cliente.clientes)):
            obj = self.cliente.clientes[self.posicion]
            self.posicion += 1
        return obj

    def hayMas(self):
        ok = False
        if((self.posicion) < len(self.cliente.clientes)):
            ok = True
        return ok

    def actual(self):
        obj = None
        if((self.posicion) < len(self.cliente.clientes)):
            obj = self.cliente.clientes[self.posicion]

        return obj


