"""
╔═══════════════════════════════════════════════════╗
║                   MATRICES                        ║
║     Operaciones básicas y aplicación práctica     ║
╚═══════════════════════════════════════════════════╝
"""

# ============= CREAR MATRICES =============
print("\n" + "="*50)
print("CREAR Y MOSTRAR MATRICES")
print("="*50)

# Matriz 3x3 simple
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nMatriz 3x3:")
for fila in matriz:
    print(f"  {fila}")

# ============= ACCEDER A ELEMENTOS =============
print("\n" + "="*50)
print("ACCEDER A ELEMENTOS")
print("="*50)

print(f"\nElemento [0][0]: {matriz[0][0]}")
print(f"Elemento [1][2]: {matriz[1][2]}")
print(f"Elemento [2][1]: {matriz[2][1]}")

# Fila completa
print(f"\nFila 1 completa: {matriz[1]}")

# ============= SUMA DE MATRICES =============
print("\n" + "="*50)
print("SUMA DE MATRICES")
print("="*50)

matriz_a = [[1, 2], [3, 4]]
matriz_b = [[5, 6], [7, 8]]

print(f"\nMatriz A: {matriz_a[0]}")
print(f"          {matriz_a[1]}")
print(f"\nMatriz B: {matriz_b[0]}")
print(f"          {matriz_b[1]}")

# Sumar matrices
suma = []
for i in range(len(matriz_a)):
    fila_suma = []
    for j in range(len(matriz_a[0])):
        fila_suma.append(matriz_a[i][j] + matriz_b[i][j])
    suma.append(fila_suma)

print(f"\nA + B:    {suma[0]}")
print(f"          {suma[1]}")

# ============= APLICACIÓN: TABLERO TA-TE-TI =============
print("\n" + "="*50)
print("APLICACIÓN: TABLERO TA-TE-TI")
print("="*50)

# Crear tablero vacío
tablero = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def mostrar_tablero(t):
    """Muestra el tablero de forma visual"""
    print("\n     0   1   2")
    print("   ┌───┬───┬───┐")
    for i, fila in enumerate(t):
        print(f" {i} │ {fila[0]} │ {fila[1]} │ {fila[2]} │")
        if i < 2:
            print("   ├───┼───┼───┤")
    print("   └───┴───┴───┘")

def colocar_ficha(t, fila, col, simbolo):
    """Coloca una ficha en el tablero"""
    if t[fila][col] == ' ':
        t[fila][col] = simbolo
        return True
    return False

# Jugar algunas jugadas
print("\n1. Tablero inicial:")
mostrar_tablero(tablero)

print("\n2. Jugador X coloca en [0,0]:")
colocar_ficha(tablero, 0, 0, 'X')
mostrar_tablero(tablero)

print("\n3. Jugador O coloca en [1,1]:")
colocar_ficha(tablero, 1, 1, 'O')
mostrar_tablero(tablero)

print("\n4. Jugador X coloca en [0,2]:")
colocar_ficha(tablero, 0, 2, 'X')
mostrar_tablero(tablero)

# ============= ESTADÍSTICAS =============
print("\n" + "="*50)
print("ESTADÍSTICAS DE LA MATRIZ")
print("="*50)

numeros = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print("\nMatriz de números:")
for fila in numeros:
    print(f"  {fila}")

# Calcular suma total
total = 0
for fila in numeros:
    for num in fila:
        total += num

print(f"\nSuma total: {total}")

# Calcular promedio
filas = len(numeros)
columnas = len(numeros[0])
promedio = total / (filas * columnas)
print(f"Promedio: {promedio:.1f}")

# Encontrar máximo
maximo = numeros[0][0]
for fila in numeros:
    for num in fila:
        if num > maximo:
            maximo = num
print(f"Máximo: {maximo}")

print("\n" + "="*50)
print("Fin del ejemplo")
print("="*50 + "\n")
