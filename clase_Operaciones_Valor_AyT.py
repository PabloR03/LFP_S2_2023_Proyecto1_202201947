from clase_Abstracta import Expresion

import math
from math import *

class valor_Numero(Expresion):
    def __init__(self, valor, fila, columna):
        self.valor = valor
        super().__init__(fila, columna)

    def operar(self, arbol):
        return self.valor

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()

class trigonometricas(Expresion):

    def __init__(self, left, tipo, fila, columna):
        self.left = left
        self.tipo = tipo

        super().__init__(fila, columna)

    def operar(self, arbol):
        leftValue = ''

        if self.left != None:
            leftValue = self.left.operar(arbol)

        if self.tipo.operar(arbol) == 'seno':
            # se convierte a radianes y se redondea a 2 decimales
            resultado = math.sin(math.radians(leftValue))
            resultado = round(resultado, 2)

            return resultado

        elif self.tipo.operar(arbol) == 'coseno':

            # se convierte a radianes y se redondea a 2 decimales
            resultado = math.cos(math.radians(leftValue))
            resultado = round(resultado, 2)

            return resultado

        elif self.tipo.operar(arbol) == 'tangente':

            # se convierte a radianes y se redondea a 2 decimales
            resultado = math.tan(math.radians(leftValue))
            resultado = round(resultado, 2)

            return resultado

        else:
            return None

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()

class aritmeticas(Expresion):

    def __init__(self, left, right, tipo, fila, columna):
        self.left = left
        self.right = right
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        leftValue = ''
        rightValue = ''

        if self.left != None:
            leftValue = self.left.operar(arbol)

        if self.right != None:
            rightValue = self.right.operar(arbol)

        if self.tipo.operar(arbol) == 'suma':

            resultado = leftValue+rightValue

            return resultado

        elif self.tipo.operar(arbol) == 'resta':

            resultado = leftValue - rightValue

            return resultado

        elif self.tipo.operar(arbol) == 'multiplicacion':

            resultado = leftValue * rightValue

            return resultado

        elif self.tipo.operar(arbol) == 'division':

            resultado = leftValue / rightValue

            return resultado

        elif self.tipo.operar(arbol) == 'modulo':

            resultado = leftValue % rightValue

            return resultado
        
        elif self.tipo.operar(arbol) == 'mod':

            resultado = leftValue % rightValue

            return resultado

        elif self.tipo.operar(arbol) == 'potencia':

            resultado = leftValue ** rightValue

            return resultado

        elif self.tipo.operar(arbol) == 'raiz':

            resultado = leftValue ** (1/rightValue)

            return resultado

        elif self.tipo.operar(arbol) == 'inverso':

            resultado = 1/leftValue

            return resultado

        else:
            return None

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()