# 1) Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

# Definición de la función
def imprimir_hola_mundo():
    """
    Imprime el mensaje 'Hola Mundo!' en la consola.
    No requiere parámetros.
    """
    print("Hola Mundo!")

print("--- Ejercicio 1: Hola Mundo ---")
imprimir_hola_mundo()

# 2) Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”.
# Llamar a esta función desde el programa principal solicitando el nombre al usuario.

# Definición de la función
def saludar_usuario(nombre):
    """
    Recibe un nombre (str) y devuelve un saludo personalizado.
    
    Parámetros:
        nombre (str): El nombre de la persona a saludar.
        
    Retorno:
        str: El mensaje de saludo, por ejemplo, "Hola Marcos!".
    """
    return f"Hola {nombre}!"

print("\n--- Ejercicio 2: Saludo Personalizado ---")

# Solicitar el nombre al usuario
nombre_ingresado = input("Por favor, ingresa tu nombre: ")

# Llamar a la función con el nombre ingresado
saludo = saludar_usuario(nombre_ingresado)

# Mostrar el resultado
print(saludo)

# 3) Crear una función llamada informacion_personal(nombre, apellido, edad, residencia)
# que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# Definición de la función
def informacion_personal(nombre, apellido, edad, residencia):
    """
    Recibe un nombre (str) y devuelve un saludo personalizado.
    
    Parámetros:
        nombre (str): El nombre de la persona a saludar.
        
    Retorno:
        str: El mensaje de saludo, por ejemplo, "Hola Marcos!".
    """
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

print("\n--- Ejercicio 3: Informacion personal ---")

# Solicitar el nombre al usuario
nombre_ing = input("Ingresa tu nombre: ")
apellido_ingresado = input("Ingresa tu apellido: ")

# Validar edad
while True:
    edad_input = input("Ingresa tu edad: ")
    if edad_input.lstrip("-").isdigit() and int(edad_input) > 0:
        edad_ingresada = int(edad_input)
        break
    else:
        print("Error: Por favor, ingresa una edad válida (número entero positivo).")

residencia_ingresada = input("Ingresa tu lugar de residencia: ")

# Llamar a la función con los valores ingresados
informacion_personal(nombre_ing, apellido_ingresado, edad_ingresada, residencia_ingresada)

# 4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo.
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

import math

# Función auxiliar para validar si una cadena es un número válido
def es_numero_valido(cadena):
    """
    Valida si una cadena puede convertirse a un número (float o int).

    Parámetros:
        cadena (str): La cadena a validar.

    Retorno:
        bool: True si es un número válido, False en caso contrario.
    """
    cadena = cadena.strip()
    if not cadena:
        return False

    # Permitir números negativos
    if cadena.startswith("-"):
        cadena = cadena[1:]

    # Permitir números que comienzan con punto (como .5)
    if cadena.startswith("."):
        cadena = cadena[1:]

    # Permitir máximo un punto decimal
    if cadena.count(".") > 1:
        return False

    # Verificar que todos los caracteres sean dígitos o punto
    if all(c.isdigit() or c == "." for c in cadena) and cadena:
        return True

    return False

# Definición de la función de Área
def calcular_area_circulo(radio):
    """
    Calcula y devuelve el área de un círculo.
    Fórmula: Área = pi * radio^2
    
    Parámetros:
        radio (float): El radio del círculo.
        
    Retorno:
        float: El área calculada.
    """
    area = math.pi * (radio ** 2)
    return area

# Definición de la función de Perímetro
def calcular_perimetro_circulo(radio):
    """
    Calcula y devuelve el perímetro (circunferencia) de un círculo.
    Fórmula: Perímetro = 2 * pi * radio
    
    Parámetros:
        radio (float): El radio del círculo.
        
    Retorno:
        float: El perímetro calculado.
    """
    perimetro = 2 * math.pi * radio
    return perimetro

print("\n--- Ejercicio 4: Área y Perímetro de un Círculo ---")

# Solicitar el radio al usuario y validar que sea un número válido
while True:
    radio_input = input("Ingresa el radio del círculo (ej: 5.0): ")
    if radio_input.replace(".", "", 1).isdigit() and float(radio_input) > 0:
        radio_usuario = float(radio_input)
        break
    else:
        print("Error: Por favor, ingresa un número válido y positivo para el radio.")

# Llamar a las funciones
area_c = calcular_area_circulo(radio_usuario)
perimetro_c = calcular_perimetro_circulo(radio_usuario)

# Mostrar los resultados
print(f"El Área del círculo es: {area_c:.2f}")
print(f"El Perímetro del círculo es: {perimetro_c:.2f}")

# 5) Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro
# y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    """
    Convierte una cantidad de segundos a su equivalente en horas.
    
    Parámetros:
        segundos (float/int): Cantidad de segundos a convertir.
        
    Retorno:
        float: La cantidad equivalente de horas.
    """
    # 1 hora = 60 minutos * 60 segundos = 3600 segundos
    horas = segundos / 3600
    return horas

print("\n--- Ejercicio 5: Segundos a Horas ---")

# Solicitar los segundos al usuario y validar que sea un número válido
while True:
    segundos_input = input("Ingresa la cantidad de segundos a convertir a horas: ")
    if segundos_input.replace(".", "", 1).isdigit() and float(segundos_input) >= 0:
        segundos_usuario = float(segundos_input)
        break
    else:
        print("Error: Por favor, ingresa una cantidad de segundos válida (solo números).")

# Llamar a la función
horas_calculadas = segundos_a_horas(segundos_usuario)

# Mostrar el resultado
print(f"{segundos_usuario} segundos equivalen a {horas_calculadas:.4f} horas.")

# 6) Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro e
# imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    """
    Imprime la tabla de multiplicar del número dado (del 1 al 10).
    
    Parámetros:
        numero (int): El número del cual se quiere la tabla.
    """
    print(f"\nTabla de multiplicar del {numero}:")
    # Iteramos desde 1 hasta 10 (range(1, 11) excluye el 11)
    for i in range(1, 11):
        resultado = numero * i
        # Imprimimos la operación en un formato claro
        print(f"{numero} x {i:2} = {resultado}")

print("\n--- Ejercicio 6: Tabla de Multiplicar ---")

# Solicitar el número al usuario y validar que sea un número entero válido
while True:
    numero_input = input("Ingresa un número entero para ver su tabla de multiplicar: ")
    if numero_input.lstrip("-").isdigit():
        numero_usuario = int(numero_input)
        break
    else:
        print("Error: Por favor, ingresa un número entero válido.")

# Llamar a la función
tabla_multiplicar(numero_usuario)

# 7) Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y
# devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    """
    Realiza las cuatro operaciones básicas (+, -, *, /) con dos números.
    
    Parámetros:
        a (float): El primer número.
        b (float): El segundo número.
        
    Retorno:
        tuple: Una tupla que contiene (suma, resta, multiplicacion, division).
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    # Manejar la división por cero para evitar errores
    if b != 0:
        division = a / b
    else:
        division = "Indefinida (División por cero)"
        
    return (suma, resta, multiplicacion, division) # Devolvemos una tupla

print("\n--- Ejercicio 7: Operaciones Básicas ---")

# Solicitar el primer número y validar que sea un número válido
while True:
    num1_input = input("Ingresa el primer número: ")
    if num1_input.replace(".", "", 1).lstrip("-").isdigit():
        num1 = float(num1_input)
        break
    else:
        print("Error: Por favor, ingresa un número válido.")

# Solicitar el segundo número y validar que sea un número válido
while True:
    num2_input = input("Ingresa el segundo número: ")
    if num2_input.replace(".", "", 1).lstrip("-").isdigit():
        num2 = float(num2_input)
        break
    else:
        print("Error: Por favor, ingresa un número válido.")

# Llamar a la función y desempaquetar la tupla
resultados = operaciones_basicas(num1, num2)
# También se puede hacer así:
# suma, resta, multi, div = operaciones_basicas(num1, num2)

# Mostrar los resultados
print("\nResultados de las operaciones:")
print(f"Suma ({num1} + {num2}): {resultados[0]}")
print(f"Resta ({num1} - {num2}): {resultados[1]}")
print(f"Multiplicación ({num1} * {num2}): {resultados[2]}")
print(f"División ({num1} / {num2}): {resultados[3]}")

# 8) Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva
# el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    """
    Calcula y devuelve el Índice de Masa Corporal (IMC).
    Fórmula: IMC = peso (kg) / altura^2 (m)
    
    Parámetros:
        peso (float): Peso en kilogramos.
        altura (float): Altura en metros.
        
    Retorno:
        float: El valor del IMC calculado.
    """
    # Verificación básica para evitar división por cero o altura cero/negativa
    if altura > 0:
        imc = peso / (altura ** 2)
        return imc
    else:
        # Devolvemos None o un valor especial para indicar un error
        return None 

print("\n--- Ejercicio 8: Cálculo de IMC ---")

# Solicitar el peso y validar que sea un número válido
while True:
    peso_input = input("Ingresa tu peso en kilogramos (ej: 70.5): ")
    if peso_input.replace(".", "", 1).isdigit() and float(peso_input) > 0:
        peso_usuario = float(peso_input)
        break
    else:
        print("Error: Por favor, ingresa un valor numérico válido y positivo.")

# Bucle de validación para la altura
while True:
    altura_input = input("Ingresa tu altura en metros (ej: 1.75): ")
    if altura_input.replace(".", "", 1).isdigit() and 0.5 <= float(altura_input) <= 3.0:
        altura_usuario = float(altura_input)
        break
    else:
        # Si el valor es irracional (como 180 metros), pedimos que lo ingrese de nuevo.
        print("Error: Por favor, ingresa la altura correctamente en metros (ej: 1.75).")

# Llamar a la función
imc_resultado = calcular_imc(peso_usuario, altura_usuario)

# Mostrar el resultado
if imc_resultado is not None:
    print(f"\nTu Índice de Masa Corporal (IMC) es: {imc_resultado:.2f}")
else:
    print("Error interno: La altura debe ser un valor positivo.")

# 9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente
# en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    """
    Convierte una temperatura de Celsius a Fahrenheit.
    Fórmula: F = C * (9/5) + 32
    
    Parámetros:
        celsius (float): Temperatura en grados Celsius.
        
    Retorno:
        float: Temperatura equivalente en Fahrenheit.
    """
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit

print("\n--- Ejercicio 9: Celsius a Fahrenheit ---")

# Solicitar la temperatura al usuario y validar que sea un número válido
while True:
    temp_input = input("Ingresa la temperatura en grados Celsius: ")
    if temp_input.replace(".", "", 1).lstrip("-").isdigit():
        temp_celsius = float(temp_input)
        break
    else:
        print("Error: Por favor, ingresa un valor numérico válido para la temperatura.")

# Llamar a la función
temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)

# Mostrar el resultado
print(f"\n{temp_celsius:.2f}°C equivalen a {temp_fahrenheit:.2f}°F.")

# 10) Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    """
    Calcula y devuelve el promedio de tres números.
    Fórmula: Promedio = (a + b + c) / 3
    
    Parámetros:
        a (float): Primer número.
        b (float): Segundo número.
        c (float): Tercer número.
        
    Retorno:
        float: El promedio de los tres números.
    """
    suma = a + b + c
    promedio = suma / 3
    return promedio

print("\n--- Ejercicio 10: Cálculo de Promedio ---")

# Solicitar el primer número y validar que sea un número válido
while True:
    num_a_input = input("Ingresa el primer número: ")
    if num_a_input.replace(".", "", 1).lstrip("-").isdigit():
        num_a = float(num_a_input)
        break
    else:
        print("Error: Por favor, ingresa un valor numérico válido.")

# Solicitar el segundo número y validar que sea un número válido
while True:
    num_b_input = input("Ingresa el segundo número: ")
    if num_b_input.replace(".", "", 1).lstrip("-").isdigit():
        num_b = float(num_b_input)
        break
    else:
        print("Error: Por favor, ingresa un valor numérico válido.")

# Solicitar el tercer número y validar que sea un número válido
while True:
    num_c_input = input("Ingresa el tercer número: ")
    if num_c_input.replace(".", "", 1).lstrip("-").isdigit():
        num_c = float(num_c_input)
        break
    else:
        print("Error: Por favor, ingresa un valor numérico válido.")

# Llamar a la función
promedio_resultado = calcular_promedio(num_a, num_b, num_c)

# Mostrar el resultado
print(f"\nEl promedio de {num_a}, {num_b} y {num_c} es: {promedio_resultado:.3f}")
