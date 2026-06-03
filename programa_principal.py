from easygui import *
import conway_gui as cg
def ventana():
    bienvenida = "Bienvenido al programa principal de juegos"
    despedida = "gracias por usar este programa"
    texto = ("Ingrese cantidades en números: ")
    parametros_defecto = ["Filas", "Columnas", "Tamaño de celdas", "Nacimiento", "Supervivencia"]
    
    inicio = buttonbox(bienvenida, choices=["Continuar", "Salir"])
    if inicio == None or inicio == "Salir":
        msgbox(despedida)
    else: 
        mensaje ="Elige tu juego deseado"
        titulo = "Selección de juego"
        eleccion = ["Juego de la vida", "Hormiga de Langton"]
        programa = buttonbox(mensaje, titulo, eleccion)
        
        if programa == "Juego de la vida":
            respuestas = multenterbox("Ingrese los parámetros iniciales:", texto, parametros_defecto)
            if respuestas is None:
                msgbox(despedida)
            else:
                filas = int(respuestas[0])
                columnas = int(respuestas[1])
                tam = int(respuestas[2])
                reglas_b = [int(x) for x in respuestas[3]]
                reglas_s = [int(x) for x in respuestas[4]]
                cg.main(filas, columnas, tam, reglas_b, reglas_s)
        elif programa == "Hormiga de Langton":
            msgbox("langton")
        else:
            msgbox(despedida)
ventana()


