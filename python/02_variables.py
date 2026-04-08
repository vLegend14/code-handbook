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
    titulo("VARIABLES EN PYTHON")

    print("Una variable es un nombre que apunta a un valor en memoria.")
    print("Permiten guardar datos para usarlos más adelante.\n")

    print("Se pueden guardar todos los tipos que ya conocemos:\n")
    print("• enteros")
    print("• decimales")
    print("• texto")
    print("• booleanos")

    pausa()
    limpiar()

    titulo("CREAR UNA VARIABLE")

    print("En Python una variable se crea usando '='.\n")

    codigo("""
nombre = "José"
edad = 20

print(nombre)
print(edad)
""")

    salida()

    nombre = "José"
    edad = 20

    print(nombre)
    time.sleep(0.3)
    print(edad)

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("El signo '=' no significa 'igual'.")
    print("Significa 'asigna este valor a esta variable'.")
    print("\nnombre recibe el valor 'José'")
    print("edad recibe el valor 20")

    pausa()
    limpiar()

    titulo("REGLAS PARA NOMBRAR VARIABLES")

    print("""
┌──────────────────────────────────────────────────┐
│  ✓  pueden contener letras, números y _          │
│  ✓  deben empezar con letra o _                  │
│  ✗  no pueden empezar con un número              │
│  ✗  no pueden tener espacios                     │
│  ✗  no pueden ser palabras reservadas de Python  │
└──────────────────────────────────────────────────┘
""")

    pausa()
    limpiar()

    seccion("Ejemplos válidos e inválidos")

    codigo("""
# válidos
nombre = "José"
edad_usuario = 25
_privado = True
dato1 = 10

# inválidos
# 1dato = 10
# mi variable = 5
# for = 3
""")

    print("Los nombres inválidos causan un error de sintaxis.")

    pausa()
    limpiar()

    titulo("CONVENCIÓN DE NOMBRES")

    print("En Python se usa snake_case para nombrar variables.")
    print("Las palabras se separan con guión bajo.\n")

    codigo("""
nombre_completo = "José García"
fecha_nacimiento = 2000
es_activo = True
""")

    pausa()
    limpiar()

    titulo("REASIGNAR VARIABLES")

    print("El valor de una variable puede cambiar.\n")

    codigo("""
contador = 1
print(contador)

contador = 2
print(contador)

contador = contador + 1
print(contador)
""")

    salida()

    contador = 1
    print(contador)
    time.sleep(0.4)

    contador = 2
    print(contador)
    time.sleep(0.4)

    contador = contador + 1
    print(contador)

    pausa()
    limpiar()

    titulo("OPERADORES DE ASIGNACIÓN")

    print("Hay formas cortas de modificar el valor de una variable.\n")

    print("""
┌──────────┬─────────────────────────┬─────────────────┐
│  +=      │  suma y asigna          │  x += 1         │
│  -=      │  resta y asigna         │  x -= 1         │
│  *=      │  multiplica y asigna    │  x *= 2         │
│  /=      │  divide y asigna        │  x /= 2         │
└──────────┴─────────────────────────┴─────────────────┘
""")

    pausa()
    limpiar()

    seccion("Ejemplo")

    codigo("""
puntos = 10

puntos += 5
print(puntos)

puntos *= 2
print(puntos)
""")

    salida()

    puntos = 10

    puntos += 5
    print(puntos)
    time.sleep(0.4)

    puntos *= 2
    print(puntos)

    pausa()
    limpiar()

    titulo("MÚLTIPLES VARIABLES")

    print("Se pueden asignar varias variables en una sola línea.\n")

    codigo("""
a, b, c = 1, 2, 3

print(a)
print(b)
print(c)
""")

    salida()

    a, b, c = 1, 2, 3

    print(a)
    time.sleep(0.3)
    print(b)
    time.sleep(0.3)
    print(c)

    pausa()
    limpiar()

    seccion("Mismo valor a varias variables")

    codigo("""
x = y = z = 0

print(x)
print(y)
print(z)
""")

    salida()

    x = y = z = 0

    print(x)
    time.sleep(0.3)
    print(y)
    time.sleep(0.3)
    print(z)

    pausa()
    limpiar()

    titulo("VARIABLES EN OPERACIONES")

    print("Las variables se pueden usar directamente en cálculos.\n")

    codigo("""
precio = 100
descuento = 20

total = precio - descuento

print(total)
""")

    salida()

    precio = 100
    descuento = 20

    total = precio - descuento

    print(total)

    pausa()
    limpiar()

    titulo("EJERCICIOS")

    print("""
Practica lo que aprendiste.

Ejercicio 1
Crea tres variables: nombre, edad y ciudad.
Imprime cada una en una línea distinta.

Ejercicio 2
Crea una variable llamada puntos con valor 0.
Agrégale 10, luego 5 más, luego multiplícala por 2.
Imprime el resultado en cada paso.

Ejercicio 3
Asigna los valores 5, 10 y 15
a tres variables en una sola línea.
Imprime su suma.
""")

    pausa()
    limpiar()

    titulo("FIN DE LA LECCIÓN")

    print("Ahora sabes:\n")

    print("✓ qué es una variable")
    print("✓ cómo crear variables")
    print("✓ reglas para nombrar variables")
    print("✓ snake_case")
    print("✓ reasignar valores")
    print("✓ operadores de asignación: +=, -=, *=, /=")
    print("✓ asignación múltiple")
    print("✓ usar variables en operaciones")

    print("\nExplora más modificando el código.")

except KeyboardInterrupt:
    print("\n\nLección cancelada por el usuario.")
    sys.exit(0)

