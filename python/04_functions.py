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
    titulo("FUNCIONES EN PYTHON")

    print("Las funciones permiten agrupar código que se repite.")
    print("Se definen una vez y se pueden usar muchas veces.\n")

    print("Ventajas de usar funciones:\n")
    print("• evitan repetir código")
    print("• hacen el programa más ordenado")
    print("• facilitan encontrar errores")
    print("• permiten reutilizar lógica")

    pausa()
    limpiar()

    titulo("DEFINIR UNA FUNCIÓN")

    print("Las funciones se crean con la palabra clave 'def'.\n")

    codigo("""
def saludar():
    print("Hola mundo")

saludar()
""")

    salida()

    def saludar():
        print("Hola mundo")

    saludar()

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("def indica que estamos definiendo una función.")
    print("saludar es el nombre de la función.")
    print("Los paréntesis () son obligatorios.")
    print("El código dentro está indentado.")

    pausa()
    limpiar()

    titulo("FUNCIONES CON PARÁMETROS")

    print("Los parámetros permiten enviar información a la función.\n")

    codigo("""
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("José")
saludar("Gonzalo")
""")

    salida()

    def saludar(nombre):
        print(f"Hola, {nombre}")

    saludar("José")
    time.sleep(0.3)
    saludar("Gonzalo")

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("nombre es el parámetro de la función.")
    print("Al llamar la función se pasa el valor entre paréntesis.")
    print("Ese valor se llama argumento.")

    pausa()
    limpiar()

    titulo("FUNCIONES CON VARIOS PARÁMETROS")

    print("Una función puede recibir más de un parámetro.\n")

    codigo("""
def presentar(nombre, edad):
    print(f"{nombre} tiene {edad} años")

presentar("José", 20)
presentar("Gonzalo", 25)
""")

    salida()

    def presentar(nombre, edad):
        print(f"{nombre} tiene {edad} años")

    presentar("José", 20)
    time.sleep(0.3)
    presentar("Gonzalo", 25)

    pausa()
    limpiar()

    titulo("FUNCIONES CON RETURN")

    print("Las funciones pueden devolver un resultado con 'return'.\n")

    codigo("""
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(resultado)
""")

    salida()

    def sumar(a, b):
        return a + b

    resultado = sumar(3, 5)
    print(resultado)

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("return envía el resultado hacia donde se llamó la función.")
    print("La función termina en cuanto encuentra return.")
    print("El resultado se puede guardar en una variable.")

    pausa()
    limpiar()

    titulo("PARÁMETROS CON VALOR POR DEFECTO")

    print("Se puede asignar un valor por defecto a un parámetro.")
    print("Si no se pasa ese argumento, se usa el valor por defecto.\n")

    codigo("""
def saludar(nombre, mensaje="Hola"):
    print(f"{mensaje}, {nombre}")

saludar("José")
saludar("Gonzalo", "Buenos días")
""")

    salida()

    def saludar(nombre, mensaje="Hola"):
        print(f"{mensaje}, {nombre}")

    saludar("José")
    time.sleep(0.3)
    saludar("Gonzalo", "Buenos días")

    pausa()
    limpiar()

    titulo("ALCANCE DE VARIABLES")

    print("Las variables creadas dentro de una función")
    print("solo existen dentro de ella.\n")

    codigo("""
def calcular():
    resultado = 10 * 2
    print(resultado)

calcular()
""")

    salida()

    def calcular():
        resultado = 10 * 2
        print(resultado)

    calcular()

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("resultado es una variable local.")
    print("No se puede acceder a ella fuera de la función.")
    print("\nA esto se le llama 'alcance' o 'scope'.")

    pausa()
    limpiar()

    titulo("EJERCICIOS")

    print("""
Practica lo que aprendiste.

Ejercicio 1
Crea una función llamada cuadrado()
que reciba un número y devuelva su cuadrado.

Ejercicio 2
Crea una función que reciba nombre y apellido
e imprima el nombre completo.

Ejercicio 3
Crea una función con un parámetro por defecto
que salude en distintos idiomas.
""")

    pausa()
    limpiar()

    titulo("FIN DE LA LECCIÓN")

    print("Ahora sabes:\n")

    print("✓ qué es una función")
    print("✓ cómo definir funciones")
    print("✓ parámetros y argumentos")
    print("✓ devolver valores con return")
    print("✓ parámetros con valor por defecto")
    print("✓ alcance de variables")

    print("\nExplora más modificando el código.")

except KeyboardInterrupt:
    print("\n\nLección cancelada por el usuario.")
    sys.exit(0)