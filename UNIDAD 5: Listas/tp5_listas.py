# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja

# Definición de la cantidad de estudiantes para el ejercicio 1.
cantidad_estudiantes = 10 

# Inicializar la lista que guardará las notas.
lista_notas = []

print(f"--- Ejercicio 1: Notas de {cantidad_estudiantes} Estudiantes ---")

# Bucle para solicitar las 10 notas y añadirlas a la lista.
for i in range(cantidad_estudiantes):
    while True:
        # Solicitar la nota.
        nota_str = input(f"Ingrese la nota del estudiante {i + 1}: ")
        nota = int(nota_str)
        
        # Validar que la nota esté en un rango razonable (ej. 0 a 10)
        if 0 <= nota <= 10:
            lista_notas.append(nota) # Usando el método append()
            break
        else:
            print("Nota fuera de rango (debe ser entre 0 y 10).")

# --- Mostrar la lista completa (usando una estructura repetitiva, como se solicita)  ---
print("\n--- Lista Completa de Notas ---")
for nota in lista_notas:
    print(f"Nota: {nota}")

# --- Calcular y mostrar el promedio  ---
# Usamos un acumulador para sumar las notas.
suma_notas = 0
for nota in lista_notas:
    suma_notas += nota

# La media es la suma total dividida por la cantidad de elementos.
promedio = suma_notas / cantidad_estudiantes
print(f"\nEl promedio de las notas es: {promedio:.2f}") # Formateado a 2 decimales

# --- Indicar la nota más alta y la más baja  ---
# Python tiene funciones integradas que son ideales para esto.
nota_maxima = max(lista_notas)
nota_minima = min(lista_notas)

print(f"La nota más alta registrada es: {nota_maxima}")
print(f"La nota más baja registrada es: {nota_minima}")

# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

cantidad_productos = 5

# Inicializar la lista de productos.
lista_productos = []

print(f"\n--- Ejercicio 2: Carga y Gestión de {cantidad_productos} Productos ---")

# Bucle para pedir los 5 productos.
for i in range(cantidad_productos):
    producto = input(f"Ingrese el nombre del producto {i + 1} de {cantidad_productos}: ")
    lista_productos.append(producto)

# --- Mostrar la lista ordenada alfabéticamente  ---
# Investigando: sorted() devuelve una *nueva* lista ordenada sin modificar la original.
lista_ordenada = sorted(lista_productos)

print("\nLista de productos ordenada alfabéticamente:")
# Usamos un bucle for para mostrar los elementos[cite: 15].
for producto in lista_ordenada:
    print(f"- {producto}")

# --- Eliminar un producto [cite: 24] ---
while True:
    producto_a_eliminar = input("\n¿Qué producto desea eliminar de la lista? (Ingrese el nombre exacto): ")

    # Comprobamos si el producto está en la lista original antes de intentar eliminarlo.
    if producto_a_eliminar in lista_productos:
        lista_productos.remove(producto_a_eliminar) # Uso del método remove()
        print(f"{producto_a_eliminar} ha sido eliminado exitosamente.")
        break
    else:
        print(f"{producto_a_eliminar} no se encontró en la lista. Intente de nuevo.")

# --- Mostrar la lista final actualizada [cite: 24] ---
print("\n--- Lista Final Actualizada ---")
for producto in lista_productos:
    print(f"- {producto}")

# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

cantidad_numeros = 15

# Usamos una lista fija para simular los 15 números al azar, 
lista_fija = [56, 17, 34, 91, 2, 77, 40, 8, 63, 100, 25, 4, 39, 72, 11]

lista_pares = []
lista_impares = []

print("--- Ejercicio 3: Separación de Pares/Impares ---")
print(f"Lista de {cantidad_numeros} números a procesar: {lista_fija}")

# Clasificar los números.
for numero in lista_fija:
    # Usando el operador módulo (%) para verificar paridad.
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

# Mostrar resultados.
# La cantidad de números se obtiene usando len().
print("\n--- Resultados de Clasificación ---")
print(f"Lista de Pares (Cantidad: {len(lista_pares)}):")
# Usamos un bucle para mostrar la lista.
for par in lista_pares:
    print(par, end=" ")
print("\n")

print(f"Lista de Impares (Cantidad: {len(lista_impares)}):")
for impar in lista_impares:
    print(impar, end=" ")
print("\n")

# 4) Dada una lista con valores repetidos:
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

print("--- Ejercicio 4: Eliminar Elementos Repetidos ---")

# Lista inicial con valores repetidos.
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

# Inicializar la nueva lista sin elementos repetidos.
lista_sin_repetidos = []

# Recorrer la lista original.
for elemento in datos:
    # Comprobar si el elemento NO está ya en la nueva lista.
    if elemento not in lista_sin_repetidos:
        lista_sin_repetidos.append(elemento)

# Mostrar el resultado.
print(f"Lista Original: {datos}")
print(f"Nueva lista sin elementos repetidos:")
for elemento in lista_sin_repetidos:
    print(elemento, end=" ")
print()

# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

# Crear la lista inicial con 8 nombres.
lista_estudiantes = [
    "Ana", "Beto", "Carlos", "Diana", 
    "Elena", "Felipe", "Gaby", "Hugo"
]

print("\n--- Ejercicio 5: Gestión de Lista de Estudiantes ---")

# Bucle principal para el menú de gestión.
while True:
    print("\nLista actual de estudiantes:")
    # Mostrar la lista usando un bucle.
    for i in range(len(lista_estudiantes)):
        print(f"  {i+1}. {lista_estudiantes[i]}")
        
    print("\nOpciones:")
    print("  1. Agregar un nuevo estudiante")
    print("  2. Eliminar un estudiante existente")
    print("  3. Mostrar la lista final y Salir")
    
    opcion = input("Elige una opción (1, 2, o 3): ")

    if opcion == '1':
        # Agregar un estudiante (uso de .append()).
        nuevo_estudiante = input("Nombre del nuevo estudiante: ")
        lista_estudiantes.append(nuevo_estudiante)
        print(f"{nuevo_estudiante} agregado.")
        
    elif opcion == '2':
        # Eliminar un estudiante (uso de .remove()).
        estudiante_a_eliminar = input("Nombre del estudiante a eliminar: ")
        if estudiante_a_eliminar in lista_estudiantes:
            lista_estudiantes.remove(estudiante_a_eliminar)
            print(f"{estudiante_a_eliminar} eliminado.")
        else:
            print(f"{estudiante_a_eliminar} no se encontró.")
            
    elif opcion == '3':
        # Salir.
        break
        
    else:
        print("Opción no válida. Inténtalo de nuevo.")

# Mostrar la lista final actualizada.
print("\n--- Lista Final de Estudiantes ---")
for nombre in lista_estudiantes:
    print(f"- {nombre}")

# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

# Lista inicial de 7 números.
numeros = [10, 20, 30, 40, 50, 60, 70]

print("\n--- Ejercicio 6: Rotación de Elementos a la Derecha ---")
print(f"Lista original: {numeros}")

# Rotar los elementos una posición hacia la derecha.
# Usar pop() para obtener y eliminar el último elemento (posición -1).
ultimo_elemento = numeros.pop() 

# Usar insert() para colocar ese elemento en la posición 0 (el inicio).
numeros.insert(0, ultimo_elemento)

# Mostrar la lista rotada.
print(f"Lista después de la rotación: {numeros}")

# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

# Crear la matriz (lista anidada) de temperaturas (7x2).
# Formato: [[mínima, máxima], ...]
temperaturas = [
    [10, 22], # Lunes
    [12, 25], # Martes
    [15, 27], # Miércoles
    [11, 23], # Jueves
    [14, 28], # Viernes
    [13, 26], # Sábado
    [10, 20]  # Domingo
]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
cantidad_dias = len(temperaturas)

print("\n--- Ejercicio 7: Matriz de Temperaturas (7x2) ---")

# --- Calcular el promedio de las mínimas y las máximas ---
suma_minimas = 0
suma_maximas = 0

for dia in temperaturas:
    # dia[0] es la mínima, dia[1] es la máxima.
    suma_minimas = suma_minimas + dia[0]
    suma_maximas = suma_maximas + dia[1]

promedio_minimas = suma_minimas / cantidad_dias
promedio_maximas = suma_maximas / cantidad_dias

print(f"Promedio de temperaturas mínimas: {promedio_minimas:.1f}°C")
print(f"Promedio de temperaturas máximas: {promedio_maximas:.1f}°C")

# --- Mostrar el día con mayor amplitud térmica ---
mayor_amplitud = -1 # Para comparar y encontrar la mayor.
dia_mayor_amplitud = ""

for i in range(cantidad_dias):
    temp_min = temperaturas[i][0]
    temp_max = temperaturas[i][1]
    
    amplitud_actual = temp_max - temp_min
    
    if amplitud_actual > mayor_amplitud:
        mayor_amplitud = amplitud_actual
        dia_mayor_amplitud = dias[i]

print(f"\nLa mayor amplitud térmica ({mayor_amplitud}°C) se registró el día: {dia_mayor_amplitud}")

# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

# Crear la matriz (lista anidada) de notas (5 estudiantes x 3 materias).
notas = [
    [8, 7, 9],  # Estudiante 1
    [6, 8, 7],  # Estudiante 2
    [9, 9, 10], # Estudiante 3
    [7, 6, 8],  # Estudiante 4
    [10, 7, 9]  # Estudiante 5
]
cantidad_estudiantes = len(notas)
cantidad_materias = len(notas[0])

print("\n--- Ejercicio 8: Matriz de Notas (5x3) ---")

# --- Mostrar el promedio de cada estudiante (por fila) ---
print("\nPromedio por Estudiante:")
for i in range(cantidad_estudiantes):
    suma_estudiante = 0
    # Recorrer las notas de un solo estudiante (la fila i).
    for nota in notas[i]:
        suma_estudiante = suma_estudiante + nota # Evitamos sum()
        
    promedio_estudiante = suma_estudiante / cantidad_materias
    print(f"Estudiante {i + 1}: {promedio_estudiante:.2f}")

# --- Mostrar el promedio de cada materia (por columna) ---
print("\nPromedio por Materia:")
for j in range(cantidad_materias):
    suma_materia = 0
    # Recorrer verticalmente (la misma columna 'j' en todas las filas 'i').
    for i in range(cantidad_estudiantes):
        suma_materia = suma_materia + notas[i][j]
        
    promedio_materia = suma_materia / cantidad_estudiantes
    print(f"Materia {j + 1}: {promedio_materia:.2f}")

# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

# Inicializar el tablero como una lista anidada (matriz) de 3x3.
# Se inicializa con guiones "-" representando casillas vacías.
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# Inicializar las variables de control.
jugador_actual = "X"
turno = 0
jugadas_maximas = 9

print("--- Ejercicio 9: Tablero de Ta-Te-Ti (3x3) ---")

# Bucle principal del juego. Se ejecuta mientras haya menos de 9 turnos.
while turno < jugadas_maximas:
    
    # --- Mostrar el Tablero Actual (No usamos función para mostrar) ---
    print("\n  0 1 2")
    # Mostrar Fila 0
    print(f"0 {tablero[0][0]} {tablero[0][1]} {tablero[0][2]}") 
    # Mostrar Fila 1
    print(f"1 {tablero[1][0]} {tablero[1][1]} {tablero[1][2]}")
    # Mostrar Fila 2
    print(f"2 {tablero[2][0]} {tablero[2][1]} {tablero[2][2]}")
    
    # -----------------------------------------------------------------
    
    print(f"\nTurno de Jugador {jugador_actual}")
    
    # Pedir la posición (fila y columna).
    entrada_fila = input("Ingresa la fila (0, 1 o 2): ")
    fila = int(entrada_fila)
    
    entrada_columna = input("Ingresa la columna (0, 1 o 2): ")
    columna = int(entrada_columna)
    
    # Validar las coordenadas.
    if 0 <= fila <= 2 and 0 <= columna <= 2:
        
        # Validar que la casilla esté vacía.
        if tablero[fila][columna] == "-":
            
            # Actualizar la matriz con la marca del jugador.
            tablero[fila][columna] = jugador_actual
            
            # Cambiar el turno y avanzar el contador.
            if jugador_actual == "X":
                jugador_actual = "O"
            else:
                jugador_actual = "X"
            
            turno = turno + 1
        else:
            print("¡Esa casilla ya está ocupada! Intenta de nuevo.")
    else:
        print("Coordenadas fuera de rango. Ingresa 0, 1 o 2.")

# El juego ha terminado (por alcanzar 9 turnos).
print("\n--- ¡Juego Terminado! ---")
# Mostrar el tablero final.
print("\n  0 1 2")
print(f"0 {tablero[0][0]} {tablero[0][1]} {tablero[0][2]}") 
print(f"1 {tablero[1][0]} {tablero[1][1]} {tablero[1][2]}")
print(f"2 {tablero[2][0]} {tablero[2][1]} {tablero[2][2]}")

# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

# Crear la matriz de ventas (4 productos x 7 días).
ventas = [
    [100, 150, 200, 120, 180, 250, 110], # Producto 0
    [50, 80, 60, 90, 100, 70, 85],       # Producto 1
    [200, 100, 150, 130, 210, 160, 190], # Producto 2
    [70, 60, 50, 40, 30, 20, 10]         # Producto 3
]
productos = ["Producto A", "Producto B", "Producto C", "Producto D"]
dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
cant_productos = len(ventas)
cant_dias = len(ventas[0])

print("\n--- Ejercicio 10: Análisis de Ventas (4x7) ---")

# --- Mostrar el total vendido por cada producto (suma de filas) ---
print("\nTotal Vendido por Cada Producto:")
max_venta_producto = -1
producto_mas_vendido = ""

for i in range(cant_productos):
    total_producto = 0
    # Sumar los elementos de la fila 'i'
    for venta_diaria in ventas[i]:
        total_producto = total_producto + venta_diaria # Evitamos sum()
        
    print(f"{productos[i]}: ${total_producto}")
    
    # Encontrar el producto más vendido.
    if total_producto > max_venta_producto:
        max_venta_producto = total_producto
        producto_mas_vendido = productos[i]

# --- Mostrar el día con mayores ventas totales (suma de columnas) ---
total_ventas_dia = []
for j in range(cant_dias):
    suma_dia = 0
    # Recorrer verticalmente (misma columna 'j' en todas las filas 'i').
    for i in range(cant_productos):
        suma_dia = suma_dia + ventas[i][j]
    total_ventas_dia.append(suma_dia)

# Encontrar el día con la mayor venta (buscando el máximo valor).
max_total_dia = -1
for venta in total_ventas_dia:
    if venta > max_total_dia:
        max_total_dia = venta

# Encontrar el índice (posición) de ese máximo valor para obtener el nombre del día.
dia_max_indice = -1
for i in range(cant_dias):
    if total_ventas_dia[i] == max_total_dia:
        dia_max_indice = i
        break # Detenerse una vez que se encuentra.

dia_max_ventas = dias[dia_max_indice]

print(f"\nDía con mayores ventas totales: {dia_max_ventas} (Total: ${max_total_dia})")

# --- Indicar el producto más vendido en la semana ---
print(f"\nEl producto más vendido en la semana fue: {producto_mas_vendido} (Total: ${max_venta_producto})")
