import pygame
import conway_logica as con
import easygui
import pickle
import sys

 

def solicitar_reglas():
    """Solicita las reglas por consola"""
    print("Configuración del Autómata Life-Like")
    campos = [
        "Cantidad de Filas:",
        "Cantidad de Columnas:",
        "Tamaño de las Celdas (píxeles):",
        "Regla de Nacimiento B (dígitos 0-8):",
        "Regla de Supervivencia S (dígitos 0-8):"
    ]

    valores_defecto = ["50", "50", "12", "3", "23"]
    respuestas = easygui.multenterbox("Ingrese los parámetros iniciales:", titulo, campos, valores_defecto)
    
    if respuestas is None:
        sys.exit()

    try:
        filas = int(respuestas[0])
        columnas = int(respuestas[1])
        tam_celda = int(respuestas[2])
  
        b_input = input("Casos donde se producen nacimientos (dígitos de 0 a 8): ").strip()
        s_input = input("Casos donde las células sobreviven (dígitos de 0 a 8): ").strip()

        reglas_b = [int(d) for d in b_input if '0' <= d <= '8']
        reglas_s = [int(d) for d in s_input if '0' <= d <= '8']
        
        return filas, columnas, tam_celda, reglas_b, reglas_s
    except ValueError:
        easygui.msgbox("Error: Filas, columnas y tamaño deben ser números enteros válidos.", "Error de entrada")
        return solicitar_reglas()

def main():
    filas, columnas, tam, reglas_b, reglas_s = solicitar_reglas()
    reglas_b, reglas_s = solicitar_reglas()
    pygame.init()
    clock = pygame.time.Clock()
    M = con.generar_matriz_aleatoria(filas, columnas)
    w, h = columnas * tam, filas * tam
    window = pygame.display.set_mode((w, h))
    loop = True
    pausa = False
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_p]:
                    pausa = not pausa
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons = pygame.mouse.get_pressed()
                x, y = pygame.mouse.get_pos()
                if buttons[0]:
                    f = y // tam
                    c = x // tam
                    M[f][c] = (M[f][c] + 1) % 2
                    
        window.fill((0, 0, 0))
        for f in range(filas):
            for c in range(columnas):
                if M[f][c] == 1:
                    x = c * tam
                    y = f * tam
                    pygame.draw.rect(window, (0, 255, 128), (x, y, tam, tam))
        if not pausa:
            M = con.transicion(M)
        pygame.display.update()
        clock.tick(10)
    pygame.quit()

if __name__ == "__main__":
    main()
