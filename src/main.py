# importar librerias
import pygame
import random
# importar el otro archivo
from puzzle import Puzzle

# inicializar pygame
pygame.init()

# CONSTANTES
BG_WIN_CLR = (0, 0, 0)
BG_SQUARE_CLR = (0, 0, 0)
BTN_CLR = (0, 0, 0)

# crear ventana
dimensiones = (800, 500)
ventana = pygame.display.set_mode(dimensiones)

# estado inicial aletorio
def generar_estado_inicial():
    puzzle = list(range(9)) # numeros del 0 al 8
    random.shuffle(puzzle)
    return [puzzle[i:i+3] for i in range(0, 9, 3)]

estado_inicial = generar_estado_inicial()
resolver = Puzzle(estado_inicial)

# tablero
def dibujar_tablero(estado):
    ventana.fill(BG_WIN_CLR)
    fuente = pygame.font.Font(None, 74)
    
    for i in range(3):
        for j in range(3):
            if estado[i][j] != 0:
                pygame.draw.rect(ventana, BG_SQUARE_CLR, (100 + j * 81, 100 + i * 81, 80, 80), 5)
                texto = fuente.render(str(estado[i][j]), True, BG_SQUARE_CLR)
                ventana.blit(texto, (100 + j * 81 + 30, 100 + i * 81 + 20))
            else:
                pygame.draw.rect(ventana, BG_SQUARE_CLR, (100 + j * 81, 100 + i * 81, 80, 80), 5)

# botones
def dibujar_botones():
    fuente = pygame.font.Font(None, 36)
    botones = [("Iniciar", 500, 100), ("BFS", 500, 180)] # ("DFS", 500, 260), ("DFS Iterativa", 500, 340)
    
    for texto, x, y in botones:
        pygame.draw.rect(ventana, BTN_CLR, (x, y, 120, 50))
        btn_txt = fuente.render(texto, True, BG_SQUARE_CLR)
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
                    resolver = Puzzle(estado_inicial)
                elif 180 <= y <= 230:

'''
# importar librerias
import pygame, sys
# inicializar pygame
pygame.init()

# CONSTANTES
BG_DISPLAY_CLR = (224, 224, 224) # red, green, blue
BG_SQUARE_CLR = (255, 255, 255)

# dimensiones de la ventana
size = (800, 500)
# Crear ventana
screen = pygame.display.set_mode(size)

# crear bucle
while True:
    # identificar eventos que suceden dentro de mi ventana
    for event in pygame.event.get():
        # cerrar ventana
        if event.type == pygame.QUIT:
            sys.exit()
    # asignar color de fondo
    screen.fill(BG_DISPLAY_CLR)
    # --- Zona de dibujo
    # pantalla, color, (punto de inicio, punto final, ancho, alto)
    pygame.draw.rect(screen, BG_SQUARE_CLR, (100, 100, 80, 80), 5) #izquierda,arriba
    pygame.draw.rect(screen, BG_SQUARE_CLR, (100, 181, 80, 80), 5) #izquierda,centro
    pygame.draw.rect(screen, BG_SQUARE_CLR, (100, 262, 80, 80), 5) #izquierda,abajo
    pygame.draw.rect(screen, BG_SQUARE_CLR, (181, 100, 80, 80), 5) #centro,arriba
    pygame.draw.rect(screen, BG_SQUARE_CLR, (181, 181, 80, 80), 5) #centro,centro
    pygame.draw.rect(screen, BG_SQUARE_CLR, (181, 262, 80, 80), 5) #centro,abajo
    pygame.draw.rect(screen, BG_SQUARE_CLR, (262, 100, 80, 80), 5) #derecha,arriba
    pygame.draw.rect(screen, BG_SQUARE_CLR, (262, 181, 80, 80), 5) #derecha,centro
    pygame.draw.rect(screen, BG_SQUARE_CLR, (262, 262, 80, 80), 5) #derecha,abajo
    # --- fin de zona de dibujo
    # actualizar pantalla
    pygame.display.flip()
    
# --- BFS ---
# estado inicial
# usar una cola para explorar cada nodo (configuracion del tablero)
# marcar estados visitidados (movimientos) para evitar ciclos
# repetir hasta encontrar el estado objetivo
'''