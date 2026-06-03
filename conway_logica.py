from random import randint
from copy import deepcopy

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

def obtener_vecinos(M, f, c):
    """Función que retorna una lista con los estados de
    los 8 vecinos de la célula en la posición f, c de M.
    Entradas: Matriz, fila,columna
    Salidas: lista con los estados de los vecinos de la celula dada
    Restrincciones:"""
    vecinos = []
    filas = len(M)
    columnas = len(M[0])

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            f_vecino = (f + i) % filas
            c_vecino = (c + j) % columnas
            
            vecinos.append(M[f_vecino][c_vecino])

    return vecinos

def transicion_celula(estado, vecinos, reglas_b, reglas_s):
    """Retorna el nuevo estado de la célula de acuerdo
    al estado de sus vecinos.
    Si estado == 0 y tiene 3 vecinos vivos --> viva
    Si estado == 1 y tiene menos de 2 vecinos vivos --> muere
    Si estado == 1 y tiene más de 3 vecinos vivos --> muere
    Cualquier otra combinación, el estado sigue igual.
    Entradas: estado, vecinos, reglas_b, reglas_s
    Salidas: 0 o 1
    Restrincciones:Estado debe ser binario, vecinos debe ser una lista al igual que las reglas dadas."""
    vecinos_vivos = sum(vecinos)
    sumatoria = vecinos.count(1)
    if estado == 0:
        if sumatoria in reglas_b:
            return 1
        return 0

    if estado == 1:
        if sumatoria in reglas_s:
            return 1
        return 0


def transicion(M, reglas_b, reglas_s):
    """Toma a la matriz completa y le aplica la función de
    transición a cada célula con su propio vecindario y deja
    el resultado en una matriz nueva.
    Entradas: M, lista de relgas b y s
    Salidas: Crea una matriz nueva a partir de las reglas y la matriz dada
    Restrincciones:M debe ser una matriz y las reglas s y b deben ser listas.
    """
    nuevaM = deepcopy(M)

    for i in range(len(M)):
        for j in range(len(M[0])):
            vecinos = obtener_vecinos(M, i, j)
            nuevaM[i][j] = transicion_celula(M[i][j], vecinos, reglas_b, reglas_s)

    return nuevaM
