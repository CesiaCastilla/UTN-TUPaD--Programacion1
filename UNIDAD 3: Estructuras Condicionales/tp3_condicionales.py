# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla
# un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir en pantalla
# el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".

numero = int(input("Ingrese un número par: "))

# El operador de módulo (%) verifica si el número es par, numero % 2 calcula el residuo de la división del número por 2.
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#   ● Niño/a: menor de 12 años.
#   ● Adolescente: mayor o igual que 12 años y menor que 18 años.
#   ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#   ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))

if edad >= 0 and edad < 12:
    print(f"Tienes {edad} años, sos un niño/a.")
elif edad >= 12 and edad < 18:
    print(f"Tienes {edad} años, sos un adolescente.")
elif edad >= 18 and edad < 30:
    print(f"Tienes {edad} años, sos un adulto/a joven.")
else:
    print(f"Tienes {edad} años, sos un adulto/a.")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por pantalla el mensaje "Ha ingresado una contraseña correcta";
# en caso contrario, imprimir "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".

password = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")

# Obtiene la longitud de la contraseña usando la función len().
longitud = len(password)

# Verifica si la longitud está en el rango permitido (de 8 a 14).
if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

import random
from statistics import mode, median, mean

# Lista con 50 números aleatorios entre 1 y 100.
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Imprime los valores calculados para referencia
print(f"Lista de números aleatorios: {numeros_aleatorios}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# Compara los valores para determinar el sesgo
if media > mediana and mediana > moda:
    print("La distribución tiene un sesgo positivo o a la derecha.")
elif media < mediana and mediana < moda:
    print("La distribución tiene un sesgo negativo o a la izquierda.")
elif media == mediana and mediana == moda:
    print("La distribución no tiene sesgo.")
else:
    print("La relación entre media, mediana y moda no se ajusta a un sesgo simple.")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal,
# añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar
# el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

vocales = ['a', 'e', 'i', 'o', 'u']

string_ingresado = input("Ingresa una palabra o frase: ")

# Obtener el último carácter del string y convertirlo a minúscula para la comparación
ultimo_caracter = string_ingresado[-1].lower()

# Verificar si el último carácter es una vocal
if ultimo_caracter in vocales:
    # Si termina en vocal, añadir un signo de exclamación
    string_resultante = string_ingresado + "!"
    print(string_resultante)
else:
    # Si no, imprimir el string original
    print(string_ingresado)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.

nombre = input("Por favor, ingresa tu nombre: ")

opcion = int(input("Elige una opción:\n1. Nombre en mayúsculas\n2. Nombre en minúsculas\n3. Nombre con la primera letra mayúscula\n\nOpción: "))

if opcion == 1:
    nombre_transformado = nombre.upper()
    print(f"\nNombre transformado: {nombre_transformado}")
elif opcion == 2:
    nombre_transformado = nombre.lower()
    print(f"\nNombre transformado: {nombre_transformado}")
elif opcion == 3:
    nombre_transformado = nombre.title()
    print(f"\nNombre transformado: {nombre_transformado}")
else:
    print("Opción no válida. Por favor, elige 1, 2 o 3.")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías
# según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Por favor, introduce la magnitud del terremoto: "))

# Clasificar la magnitud.
if magnitud < 3:
    categoria = "Muy leve"
elif magnitud >= 3 and magnitud < 4:
    categoria = "Leve"
elif magnitud >= 4 and magnitud < 5:
    categoria = "Moderado"
elif magnitud >= 5 and magnitud < 6:
    categoria = "Fuerte"
elif magnitud >= 6 and magnitud < 7:
    categoria = "Muy Fuerte"
elif magnitud >= 7:
    categoria = "Extremo"
else:
    categoria = "Magnitud no válida" # En caso de que el número sea negativo.
        
# Imprimir el resultado.
print(f"La categoría del terremoto con magnitud {magnitud} es: {categoria}.")

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es.
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("¿En qué hemisferio te encuentras (N/S)? ").upper()
mes = int(input("Introduce el número del mes (1-12): "))
dia = int(input("Introduce el día: "))

# Validar que los datos de la fecha sean correctos
if mes < 1 or mes > 12 or dia < 1 or dia > 31:
    print("Error: La fecha ingresada no es válida.")
elif hemisferio != 'N' and hemisferio != 'S':
    print("Error: El hemisferio debe ser 'N' o 'S'.")
else:
    # Lógica para el hemisferio norte
    if hemisferio == 'N':
        if (mes == 12 and dia >= 21) or (mes >= 1 and mes <= 2 and dia <= 31) or (mes == 3 and dia <= 20):
            estacion = "Invierno"
        elif (mes == 3 and dia >= 21) or (mes >= 4 and mes <= 5 and dia <= 31) or (mes == 6 and dia <= 20):
            estacion = "Primavera"
        elif (mes == 6 and dia >= 21) or (mes >= 7 and mes <= 8 and dia <= 31) or (mes == 9 and dia <= 20):
            estacion = "Verano"
        elif (mes == 9 and dia >= 21) or (mes >= 10 and mes <= 11 and dia <= 31) or (mes == 12 and dia <= 20):
            estacion = "Otoño"
    
    # Lógica para el hemisferio sur
    elif hemisferio == 'S':
        if (mes == 12 and dia >= 21) or (mes >= 1 and mes <= 2 and dia <= 31) or (mes == 3 and dia <= 20):
            estacion = "Verano"
        elif (mes == 3 and dia >= 21) or (mes >= 4 and mes <= 5 and dia <= 31) or (mes == 6 and dia <= 20):
            estacion = "Otoño"
        elif (mes == 6 and dia >= 21) or (mes >= 7 and mes <= 8 and dia <= 31) or (mes == 9 and dia <= 20):
            estacion = "Invierno"
        elif (mes == 9 and dia >= 21) or (mes >= 10 and mes <= 11 and dia <= 31) or (mes == 12 and dia <= 20):
            estacion = "Primavera"
    print(f"Te encuentras en: {estacion}.")
