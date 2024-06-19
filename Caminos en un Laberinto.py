def encontrar_caminos(laberinto, entrada, salida):
    """Encuentra todos los caminos posibles en un laberinto.

    Args:
        laberinto: Una lista de listas que representa el laberinto.
        entrada: Una tupla que representa las coordenadas de la entrada.
        salida: Una tupla que representa las coordenadas de la salida.

    Returns:
        Una lista de caminos, donde cada camino es una lista de coordenadas.
    """

    filas = len(laberinto)
    columnas = len(laberinto[0])

    def es_valido(fila, columna):
        """Verifica si una coordenada es válida dentro del laberinto."""
        return 0 <= fila < filas and 0 <= columna < columnas and laberinto[fila][columna] == 0

    def dfs(fila, columna, camino):
        """Busca caminos recursivamente usando DFS."""
        if (fila, columna) == salida:
            caminos.append(camino.copy())
            return

        camino.append((fila, columna))
        laberinto[fila][columna] = 1  # Marca la celda actual como visitada

        # Intenta moverse en las cuatro direcciones posibles
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nueva_fila = fila + dr
            nueva_columna = columna + dc
            if es_valido(nueva_fila, nueva_columna):
                dfs(nueva_fila, nueva_columna, camino)

        laberinto[fila][columna] = 0  # Desmarca la celda actual

    caminos = []
    dfs(entrada[0], entrada[1], [])
    return caminos


# Ejemplo de uso
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]
entrada = (0, 0)
salida = (4, 4)

caminos_posibles = encontrar_caminos(laberinto, entrada, salida)

print("Caminos posibles:")
for camino in caminos_posibles:
    print(camino)
