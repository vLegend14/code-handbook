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

    print("Las variables permiten guardar información en memoria.")
    print("Son la base de casi todos los programas.\n")

    print("Una variable puede guardar:\n")
    print("• números")
    print("• texto")
    print("• listas")
    print("• resultados de cálculos")

    pausa()
    limpiar()

    titulo("CREAR UNA VARIABLE")

    print("En Python una variable se crea usando '='\n")

    codigo("""
nombre = "Ana"
edad = 20

print(nombre)
print(edad)
""")

    salida()

    nombre = "Ana"
    edad = 20

    print(nombre)
    print(edad)

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("nombre y edad son variables.")
    print("El signo '=' asigna un valor a la variable.")

    pausa()
    limpiar()

    titulo("TIPOS DE DATOS BÁSICOS")

    print("""
Los tipos más comunes en Python son:

int     → números enteros
float   → números con decimales
str     → texto
bool    → verdadero o falso
""")

    pausa()
    limpiar()

    seccion("Ejemplo de tipos")

    codigo("""
numero = 10
precio = 9.99
texto = "Hola"
activo = True

print(numero)
print(precio)
print(texto)
print(activo)
""")

    salida()

    numero = 10
    precio = 9.99
    texto = "Hola"
    activo = True

    print(numero)
    print(precio)
    print(texto)
    print(activo)

    pausa()
    limpiar()

    titulo("OPERACIONES CON VARIABLES")

    print("Las variables pueden usarse en cálculos.\n")

    codigo("""
a = 5
b = 3

resultado = a + b

print(resultado)
""")

    salida()

    a = 5
    b = 3
    resultado = a + b

    print(resultado)

    pausa()
    limpiar()

    titulo("REASIGNAR VARIABLES")

    print("El valor de una variable puede cambiar.\n")

    codigo("""
contador = 1
print(contador)

contador = 2
print(contador)
""")

    salida()

    contador = 1
    print(contador)
    time.sleep(0.5)

    contador = 2
    print(contador)

    pausa()
    limpiar()

    titulo("USAR VARIABLES EN TEXTO")

    print("Podemos insertar variables dentro de texto usando f-strings.\n")

    codigo("""
nombre = "Luis"
edad = 25

print(f"{nombre} tiene {edad} años")
""")

    salida()

    nombre = "Luis"
    edad = 25

    print(f"{nombre} tiene {edad} años")

    pausa()
    limpiar()

    titulo("EJERCICIOS")

    print("""
Practica lo que aprendiste.

Ejercicio 1
Crea una variable llamada nombre
y guarda tu nombre.

Ejercicio 2
Crea una variable edad
y guarda tu edad.

Ejercicio 3
Imprime una frase usando ambas variables.
""")

    pausa()
    limpiar()

    titulo("FIN DE LA LECCIÓN")

    print("Ahora sabes:\n")

    print("✓ qué es una variable")
    print("✓ cómo crear variables")
    print("✓ tipos de datos básicos")
    print("✓ usar variables en cálculos")
    print("✓ usar variables en texto")

    print("\nExplora más modificando el código.")

except KeyboardInterrupt:
    print("\n\nLección cancelada por el usuario.")
    sys.exit(0)