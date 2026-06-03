from easygui import *

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
        elif programa == "Hormiga de Langton":
            msgbox("langton")
        else:
            msgbox(despedida)
ventana()

