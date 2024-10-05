from collections import deque
import random

class Puzzle:
    def __init__(self, estado_inicial):
        self.estado_inicial = estado_inicial
        self.visitados = set()

    def movimientos_validos(self, estado):
        vecinos = []
        fila, columna = self.encontrar_espacio(estado)
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # arriba, abajo, izquierda, derecha

        for df, dc in direcciones:
            nueva_fila = fila + df
            nueva_columna = columna + dc
            if 0 <= nueva_fila < 3 and 0 <= nueva_columna < 3:
                nuevo_estado = [list(f) for f in estado]
                nuevo_estado[fila][columna], nuevo_estado[nueva_fila][nueva_columna] = nuevo_estado[nueva_fila][nueva_columna], nuevo_estado[fila][columna]
                vecinos.append(nuevo_estado)
        
        return vecinos

    def encontrar_espacio(self, estado):
        for i in range(3):
            for j in range(3):
                if estado[i][j] == 0:
                    return i, j

    def busqueda_en_amplitud(self, estado_objetivo):
        cola = deque([(self.estado_inicial, [])])
        self.visitados = {self._estado_a_tupla(self.estado_inicial)}
        
        while cola:
            estado_actual, ruta = cola.popleft()
            
            if estado_actual == estado_objetivo:
                return ruta + [estado_actual]
            
            for vecino in self.movimientos_validos(estado_actual):
                vecino_tupla = self._estado_a_tupla(vecino)
                if vecino_tupla not in self.visitados:
                    self.visitados.add(vecino_tupla)
                    cola.append((vecino, ruta + [vecino]))

        return None

    def _estado_a_tupla(self, estado):
        return tuple(map(tuple, estado))

# Ejemplo para generar estado inicial aleatorio
def generar_estado_inicial():
    puzzle = list(range(9))  # números del 0 al 8
    random.shuffle(puzzle)
    return [puzzle[i:i+3] for i in range(0, 9, 3)]

# Uso de ejemplo
estado_inicial = generar_estado_inicial()
estado_objetivo = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
solver = Puzzle(estado_inicial)
solucion = solver.busqueda_en_amplitud(estado_objetivo)
print(solucion)
