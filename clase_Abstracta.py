from abc import ABC, abstractmethod
#clases abstractas para que el programa pueda crear instancias de las clases hijas
class Expresion(ABC):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    @abstractmethod
    def operar(self, arbol):
        pass

    @abstractmethod
    def getFila(self):
        return self.fila

    @abstractmethod
    def getColumna(self):
        return self.columna