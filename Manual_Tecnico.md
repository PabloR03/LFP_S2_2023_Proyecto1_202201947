# LENGUAJES FORMALES DE PROGRAMACION B-
## Proyecto 1
### Segundo Semestre 2023
```js
Universidad San Carlos de Guatemala
Programador: Pablo Andres Rodriguez Lima
Carne: 202201947
Correo: pabloa10rodriguez@gmail.com
```
---
## Descripción del Proyecto
Presentacion de programa para el manejo de archivos del tipo json, bajo una interfaz grafica, para realizar operaciones en forma de arbol, pero con la principal funcion de detectar errores lexicos, tomando en cuenta que las palabras reservadas son palabras basicas que tambien tienen opciones de configurar al reporte
Requerimientos mínimos para el uso del programa
Python en su versión 2.8 o posteriores (se creó bajo la versión 3.11.4), Se recomienda un ide como Pycharm o bien un editor de texto con su extensión como Visual Studio Code. tambien tener instalada una version de Graphviz.


## Objetivos
* Objetivo General
    * Desarrollar y presentar un programa de software integral que permite usar una interfaz grafica para abrir, guardar y revisar errores lexicos.
* Objetivos Específicos
    * Crear una interfaz de usuario intuitiva y de fácil uso que posibilite editar texto para analizar.
    * Implementar un sistema de de operaciones del tipo iterativas para hacer arboles.

---
## Clases y métodos utilizados

**App -interfaz grafica-**
* Clase ventana principal:
    Se crea una ventana que almacena dos "contenedores" son formas que buscan señalizar y ordenar un area donde van destinados los botones y el cuadro de texto editables. tambien crea los botones utilizados en el programa.
    * Funcion "fun_bArchivo" le da funcionalidad al boton que esta en el menu el cual es el de abrir un archivo, busca unicamente a los archivos del tipo json, los abre y muestra en el cuadro de texto antes creado
    * Funcion "fun_gArchivo" le da funcionalidad al boton guardar, el texto que esta guardado en el textArea se crea una copia en la ruta antes guardada modificando el mismo archivo antes creado.
    * "fun_gcArchivo" le da funcionalidad al boton buscar como, crea un archivo nuevo con la misma informacion cargada en el textArea con la posibilidad de cambiarle nombre tal como si de hacer una copia se tratara.
    * "salir" le da funcionalidad al boton de salir, lo que busca es exterminar la terminal grafica, tal como lo indica el nombre
    * "analizar_Archivo" es una funcion que como principal funcion es habilitar el boton de crear archivo de errores y lo que hace es inicializar el sistema, carga las listas con los errores y operaciones efectuadas.
    * "errores" es una funcion que crea el archivo de salida del tipo Json, y da paso a crear el reporte que es la grafica con los datos ya hechos.
    * "reporte" es una funcion que le da paso a crear un archivo del tipo pdf que es la grafica con los datos ya hechos.

**Clases para la ordenacion y formateo de datos**
* Clase Abstracta:
    * Clase "Expresion" crea metodos bajo la exportacion abstract, busca que bajo un metodo iterativo archivos con el mismo requisito de datos genere y se utilice de diferente manera.
        * Metodo "operar" es una funcion que busca llamarse a si misma para ir guardando a su vez los datos que vaya almacenando cada vez que se le vaya llamando.
        * Metodo "getFila" es una funcion que en cada llamado obtiene mediante un contador (posteriormente utilizado) almacenar el numero de fila.
        * Metodo "getColumna" es una funcion que en cada llamado obtiene mediante un contador (posteriormente utilizado) almacenar el numero de columna.
* Clase Lexema y Error:
    * Clase "palabra_Lexema" crea metodos el cual es necesario para el lexema ya que su funcion es hacer operaciones matematicas es la palabra que le da una orden al programa.
    * Clase "palabra_Error" crea un formato para el archivo de errores es donde se van guardando e imprimiendo en la lista de los errores para su posterior creacion en archivo tipo json.
* Clase Operaciones Valor, Aritmetica y Trigonometrica
    * Clase valor_Numero: Interpreta el lexema como un numero para su uso en las operaciones matematicas, tal como lo indica el archivo es el valor a tomar en cuenta.
    * Clase "trigonometricas" Usa la importacion de las clases math funciones basicas trigonometricas requeridas
    * Clase "Aritmetica" Usa la importacion de las clases math funciones basicas Aritmeticas requeridas

**Clase para el Analizador Lexico**
* Clases para la ejecucion y funcionamiento del analizador
    * Clases "fun_instruccion" el archivo de entrada es leido y es examinado linea por linea en este caso es para armar el lexema de instruccion, este es buscado por las comillas, busca la palabra que esta entre las comillas y dependiendo si es considerada una de las palabras reservadas ejecuta una accion, la cual dictaminan las clases anteriores.
    * Clases "fun_construirLex" es una clase que es llamada iterativa ya que cada que una palabra se este entre comillas la almacena y la compara en las palabras reservadas esto con la finalidad de ejecutar una accion o un error segun dependan o no
    * Clases "fun_construirNum" es una clase la cual arma un valor del tipo entero o decimal la cual es el valor que busca operar y guardar para la creacion del grafico.
    * Clase "Operar" es una funcion que opera las funciones trigonometricas, segun su estado en el arbol para mostrar el resultado.
    * Clase "Operar_" es una funcion iterativa que determina y da prioridad a operar de lado derecho del arbol siempre mostrando el resultado en el lado izquierdo.
    * Clases para graficas "fun_grafico, fun_genGrafico" son funciones para obtener las instrucciones de armar el grafico, obtiene el titulo, y los nodos del arbol
    * Clases "Delete" limpian listas son utilizadas en la clase app para inicializar el sistema.
    * Clases "fun_obtenerErrores" es una clase que obtiene el los datos enviado de los errores y cada caracter los envia a la clase de errores para formatearlos e imprimirlos en el archivo de salida.
    * Clase "fun_Archivo_salida_errores" es una clase que  tiene la lista de los errores y las imprime en el archivo tipo Json que el mismo crea, para abrirlo en este caso con el block de notas.



