from random import randint

def generar_matriz_aleatoria(filas, columnas):
    """Función que retorna una matriz de las dimensiones
    especificadas con valores enteros aleatorios de 0 o 1"""
    return [[randint(0, 1) for c in range(columnas)] for f in range(filas)]    

def generar_matriz_vacia(filas, columnas):
    """Funcion que crea una matriz a base de las dimensiones dadas, llenada con ceros."""
    return [[0 for c in range(columnas)] for f in range(filas)]

def obtener_vecinos(M, f, c):
    """Función que retorna una lista con los estados de
    los 8 vecinos de la célula en la posición f, c de M."""
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
    Cualquier otra combinación, el estado sigue igual."""
    vecinos_vivos = sum(vecinos)

    if estado == 0:
        if vecinos_vivos in reglas_b:
            return 1
    else:
        if vecinos_vivos in reglas_s:
            return 1
        else:
            return 0
    return estado

def transicion(M, reglas_b, reglas_s):
    """Toma a la matriz completa y le aplica la función de
    transición a cada célula con su propio vecindario y deja
    el resultado en una matriz nueva."""
    filas = len(M)
    columnas = len(M[0])
    
    nueva_matriz = generar_matriz_vacia(filas, columnas)
    
    for f in range(filas):
        for c in range(columnas):
            estado = M[f][c]
            vecinos = obtener_vecinos(M, f, c)
            nueva_matriz[f][c] = transicion_celula(estado, vecinos, reglas_b, reglas_s)
    return nueva_matriz
