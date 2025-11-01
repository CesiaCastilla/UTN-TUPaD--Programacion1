"""
Segundo Parcial - Programacion 1
Sistema de gestion de biblioteca escolar

Este programa permite cargar, consultar y actualizar el inventario de libros
manteniendo registros persistentes en un archivo CSV.
"""

import csv
import os

def cargar_catalogo(nombre_archivo):
    """
    Carga el catalogo desde un archivo CSV.
    Si el archivo no existe, retorna un catalogo vacio.

    Args:
        nombre_archivo: Ruta del archivo CSV

    Returns:
        Lista de diccionarios con los libros
    """
    catalogo = []

    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if fila:
                    catalogo.append({
                        'TITULO': fila['TITULO'].strip(),
                        'CANTIDAD': int(fila['CANTIDAD'])
                    })
    return catalogo

def guardar_catalogo(nombre_archivo, catalogo):
    """
    Guarda el catalogo en un archivo CSV.

    Args:
        nombre_archivo: Ruta del archivo CSV
        catalogo: Lista de diccionarios con los libros
    """
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=['TITULO', 'CANTIDAD'])
        escritor.writeheader()
        escritor.writerows(catalogo)

def normalizar_titulo(titulo):
    """
    Normaliza un titulo: elimina espacios extra y convierte a minusculas.

    Args:
        titulo: Titulo a normalizar

    Returns:
        Titulo normalizado
    """
    return ' '.join(titulo.split()).lower()

def validar_titulo(titulo):
    """
    Valida que el titulo no este vacio.

    Args:
        titulo: Titulo a validar

    Returns:
        True si es valido, False en caso contrario
    """
    return len(titulo.strip()) > 0

def validar_cantidad(cantidad_str):
    """
    Valida que la cantidad sea un numero entero no negativo.

    Args:
        cantidad_str: Cantidad como string

    Returns:
        Tupla (es_valida, cantidad) donde es_valida es bool y cantidad es int
    """
    if cantidad_str.isdigit():
        cantidad = int(cantidad_str)
        if cantidad >= 0:
            return True, cantidad
    return False, 0

def buscar_libro(catalogo, titulo):
    """
    Busca un libro por titulo en el catalogo.

    Args:
        catalogo: Lista de diccionarios con los libros
        titulo: Titulo a buscar

    Returns:
        Indice del libro si existe, -1 en caso contrario
    """
    titulo_normalizado = normalizar_titulo(titulo)

    for i, libro in enumerate(catalogo):
        if normalizar_titulo(libro['TITULO']) == titulo_normalizado:
            return i
    return -1

def libro_existe(catalogo, titulo):
    """
    Verifica si un libro existe en el catalogo.

    Args:
        catalogo: Lista de diccionarios con los libros
        titulo: Titulo a verificar

    Returns:
        True si existe, False en caso contrario
    """
    return buscar_libro(catalogo, titulo) != -1

def opcion_1_ingresar_multiples(catalogo, nombre_archivo):
    """
    Opcion 1: Ingresa multiples titulos nuevos.

    Args:
        catalogo: Lista de diccionarios con los libros
        nombre_archivo: Ruta del archivo CSV
    """
    print("\n" + "=" * 60)
    print("OPCION 1: INGRESAR MULTIPLES TITULOS")
    print("=" * 60)

    # Validar cantidad de libros a ingresar
    while True:
        cantidad_libros_str = input("\nCuantos libros desea cargar: ")
        if cantidad_libros_str.isdigit() and int(cantidad_libros_str) > 0:
            cantidad_libros = int(cantidad_libros_str)
            break
        else:
            print("Error: Ingrese un numero positivo.")

    libros_agregados = 0

    for i in range(cantidad_libros):
        print(f"\nLibro {i + 1}:")
        titulo = input("  Titulo: ").strip()

        # Validar titulo vacio
        if not validar_titulo(titulo):
            print("  Error: El titulo no puede estar vacio.")
            continue

        # Validar titulo duplicado
        if libro_existe(catalogo, titulo):
            print("  Error: Este libro ya existe en el catalogo.")
            continue

        cantidad_str = input("  Cantidad: ")
        es_valida, cantidad = validar_cantidad(cantidad_str)

        if not es_valida:
            print("  Error: La cantidad debe ser un numero entero >= 0.")
            continue

        # Agregar libro
        catalogo.append({
            'TITULO': titulo,
            'CANTIDAD': cantidad
        })
        libros_agregados += 1
        print(f"  Libro '{titulo}' agregado exitosamente.")

    if libros_agregados > 0:
        guardar_catalogo(nombre_archivo, catalogo)
        print(f"\nSe agregaron {libros_agregados} libro(s) al catalogo.")
        print("Catalogo guardado en archivo.")

def opcion_2_ingresar_ejemplares(catalogo, nombre_archivo):
    """
    Opcion 2: Suma ejemplares a un titulo existente.

    Args:
        catalogo: Lista de diccionarios con los libros
        nombre_archivo: Ruta del archivo CSV
    """
    print("\n" + "=" * 60)
    print("OPCION 2: INGRESAR EJEMPLARES")
    print("=" * 60)

    titulo = input("\nIngrese el titulo del libro: ").strip()

    # Validar que el titulo no este vacio
    if not validar_titulo(titulo):
        print("Error: El titulo no puede estar vacio.")
        return

    indice = buscar_libro(catalogo, titulo)
    if indice == -1:
        print(f"Error: El libro '{titulo}' no existe en el catalogo.")
        return

    # Validar cantidad a ingresar
    while True:
        cantidad_str = input("Cantidad a ingresar: ")
        es_valida, cantidad = validar_cantidad(cantidad_str)

        if es_valida:
            break
        else:
            print("Error: La cantidad debe ser un numero entero >= 0.")

    catalogo[indice]['CANTIDAD'] += cantidad
    guardar_catalogo(nombre_archivo, catalogo)
    print(f"\nSe agregaron {cantidad} ejemplar(es) a '{catalogo[indice]['TITULO']}'.")
    print(f"Nueva cantidad: {catalogo[indice]['CANTIDAD']}")
    print("Catalogo guardado en archivo.")

def opcion_3_mostrar_catalogo(catalogo):
    """
    Opcion 3: Muestra todos los libros del catalogo.

    Args:
        catalogo: Lista de diccionarios con los libros
    """
    print("\n" + "=" * 60)
    print("CATALOGO DE LIBROS")
    print("=" * 60)

    if len(catalogo) == 0:
        print("\nEl catalogo esta vacio.")
        return

    print("\n{:<45} {}".format("TITULO", "CANTIDAD"))
    print("-" * 60)

    for libro in catalogo:
        print("{:<45} {}".format(libro['TITULO'], libro['CANTIDAD']))

    print("-" * 60)
    print(f"Total de titulos: {len(catalogo)}")

def opcion_4_consultar_disponibilidad(catalogo):
    """
    Opcion 4: Consulta la disponibilidad de un libro.

    Args:
        catalogo: Lista de diccionarios con los libros
    """
    print("\n" + "=" * 60)
    print("CONSULTAR DISPONIBILIDAD")
    print("=" * 60)

    titulo = input("\nIngrese el titulo del libro: ").strip()

    # Validar que el titulo no este vacio
    if not validar_titulo(titulo):
        print("Error: El titulo no puede estar vacio.")
        return

    indice = buscar_libro(catalogo, titulo)
    if indice == -1:
        print(f"Error: El libro '{titulo}' no existe en el catalogo.")
        return

    cantidad = catalogo[indice]['CANTIDAD']
    print(f"\nTitulo: {catalogo[indice]['TITULO']}")
    print(f"Ejemplares disponibles: {cantidad}")

    if cantidad == 0:
        print("Estado: AGOTADO")
    elif cantidad == 1:
        print("Estado: ULTIMO EJEMPLAR")
    else:
        print(f"Estado: DISPONIBLE ({cantidad} ejemplares)")

def opcion_5_listar_agotados(catalogo):
    """
    Opcion 5: Lista los libros con cantidad = 0.

    Args:
        catalogo: Lista de diccionarios con los libros
    """
    print("\n" + "=" * 60)
    print("LIBROS AGOTADOS")
    print("=" * 60)

    agotados = [libro for libro in catalogo if libro['CANTIDAD'] == 0]

    if len(agotados) == 0:
        print("\nNo hay libros agotados.")
        return

    print("\n{:<45} {}".format("TITULO", "CANTIDAD"))
    print("-" * 60)

    for libro in agotados:
        print("{:<45} {}".format(libro['TITULO'], libro['CANTIDAD']))

    print("-" * 60)
    print(f"Total de titulos agotados: {len(agotados)}")

def opcion_6_agregar_titulo(catalogo, nombre_archivo):
    """
    Opcion 6: Agrega un titulo individual con validacion de duplicados.

    Args:
        catalogo: Lista de diccionarios con los libros
        nombre_archivo: Ruta del archivo CSV
    """
    print("\n" + "=" * 60)
    print("AGREGAR NUEVO TITULO")
    print("=" * 60)

    titulo = input("\nIngrese el titulo del libro: ").strip()

    # Validar titulo vacio
    if not validar_titulo(titulo):
        print("Error: El titulo no puede estar vacio.")
        return

    # Validar titulo duplicado
    if libro_existe(catalogo, titulo):
        print(f"Error: El libro '{titulo}' ya existe en el catalogo.")
        return

    # Validar cantidad de ejemplares
    while True:
        cantidad_str = input("Ingrese la cantidad de ejemplares: ")
        es_valida, cantidad = validar_cantidad(cantidad_str)

        if es_valida:
            break
        else:
            print("Error: La cantidad debe ser un numero entero >= 0.")

    # Agregar libro
    catalogo.append({
        'TITULO': titulo,
        'CANTIDAD': cantidad
    })
    guardar_catalogo(nombre_archivo, catalogo)
    print(f"\nLibro '{titulo}' agregado exitosamente.")
    print(f"Cantidad inicial: {cantidad} ejemplar(es)")
    print("Catalogo guardado en archivo.")

def opcion_7_actualizar_ejemplares(catalogo, nombre_archivo):
    """
    Opcion 7: Maneja prestamos y devoluciones.

    Args:
        catalogo: Lista de diccionarios con los libros
        nombre_archivo: Ruta del archivo CSV
    """
    print("\n" + "=" * 60)
    print("ACTUALIZAR EJEMPLARES (PRESTAMO/DEVOLUCION)")
    print("=" * 60)

    # Validar opcion de prestamo/devolucion
    while True:
        print("\n1. Prestamo")
        print("2. Devolucion")
        sub_opcion = input("\nSeleccione una opcion: ").strip()

        if sub_opcion in ['1', '2']:
            break
        else:
            print("Error: Ingrese una opcion valida (1 o 2).")

    # Solicitar titulo del libro
    titulo = input("\nIngrese el titulo del libro: ").strip()

    # Validar que el titulo no este vacio
    if not validar_titulo(titulo):
        print("Error: El titulo no puede estar vacio.")
        return

    indice = buscar_libro(catalogo, titulo)
    if indice == -1:
        print(f"Error: El libro '{titulo}' no existe en el catalogo.")
        return

    if sub_opcion == '1':
        # Prestamo
        if catalogo[indice]['CANTIDAD'] == 0:
            print(f"Error: No hay ejemplares disponibles de '{catalogo[indice]['TITULO']}'.")
            return

        catalogo[indice]['CANTIDAD'] -= 1
        guardar_catalogo(nombre_archivo, catalogo)
        print(f"\nPrestamo registrado para '{catalogo[indice]['TITULO']}'.")
        print(f"Ejemplares restantes: {catalogo[indice]['CANTIDAD']}")
        print("Catalogo guardado en archivo.")

    elif sub_opcion == '2':
        # Devolucion
        catalogo[indice]['CANTIDAD'] += 1
        guardar_catalogo(nombre_archivo, catalogo)
        print(f"\nDevolucion registrada para '{catalogo[indice]['TITULO']}'.")
        print(f"Ejemplares totales: {catalogo[indice]['CANTIDAD']}")
        print("Catalogo guardado en archivo.")

def menu_principal():
    """
    Muestra el menu principal y gestiona las opciones del usuario.
    """
    # Obtener la ruta del directorio donde esta el script
    directorio_script = os.path.dirname(os.path.abspath(__file__))
    nombre_archivo = os.path.join(directorio_script, "catalogo.csv")

    # Cargar catalogo al iniciar
    catalogo = cargar_catalogo(nombre_archivo)

    while True:
        print("\n" + "=" * 60)
        print("SISTEMA DE GESTION DE BIBLIOTECA ESCOLAR")
        print("=" * 60)
        print("1. Ingresar titulos (multiples)")
        print("2. Ingresar ejemplares")
        print("3. Mostrar catalogo")
        print("4. Consultar disponibilidad")
        print("5. Listar agotados")
        print("6. Agregar titulo (individual)")
        print("7. Actualizar ejemplares (prestamo/devolucion)")
        print("8. Salir")
        print("=" * 60)

        opcion = input("Seleccione una opcion: ").strip()

        match opcion:
            case '1':
                opcion_1_ingresar_multiples(catalogo, nombre_archivo)

            case '2':
                opcion_2_ingresar_ejemplares(catalogo, nombre_archivo)

            case '3':
                opcion_3_mostrar_catalogo(catalogo)

            case '4':
                opcion_4_consultar_disponibilidad(catalogo)

            case '5':
                opcion_5_listar_agotados(catalogo)

            case '6':
                opcion_6_agregar_titulo(catalogo, nombre_archivo)

            case '7':
                opcion_7_actualizar_ejemplares(catalogo, nombre_archivo)

            case '8':
                print("\nGracias por usar el sistema de biblioteca.")
                break

            case _:
                print("Opcion invalida. Por favor, seleccione una opcion del 1 al 8.")

def main():
    """
    Funcion principal del programa.
    """
    menu_principal()

if __name__ == "__main__":
    main()
