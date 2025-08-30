# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.

nombre = input("Ingrese su nombre: ")

print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = float(input("Ingrese el radio del círculo: "))
pi = 3.14159
area = pi * radio * radio
perimetro = 2 * pi * radio

# Imprimir los resultados
print(f"El área del círculo con radio {radio} es: {area}")
print(f"El perímetro del círculo con radio {radio} es: {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos = int(input("Por favor, ingrese una cantidad de segundos: "))
horas = segundos / 3600

# Imprimir el resultado
print(f"{segundos} segundos equivalen a {horas} horas.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Ingrese un número entero: "))

# Imprimir el encabezado de la tabla
print(f"Tabla de multiplicar del {numero}:")

# Usar un bucle for para iterar del 1 al 10
for i in range(1, 11):
    # Calcular el resultado de la multiplicación
    resultado = numero * i
    # Imprimir cada línea de la tabla
    print(f"{numero} x {i} = {resultado}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Por favor, introduce el primer número entero (distinto de 0): "))
num2 = int(input("Por favor, introduce el segundo número entero (distinto de 0): "))

# Verificar que los números no sean 0 para evitar errores en la división
if num1 == 0 or num2 == 0:
    print("Error: Los números no pueden ser 0.")
else:
    # Realizar las operaciones
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    
# Imprimir los resultados
print("Resultados de las operaciones:")
print(f"Suma: {num1} + {num2} = {suma}")
print(f"Resta: {num1} - {num2} = {resta}")
print(f"Multiplicación: {num1} * {num2} = {multiplicacion}")
print(f"División: {num1} / {num2} = {division:.2f}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

altura = float(input("Ingrese su altura en metros (ej. 1.75): "))
peso = float(input("Ingrese su peso en kilogramos (ej. 70.5): "))

# IMC = peso / altura al cuadrado
imc = peso / (altura ** 2)

# Imprimir el resultado
print(f"Su índice de masa corporal (IMC) es: {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.

celsius = float(input("Ingrese una temperatura en grados Celsius: "))
    
# Calcular la temperatura en grados Fahrenheit usando la fórmula
fahrenheit = (celsius * 9/5) + 32

# Imprimir el resultado
print(f"La temperatura de {celsius}°C equivale a {fahrenheit}°F.")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Calcular el promedio
promedio = (num1 + num2 + num3) / 3

# Imprimir el resultado
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio}")
