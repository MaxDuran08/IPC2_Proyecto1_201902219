class Nodo:
    def __init__(self, Valor):
        self.Valor=Valor
        self.SiguienteValor=None
        #self.Posicion=None
        
        #Devolver el valor en forma de string
    def __str__(self):
        return str(self.Valor)