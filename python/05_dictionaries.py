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
    titulo("DICCIONARIOS EN PYTHON")

    print("Los diccionarios guardan datos en pares clave-valor.")
    print("Cada valor tiene un nombre único para identificarlo.\n")

    print("Son útiles cuando los datos tienen etiquetas:\n")
    print("• información de una persona")
    print("• configuración de un programa")
    print("• resultados agrupados por nombre")

    pausa()
    limpiar()

    titulo("CREAR UN DICCIONARIO")

    print("Un diccionario se crea usando llaves {}.\n")

    codigo("""
persona = {
    "nombre": "Ana",
    "edad": 20,
    "ciudad": "Santiago"
}

print(persona)
""")

    salida()

    persona = {
        "nombre": "Ana",
        "edad": 20,
        "ciudad": "Santiago"
    }

    print(persona)

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("Cada elemento tiene una clave y un valor.")
    print("La clave va entre comillas si es texto.")
    print("El par se separa con ':'")
    print("Los elementos se separan con ','")

    pausa()
    limpiar()

    titulo("ACCEDER A UN VALOR")

    print("Se accede a un valor usando su clave entre corchetes.\n")

    codigo("""
persona = {
    "nombre": "Ana",
    "edad": 20
}

print(persona["nombre"])
print(persona["edad"])
""")

    salida()

    persona = {
        "nombre": "Ana",
        "edad": 20
    }

    print(persona["nombre"])
    time.sleep(0.3)
    print(persona["edad"])

    pausa()
    limpiar()

    titulo("MÉTODO GET")

    print("get() permite acceder a un valor de forma segura.")
    print("Si la clave no existe, devuelve None o un valor por defecto.\n")

    codigo("""
persona = {
    "nombre": "Ana",
    "edad": 20
}

print(persona.get("nombre"))
print(persona.get("ciudad"))
print(persona.get("telefono", "sin datos"))
""")

    salida()

    persona = {"nombre": "Ana", "edad": 20}

    print(persona.get("nombre"))
    time.sleep(0.3)
    print(persona.get("ciudad"))
    time.sleep(0.3)
    print(persona.get("telefono", "sin datos"))

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("Con corchetes, si la clave no existe el programa lanza un error.")
    print("Con get() el programa sigue funcionando.")

    pausa()
    limpiar()

    titulo("AGREGAR Y MODIFICAR")

    print("Se puede agregar o cambiar un valor usando la clave.\n")

    codigo("""
persona = {
    "nombre": "Ana",
    "edad": 20
}

persona["edad"] = 22
persona["nombre"] = "María"

print(persona)
""")

    salida()

    persona = {
        "nombre": "Ana",
        "edad": 20
    }

    persona["edad"] = 22
    persona["nombre"] = "María"

    print(persona)

    pausa()
    limpiar()

    titulo("ELIMINAR UN ELEMENTO")

    print("Se elimina un par clave-valor con 'del' o con pop().\n")

    codigo("""
persona = {
    "nombre": "Ana",
    "edad": 20,
    "ciudad": "Santiago"
}

del persona["ciudad"]

print(persona)
""")

    salida()

    persona = {
        "nombre": "Ana",
        "edad": 20,
        "ciudad": "Santiago"
    }

    del persona["ciudad"]

    print(persona)

    pausa()
    limpiar()

    titulo("RECORRER UN DICCIONARIO")

    print("Se puede recorrer un diccionario con un bucle for.\n")

    print("""
┌────────────────┬──────────────────────────────────────┐
│  .keys()       │  devuelve todas las claves           │
│  .values()     │  devuelve todos los valores          │
│  .items()      │  devuelve pares (clave, valor)       │
└────────────────┴──────────────────────────────────────┘
""")

    pausa()
    limpiar()

    seccion("Recorrer claves y valores con items()")

    codigo("""
persona = {
    "nombre": "Ana",
    "edad": 20,
    "ciudad": "Santiago"
}

for clave, valor in persona.items():
    print(f"{clave}: {valor}")
""")

    salida()

    persona = {"nombre": "Ana", "edad": 20, "ciudad": "Santiago"}

    for clave, valor in persona.items():
        print(f"{clave}: {valor}")
        time.sleep(0.3)

    pausa()
    limpiar()

    titulo("VERIFICAR SI UNA CLAVE EXISTE")

    print("Se puede comprobar si una clave está en el diccionario.\n")

    codigo("""
persona = {
    "nombre": "Ana",
    "edad": 20
}

if "nombre" in persona:
    print("La clave existe")

if "telefono" not in persona:
    print("La clave no existe")
""")

    salida()

    persona = {"nombre": "Ana", "edad": 20}

    if "nombre" in persona:
        print("La clave existe")

    time.sleep(0.3)

    if "telefono" not in persona:
        print("La clave no existe")

    pausa()
    limpiar()

    titulo("EJERCICIOS")

    print("""
Practica lo que aprendiste.

Ejercicio 1
Crea un diccionario con tu nombre, edad y ciudad.
Imprime cada valor usando su clave.

Ejercicio 2
Agrega una clave nueva al diccionario
y luego elimina una existente.

Ejercicio 3
Recorre el diccionario con items()
e imprime cada par clave-valor.
""")

    pausa()
    limpiar()

    titulo("FIN DE LA LECCIÓN")

    print("Ahora sabes:\n")

    print("✓ qué es un diccionario")
    print("✓ cómo crear diccionarios")
    print("✓ acceder a valores con [] y get()")
    print("✓ agregar y modificar valores")
    print("✓ eliminar elementos")
    print("✓ recorrer diccionarios")
    print("✓ verificar si una clave existe")

    print("\nExplora más modificando el código.")

except KeyboardInterrupt:
    print("\n\nLección cancelada por el usuario.")
    sys.exit(0)