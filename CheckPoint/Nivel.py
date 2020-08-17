from .Memento import *

class Nivel:

    def __init__(self, clientes):
        self.clientes = clientes
    
        self.nivel = 0

    def setMemento(self, memento):
        self.memento = memento

    def createMemento(self):
        return Memento(self.clientes, self.nivel)
    
    def getNivel(self):
        return self.nivel

    def setNivel(self, nivel):
        self.nivel = nivel

    def sumarNivel(self):
        self.nivel += 1

    def setClientes(self, clientes):
        self.clientes = clientes

    def getClientes(self):
        return self.clientes

    def cambiarNivel(self):
        self.clientes.eliminar()

        algo = -1
        for i in range(self.nivel):
            if(i % 4 == 0):
                algo += 1
            self.clientes.clone(i % 4, algo)

        
        