from clase_Abstracta import Expresion

import math
from math import *
#clase de valor numero, se encarga de guardar el valor numerico para efectuar las operaciones
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

#clase de valor cadena, se encarga de guardar el valor cadena para efectuar las operaciones de tipo trigonometricas
class trigonometricas(Expresion):

    def __init__(self, left, tipo, fila, columna):
        self.left = left
        self.tipo = tipo

        super().__init__(fila, columna)
    #metodo que se encarga de realizar las operaciones trigonometricas, usa los arboles para obtener el valor de la expresion
    def operar(self, arbol):
        leftValue = ''
        #se obtiene el valor de la expresion
        if self.left != None:
            leftValue = self.left.operar(arbol)

        if self.tipo.operar(arbol) == 'seno':
            # usa radianes y aproxima para evitar grandes cadenas de numeros
            resultado = math.sin(math.radians(leftValue))
            resultado = round(resultado, 2)

            return resultado

        elif self.tipo.operar(arbol) == 'coseno':

            # usa radianes y aproxima para evitar grandes cadenas de numeros
            resultado = math.cos(math.radians(leftValue))
            resultado = round(resultado, 2)

            return resultado

        elif self.tipo.operar(arbol) == 'tangente':

            # usa radianes y aproxima para evitar grandes cadenas de numeros
            resultado = math.tan(math.radians(leftValue))
            resultado = round(resultado, 2)

            return resultado

        else:
            return None
        #se obtienen las filas y columnas para luego ser usadas en el reporte
    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()

class aritmeticas(Expresion):
    #clase de valor aritmetico, se encarga de guardar el valor aritmetico para efectuar las operaciones
    def __init__(self, left, right, tipo, fila, columna):
        self.left = left
        self.right = right
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        leftValue = ''
        rightValue = ''
        #el != None se usa para no operar con valores nulos
        if self.left != None:
            leftValue = self.left.operar(arbol)
        #se efectuan las operaciones con las palabras reservadas ya cargadas en mis listas
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