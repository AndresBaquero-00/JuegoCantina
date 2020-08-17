class Memento:

    def __init__(self, clientes, nivel):
        self.clientes = clientes
        self.nivel = nivel

    def getClientes(self):
        return self.clientes

    def getNivel(self):
        return self.nivel

    def setClientes(self, clientes):
        self.clientes = clientes

    def setNivel(self, nivel):
        self.nivel = nivel