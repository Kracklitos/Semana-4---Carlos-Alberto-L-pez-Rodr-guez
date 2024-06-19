def imprimir_tablero(tablero):
    for fila in tablero:
        print(fila)

def encontrar_celda_vacia(tablero):
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                return (i, j)
    return None

def es_valido(tablero, numero, posicion):
    # Verificar fila
    for i in range(9):
        if tablero[posicion[0]][i] == numero and posicion[1] != i:
            return False
    # Verificar columna
    for i in range(9):
        if tablero[i][posicion[1]] == numero and posicion[0] != i:
            return False
    # Verificar cuadrante
    cuadrante_x = posicion[1] // 3
    cuadrante_y = posicion[0] // 3
    for i in range(cuadrante_y*3, cuadrante_y*3 + 3):
        for j in range(cuadrante_x*3, cuadrante_x*3 + 3):
            if tablero[i][j] == numero and (i, j) != posicion:
                return False
    return True

def resolver_sudoku(tablero):
    celda_vacia = encontrar_celda_vacia(tablero)
    if not celda_vacia:
        return True
    else:
        fila, columna = celda_vacia

    for i in range(1, 10):
        if es_valido(tablero, i, (fila, columna)):
            tablero[fila][columna] = i

            if resolver_sudoku(tablero):
                return True

            tablero[fila][columna] = 0

    return False

tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Tablero inicial:")
imprimir_tablero(tablero)

if resolver_sudoku(tablero):
    print("\nSolución encontrada:")
    imprimir_tablero(tablero)
else:
    print("\nNo se encontró solución para este tablero.")
