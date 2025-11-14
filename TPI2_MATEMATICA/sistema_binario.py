"""
╔════════════════════════════════════════════════╗
║               SISTEMA BINARIO                  ║
║       Conversiones y operaciones básicas       ║
╚════════════════════════════════════════════════╝
"""

# ============= CONVERSIONES =============
print("\n" + "="*50)
print("CONVERSIÓN DECIMAL ↔ BINARIO")
print("="*50)

# Números a convertir
numeros = [5, 10, 25, 42]

print("\nTabla de conversión:")
print(f"\n{'Decimal':<10} {'Binario':<15} {'Verificación'}")
print("-" * 40)

for num in numeros:
    binario = bin(num)[2:]  # [2:] quita el '0b'
    verificacion = int(binario, 2)  # Convertir de vuelta
    print(f"{num:<10} {binario:<15} {verificacion}")

# ============= OPERACIONES BITWISE =============
print("\n" + "="*50)
print("OPERACIONES BITWISE")
print("="*50)

a, b = 12, 10

print(f"\nNúmero A: {a} = {bin(a)[2:]:>6}")
print(f"Número B: {b} = {bin(b)[2:]:>6}")
print("-" * 35)

print(f"AND (&):  {a & b:<2} = {bin(a & b)[2:]:>6}")
print(f"OR  (|):  {a | b:<2} = {bin(a | b)[2:]:>6}")
print(f"XOR (^):  {a ^ b:<2} = {bin(a ^ b)[2:]:>6}")

# ============= APLICACIÓN PRÁCTICA =============
print("\n" + "="*50)
print("APLICACIÓN: VERIFICAR SI ES PAR/IMPAR")
print("="*50)

for numero in [7, 8, 15, 20]:
    es_par = (numero & 1) == 0
    print(f"\n{numero} en binario: {bin(numero)[2:]:>6}")
    print(f"  Último bit: {numero & 1}")
    print(f"  Es {'PAR' if es_par else 'IMPAR'}")

# ============= TRUCO: MULTIPLICAR POR 2 =============
print("\n" + "="*50)
print("TRUCO: MULTIPLICAR/DIVIDIR POR 2")
print("="*50)

numero = 5
print(f"\nNúmero: {numero} = {bin(numero)[2:]:>6}")
print(f"  × 2:  {numero << 1:<2} = {bin(numero << 1)[2:]:>6} (desplazar izq)")
print(f"  ÷ 2:  {numero >> 1:<2} = {bin(numero >> 1)[2:]:>6} (desplazar der)")

print("\n" + "="*50)
print("Fin del ejemplo")
print("="*50 + "\n")
