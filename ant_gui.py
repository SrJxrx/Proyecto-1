import pygame
import pickle
import matrices as mat
import ant_logic as log

def main(filas, columnas, tam, regla):
    """Función principal que recibe los valores que definen la partida,
    ademas de manejar el guardado y carga de la partida
    también genera la ventana del juego
    Entradas:filas, columnas, tam, regla)
    Salidas:
    Restricciones:filas, columnas, tam: deben ser int positivo
    regla: debe ser string L o R""" 
    pygame.init()
    clock = pygame.time.Clock()
    M = mat.generar_matriz_vacia(filas, columnas)
    fila_hormiga = filas // 2
    columna_hormiga = columnas // 2
    direccion = "D"
    w = columnas * tam
    h = filas * tam
    window = pygame.display.set_mode((w, h))
    pausa = False
    loop = True
    colores = log.generar_colores(len(regla))
    tick = 100
    while loop:
        if tick < 0:
            tick = 3
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pausa = not pausa
                elif event.key == pygame.K_r:
                    M = mat.generar_matriz_vacia(filas,columnas)
                    colores = log.generar_colores(len(regla))
                    fila_hormiga = filas // 2
                    columna_hormiga = columnas // 2
                    direccion = "W"
                elif event.key == pygame.K_h:
                    tick+=10
                elif event.key == pygame.K_l:
                    tick-=10
                elif event.key == pygame.K_g:
                    datos = {"matriz": M,"fila_hormiga": fila_hormiga,"columna_hormiga": columna_hormiga,"direccion": direccion,"regla": regla, "filas": filas, "columnas" : columnas, "tam": tam}
                    with open("langton.pkl", "wb") as archivo:
                        pickle.dump(datos, archivo)
                elif event.key == pygame.K_c:
                    try:
                        with open("langton.pkl", "rb") as archivo:
                            datos = pickle.load(archivo)
                        M = datos["matriz"]
                        fila_hormiga = datos["fila_hormiga"]
                        columna_hormiga = datos["columna_hormiga"]
                        direccion = datos["direccion"]
                        regla = datos["regla"]
                        filas = datos["filas"]
                        columnas = datos["columnas"]
                        tam = datos["tam"]

                        filas = len(M)
                        columnas = len(M[0])
                        w = columnas * tam
                        h = filas * tam
                        window = pygame.display.set_mode((w, h))
                    except FileNotFoundError:
                        print("No existe archivo guardado")
        
        if not pausa:
            fila_hormiga, columna_hormiga, direccion = \
                log.siguiente(M,fila_hormiga,columna_hormiga,direccion,regla)
            
        window.fill((255,255,255))
        for f in range(filas):
            for c in range(columnas):
                color = M[f][c]
                pygame.draw.rect(window,colores[color % len(colores)],(c * tam,f * tam,tam,tam))

        pygame.draw.rect(window,(255,128,0),(columna_hormiga * tam,fila_hormiga * tam,tam,tam))
        pygame.display.update()
        clock.tick(tick)

    pygame.quit()
