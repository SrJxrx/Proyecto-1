from easygui import *
import conway_gui as con
import ant_gui as ag
def ventana():
    """programa principal que ejecuta los demás programas y envia los valores
    que puso el usuario hacia los juegos
    ademas de manejar el guardado y carga de la partida
    también genera la ventana del juego
    Entradas:filas, columnas, tam, regla, reglas_b, reglas_s)
    Salidas: Los juegos ejecutados
    Restricciones:filas, columnas, tam: deben ser int positivo
    regla: debe ser string L o R
    reglas_b, reglas_s: deben ser int entre 0 y 8"""
    
    bienvenida = "Bienvenido al programa principal de juegos"
    despedida = "gracias por usar este programa"
    texto = "Ingrese cantidades en números: "
    parametros_conway = ["Filas", "Columnas", "Tamaño de celdas", "Nacimiento (0 a 8)", "Supervivencia (0 a 8)"]
    parametros_langton = ["Filas", "Columnas", "Tamaño de celdas", "Reglas LR"]
    error = "ERROR: ingrese valores correctamente"
    inicio = buttonbox(bienvenida, choices=["Continuar", "Salir"])
    if inicio == None or inicio == "Salir":
        msgbox(despedida)
    else: 
        mensaje ="Elige tu juego deseado"
        titulo = "Selección de juego"
        eleccion = ["Juego de la vida", "Hormiga de Langton"]
        programa = buttonbox(mensaje, titulo, eleccion)
        
        if programa == "Juego de la vida": 
            while True:
                respuestas = multenterbox("Ingrese los parámetros iniciales:",texto,parametros_conway)
                if respuestas is None:
                    msgbox(despedida)
                    return

                try:
                    filas = int(respuestas[0])
                    columnas = int(respuestas[1])
                    tam = int(respuestas[2])
                    reglas_b = [int(x) for x in respuestas[3]]
                    reglas_s = [int(x) for x in respuestas[4]]
                    if "" in respuestas:
                        raise ValueError
                    if filas <= 0 or columnas <= 0 or tam <= 0:
                        raise ValueError
                    for n in reglas_b:
                        if n < 0 or n > 8:
                            raise ValueError
                    for n in reglas_s:
                        if n < 0 or n > 8:
                            raise ValueError
                    break

                except:
                    msgbox(error)
                
            con.main(filas, columnas, tam, reglas_b, reglas_s)
                
        elif programa == "Hormiga de Langton":
            while True:
                respuestas = multenterbox("Ingrese los parámetros iniciales:", texto, parametros_langton)
                if respuestas is None:
                    msgbox(despedida)
                    return
                try:
                    filas = int(respuestas[0])
                    columnas = int(respuestas[1])
                    tam = int(respuestas[2])
                    regla = (respuestas[3])
                    if "" in respuestas:
                        raise ValueError
                    if filas <= 0 or columnas <= 0 or tam <= 0:
                        raise ValueError
                    for letra in regla.upper():
                        if letra not in "LR":
                            raise ValueError
                    break 
                except:
                    msgbox(error)
            ag.main(filas, columnas, tam, regla)
            
        else:
            msgbox(despedida)
       
ventana()
