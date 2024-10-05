# importar librerias
import pygame
import random
import sys
# importar el otro archivo
from puzzle import Puzzle

# inicializar pygame
pygame.init()

# CONSTANTES
BG_WIN_CLR = (245, 245, 245)
SQUARE_FRAME_CLR = (0, 76, 153)
SQUARE_TXT_CLR = (0, 0, 0)
BG_BTN_CLR = (96, 96, 96)
BTN_TXT_CLR = (255, 255, 255)

# crear ventana
dimensiones = (800, 500)
ventana = pygame.display.set_mode(dimensiones)

# estado inicial aleatorio
def generar_estado_inicial():
    puzzle = list(range(9))  # números del 0 al 8
    random.shuffle(puzzle)
    return [puzzle[i:i+3] for i in range(0, 9, 3)]

estado_inicial = generar_estado_inicial()
solver = Puzzle(estado_inicial)

# tablero
def dibujar_tablero(estado):
    ventana.fill(BG_WIN_CLR)
    fuente = pygame.font.Font(None, 74)
    
    for i in range(3):
        for j in range(3):
            if estado[i][j] != 0:
                pygame.draw.rect(ventana, SQUARE_FRAME_CLR, (100 + j * 81, 100 + i * 81, 80, 80), 5)
                texto = fuente.render(str(estado[i][j]), True, SQUARE_TXT_CLR)
                ventana.blit(texto, (100 + j * 81 + 30, 100 + i * 81 + 20))
            else:
                pygame.draw.rect(ventana, SQUARE_FRAME_CLR, (100 + j * 81, 100 + i * 81, 80, 80), 5)

# botones
def dibujar_botones():
    fuente = pygame.font.Font(None, 36)
    botones = [("Iniciar", 500, 100), ("BFS", 500, 180)]  # Agregar los otros botones después ("DFS", 500, 260), ("DFS Iterativa", 500, 340)
    
    for texto, x, y in botones:
        pygame.draw.rect(ventana, BG_BTN_CLR, (x, y, 120, 50))
        btn_txt = fuente.render(texto, True, BTN_TXT_CLR)
        ventana.blit(btn_txt, (x + 10, y + 10))

# bucle
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            
            if 500 <= x <= 620:
                if 100 <= y <= 150:
                    estado_inicial = generar_estado_inicial()
                    solver = Puzzle(estado_inicial)
                elif 180 <= y <= 230:
                    # definir el estado objetivo
                    estado_objetivo = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
                    ruta = solver.busqueda_en_amplitud(estado_objetivo)
                    #
                    if ruta is not None:
                        for estado in ruta:
                            dibujar_tablero(estado)
                            pygame.display.flip()
                            # duración de cada movimiento
                            pygame.time.delay(500)
                        # actualizar el estado final
                        estado_inicial = ruta[-1]
                    else:
                        print("No se encontró una solución.")
                    
    dibujar_tablero(estado_inicial)
    dibujar_botones()
    pygame.display.flip()