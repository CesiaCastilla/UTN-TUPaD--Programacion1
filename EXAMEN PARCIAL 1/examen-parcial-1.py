# --- Primer Parcial – Programación 1 --- #

# Listas paralelas requeridas. Deben mantener la misma longitud y orden.
titulos = []
ejemplares = []
opcion = ""

print("--- SISTEMA DE GESTIÓN DE BIBLIOTECA ESCOLAR ---")

# Bucle while para navegar por las opciones del menú hasta que el usuario elija salir.
while opcion != "8":
    print("\n" + "=" * 40)
    print("MENÚ PRINCIPAL")
    print("=" * 40)
    print("1. Ingresar títulos iniciales")
    print("2. Ingresar ejemplares iniciales")
    print("3. Mostrar catálogo completo")
    print("4. Consultar disponibilidad de un título")
    print("5. Listar títulos agotados")
    print("6. Agregar nuevo título y ejemplares")
    print("7. Actualizar ejemplares (Préstamo/Devolución)")
    print("8. Salir")
    print("-" * 40)
    
    opcion = input("Ingrese el número de la opción deseada: ")

    # Uso de if/elif/else para la estructura del menú.
    if opcion == "1":
        # 1. Ingresar títulos iniciales
        print("\n--- 1. INGRESO DE TÍTULOS INICIALES ---")
        
        entrada_cantidad = input("¿Cuántos títulos desea ingresar inicialmente?: ")
        
        if not entrada_cantidad.isdigit():
            print("Error: La cantidad debe ser un número entero.")
        else:
            cantidad = int(entrada_cantidad)
            
            i = 0
            while i < cantidad:
                nuevo_titulo = input(f"Ingrese Título {i + 1}: ")
                
                # C3: Validar que el título no sea vacío.
                if nuevo_titulo.strip() == "":
                    print("Error: El título no puede estar vacío.")
                    continue

                # C1: Evitar duplicados.
                es_duplicado = False
                j = 0
                while j < len(titulos):
                    if titulos[j].lower() == nuevo_titulo.lower():
                        es_duplicado = True
                        break
                    j = j + 1
                    
                if es_duplicado:
                    print(f"Error: El título {nuevo_titulo} ya existe en el catálogo.")
                    continue
                
                # Agregar a las listas paralelas.
                titulos.append(nuevo_titulo)
                ejemplares.append(0) # Inicializar ejemplares en 0.
                i = i + 1
            
            print(f"Se agregaron {i} títulos. Use la opción 2 para asignar ejemplares.")

    elif opcion == "2":
        # 2. Ingresar ejemplares iniciales
        print("\n--- 2. INGRESO DE EJEMPLARES INICIALES ---")
        if len(titulos) == 0:
            print("El catálogo está vacío. Ingrese títulos primero (Opción 1).")
        else:
            i = 0
            while i < len(titulos):
                titulo_actual = titulos[i]
                
                while True:
                    entrada_ejemplares = input(f"Ingrese ejemplares para {titulo_actual}: ")
                    
                    if not entrada_ejemplares.isdigit():
                        print("Error: La cantidad debe ser un número entero positivo o cero.")
                        continue
                    
                    ejemplares_nuevos = int(entrada_ejemplares)
                    
                    if ejemplares_nuevos < 0:
                        print("Error: La cantidad no puede ser negativa.")
                        continue
                        
                    # Actualizar ejemplares en la lista paralela.
                    ejemplares[i] = ejemplares_nuevos
                    print(f"Stock de {titulo_actual} actualizado a {ejemplares_nuevos}.")
                    break
                
                i = i + 1

    elif opcion == "3":
        # 3. Mostrar catálogo
        print("\n--- 3. CATÁLOGO COMPLETO ---")
        if len(titulos) == 0:
            print("El catálogo está vacío.")
        else:
            print("TÍTULO" + " " * 30 + "STOCK")
            print("-" * 40)
            
            i = 0
            while i < len(titulos):
                print(f"{titulos[i]:<35} {ejemplares[i]}")
                i = i + 1

    elif opcion == "4":
        # 4. Consultar disponibilidad
        print("\n--- 4. CONSULTAR DISPONIBILIDAD ---")
        titulo_buscar = input("Ingrese el título a consultar: ").lower()
        
        i = 0
        indice_encontrado = -1
        while i < len(titulos):
            if titulos[i].lower() == titulo_buscar:
                indice_encontrado = i
                break
            i = i + 1
            
        if indice_encontrado != -1:
            stock = ejemplares[indice_encontrado]
            print(f"El libro {titulos[indice_encontrado]} tiene {stock} ejemplares disponibles.")
        else:
            print(f"Error: El título {titulo_buscar} no se encontró en el catálogo.")

    elif opcion == "5":
        # 5. Listar agotados (ejemplares = 0)
        print("\n--- 5. TÍTULOS AGOTADOS ---")
        hay_agotados = False
        
        i = 0
        while i < len(titulos):
            if ejemplares[i] == 0:
                print(f"- {titulos[i]}")
                hay_agotados = True
            i = i + 1
            
        if not hay_agotados:
            print("¡No hay títulos agotados!")

    elif opcion == "6":
        # 6. Agregar nuevo título y ejemplares
        print("\n--- 6. AGREGAR NUEVO TÍTULO ---")
        
        nuevo_titulo = input("Ingrese el nuevo título: ")
        
        # C3: Validar que el título no sea vacío.
        if nuevo_titulo.strip() == "":
            print("Error: El título no puede estar vacío.")
            continue
            
        # C1: Evitar duplicados.
        i = 0
        es_duplicado = False
        while i < len(titulos):
            if titulos[i].lower() == nuevo_titulo.lower():
                es_duplicado = True
                break
            i = i + 1
            
        if es_duplicado:
            print(f"Error: El título {nuevo_titulo} ya existe en el catálogo.")
            continue
            
        while True:
            entrada_ejemplares = input(f"Ingrese ejemplares iniciales para {nuevo_titulo}: ")
            
            # C3: Validar que las cantidades sean enteros y positivas o cero.
            if not entrada_ejemplares.isdigit():
                print("Error: La cantidad debe ser un número entero positivo o cero.")
                continue
                
            ejemplares_nuevos = int(entrada_ejemplares)
            
            # Agregar a las listas paralelas. C2: Mantener sincronía.
            titulos.append(nuevo_titulo)
            ejemplares.append(ejemplares_nuevos)
            print(f"Título {nuevo_titulo} agregado con {ejemplares_nuevos} ejemplares.")
            break

    elif opcion == "7":
        # 7. Actualizar ejemplares (préstamo/devolución)
        print("\n--- 7. ACTUALIZAR EJEMPLARES (P/D) ---")
        titulo_actualizar = input("Ingrese el título a modificar: ").lower()
        
        i = 0
        indice_encontrado = -1
        while i < len(titulos):
            if titulos[i].lower() == titulo_actualizar:
                indice_encontrado = i
                break
            i = i + 1
            
        if indice_encontrado != -1:
            titulo_real = titulos[indice_encontrado]
            stock_actual = ejemplares[indice_encontrado]
            
            op_pd = input("¿Es Préstamo (P) o Devolución (D)?: ").upper()
            
            if op_pd == "P":
                # Préstamo: Disminuye en 1, si hay unidades suficientes.
                if stock_actual > 0:
                    ejemplares[indice_encontrado] = stock_actual - 1
                    print(f"Préstamo registrado. Stock actual de {titulo_real}: {ejemplares[indice_encontrado]}")
                else:
                    # C3: No permitir prestar más de lo disponible.
                    print(f"Error: No hay ejemplares disponibles para {titulo_real}. Stock: {stock_actual}")
            
            elif op_pd == "D":
                # Devolución: Aumenta en 1 la cantidad de ejemplares.
                ejemplares[indice_encontrado] = stock_actual + 1
                print(f"Devolución registrada. Stock actual de {titulo_real}: {ejemplares[indice_encontrado]}")

            else:
                print("Error: Operación no válida. Ingrese 'P' para Préstamo o 'D' para Devolución.")
        else:
            # C3: Verificar la existencia del título antes de cualquier operación.
            print(f"Error: El título {titulo_actualizar} no se encontró en el catálogo.")


    elif opcion == "8":
        # 8. Salir
        print("\nGracias por usar el Sistema de Gestión de Biblioteca. ¡Hasta luego!")

    else:
        # Manejo de opciones inválidas.
        print("\nOpción no válida. Por favor, ingrese un número del 1 al 8.")
