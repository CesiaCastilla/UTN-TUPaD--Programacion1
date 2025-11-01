"""
TP 9 - Recursividad
Este programa implementa 8 ejercicios de recursividad.
"""

# EJERCICIO 1: Factorial recursivo
def factorial(n):
    """
    Calcula el factorial de un numero de forma recursiva.

    Args:
        n: Numero entero positivo

    Returns:
        El factorial de n
    """
    # Caso base
    if n == 0 or n == 1:
        return 1
    # Caso recursivo
    return n * factorial(n - 1)

def mostrar_factoriales():
    """
    Solicita un numero al usuario y muestra el factorial de todos los
    numeros enteros entre 1 y ese numero.
    """
    print("\n=== EJERCICIO 1: FACTORIAL ===")

    while True:
        numero_input = input("Ingrese un numero entero positivo: ").strip()
        # Validar que sea un número entero
        if numero_input.lstrip("-").isdigit():
            numero = int(numero_input)
            if numero >= 1:
                break
            else:
                print("Error: El numero debe ser mayor o igual a 1.")
        else:
            print("Error: Ingrese un numero entero valido.")

    print(f"\nFactoriales de 1 a {numero}:")
    for i in range(1, numero + 1):
        print(f"Factorial de {i} = {factorial(i)}")

# EJERCICIO 2: Serie de Fibonacci recursiva
def fibonacci(n):
    """
    Calcula el valor de la serie de Fibonacci en la posicion n.

    Args:
        n: Posicion en la serie (comenzando desde 0)

    Returns:
        Valor de Fibonacci en la posicion n
    """
    # Casos base
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Caso recursivo
    return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_fibonacci():
    """
    Solicita una posicion al usuario y muestra la serie de Fibonacci
    completa hasta esa posicion.
    """
    print("\n=== EJERCICIO 2: FIBONACCI ===")

    while True:
        posicion_input = input("Ingrese la posicion hasta donde mostrar la serie: ").strip()
        # Validar que sea un número entero
        if posicion_input.lstrip("-").isdigit():
            posicion = int(posicion_input)
            if posicion >= 0:
                break
            else:
                print("Error: La posicion debe ser mayor o igual a 0.")
        else:
            print("Error: Ingrese un numero entero valido.")

    print(f"\nSerie de Fibonacci hasta la posicion {posicion}:")
    for i in range(posicion + 1):
        print(f"Fibonacci({i}) = {fibonacci(i)}")

# EJERCICIO 3: Potencia recursiva
def potencia(base, exponente):
    """
    Calcula la potencia de un numero base elevado a un exponente de forma recursiva.
    Utiliza la formula: n^m = n * n^(m-1)

    Args:
        base: Numero base
        exponente: Exponente (entero no negativo)

    Returns:
        base elevado a exponente
    """
    # Caso base
    if exponente == 0:
        return 1
    # Caso recursivo
    return base * potencia(base, exponente - 1)

def probar_potencia():
    """
    Prueba la funcion de potencia recursiva con valores ingresados por el usuario.
    """
    print("\n=== EJERCICIO 3: POTENCIA ===")

    while True:
        base_input = input("Ingrese la base: ").strip()
        # Validar que sea un número (decimal o entero)
        if base_input.replace(".", "", 1).lstrip("-").isdigit() and base_input:
            base = float(base_input)
            break
        else:
            print("Error: Ingrese un valor numerico valido para la base.")

    while True:
        exponente_input = input("Ingrese el exponente (entero no negativo): ").strip()
        # Validar que sea un número entero
        if exponente_input.lstrip("-").isdigit() and exponente_input:
            exponente = int(exponente_input)
            if exponente >= 0:
                break
            else:
                print("Error: El exponente debe ser no negativo.")
        else:
            print("Error: Ingrese un numero entero valido para el exponente.")

    resultado = potencia(base, exponente)
    print(f"\n{base}^{exponente} = {resultado}")

# EJERCICIO 4: Decimal a binario recursivo
def decimal_a_binario(n):
    """
    Convierte un numero decimal a binario de forma recursiva.

    Args:
        n: Numero entero positivo en base decimal

    Returns:
        Representacion binaria como cadena de texto
    """
    # Caso base
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    # Caso recursivo
    return decimal_a_binario(n // 2) + str(n % 2)

def probar_decimal_a_binario():
    """
    Solicita un numero decimal y muestra su representacion en binario.
    """
    print("\n=== EJERCICIO 4: DECIMAL A BINARIO ===")

    while True:
        numero_input = input("Ingrese un numero entero positivo: ").strip()
        # Validar que sea un número entero
        if numero_input.lstrip("-").isdigit() and numero_input:
            numero = int(numero_input)
            if numero >= 0:
                break
            else:
                print("Error: El numero debe ser positivo.")
        else:
            print("Error: Ingrese un numero entero valido.")

    binario = decimal_a_binario(numero)
    print(f"\nEl numero {numero} en binario es: {binario}")

# EJERCICIO 5: Verificar palindromo recursivo
def es_palindromo(palabra):
    """
    Verifica si una palabra es palindromo de forma recursiva.
    No usa [::-1] ni reversed().

    Args:
        palabra: Cadena de texto sin espacios ni tildes

    Returns:
        True si es palindromo, False en caso contrario
    """
    # Caso base: palabra vacia o de un caracter
    if len(palabra) <= 1:
        return True

    # Caso recursivo: comparar primer y ultimo caracter
    if palabra[0].lower() != palabra[-1].lower():
        return False

    # Llamada recursiva con la palabra sin el primer y ultimo caracter
    return es_palindromo(palabra[1:-1])

def probar_palindromo():
    """
    Solicita una palabra y verifica si es palindromo.
    """
    print("\n=== EJERCICIO 5: PALINDROMO ===")

    palabra = input("Ingrese una palabra (sin espacios ni tildes): ").strip()

    if es_palindromo(palabra):
        print(f"\n'{palabra}' ES un palindromo.")
    else:
        print(f"\n'{palabra}' NO es un palindromo.")

# EJERCICIO 6: Suma de digitos recursiva
def suma_digitos(n):
    """
    Calcula la suma de todos los digitos de un numero de forma recursiva.
    No convierte el numero a string, usa operaciones matematicas (%, //).

    Args:
        n: Numero entero positivo

    Returns:
        Suma de todos los digitos
    """
    # Caso base
    if n < 10:
        return n
    # Caso recursivo
    return (n % 10) + suma_digitos(n // 10)

def probar_suma_digitos():
    """
    Solicita un numero y muestra la suma de sus digitos.
    """
    print("\n=== EJERCICIO 6: SUMA DE DIGITOS ===")

    while True:
        numero_input = input("Ingrese un numero entero positivo: ").strip()
        # Validar que sea un número entero
        if numero_input.lstrip("-").isdigit() and numero_input:
            numero = int(numero_input)
            if numero >= 0:
                break
            else:
                print("Error: El numero debe ser positivo.")
        else:
            print("Error: Ingrese un numero entero valido.")

    suma = suma_digitos(numero)
    print(f"\nLa suma de los digitos de {numero} es: {suma}")

# EJERCICIO 7: Contar bloques de piramide recursivo
def contar_bloques(n):
    """
    Calcula el total de bloques necesarios para construir una piramide.
    En el nivel mas bajo hay n bloques, en el siguiente n-1, y asi sucesivamente.

    Args:
        n: Numero de bloques en el nivel mas bajo

    Returns:
        Total de bloques necesarios
    """
    # Caso base
    if n == 1:
        return 1
    # Caso recursivo
    return n + contar_bloques(n - 1)

def probar_contar_bloques():
    """
    Solicita el numero de bloques del nivel mas bajo y calcula el total.
    """
    print("\n=== EJERCICIO 7: CONTAR BLOQUES DE PIRAMIDE ===")

    while True:
        n_input = input("Ingrese el numero de bloques en el nivel mas bajo: ").strip()
        # Validar que sea un número entero
        if n_input.lstrip("-").isdigit() and n_input:
            n = int(n_input)
            if n >= 1:
                break
            else:
                print("Error: El numero debe ser mayor o igual a 1.")
        else:
            print("Error: Ingrese un numero entero valido.")

    total = contar_bloques(n)
    print(f"\nTotal de bloques necesarios: {total}")

# EJERCICIO 8: Contar apariciones de un digito recursivo
def contar_digito(numero, digito):
    """
    Cuenta cuantas veces aparece un digito dentro de un numero de forma recursiva.

    Args:
        numero: Numero entero positivo
        digito: Digito a buscar (entre 0 y 9)

    Returns:
        Cantidad de veces que aparece el digito
    """
    # Caso base
    if numero == 0:
        return 1 if digito == 0 else 0

    # Obtener el ultimo digito
    ultimo_digito = numero % 10

    # Contar si coincide
    cuenta = 1 if ultimo_digito == digito else 0

    # Caso recursivo: sumar con el resto del numero
    return cuenta + contar_digito(numero // 10, digito)

def probar_contar_digito():
    """
    Solicita un numero y un digito, y cuenta cuantas veces aparece.
    """
    print("\n=== EJERCICIO 8: CONTAR DIGITO ===")

    while True:
        numero_input = input("Ingrese un numero entero positivo: ").strip()
        # Validar que sea un número entero
        if numero_input.lstrip("-").isdigit() and numero_input:
            numero = int(numero_input)
            if numero >= 0:
                break
            else:
                print("Error: El numero debe ser positivo.")
        else:
            print("Error: Ingrese un numero entero valido.")

    while True:
        digito_input = input("Ingrese un digito a buscar (0-9): ").strip()
        # Validar que sea un número entero
        if digito_input.lstrip("-").isdigit() and digito_input:
            digito = int(digito_input)
            if 0 <= digito <= 9:
                break
            else:
                print("Error: El digito debe estar entre 0 y 9.")
        else:
            print("Error: Ingrese un numero entero valido.")

    cantidad = contar_digito(numero, digito)
    print(f"\nEl digito {digito} aparece {cantidad} veces en {numero}")

def menu_principal():
    """
    Muestra el menu principal y permite ejecutar cada ejercicio.
    """
    while True:
        print("\n" + "=" * 60)
        print("TP 9 - RECURSIVIDAD")
        print("=" * 60)
        print("1. Factorial recursivo")
        print("2. Serie de Fibonacci")
        print("3. Potencia recursiva")
        print("4. Decimal a binario")
        print("5. Verificar palindromo")
        print("6. Suma de digitos")
        print("7. Contar bloques de piramide")
        print("8. Contar apariciones de digito")
        print("9. Salir")
        print("=" * 60)

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == '1':
            mostrar_factoriales()
        elif opcion == '2':
            mostrar_fibonacci()
        elif opcion == '3':
            probar_potencia()
        elif opcion == '4':
            probar_decimal_a_binario()
        elif opcion == '5':
            probar_palindromo()
        elif opcion == '6':
            probar_suma_digitos()
        elif opcion == '7':
            probar_contar_bloques()
        elif opcion == '8':
            probar_contar_digito()
        elif opcion == '9':
            print("\nGracias por usar el programa de recursividad!")
            break
        else:
            print("\nOpcion invalida. Por favor, seleccione una opcion del 1 al 9.")

def main():
    """
    Funcion principal del programa.
    """
    menu_principal()

if __name__ == "__main__":
    main()
