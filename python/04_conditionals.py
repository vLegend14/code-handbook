#!/usr/bin/env python3

import os
import sys
import time


def limpiar():
    os.system("clear" if os.name == "posix" else "cls")


def pausa():
    try:
        input("\nPresiona ENTER para continuar...")
    except KeyboardInterrupt:
        print("\n\nInterrumpido por el usuario.")
        sys.exit(0)


def titulo(texto):
    print("\n" + "=" * 50)
    print(texto)
    print("=" * 50 + "\n")


def seccion(texto):
    print("\n" + "-" * 50)
    print(texto)
    print("-" * 50 + "\n")


def codigo(texto):
    print("Código:")
    print(texto)


def salida():
    print("Salida:")


try:

    limpiar()
    titulo("CONDICIONALES EN PYTHON")

    print("Los condicionales permiten tomar decisiones en el código.")
    print("Ejecutan distintas instrucciones según si algo es verdadero o falso.\n")

    print("Python tiene tres palabras clave para esto:\n")
    print("• if    → si se cumple la condición")
    print("• elif  → si no se cumplió la anterior y se cumple esta")
    print("• else  → si no se cumplió ninguna condición anterior")

    pausa()
    limpiar()

    titulo("IF BÁSICO")

    print("'if' ejecuta un bloque de código si la condición es True.\n")

    codigo("""
edad = 20

if edad >= 18:
    print("Eres mayor de edad")
""")

    salida()

    edad = 20

    if edad >= 18:
        print("Eres mayor de edad")

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("La condición va después de 'if' y antes de ':'")
    print("El código del bloque debe estar indentado.")
    print("Si la condición es False, el bloque no se ejecuta.")

    pausa()
    limpiar()

    titulo("IF / ELSE")

    print("'else' define qué hacer cuando la condición es False.\n")

    codigo("""
edad = 15

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
""")

    salida()

    edad = 15

    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

    pausa()
    limpiar()

    titulo("IF / ELIF / ELSE")

    print("'elif' permite evaluar más de una condición.\n")

    codigo("""
nota = 65

if nota >= 90:
    print("Sobresaliente")
elif nota >= 70:
    print("Notable")
elif nota >= 50:
    print("Aprobado")
else:
    print("Reprobado")
""")

    salida()

    nota = 65

    if nota >= 90:
        print("Sobresaliente")
    elif nota >= 70:
        print("Notable")
    elif nota >= 50:
        print("Aprobado")
    else:
        print("Reprobado")

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("Python evalúa las condiciones de arriba hacia abajo.")
    print("Ejecuta el primer bloque cuya condición sea True.")
    print("Los demás bloques se ignoran.")

    pausa()
    limpiar()

    titulo("OPERADORES DE COMPARACIÓN")

    print("""
┌──────┬───────────────────────┐
│  ==  │  igual a              │
│  !=  │  distinto de          │
│  >   │  mayor que            │
│  <   │  menor que            │
│  >=  │  mayor o igual que    │
│  <=  │  menor o igual que    │
└──────┴───────────────────────┘
""")

    pausa()
    limpiar()

    seccion("Ejemplo operadores")

    codigo("""
x = 10

print(x == 10)
print(x != 5)
print(x > 3)
print(x <= 10)
""")

    salida()

    x = 10

    print(x == 10)
    time.sleep(0.2)
    print(x != 5)
    time.sleep(0.2)
    print(x > 3)
    time.sleep(0.2)
    print(x <= 10)

    pausa()
    limpiar()

    titulo("OPERADORES LÓGICOS")

    print("""
┌─────────┬────────────────────────────────────────────┐
│  and    │  True si ambas condiciones son True        │
│  or     │  True si al menos una condición es True    │
│  not    │  invierte el valor de la condición         │
└─────────┴────────────────────────────────────────────┘
""")

    pausa()
    limpiar()

    seccion("Ejemplo and")

    codigo("""
edad = 25
tiene_entrada = True

if edad >= 18 and tiene_entrada:
    print("Puede entrar")
""")

    salida()

    edad = 25
    tiene_entrada = True

    if edad >= 18 and tiene_entrada:
        print("Puede entrar")

    pausa()
    limpiar()

    seccion("Ejemplo or")

    codigo("""
es_admin = False
es_moderador = True

if es_admin or es_moderador:
    print("Tiene permisos")
""")

    salida()

    es_admin = False
    es_moderador = True

    if es_admin or es_moderador:
        print("Tiene permisos")

    pausa()
    limpiar()

    seccion("Ejemplo not")

    codigo("""
conectado = False

if not conectado:
    print("El usuario no está conectado")
""")

    salida()

    conectado = False

    if not conectado:
        print("El usuario no está conectado")

    pausa()
    limpiar()

    titulo("CONDICIONAL EN UNA LÍNEA")

    print("Python permite escribir un if/else simple en una sola línea.")
    print("Se llama operador ternario.\n")

    codigo("""
edad = 20

estado = "mayor" if edad >= 18 else "menor"

print(estado)
""")

    salida()

    edad = 20

    estado = "mayor" if edad >= 18 else "menor"

    print(estado)

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("valor_si_true  if  condicion  else  valor_si_false")
    print("\nEs útil cuando la lógica es simple.")
    print("Para condiciones complejas es mejor usar if/else normal.")

    pausa()
    limpiar()

    titulo("VERIFICAR VALORES ESPECIALES")

    print("Algunos valores en Python son considerados False:\n")

    print("""
┌─────────────┬─────────────────────────────────────┐
│  False      │  booleano falso                     │
│  0          │  número cero                        │
│  ""         │  texto vacío                        │
│  []         │  lista vacía                        │
│  {}         │  diccionario vacío                  │
│  None       │  ausencia de valor                  │
└─────────────┴─────────────────────────────────────┘
""")

    pausa()
    limpiar()

    seccion("Ejemplo")

    codigo("""
nombre = ""

if nombre:
    print(f"Hola, {nombre}")
else:
    print("No se ingresó un nombre")
""")

    salida()

    nombre = ""

    if nombre:
        print(f"Hola, {nombre}")
    else:
        print("No se ingresó un nombre")

    pausa()
    limpiar()

    titulo("EJERCICIOS")

    print("""
Practica lo que aprendiste.

Ejercicio 1
Escribe un programa que reciba una temperatura.
Si es mayor a 30 imprime "calor".
Si es menor a 10 imprime "frío".
En otro caso imprime "templado".

Ejercicio 2
Crea una variable con tu edad.
Usa and para verificar que sea mayor a 0 y menor a 120.
Imprime si es una edad válida o no.

Ejercicio 3
Usa el operador ternario para asignar
"aprobado" o "reprobado" según una nota.
""")

    pausa()
    limpiar()

    titulo("FIN DE LA LECCIÓN")

    print("Ahora sabes:\n")

    print("✓ qué son los condicionales")
    print("✓ usar if, elif y else")
    print("✓ operadores de comparación")
    print("✓ operadores lógicos: and, or, not")
    print("✓ operador ternario")
    print("✓ valores considerados False")

    print("\nExplora más modificando el código.")

except KeyboardInterrupt:
    print("\n\nLección cancelada por el usuario.")
    sys.exit(0)

