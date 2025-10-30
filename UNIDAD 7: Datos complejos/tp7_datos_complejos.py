# 1) Dado el diccionario precios_frutas, agregar las frutas con sus respectivos precios.
# Diccionario inicial
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Nuevas frutas y precios a añadir
nuevas_frutas = {'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

# El método .update() fusiona el diccionario 'nuevas_frutas' con 'precios_frutas'.
precios_frutas.update(nuevas_frutas)

# Mostrar el diccionario resultante
print("Diccionario de precios después de añadir nuevas frutas:")
print(precios_frutas)

# 2)
# Diccionario resultante del punto anterior:
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

# Actualizar los precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Mostrar el diccionario con los precios actualizados
print("\nDiccionario de precios después de la actualización:")
print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado
# en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

# Diccionario resultante del punto anterior:
# precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

# Crear una lista solo con los nombres de las frutas (las claves)
lista_frutas = list(precios_frutas.keys())

# Mostrar la lista resultante
print("\nLista que contiene únicamente los nombres de las frutas:")
print(lista_frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

print("\n--- Programa de Almacenamiento y Consulta de Contactos (Validado) ---")

# Inicializar el diccionario de contactos
contactos = {}
numero_de_contactos = 5

# Permitir al usuario cargar 5 contactos con validación
print(f"Por favor, ingrese los detalles de {numero_de_contactos} contactos:")
for i in range(numero_de_contactos):
    print(f"\nContacto #{i + 1}:")
    
    # --- Validación para el Nombre (solo strings no vacíos) ---
    while True:
        nombre = input("Ingrese el nombre del contacto: ").strip().title()
        if nombre:
            # Si el nombre no está vacío, rompemos el bucle de validación
            break
        else:
            print("Error: El nombre del contacto no puede estar vacío. Intente de nuevo.")

    # --- Validación para el Número (solo números enteros) ---
    while True:
        numero_str = input("Ingrese el número telefónico (solo números): ").strip()
        try:
            # Intentamos convertir la entrada a un entero.
            # No guardamos el int, lo guardamos como string para preservar ceros a la izquierda
            # si los hubiera, pero nos aseguramos de que sea solo numérico.
            int(numero_str) 
            if numero_str:
                numero = numero_str
                break # Si la conversión es exitosa y no está vacío, rompemos el bucle
            else:
                print("Error: El número telefónico no puede estar vacío. Intente de nuevo.")
        except ValueError:
            # Si la conversión falla, significa que había caracteres no numéricos.
            print("Error: El número debe contener solo dígitos enteros. Intente de nuevo.")

    # Almacenar en el diccionario
    contactos[nombre] = numero

# Mostrar los contactos cargados
print("\nContactos cargados:")
print(contactos)

# Consultar un número telefónico (sin cambios en la lógica de consulta)
nombre_a_buscar = input("\nIngrese el nombre del contacto cuyo número desea buscar: ").strip().title()

# Verificar si el nombre existe en el diccionario (es decir, es una clave)
if nombre_a_buscar in contactos:
    numero_encontrado = contactos[nombre_a_buscar]
    print(f"El número de teléfono de {nombre_a_buscar} es: {numero_encontrado}")
else:
    print(f"Lo siento, el contacto '{nombre_a_buscar}' no se encontró en la agenda.")

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

print("\n--- Analizador de Frases ---")

# Solicitar la frase al usuario
frase = input("Ingrese una frase: ")

# Preprocesar la frase
# Convertir a minúsculas para tratar 'Hola' y 'hola' como la misma palabra.
# Dividir la cadena en una lista de palabras usando el espacio como separador.
palabras = frase.lower().split()

# Calcular las palabras únicas (usando un set)
palabras_unicas = set(palabras)

# Calcular la cantidad de veces que aparece cada palabra (usando un diccionario)
frecuencia_palabras = {}
for palabra in palabras:
    # Si la palabra ya está en el diccionario, incrementa el contador
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    # Si es la primera vez que se encuentra, inicializa el contador en 1
    else:
        frecuencia_palabras[palabra] = 1
        
# Imprimir los resultados
print("\n--- Resultados ---")
print("Palabras únicas encontradas (Set):")
print(palabras_unicas)
print("\nConteo de frecuencia de cada palabra (Diccionario):")
print(frecuencia_palabras)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

print("\n--- Calculadora de Promedio de Notas ---")

# Inicializar el diccionario de alumnos
alumnos_notas = {}
numero_de_alumnos = 3

# Ingresar nombres de alumnos y sus tuplas de notas
for i in range(numero_de_alumnos):
    nombre = input(f"Ingrese el nombre del alumno #{i + 1}: ")
    
    # Solicitar las 3 notas
    print(f"Ingrese las 3 notas para {nombre}:")
    # Utilizamos list comprehension para facilitar el ingreso de las 3 notas
    notas_str = [input(f"Nota {j + 1}: ") for j in range(3)]
    
    # Convertir las notas a números (float) y guardarlas como una tupla
    try:
        notas_float = tuple(float(n) for n in notas_str)
        alumnos_notas[nombre] = notas_float
    except ValueError:
        print("¡Advertencia! Asegúrese de ingresar números válidos para las notas. Saltando este alumno.")

# Mostrar el promedio de cada alumno
print("\n--- Promedios de Alumnos ---")

for nombre, notas in alumnos_notas.items():
    # 'notas' es una tupla, y podemos usar las funciones sum() y len() directamente
    suma_notas = sum(notas)
    cantidad_notas = len(notas)
    
    # Calcular el promedio
    if cantidad_notas > 0:
        promedio = suma_notas / cantidad_notas
        # Usamos un formato de cadena f-string para limitar el promedio a 2 decimales
        print(f"El promedio de notas de {nombre} es: {promedio:.2f}")
    else:
        print(f"Error: {nombre} no tiene notas registradas.")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

print("\n--- Análisis de Estudiantes Aprobados ---")

# Sets de estudiantes que aprobaron cada parcial
aprobados_parcial1 = {'Ana', 'Pedro', 'Luis', 'Sofia', 'Marta', 'Javier'}
aprobados_parcial2 = {'Pedro', 'Sofia', 'Elena', 'Diego', 'Javier', 'Carmen'}

print("Aprobados Parcial 1:", aprobados_parcial1)
print("Aprobados Parcial 2:", aprobados_parcial2)

# Mostrar los que aprobaron ambos parciales (Intersección)
aprobados_ambos = aprobados_parcial1.intersection(aprobados_parcial2)
# Alternativa: aprobados_ambos = aprobados_parcial1 & aprobados_parcial2
print("\nEstudiantes que aprobaron AMBOS parciales (Intersección):")
print(aprobados_ambos)

# Mostrar los que aprobaron solo uno de los dos (Diferencia Simétrica)
aprobados_solo_uno = aprobados_parcial1.symmetric_difference(aprobados_parcial2)
# Alternativa: aprobados_solo_uno = aprobados_parcial1 ^ aprobados_parcial2
print("Estudiantes que aprobaron SOLO UNO de los dos (Diferencia Simétrica):")
print(aprobados_solo_uno)

# Lista total de estudiantes que aprobaron al menos un parcial (Unión)
aprobados_total = aprobados_parcial1.union(aprobados_parcial2)
# Alternativa: aprobados_total = aprobados_parcial1 | aprobados_parcial2
print("Lista total de estudiantes que aprobaron AL MENOS UN parcial (Unión):")
print(aprobados_total)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

print("\n--- Sistema de Gestión de Stock ---")

# Diccionario inicial de stock (producto: cantidad)
stock_productos = {'Teclado': 15, 'Mouse': 20, 'Monitor': 8}
print("Stock inicial:", stock_productos)

while True:
    print("\n--- Opciones ---")
    print("1. Consultar Stock de un producto")
    print("2. Agregar Unidades al Stock (producto existente)")
    print("3. Agregar Nuevo Producto y Stock")
    print("4. Salir")
    
    opcion = input("Ingrese el número de su opción: ")
    
    if opcion == '1':
        # Consultar Stock
        producto = input("Ingrese el nombre del producto a consultar: ").strip().title()
        if producto in stock_productos:
            print(f"Stock de {producto}: {stock_productos[producto]} unidades.")
        else:
            print(f"El producto '{producto}' no está en el inventario.")

    elif opcion == '2':
        # Agregar Unidades al Stock
        producto = input("Ingrese el nombre del producto para agregar unidades: ").strip().title()
        if producto in stock_productos:
            try:
                cantidad = int(input(f"Ingrese cuántas unidades agregar a {producto}: "))
                if cantidad > 0:
                    stock_productos[producto] += cantidad
                    print(f"Stock de {producto} actualizado. Nuevo stock: {stock_productos[producto]}")
                else:
                    print("La cantidad debe ser un número positivo.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número entero.")
        else:
            print(f"El producto '{producto}' no existe. Use la opción 3 para agregarlo.")

    elif opcion == '3':
        # Agregar Nuevo Producto
        nuevo_producto = input("Ingrese el nombre del nuevo producto: ").strip().title()
        if nuevo_producto not in stock_productos:
            try:
                nuevo_stock = int(input(f"Ingrese el stock inicial para {nuevo_producto}: "))
                if nuevo_stock >= 0:
                    stock_productos[nuevo_producto] = nuevo_stock
                    print(f"Producto '{nuevo_producto}' agregado con stock inicial de {nuevo_stock}.")
                else:
                    print("El stock inicial no puede ser negativo.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número entero.")
        else:
            print(f"El producto '{nuevo_producto}' ya existe. Use la opción 2 para actualizar su stock.")

    elif opcion == '4':
        # --- Salir ---
        print("Saliendo del sistema. Stock final:", stock_productos)
        break
        
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 4.")

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

print("\n--- Agenda de Eventos ---")

# Agenda con tuplas (día, hora) como claves
agenda = {
    ('Lunes', 10): 'Reunión de planificación',
    ('Martes', 15): 'Clase de Python',
    ('Miércoles', 9): 'Cita con el dentista',
    ('Viernes', 18): 'Evento de networking'
}

print("Eventos programados:", agenda)

# Permitir al usuario consultar un día y hora
print("\n--- Consulta de Actividad ---")
dia_consulta = input("Ingrese el día (ej: Lunes, Martes): ").strip().title()
hora_consulta_str = input("Ingrese la hora (formato 24h, ej: 10, 15): ").strip()

try:
    # Convertir la hora a entero
    hora_consulta = int(hora_consulta_str)
    
    # Construir la clave de la tupla para la búsqueda
    clave_consulta = (dia_consulta, hora_consulta)
    
    # Consultar la actividad usando la clave de tupla
    if clave_consulta in agenda:
        evento = agenda[clave_consulta]
        print(f"\nActividad para el {dia_consulta} a las {hora_consulta}:00: **{evento}**")
    else:
        print(f"\nNo hay actividad programada para el {dia_consulta} a las {hora_consulta}:00.")
        
except ValueError:
    print("Error: La hora ingresada no es un número válido.")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

print("\n--- Inversor de Diccionario País-Capital ---")

# Diccionario original (País: Capital)
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago',
    'Perú': 'Lima',
    'Colombia': 'Bogotá',
    'España': 'Madrid'
}
print("Diccionario original (País: Capital):")
print(paises_capitales)

# Construir el nuevo diccionario invertido
capitales_paises = {}

# Iterar sobre el diccionario original
for pais, capital in paises_capitales.items():
    # Asignar la capital como la clave y el país como el valor en el nuevo diccionario
    capitales_paises[capital] = pais

# Mostrar el diccionario invertido
print("\nDiccionario Invertido (Capital: País):")
print(capitales_paises)
