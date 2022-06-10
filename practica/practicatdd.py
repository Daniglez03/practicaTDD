class Contador():
    def __init__(self, inicial = 0, incremento = 1, limite = None, valorAct = 0):
        self.inicio = inicial
        self.incremento = incremento
        self.limite = limite
        self.valorAct = valorAct

    def __inicio__(self):
        return self.inicio

    def __incremento__(self):
        return self.incremento

    def __limite__(self):
        return self.limite

    def __incrementar__(self):
        self.inicio = self.inicio + self.incremento
        if self.valorAct > self.limite:
            print("Se ha superado el límite")
            self.valorAct = self.inicio
            
    def __valorActual__(self):
        return self.valorAct
