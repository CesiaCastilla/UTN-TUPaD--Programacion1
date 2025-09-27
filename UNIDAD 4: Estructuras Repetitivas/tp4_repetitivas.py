# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for numero in range(0, 101):
    print(numero)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad
# de dígitos que contiene. 

num = int(input("Ingrese un número entero: "))

# Se convierte el número a una cadena de texto, para poder usar la función len()
cadena_numero = str(abs(num))

# Se usa len() para obtener la cantidad de caracteres de la cadena
# abs() se usa para manejar números negativos y contar sus dígitos
cantidad_digitos = len(cadena_numero)

# Se imprime el resultado por consola
print(f"El número {num} tiene {cantidad_digitos} dígito(s).")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

numero1 = int(input("Ingresa el primer número entero: "))
numero2 = int(input("Ingresa el segundo número entero: "))

# Identificar el número menor y el mayor.
inicio_rango = min(numero1, numero2)
fin_rango = max(numero1, numero2)

# Inicializar la variable que guardará la suma.
suma_total = 0

# Si los números son consecutivos (ej: 5 y 6), el bucle no se ejecutará, y la suma será 0, lo cual es correcto.
for numero in range(inicio_rango + 1, fin_rango):
    suma_total = suma_total + numero

# Mostrar el resultado al usuario.
print(f"\nLos números que sumamos son los que están entre {inicio_rango} y {fin_rango}.")
print(f"La suma de los enteros comprendidos entre {numero1} y {numero2} (excluidos) es: {suma_total}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia.
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

# Inicializar la variable que almacenará la suma total (el acumulador).
suma_total = 0

# Inicializar la variable para la entrada, con un valor que no sea 0 para asegurar que el bucle comience.
numero_ingresado = -1 

print("Ingresa números enteros para sumarlos.")
print("Cuando quieras ver el resultado, simplemente ingresa el número 0.")
print("-" * 40)

# Iniciar el bucle 'while'. Se ejecutará mientras el número_ingresado no sea 0.
while numero_ingresado != 0:
    entrada = input("Ingresa un número (o 0 para detener y ver el total): ")
    
    # Convertir la entrada a un número entero.
    numero_ingresado = int(entrada)
    
    # Sumar el número al total acumulado, pero solo si NO es 0.
    if numero_ingresado != 0:
        suma_total += numero_ingresado
        print(f"Número {numero_ingresado} agregado. Suma actual: {suma_total}")

# El bucle ha terminado (porque numero_ingresado es 0). Mostrar el resultado final.
print("-" * 40)
print(f"¡Proceso finalizado por ingresar 0!")
print(f"La suma total de todos los números ingresados es: {suma_total}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final,
# el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# Definir el número secreto que el usuario debe adivinar.
numero_secreto = 7
# Inicializar el contador de intentos.
intentos = 0

# Inicializar la variable de la adivinanza con un valor diferente al secreto
adivinanza = -1 

print("Adivina el número entero entre 0 y 9. ¿Cuál es?")

# Iniciar el bucle 'while'. Se ejecutará mientras la adivinanza no coincida con el secreto.
while adivinanza != numero_secreto:
    entrada = input("Tu intento: ")
    
    # Convertir la entrada a un número entero.
    adivinanza = int(entrada)
    
    # Aumentar el contador de intentos.
    intentos = intentos + 1
    
    # Dar pistas y verificar si es correcto.
    if adivinanza < numero_secreto:
        print("Demasiado bajo. ¡Intenta con un número mayor!")
    elif adivinanza > numero_secreto:
        print("Demasiado alto. ¡Intenta con un número menor!")
    else:
        print("Eso no es un número válido. Por favor, ingresa un número entero.")

# Muestra el resultado final.
print("-" * 40)
print(f"¡Felicidades! ¡Adivinaste el número {numero_secreto}!")
print(f"Te tomó un total de {intentos} intentos para acertar.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

print("Iniciando la impresión de números pares de 100 a 0:")
print("-" * 40)

# Inicio: 100 (El primer par, en orden decreciente).
# Fin: -1 (El bucle se detiene antes de -1, asegurando que 0 sea incluido).
# Paso: -2 (Garantiza que solo se generen números pares, saltando de dos en dos hacia atrás).
for numero in range(100, -1, -2):
    print(numero)

print("-" * 40)
print("¡Fin de la lista!")

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# Inicializar la variable que almacenará la suma total.
suma_total = 0
limite = -1

# Bucle para asegurar que el usuario ingrese un número entero y positivo.
while limite < 0:
    # Pedir el número límite al usuario.
    entrada = input("Ingresa un número entero positivo (incluyendo el 0): ")
    limite = int(entrada)
    
    # Validar que el número sea positivo.
    if limite < 0:
        print("El número debe ser positivo o cero. Inténtalo de nuevo.")
    else:
        print("Ingresaste un número entero positivo correcto.")

# Comienza en 0.
# El '+ 1' es crucial, ya que range() se detiene ANTES del segundo valor, 
# y necesitamos INCLUIR el número que el usuario proporcionó en la suma.
print(f"\nSumando todos los números desde 0 hasta {limite}...")

for numero in range(0, limite):
    suma_total += numero

# Mostrar el resultado final.
print("-" * 40)
print(f"La suma total de los números entre 0 y {limite} es: {suma_total}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# Definir la cantidad total de números a ingresar.
cantidad_ingresar = 100

# Inicializar las variables de contador en cero.
conteo_pares = 0
conteo_impares = 0
conteo_positivos = 0
conteo_negativos = 0
conteo_ceros = 0

print(f"Deberás ingresar {cantidad_ingresar} números enteros.")
print("-" * 50)

# Iniciar el bucle 'for' para iterar la cantidad de veces definida.
# range(cantidad_ingresar) generará números de 0 hasta 99 (100 veces).
for i in range(cantidad_ingresar):
    while True:
        # Pedir la entrada. Usamos i + 1 para que el mensaje sea 1 de 100, 2 de 100, etc.
        entrada = input(f"Ingresa el número {i + 1} de {cantidad_ingresar}: ")
        numero = int(entrada)
        break # Si la conversión a int es exitosa, salimos del bucle while interno.

    # Lógica de Par/Impar (Módulo o Residuo: %)
    # Un número es par si su residuo al dividir entre 2 es 0.
    if numero % 2 == 0:
        conteo_pares += 1
    else:
        conteo_impares += 1

    # Lógica de Positivo/Negativo/Cero
    if numero > 0:
        conteo_positivos += 1
    elif numero < 0:
        conteo_negativos += 1
    else:
        # El cero (0) es el caso que queda: no es positivo ni negativo.
        conteo_ceros += 1
        
# Mostrar los resultados finales.
print("-" * 50)
print("\n--- ¡Análisis Completo de los Números Ingresados! ---")
print(f"Total de números ingresados: {cantidad_ingresar}")
print(f"Pares: {conteo_pares}")
print(f"Impares: {conteo_impares}")
print(f"Positivos: {conteo_positivos}")
print(f"Negativos: {conteo_negativos}")
print(f"Ceros: {conteo_ceros}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# Definir la cantidad total de números a ingresar.
# Cambia este valor a un número más pequeño (ej. 10) para una prueba rápida.
cantidad_ingresar = 10

# Inicializar la variable que almacenará la suma total (el acumulador).
suma_total = 0

# Iniciar el bucle 'for' para pedir los números y sumarlos.
for i in range(cantidad_ingresar):
    while True:
        # Pedir la entrada. Usamos i + 1 para que el mensaje sea 1 de 100, 2 de 100, etc.
        entrada = input(f"Ingresa el número {i + 1} de {cantidad_ingresar}: ")
        numero = int(entrada)
        
        # Si la conversión a int es exitosa:
        suma_total += numero # 4. Acumular el valor al total.
        break # Salir del bucle while interno y pasar al siguiente número.

# Cálculo de la Media.
media = suma_total / cantidad_ingresar

# Mostrar los resultados finales.
print("-" * 55)
print("--- Cálculo Finalizado ---")
print(f"La suma total de los {cantidad_ingresar} números ingresados es: {suma_total}")
print(f"La media (promedio) de los valores es: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

print("--- Inversor de Dígitos ---")

# Pedir el número al usuario como entrada de texto.
while True:
    numero_str = input("Ingresa un número entero (ej. 547): ")
    
    # Simple validación para asegurarse de que la entrada sea solo dígitos.
    if numero_str.isdigit() or (numero_str.startswith('-') and numero_str[1:].isdigit()):
        break
    else:
        print("Por favor, ingresa un número entero válido.")

# Invertir la cadena de texto usando slicing [::-1].
# [::-1] significa: empezar al inicio, terminar al final, con un paso de -1 (hacia atrás).
numero_invertido_str = numero_str[::-1]

# Manejar el signo negativo (si existe).
if numero_invertido_str.endswith('-'):
    # Si la cadena invertida termina en '-', significa que el original era negativo.
    # Movemos el signo al inicio y eliminamos el guion del final.
    numero_invertido_str = "-" + numero_invertido_str.rstrip('-')
    
# Mostrar el resultado.
print(f"El número ingresado fue: {numero_str}")
print(f"El número con los dígitos invertidos es: {numero_invertido_str}")
