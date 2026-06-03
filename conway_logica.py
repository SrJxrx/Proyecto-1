from random import randint
from copy import deepcopy

def generar_matriz(filas, columnas):
    """Función que retorna una matriz de las dimensiones
    especificadas con valores enteros aleatorios de 0 o 1"""
    return [[randint(0, 1) for c in range(columnas)] for f in range(filas)]    

def obtener_vecinos(M, f, c):

    vecinos = []

    fs = len(M)
    cs = len(M[0])

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nueva_fila = (f + i) % fs
            nueva_columna = (c + j) % cs
            vecinos.append(M[nueva_fila][nueva_columna])

    return vecinos

def transicion_celula(estado, vecinos):
    """Retorna el nuevo estado de la célula de acuerdo
    al estado de sus vecinos.
    Si estado == 0 y tiene 3 vecinos vivos --> viva
    Si estado == 1 y tiene menos de 2 vecinos vivos --> muere
    Si estado == 1 y tiene más de 3 vecinos vivos --> muere
    Cualquier otra combinación, el estado sigue igual."""
    sumatoria = vecinos.count(1)
    if estado == 0 and sumatoria == 3:
        estado = 1
    elif estado == 1 and sumatoria <2 or estado == 1 and sumatoria > 3:
        estado = 0         
    return estado

def transicion(M):
    #deepcopy de matriz
    """Toma a la matriz completa y le aplica la función de
    transición a cada célula con su propio vecindario y deja
    el resultado en una matriz nueva."""
    nuevaM = deepcopy(M)
    for i in range(len(M)):
        for j in range(len(M[0])):
           vecinos = obtener_vecinos(M, i, j)
           transicion_celula(M[i][j], vecinos)
           nuevaM[i][j] = transicion_celula(M[i][j], vecinos)
     
    return nuevaM
