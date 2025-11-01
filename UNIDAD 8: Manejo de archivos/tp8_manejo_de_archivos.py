"""
TP 8 - Manejo de archivos
Este programa gestiona un sistema de productos utilizando archivos de texto.
Permite leer, mostrar, agregar, buscar y actualizar productos.
"""


# ACTIVIDAD 2: Leer y mostrar productos
# ACTIVIDAD 4: Cargar productos en una lista de diccionarios
def leer_productos(nombre_archivo):
    """
    Lee los productos desde un archivo de texto y los carga en una lista de diccionarios.

    Args:
        nombre_archivo: Ruta del archivo de productos

    Returns:
        Lista de diccionarios con los productos
    """
    productos = []

    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:  # Ignorar lineas vacias
                    datos = linea.split(',')
                    if len(datos) == 3:
                        producto = {
                            'nombre': datos[0],
                            'precio': float(datos[1]),
                            'cantidad': int(datos[2])
                        }
                        productos.append(producto)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

    return productos


# ACTIVIDAD 2: Leer y mostrar productos
def mostrar_productos(productos):
    """
    Muestra todos los productos en formato legible.

    Args:
        productos: Lista de diccionarios con los productos
    """
    print("\n=== LISTA DE PRODUCTOS ===")
    if not productos:
        print("No hay productos para mostrar.")
    else:
        for producto in productos:
            print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
    print("=" * 50)


# ACTIVIDAD 3: Agregar productos desde teclado
def agregar_producto(productos):
    """
    Solicita al usuario los datos de un nuevo producto y lo agrega a la lista.
    Si el producto ya existe (mismo nombre), actualiza sus datos.

    Args:
        productos: Lista de diccionarios con los productos
    """
    print("\n--- Agregar nuevo producto ---")

    nombre = input("Ingrese el nombre del producto: ").strip()

    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("Error: El precio no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Error: Ingrese un numero valido para el precio.")

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad < 0:
                print("Error: La cantidad no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Error: Ingrese un numero entero valido para la cantidad.")

    # Buscar si el producto ya existe
    producto_existente = None
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            producto_existente = producto
            break

    if producto_existente:
        # Actualizar producto existente
        producto_existente['precio'] = precio
        producto_existente['cantidad'] = cantidad
        print(f"\nProducto '{nombre}' actualizado exitosamente.")
    else:
        # Agregar nuevo producto
        nuevo_producto = {
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad
        }
        productos.append(nuevo_producto)
        print(f"\nProducto '{nombre}' agregado exitosamente.")


# ACTIVIDAD 5: Buscar producto por nombre
def buscar_producto(productos, nombre_buscado):
    """
    Busca un producto por nombre y muestra sus datos.

    Args:
        productos: Lista de diccionarios con los productos
        nombre_buscado: Nombre del producto a buscar

    Returns:
        El diccionario del producto si se encuentra, None si no existe
    """
    for producto in productos:
        if producto['nombre'].lower() == nombre_buscado.lower():
            return producto
    return None


# ACTIVIDAD 6: Guardar los productos actualizados
def guardar_productos(nombre_archivo, productos):
    """
    Guarda todos los productos en el archivo, sobrescribiendo el contenido anterior.

    Args:
        nombre_archivo: Ruta del archivo de productos
        productos: Lista de diccionarios con los productos
    """
    try:
        with open(nombre_archivo, 'w') as archivo:
            for producto in productos:
                linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
                archivo.write(linea)
        print(f"\nProductos guardados exitosamente en '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")


def menu_principal():
    """
    Muestra el menu principal y gestiona las opciones del usuario.
    """
    import os

    # Obtener la ruta del directorio donde esta el script
    directorio_script = os.path.dirname(os.path.abspath(__file__))
    nombre_archivo = os.path.join(directorio_script, "productos.txt")

    # Cargar productos al inicio del programa
    productos = leer_productos(nombre_archivo)

    while True:
        print("\n" + "=" * 50)
        print("SISTEMA DE GESTION DE PRODUCTOS")
        print("=" * 50)
        print("1. Mostrar productos")
        print("2. Agregar/Actualizar producto")
        print("3. Buscar producto por nombre")
        print("4. Guardar productos actualizados")
        print("5. Recargar productos desde archivo")
        print("6. Salir")
        print("=" * 50)

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == '1':
            # Mostrar productos en memoria
            mostrar_productos(productos)

        elif opcion == '2':
            # Agregar o actualizar producto
            agregar_producto(productos)

        elif opcion == '3':
            # Buscar producto por nombre
            if not productos:
                print("\nNo hay productos en memoria.")
            else:
                nombre = input("\nIngrese el nombre del producto a buscar: ").strip()
                producto_encontrado = buscar_producto(productos, nombre)

                if producto_encontrado:
                    print("\n--- Producto encontrado ---")
                    print(f"Nombre: {producto_encontrado['nombre']}")
                    print(f"Precio: ${producto_encontrado['precio']}")
                    print(f"Cantidad: {producto_encontrado['cantidad']}")
                else:
                    print(f"\nError: El producto '{nombre}' no existe en el sistema.")

        elif opcion == '4':
            # Guardar productos actualizados
            if not productos:
                print("\nNo hay productos para guardar.")
            else:
                guardar_productos(nombre_archivo, productos)

        elif opcion == '5':
            # Recargar productos desde archivo
            productos = leer_productos(nombre_archivo)
            print("\nProductos recargados desde el archivo.")
            mostrar_productos(productos)

        elif opcion == '6':
            # Salir
            print("\nGracias por usar el sistema de gestion de productos!")
            break

        else:
            print("\nOpcion invalida. Por favor, seleccione una opcion del 1 al 6.")


def main():
    """
    Funcion principal del programa.
    """
    menu_principal()


if __name__ == "__main__":
    main()
