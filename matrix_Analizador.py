from clase_Operaciones_Valor_AyT import *
from clase_LexemayError import *
import os, webbrowser

# Lexemas usados como Palabras reservadas
lexemas=["operacion", "valor1", "valor2", "suma", "resta", "multiplicacion", "division", "potencia", "raiz", "inverso", "seno", "coseno", "tangente", "mod", "modulo", "texto", "fondo", "fuente", "forma", ",", ".", ":", "[", "]", "{", "}", "-"]

global n_linea
global n_columna
global comandos
global l_lexemas
global l_errores
global l_comandosG

n_linea = 1
n_columna = 0
l_lexemas = []
comandos = []
l_errores = []
l_comandosG = []


def fun_instruccion(cadena):
    global n_linea
    global n_columna
    global l_lexemas
    lexema = ""
    puntero = 0
    while cadena:
        char = cadena[puntero]
        puntero += 1
        # si se encuentra la comilla de apertura
        if char == '\"':
            # se envia al metodo la cadena sin la comilla inicial
            lexema, cadena = fun_construirLex(cadena[puntero:])
            # si no es None ninguna de las dos condiciones entonces
            if lexema and cadena:
                # +1 por la comilla de inicio
                n_columna += 1

                # Armado de lexema como clase
                l = palabra_Lexema(lexema, n_linea, n_columna)

                # se guarda el lexema en la lista
                l_lexemas.append(l)
                # +1 por la comilla final
                n_columna += len(lexema)+1
                puntero = 0

        elif char.isdigit():
            # no se recorta porque se estaria eliminando el primer numero
            token, cadena = fun_construirNum(cadena)

            if token and cadena:
                # n_columna += 1

                # Armado de lexema como clase
                n = valor_Numero(token, n_linea, n_columna)

                # se guarda el lexema en la lista
                l_lexemas.append(n)
                # +1 por la comilla final
                n_columna += len(str(token))
                puntero = 0

        elif char == '-':
            # no se recorta porque se estaria eliminando el primer numero
            token, cadena = fun_construirNum(cadena)

            if token and cadena:
                # n_columna += 1

                # Armado de lexema como clase
                n = valor_Numero(token, n_linea, n_columna)

                # se guarda el lexema en la lista
                l_lexemas.append(n)
                # +1 por la comilla final
                n_columna += len(str(token))
                puntero = 0

        elif char == "[" or char == "]":
            # Armado de lexema como clase
            pos_lexema = palabra_Lexema(char, n_linea, n_columna)

            n_columna += 1
            l_lexemas.append(pos_lexema)
            cadena = cadena[1:]
            puntero = 0

        elif char == "\t":
            cadena = cadena[4:]
            n_columna += 4
            puntero = 0

        elif char == "\n":
            cadena = cadena[1:]
            n_columna = 0
            n_linea += 1
            puntero = 0

        elif char == ' ' or char == '\r' or char == '{' or char == '}' or char == ',' or char == ':' or char == '.':
            cadena = cadena[1:]
            n_columna += 1
            puntero = 0
        else:
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1
            l_errores.append(palabra_Error(char, n_linea, n_columna))

    # for lexema in l_lexemas:
    #     print(lexema)

    return l_lexemas

def fun_construirLex(cadena):
    global n_linea
    global n_columna
    global l_lexemas
    lexema = ""
    puntero = ""
    # se recorre toda lacadena con el puntero hasta encontrar ["]
    for char in cadena:
        puntero += char
        if char == '\"':
            # en cadena el slicing devuelce desde el puntero hasta el final
            return lexema, cadena[len(puntero):]
        else:
            # se va agregando letra por letra al lexema
            lexema += char
    # para evitar que se detenga el problema en caso de un error
    return None, None

def fun_construirNum(cadena):
    numero = ''
    puntero = ''
    is_decimal = False
    isNegative = False

    for char in cadena:
        puntero += char

        if char == "-":
            isNegative = True

        if char == ".":
            is_decimal = True

        # se comprueba cuando es que termino de leer el numero
        if char == '"' or char == ' ' or char == '\n' or char == '\t' or char == ']' or char == ',':
            if is_decimal:
                # el -1 se agrega para que la cadena devuelta tenga el salto de linea (\n), para asi sumarle la fila
                return float(numero), cadena[len(puntero)-1:]
            if isNegative:
                return int(numero), cadena[len(puntero)-1:]
            else:
                return int(numero), cadena[len(puntero)-1:]

        # si aun no se a terminado de leer el numero se sigue armando
        else:
            numero += char
    return None, None

def operar():
    global l_lexemas
    global comandos
    operacion = ''
    n1 = ''
    n2 = ''
    # mientras exista una losta de lexemas se opera el while
    while l_lexemas:
        lexema = l_lexemas.pop(0)

        if lexema.operar(None) == 'operacion':
            operacion = l_lexemas.pop(0)
        elif lexema.operar(None) == 'valor1':
            n1 = l_lexemas.pop(0)
            if n1.operar(None) == '[':
                n1 = operar()  # se llama a el mismo hasta que devuelva un numero
        elif lexema.operar(None) == 'valor2':
            n2 = l_lexemas.pop(0)
            if n2.operar(None) == '[':
                n2 = operar()

        # se arma la operacion segun sea aritmetico o trigonometrica

        if operacion and n1 and n2:
            # print("Operacion===>", operacion.lexema)
            # print("N1===>", n1.operar(None))
            # print("N2===>", n2.operar(None))

            return aritmeticas(n1, n2, operacion, f'Inicio: {operacion.getFila()}: {operacion.getColumna()}', f'Fin: {n2.getFila()}:{n2.getColumna()}')

        elif operacion and n1 and (operacion.operar(None) == 'seno' or operacion.operar(None) == 'coseno' or operacion.operar(None) == 'tangente'):

            return trigonometricas(n1, operacion, f'Inicio: {operacion.getFila()}: {operacion.getColumna()}', f'Fin: {n1.getFila()}:{n1.getColumna()}')

    return None

# Antes de operar y eliminar los valores de la lista de lexemas, se guardan los datos para el grafico
def fun_lGrafico():
    global l_lexemas

    for i in range(len(l_lexemas)):
        lexema = l_lexemas[i]
        if lexema.operar(None) == 'texto':
            l_comandosG.append(l_lexemas[i+1].operar(None))
        if lexema.operar(None) == 'fondo':
            l_comandosG.append(l_lexemas[i+1].operar(None))
        elif lexema.operar(None) == 'fuente':
            l_comandosG.append(l_lexemas[i+1].operar(None))
        elif lexema.operar(None) == 'forma':
            l_comandosG.append(l_lexemas[i+1].operar(None))

def operar_():
    global comandos

    left = ""
    right = ""

    while True:

        operacion = operar()
        # se agregan los objetos que son operaciones a comandos
        if operacion:
            comandos.append(operacion)
        else:
            break

        # Se operan para obtener los resultados de las operaciones
        for fun_instruccion in comandos:
            fun_instruccion.operar(None)

    return comandos

def fun_grafico():

    titulo = l_comandosG[0]

    dot = 'digraph grafo{\n'

    for i in range(len(comandos)):
        dot += fun_AtributosyCrearGrafico(i, 0, '', comandos[i])

    dot += f'''
    labelloc = "t"
    label = "{titulo}"
    '''

    dot += '}'

    return dot

def fun_genGrafico(nombreGrafica):

    nombre = nombreGrafica+".dot"

    # Creación del dot
    with open(nombre, 'w') as f:
        f.write(fun_grafico())

    # creamos la imagen
    os.system(
        f'dot -Tpdf {nombre} -o {nombreGrafica}.pdf')

    # obtener direccion actual
    ruta = os.path.dirname(os.path.abspath(f"{nombreGrafica}.pdf"))

    # reta del pdf
    archivo_pdf = ruta+f"\{nombreGrafica}.pdf"

    path = f'file:///{archivo_pdf}'

    # Abrir pdf en el navegador
    webbrowser.open_new(path)

def fun_deleteL():
    comandos.clear()
    l_comandosG.clear()

def fun_deleteLE():
    global n_linea
    l_errores.clear()
    n_linea = 1

def fun_AtributosyCrearGrafico(i, id, etiqueta, objeto):

    global l_comandosG
    dot = ""
    colorFondo = l_comandosG[1]
    colorFuente = l_comandosG[2]
    forma = l_comandosG[3]
    if objeto:
        if type(objeto) == valor_Numero:
            # print(objeto.valor)
            dot += f'nodo_{i}{id}{etiqueta}[label="{objeto.operar(None)}",fontcolor="{colorFuente}",fillcolor={colorFondo}, style=filled,shape={forma}];\n' 
        if type(objeto) == trigonometricas:
            # print(objeto.valor)
            dot += f'nodo_{i}{id}{etiqueta}[label="{objeto.tipo.lexema}\\n{objeto.operar(None)}",fontcolor="{colorFuente}",fillcolor={colorFondo}, style=filled,shape={forma}];\n'  
            dot += fun_AtributosyCrearGrafico(i, id+1, etiqueta+"_angulo", objeto.left)
            # uniones de nodos
            dot += f'nodo_{i}{id}{etiqueta} -> nodo_{i}{id+1}{etiqueta}_angulo;\n'  
        if type(objeto) ==  aritmeticas:
            # print(objeto.tipo.lexema)
            # print(objeto.valor)
            dot += f'nodo_{i}{id}{etiqueta}[label="{objeto.tipo.lexema}\\n{objeto.operar(None)}",fontcolor="{colorFuente}",fillcolor={colorFondo}, style=filled,shape={forma}];\n'
            # print("sub izquierdo")    
            dot += fun_AtributosyCrearGrafico(i, id+1, etiqueta + "_left", objeto.left)
            # uniones de nodos
            dot += f'nodo_{i}{id}{etiqueta} -> nodo_{i}{id+1}{etiqueta}_left;\n'
            # print("Sub derecho")
            dot += fun_AtributosyCrearGrafico(i, id+1, etiqueta+"_right", objeto.right)    
            # uniones de nodos
            dot += f'nodo_{i}{id}{etiqueta} -> nodo_{i}{id+1}{etiqueta}_right;\n'   
    return dot

def fun_obtenerErrores():
    global l_errores
    formatoErrores = '{\n\t"errores":[\n'
    for i in range(len(l_errores)):
        error = l_errores[i]
        formatoErrores += error.operar(i+1)
        if i != len(l_errores)-1:
            formatoErrores += ',\n'
        else:
            formatoErrores += '\n'
    formatoErrores += '\t]\n}'
    return formatoErrores

def fun_Archivo_salida_errores():

    nombre = "RESULTADOS_202201947"+".json"

    # Creación del dot
    with open(nombre, 'w') as f:
        f.write(fun_obtenerErrores())

    # obtener direccion actual
    ruta = os.path.abspath(nombre)

    print(ruta)

    os.system(f'start notepad.exe {ruta}')