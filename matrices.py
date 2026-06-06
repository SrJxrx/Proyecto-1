from random import randint

def generar_matriz_aleatoria(filas, columnas):
    """Función que retorna una matriz de las dimensiones
    especificadas con valores enteros aleatorios de 0 o 1
    Entradas:filas, columnas
    Salidas: matriz con valores enteros aleatorios de 0 o 1
    Restrincciones:numeros enteros mayores a 0"""
    return [[randint(0, 1) for c in range(columnas)] for f in range(filas)]    

def generar_matriz_vacia(filas, columnas):
    """Funcion que crea una matriz a base de las dimensiones dadas, llenada con ceros.
    Entradas: filas, columnas
    Salidas: matriz llenada con ceros
    Restrincciones:numeros enteros mayores a 0"""
    return [[0 for c in range(columnas)] for f in range(filas)]

def generar_matriz_multialeatoria(filas, columnas, cantidad_colores):
    """Función que retorna una matriz de las dimensiones
    especificadas con valores enteros aleatorios de 0 hasta la cantidad de valores puestos
    Entradas:filas, columnas
    Salidas: matriz con valores enteros aleatorios de 0 o 1
    Restrincciones:numeros enteros mayores a 0"""
    return [[randint(0, cantidad_colores - 1 ) for c in range(columnas)] for f in range(filas)]
