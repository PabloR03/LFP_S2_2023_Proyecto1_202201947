from clase_Abstracta import Expresion
#Hereda de la clase abstracta, se encarga de guardar el lexema para lo que sobre sea un error
class palabra_Lexema(Expresion):
    def __init__(self, lexema, fila, columna):
        self.lexema = lexema
        super().__init__(fila, columna)

    def operar(self, arbol):
        return self.lexema

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()
#Escribe los errores en el archivo de salida, pero antes los almacena en una lista
class palabra_Error(Expresion):
    def __init__(self, lexema, fila, columna):
        self.lexema = lexema
        super().__init__(fila, columna)
    def operar(self, no):
        no_ = f'\t\t"error no.":{no}'+','+'\n'
        desc = '\t\t"descripcion":{\n'
        lex = f'\t\t\t"lexema de error": "{self.lexema}"'+','+'\n'
        tipo = '\t\t\t"tipo": "error lexico"'+','+'\n'
        fila = f'\t\t\t"fila": {self.fila}\n'
        columna = f'\t\t\t"columna": {self.columna}'+','+'\n'
        fin = "\t\t}\n"
        return '\t{\n' + no_ + desc + lex + tipo + columna + fila + fin + '\t}'
    def getColumna(self):
        return super().getColumna()
    def getFila(self):
        return super().getFila()
