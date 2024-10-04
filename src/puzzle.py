from collections import deque

class Puzzle:
    def __init__(self, estado_incial):
        self.estado_inicial = estado_incial
        self.visitados = set()
    #
    def movimientos_validos(self, estado):
        vecinos = []
        fila, columna = self.encontrar_espacio(estado)
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)] # arriba, abajo, izquierda, derecha
        
        for df, dc in direcciones:
            nueva_fila = fila + df
            nueva_columna = columna + dc
            if 0 <= nueva_fila < 3 and 0 <= nueva_columna < 3:
                nuevo_estado = [list(fila) for fila in estado]
                nuevo_estado[fila][columna] = nuevo_estado[nueva_fila][nueva_columna]
                nuevo_estado[nueva_fila][nueva_columna] = nuevo_estado[fila][columna]
                vecinos.append(nuevo_estado)
            else:
                pass
        return vecinos
    #
    def encontrar_espacio(self, estado):
        for i in range(3):
            for j in range(3):
                if estado[i][j] == 0:
                    return i, j
                else:
                    pass
    #
    def busqueda_en_amplitud(self, estado_objetivo):
        cola = deque([self.estado_inicial])
        self.visitados.add(tuple(map(tuple, self.estado_inicial)))
        
        while cola:
            estado_actual = cola.popleft()
            
            if estado_actual == estado_objetivo:
                return estado_actual
            
            for vecino in self.movimientos_validos(estado_actual):
                vecino_tupla = self._estado_a_tupla(vecino)
                if vecino_tupla not in self.visitados:
                    self.visitados.add(vecino_tupla)
                    cola.append(vecino)
        return None
    
    def _estado_a_tupla(self, estado):
        return tuple(map(tuple, estado))