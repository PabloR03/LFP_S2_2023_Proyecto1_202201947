from clase_Operaciones_Valor_AyT import *
from clase_LexemayError import *
import os, webbrowser

# Lexemas usados como Palabras reservadas
lexemas=["operacion", "valor1", "valor2", "suma",
        "resta", "multiplicacion", "division", "potencia",
        "raiz", "inverso", "seno", "coseno", "tangente", "mod", 
        "modulo", "texto", "fondo", "fuente", "forma", ",", 
        ".", ":", "[", "]", "{", "}", "-"]

#se declaran las listas globales
global n_linea
global n_columna
global comandos
global l_lexemas
global l_errores
global l_comandosG

# se inicializan las variables globales el n_linea inicia en 1 porque la primera linea es la 1, no empezamos a contar desde '0'
n_linea = 1
n_columna = 0
l_lexemas = []
#comandos es una lista que guarda los objetos que son operaciones
comandos = []
l_errores = []
l_comandosG = []


def fun_instruccion(cadena):
    #las variables globales se declaran para que se puedan usar en las funciones
    global n_linea
    global n_columna
    global l_lexemas
    #inician las valiables vacias para que no se guarden datos de la ejecucion anterior, en caso se repitan
    lexema = ""
    puntero = 0
    #cadena es el archivo de entrada
    while cadena:
        char = cadena[puntero]
        puntero += 1
        # cuando en cuentre las primeras comillas, se envia al metodo para que se construya el lexema
        if char == '\"':
            # se construye el lexema pero quitando la comilla inicial, para guardar solo el texto
            lexema, cadena = fun_construirLex(cadena[puntero:])
            # si lexema y cadena son diferentes de none, se guarda el lexema en la lista y salta de linea
            if lexema and cadena:
                # se le suma 1 a la columna porque se necesita la comilla inicial a pesar de no ser tomada en cuenta ocupa un espacio
                n_columna += 1

                # llama a la clase para armar el lexema, segun sus atributos
                l = palabra_Lexema(lexema, n_linea, n_columna)

                # la palabra almacenada en la clase se guarda en la lista
                l_lexemas.append(l)
                # se le vuelve a sumar 1 a la columna porque se necesita la comilla final a pesar de no ser tomada en cuenta ocupa un espacio
                n_columna += len(lexema)+1
                #se declara el puntero en 0 para que no acumule los caracteres y vuelva a iniciar su cuenta
                puntero = 0

        elif char.isdigit():
            # por ser numero no se recorta la cadena para que no se pierda el primer numero
            #la variable token es el numero que se va a guardar
            token, cadena = fun_construirNum(cadena)
            #construye el numero y lo guarda en la lista
            if token and cadena:
                # se arma el lexema como clase para que se pueda guardar en la lista y tengan sus atributos
                n = valor_Numero(token, n_linea, n_columna)

                # se guarda el lexema en la lista ya formateado por las clases
                l_lexemas.append(n)
                #no se suma 1 porque no se necesita la comilla final, no lleva el numero
                n_columna += len(str(token))
                #se declara el puntero en 0 para que no acumule los caracteres y vuelva a iniciar su cuenta
                puntero = 0

        elif char == '-':
            #para los numeros negativos busca el signo - y lo guarda en la lista
            token, cadena = fun_construirNum(cadena)
            #token es el numero que se guarda en la lista
            if token and cadena:
                # guarda el numero como clase para que se pueda guardar en la lista y tengan sus atributos
                n = valor_Numero(token, n_linea, n_columna)

                # se guarda el numero en la lista ya formateado por las clases
                l_lexemas.append(n)
                # no se le resta 1 porque se necesita el signo negativo
                n_columna += len(str(token))
                puntero = 0
            # en caso de encontrar los corchetes
        elif char == "[" or char == "]":
            # Armado de lexema como clase
            pos_lexema = palabra_Lexema(char, n_linea, n_columna)
            #se suma 1 a la columna porque da un salto de linea
            n_columna += 1
            # se guarda el lexema en la lista "pos_lexema" es el lexema que se guarda en la lista
            l_lexemas.append(pos_lexema)
            cadena = cadena[1:]
            puntero = 0
            # en caso de encontrar una tabulacion se le suman 4 espacios a la columna y se reinicia el puntero
        elif char == "\t":
            cadena = cadena[4:]
            n_columna += 4
            puntero = 0
            # en caso de encontrar un salto de linea se le suma 1 a la linea y se reinicia la columna y el puntero
        elif char == "\n":
            cadena = cadena[1:]
            n_columna = 0
            n_linea += 1
            puntero = 0
            #en caso de no encontrar algun caracrer reservado, lo lee lo ignora y suma una columna y se reinicia el puntero
        elif char == ' ' or char == '\r' or char == '{' or char == '}' or char == ',' or char == ':' or char == '.':
            cadena = cadena[1:]
            n_columna += 1
            puntero = 0
        else:
            #en caso cadena no sea ninguno de los anteriores, se guarda como error para su escritura en el archivo de entrada
            #los errores son caracteres no palabras completas
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1
            l_errores.append(palabra_Error(char, n_linea, n_columna))

    # for lexema in l_lexemas:
    #     print(lexema)

    return l_lexemas

def fun_construirLex(cadena):
    #construye el lexema de texto
    global n_linea
    global n_columna
    global l_lexemas
    lexema = ""
    puntero = ""
    # el archivo de entrada inicia o corta con comillas, la primera inicial y la segunda final
    for char in cadena:
        puntero += char
        if char == '\"':
            # aqui no se le resta 1 porque se necesita la comilla final
            return lexema, cadena[len(puntero):]
        else:
            # para ir verificando las cadenas del lexema, se va guardando en la variable lexema
            lexema += char
    # en caso de terminar el none es para que no se quede en un ciclo infinito, y el segundo none es para que no se guarde en la lista
    return None, None

def fun_construirNum(cadena):
    #numero es el numero que se va a guardar inicia en vacio
    #puntero es el que se va a ir recorriendo la cadena
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

        # se declaran los posibles finales o cortes que puede tener el numero
        if char == '"' or char == ' ' or char == '\n' or char == '\t' or char == ']' or char == ',':
            if is_decimal:
                # el -1 es para que no se incluya el punto o el estado de corte
                #[len(puntero)-1:] es un termino en listas para cortar desde el punto que se le indique
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
    #la funcion recorre los lexemas para obtener los datos y extraerlos de la lista para operarlos
    global l_lexemas
    global comandos
    operacion = ''
    n1 = ''
    n2 = ''
    # mientras existan lexemas en la lista se va recorrer
    while l_lexemas:
        # el .pop elimina el lexema de la lista y lo retorna
        lexema = l_lexemas.pop(0)

        if lexema.operar(None) == 'operacion':
            operacion = l_lexemas.pop(0)
        elif lexema.operar(None) == 'valor1':
            n1 = l_lexemas.pop(0)
            if n1.operar(None) == '[':
                n1 = operar()  # es un metodo iterativo para que se pueda operar siempre y cuando existan mas operaciones del lado derecho
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

def fun_lGrafico():
    # Antes de operar y eliminar los valores de la lista de lexemas, se guardan los datos para el grafico
    global l_lexemas
    #se recorre la lista de lexemas para obtener los datos que se van a graficar
    #se guardan en una lista global para que se puedan usar en la funcion de graficar
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
    #Funcion iterativa para operar las operaciones siempre y cuando no existan mas en el lado derecho
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
    #se llama a la lista de comandos para obtener los datos y guardarlos en el archivo de salida
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
    # nombre del archivo de salida
    nombre = nombreGrafica+".dot"

    # Creación del archivo .dot
    with open(nombre, 'w') as f:
        f.write(fun_grafico())

    os.system(
        f'dot -Tpdf {nombre} -o {nombreGrafica}.pdf')

    # obtiene la direccion de la carpeta donde se encuentra el archivo
    ruta = os.path.dirname(os.path.abspath(f"{nombreGrafica}.pdf"))

    # la ruta del archivo es la misma que la del programa
    archivo_pdf = ruta+f"\{nombreGrafica}.pdf"
    #abre el archivo de salida para visualizarlo
    path = f'file:///{archivo_pdf}'

    # manda a llamar el pfd para abrirlo con el navegador predeterminado
    webbrowser.open_new(path)

def fun_deleteL():
    #se limpian las listas para que no se guarden los datos de la ejecucion anterior, es para cargar un nuevo archivo
    comandos.clear()
    l_comandosG.clear()

def fun_deleteLE():
    #se limpian las listas para que no se guarden los datos de la ejecucion anterior, es para cargar un nuevo archivo
    global n_linea
    l_errores.clear()
    n_linea = 1

def fun_AtributosyCrearGrafico(i, id, etiqueta, objeto):
    #son los atributos que se le agregan a los nodos
    global l_comandosG
    # dot es para crear el grafico
    dot = ""
    #las formas que puede tener el nodo, sus colores y su etiqueta
    colorFondo = l_comandosG[1]
    colorFuente = l_comandosG[2]
    forma = l_comandosG[3]
    #mediante condicionales crea el nodo con sus atributos
    if objeto:
        if type(objeto) == valor_Numero:
            
            dot += f'nodo_{i}{id}{etiqueta}[label="{objeto.operar(None)}",fontcolor="{colorFuente}",fillcolor={colorFondo}, style=filled,shape={forma}];\n' 
        if type(objeto) == trigonometricas:
            dot += f'nodo_{i}{id}{etiqueta}[label="{objeto.tipo.lexema}\\n{objeto.operar(None)}",fontcolor="{colorFuente}",fillcolor={colorFondo}, style=filled,shape={forma}];\n'  
            dot += fun_AtributosyCrearGrafico(i, id+1, etiqueta+"_angulo", objeto.left)
            # uniones de nodos
            dot += f'nodo_{i}{id}{etiqueta} -> nodo_{i}{id+1}{etiqueta}_angulo;\n'  
        if type(objeto) ==  aritmeticas:
            
            dot += f'nodo_{i}{id}{etiqueta}[label="{objeto.tipo.lexema}\\n{objeto.operar(None)}",fontcolor="{colorFuente}",fillcolor={colorFondo}, style=filled,shape={forma}];\n'
            # print("sub izquierdo")    
            dot += fun_AtributosyCrearGrafico(i, id+1, etiqueta + "_left", objeto.left)
            # uniones de nodos
            dot += f'nodo_{i}{id}{etiqueta} -> nodo_{i}{id+1}{etiqueta}_left;\n'
            
            dot += fun_AtributosyCrearGrafico(i, id+1, etiqueta+"_right", objeto.right)    
            # uniones de nodos
            dot += f'nodo_{i}{id}{etiqueta} -> nodo_{i}{id+1}{etiqueta}_right;\n'   
    return dot

def fun_obtenerErrores():
    #llama a la lista de errores para obtener los datos y guardarlos en el archivo de salida
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
    #retorna el formato de errores en el archivo de salida
    return formatoErrores

def fun_Archivo_salida_errores():
    # nombre del archivo de salida
    nombre = "RESULTADOS_202201947"+".json"

    # Creación del archivo .dot para que el programa lo pueda leer y graficar
    with open(nombre, 'w') as f:
        f.write(fun_obtenerErrores())

    # la ruta del archivo es la misma que la del programa
    ruta = os.path.abspath(nombre)
    #imprime en pantalla la ruta del archivo
    print(ruta)
    #abre el archivo de salida para visualizarlo
    os.system(f'start notepad.exe {ruta}')