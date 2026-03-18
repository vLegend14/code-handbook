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
    titulo("STRINGS EN PYTHON")

    print("Un string es una cadena de texto.")
    print("Es uno de los tipos de datos más usados en Python.\n")

    print("Se puede crear con comillas simples o dobles:\n")
    print("• 'hola'")
    print('• "hola"')

    pausa()
    limpiar()

    titulo("CREAR STRINGS")

    codigo("""
nombre = "José"
saludo = 'Hola mundo'
vacio = ""

print(nombre)
print(saludo)
print(vacio)
""")

    salida()

    nombre = "José"
    saludo = 'Hola mundo'
    vacio = ""

    print(nombre)
    time.sleep(0.3)
    print(saludo)
    time.sleep(0.3)
    print(vacio)

    pausa()
    limpiar()

    titulo("STRINGS MULTILÍNEA")

    print("Para texto que ocupa varias líneas se usan triple comillas.\n")

    codigo("""
texto = \"\"\"
Esta es una línea.
Esta es otra línea.
Y una más.
\"\"\"

print(texto)
""")

    salida()

    texto = """
Esta es una línea.
Esta es otra línea.
Y una más.
"""

    print(texto)

    pausa()
    limpiar()

    titulo("LONGITUD DE UN STRING")

    print("len() devuelve la cantidad de caracteres.\n")

    codigo("""
nombre = "Python"

print(len(nombre))
""")

    salida()

    nombre = "Python"

    print(len(nombre))

    pausa()
    limpiar()

    titulo("ACCEDER A CARACTERES")

    print("Cada carácter tiene un índice, comenzando en 0.")
    print("Los índices negativos cuentan desde el final.\n")

    codigo("""
texto = "Python"

print(texto[0])
print(texto[1])
print(texto[-1])
""")

    salida()

    texto = "Python"

    print(texto[0])
    time.sleep(0.3)
    print(texto[1])
    time.sleep(0.3)
    print(texto[-1])

    pausa()
    limpiar()

    titulo("SLICING")

    print("El slicing permite extraer una parte del string.\n")

    codigo("""
texto = "Python"

print(texto[0:3])
print(texto[2:])
print(texto[:4])
print(texto[-3:])
""")

    salida()

    texto = "Python"

    print(texto[0:3])
    time.sleep(0.3)
    print(texto[2:])
    time.sleep(0.3)
    print(texto[:4])
    time.sleep(0.3)
    print(texto[-3:])

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("""
texto[inicio:fin]

inicio → desde dónde empieza (incluido)
fin    → hasta dónde llega (no incluido)

Si se omite inicio, comienza desde el principio.
Si se omite fin, llega hasta el final.
""")

    pausa()
    limpiar()

    titulo("MÉTODOS COMUNES")

    print("""
┌───────────────┬──────────────────────────────────────┐
│  upper()      │  convierte a mayúsculas              │
│  lower()      │  convierte a minúsculas              │
│  strip()      │  elimina espacios al inicio y final  │
│  replace()    │  reemplaza texto                     │
│  split()      │  divide el string en una lista       │
│  join()       │  une una lista en un string          │
│  startswith() │  verifica cómo empieza               │
│  endswith()   │  verifica cómo termina               │
└───────────────┴──────────────────────────────────────┘
""")

    pausa()
    limpiar()

    seccion("upper() y lower()")

    codigo("""
texto = "Hola Mundo"

print(texto.upper())
print(texto.lower())
""")

    salida()

    texto = "Hola Mundo"

    print(texto.upper())
    time.sleep(0.3)
    print(texto.lower())

    pausa()
    limpiar()

    seccion("strip()")

    codigo("""
texto = "   hola   "

print(texto.strip())
""")

    salida()

    texto = "   hola   "

    print(texto.strip())

    pausa()
    limpiar()

    seccion("replace()")

    codigo("""
texto = "Hola mundo"

nuevo = texto.replace("mundo", "Python")

print(nuevo)
""")

    salida()

    texto = "Hola mundo"

    nuevo = texto.replace("mundo", "Python")

    print(nuevo)

    pausa()
    limpiar()

    seccion("split()")

    codigo("""
texto = "manzana,plátano,pera"

frutas = texto.split(",")

print(frutas)
""")

    salida()

    texto = "manzana,plátano,pera"

    frutas = texto.split(",")

    print(frutas)

    pausa()
    limpiar()

    seccion("join()")

    codigo("""
frutas = ["manzana", "plátano", "pera"]

texto = ", ".join(frutas)

print(texto)
""")

    salida()

    frutas = ["manzana", "plátano", "pera"]

    texto = ", ".join(frutas)

    print(texto)

    pausa()
    limpiar()

    seccion("startswith() y endswith()")

    codigo("""
texto = "archivo.py"

print(texto.startswith("archivo"))
print(texto.endswith(".py"))
""")

    salida()

    texto = "archivo.py"

    print(texto.startswith("archivo"))
    time.sleep(0.3)
    print(texto.endswith(".py"))

    pausa()
    limpiar()

    titulo("F-STRINGS")

    print("Las f-strings permiten insertar variables dentro de un texto.")
    print("Se colocan entre llaves {} dentro del string.\n")

    codigo("""
nombre = "José"
edad = 20

print(f"{nombre} tiene {edad} años")
print(f"El doble de su edad es {edad * 2}")
""")

    salida()

    nombre = "José"
    edad = 20

    print(f"{nombre} tiene {edad} años")
    time.sleep(0.3)
    print(f"El doble de su edad es {edad * 2}")

    pausa()
    limpiar()

    titulo("VERIFICAR CONTENIDO")

    print("Se puede comprobar si un texto está dentro de otro con 'in'.\n")

    codigo("""
texto = "Hola mundo"

print("mundo" in texto)
print("Python" in texto)
""")

    salida()

    texto = "Hola mundo"

    print("mundo" in texto)
    time.sleep(0.3)
    print("Python" in texto)

    pausa()
    limpiar()

    titulo("EJERCICIOS")

    print("""
Practica lo que aprendiste.

Ejercicio 1
Crea un string con tu nombre completo.
Imprime cuántos caracteres tiene.

Ejercicio 2
Toma el string "  Python es genial  "
y elimina los espacios con strip().
Luego conviértelo a mayúsculas.

Ejercicio 3
Toma el string "rojo,verde,azul"
y sepáralo en una lista usando split().
Luego únelo de nuevo con " - " usando join().
""")

    pausa()
    limpiar()

    titulo("FIN DE LA LECCIÓN")

    print("Ahora sabes:\n")

    print("✓ qué es un string")
    print("✓ strings multilínea")
    print("✓ acceder a caracteres por índice")
    print("✓ slicing")
    print("✓ métodos: upper, lower, strip, replace, split, join")
    print("✓ f-strings")
    print("✓ verificar contenido con in")

    print("\nExplora más modificando el código.")

except KeyboardInterrupt:
    print("\n\nLección cancelada por el usuario.")
    sys.exit(0)
