"""
╔═════════════════════════════════════════════════════╗
║       CONJUNTOS - ANÁLISIS DE REDES SOCIALES        ║  
╚═════════════════════════════════════════════════════╝
"""

# Amigos de cada persona
amigos_juan = {'Ana', 'Carlos', 'Diana', 'Luis'}
amigos_maria = {'Carlos', 'Diana', 'Pedro', 'Sofia'}
amigos_pedro = {'Diana', 'Luis', 'Sofia', 'Juan'}

print("\n" + "="*50)
print("AMIGOS EN REDES SOCIALES")
print("="*50)

print(f"\nJuan:  {amigos_juan}")
print(f"María: {amigos_maria}")
print(f"Pedro: {amigos_pedro}")

# ===== OPERACIONES =====

print("\n" + "="*50)
print("ANÁLISIS")
print("="*50)

# 1. Amigos en común de Juan y María
comunes_juan_maria = amigos_juan & amigos_maria
print(f"\n1. Amigos en común de Juan y María:")
print(f"   {comunes_juan_maria}")
print(f"Pueden presentarles nuevas personas")

# 2. Todos los amigos (red completa)
red_completa = amigos_juan | amigos_maria | amigos_pedro
print(f"\n2. Red completa de amigos:")
print(f"{red_completa}")
print(f"Total: {len(red_completa)} personas")

# 3. Amigos solo de Juan (no de María)
solo_juan = amigos_juan - amigos_maria
print(f"\n3. Amigos exclusivos de Juan:")
print(f"{solo_juan}")
print(f"María podría conocer a: {solo_juan}")

# 4. Amigos de Juan O María, pero NO de ambos
diferentes = amigos_juan ^ amigos_maria
print(f"\n4. Amigos que no comparten:")
print(f"{diferentes}")

# 5. Verificar si alguien es amigo
print(f"\n5. Consultas:")
print(f"¿Ana es amiga de Juan? {'Ana' in amigos_juan}")
print(f"¿Ana es amiga de María? {'Ana' in amigos_maria}")

# 6. Sugerencias de amistad
print(f"\n6. Sugerencias de amistad para Juan:")
sugerencias = (amigos_maria | amigos_pedro) - amigos_juan
print(f"Podrías conocer a: {sugerencias}")

print("\n" + "="*50)
print("Fin del análisis")
print("="*50 + "\n")
