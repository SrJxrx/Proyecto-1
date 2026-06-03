import pygame
import conway_logica as con
import pickle

 



def main(filas, columnas, tam, reglas_b, reglas_s):
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
                if event.key == pygame.K_SPACE:
                    pausa = not pausa
                elif event.key == pygame.K_r:
                    M = con.generar_matriz_aleatoria(filas, columnas)
                elif event.key == pygame.K_b:
                    M = con.generar_matriz_vacia(filas, columnas)
                elif event.key == pygame.K_g:
                    datos_a_guardar = {
                        "matriz": M,
                        "filas": filas,
                        "columnas": columnas,
                        "tam_celda": tam,
                        "reglas_b": reglas_b,
                        "reglas_s": reglas_s
                    }
                    with open("partida.pkl", "wb") as f_archivo:
                        pickle.dump(datos_a_guardar, f_archivo)
                    print("Guardado con éxito.")
                    
                
                elif event.key == pygame.K_c:
                    try:
                        with open("partida.pkl", "rb") as f_archivo:
                            datos_cargados = pickle.load(f_archivo)
                        M = datos_cargados["matriz"]
                        filas = datos_cargados["filas"]
                        columnas = datos_cargados["columnas"]
                        tam = datos_cargados["tam_celda"]
                        reglas_b = datos_cargados["reglas_b"]
                        reglas_s = datos_cargados["reglas_s"]
                        w, h = columnas * tam, filas * tam
                        window = pygame.display.set_mode((w, h))
                        print("Estado cargado correctamente desde el archivo.")
                    except FileNotFoundError:
                        print("Error: No se encontró ningún archivo de guardado previo ('partida.pkl').")
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                c = x // tam
                f = y // tam
                if 0 <= f < filas and 0 <= c < columnas:
                    M[f][c] = (M[f][c] + 1) % 2
                    
        window.fill((0, 0, 0))
        for f in range(filas):
            for c in range(columnas):
                if M[f][c] == 1:
                    x = c * tam
                    y = f * tam
                    pygame.draw.rect(window, (0, 255, 128), (x, y, tam, tam))
        if not pausa:
            M = con.transicion(M, reglas_b, reglas_s)
        pygame.display.update()
        clock.tick(10)
    pygame.quit()
