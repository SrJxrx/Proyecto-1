import random

def girar_hormiga(direccion, giro):
    """Función que actualiza la dirección de giro de la hormiga según su posicion anterior.
    Entradas: direccion, giro
    Salidas: la nueva dirección
    Restricciones:giro debe ser L o R"""
    if giro == "L":
        if direccion == "W":
            return "A"
        elif direccion == "A":
            return "S"
        elif direccion == "S":
            return "D"
        elif direccion == "D":
            return "W"
    else:

        if direccion == "W":
            return "D"
        elif direccion == "D":
            return "S"
        elif direccion == "S":
            return "A"
        elif direccion == "A":
            return "W"

def avanzar_hormiga(fila,columna,direccion,filas,columnas):
    """Función que la hormiga avance.
    Entradas: fila,columna,direccion,filas,columnas
    Salidas: la hormiga avanza una casilla
    Restricciones:
    fila,columna,filas,columnas: deben ser Entero positivo
    direccion: debe ser string"""
    if direccion == "W":
        fila = (fila - 1) % filas
    elif direccion == "S":
        fila = (fila + 1) % filas
    elif direccion == "A":
        columna = (columna - 1) % columnas
    elif direccion == "D":
        columna = (columna + 1) % columnas
    return fila, columna

def generar_colores(n):
    """Función que genera colores de manera aleatoria y los guarda en una lista
    Entradas: n (es el len de cuantas letras pone el usuario)
    Salidas: una lista con colores aleatorios
    Restricciones:"""
    colores = []

    for i in range(n):
        colores.append((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    return colores


def siguiente(M,fila,columna,direccion,regla):
    """Función que analiza que acción realizar en función de los colores
    para actualizar la matriz y la hormiga
    Entradas: M,fila,columna,direccion,regla
    Salidas: una lista con colores aleatorios
    Restricciones:"""
    color_actual = M[fila][columna]
    giro = regla[color_actual]
    direccion = girar_hormiga(direccion,giro)
    M[fila][columna] = (color_actual + 1) % len(regla)
    fila, columna = avanzar_hormiga(fila,columna,direccion,len(M),len(M[0]))
    return fila, columna, direccion
