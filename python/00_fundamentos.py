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
    titulo("INTRODUCCIÓN A PYTHON")

    print("Python es un lenguaje de programación.")
    print("Se utiliza para crear programas, automatizar tareas,")
    print("analizar datos, desarrollar aplicaciones y mucho más.\n")

    print("En este curso aprenderás los fundamentos básicos")
    print("del lenguaje paso a paso.")

    pausa()
    limpiar()

    titulo("INSTALAR PYTHON")

    print("Para ejecutar programas necesitas tener Python instalado.\n")

    print("Dependiendo del sistema operativo el proceso cambia.\n")

    print("""
┌───────────┬────────────────────────────────────────┐
│ Linux     │ normalmente ya viene instalado         │
│ macOS     │ instalador .pkg o Homebrew             │
│ Windows   │ puede instalarse fácilmente con winget │
└───────────┴────────────────────────────────────────┘
""")

    pausa()
    limpiar()

    seccion("Instalar Python en Windows")

    print("La forma más fácil es usar winget.")
    print("Winget es el gestor de paquetes de Windows.\n")

    codigo("""
winget install Python.Python.3
""")

    print("\nEsto descargará e instalará Python automáticamente.")

    pausa()
    limpiar()

    seccion("Instalar Python en Linux")

    print("En la mayoría de distribuciones Python ya está instalado.\n")

    print("Puedes verificarlo con:\n")

    codigo("""
python3 --version
""")

    print("\nSi no está instalado puedes usar el gestor de paquetes.\n")

    print("Ejemplo en distribuciones basadas en Debian:")

    codigo("""
sudo apt install python3
""")

    pausa()
    limpiar()

    seccion("Instalar Python en macOS")

    print("La forma estándar es usar el instalador oficial.\n")

    print("1. Descarga el instalador .pkg desde el sitio oficial de Python.")
    print("2. Ábrelo.")
    print("3. Sigue el asistente de instalación.\n")

    print("Esto instalará Python automáticamente en el sistema.")

    pausa()
    limpiar()

    print("Alternativa para desarrolladores: usar Homebrew.\n")

    codigo("""
brew install python
""")

    print("\nHomebrew es un gestor de paquetes popular en macOS.")

    pausa()
    limpiar()

    seccion("Verificar instalación")

    print("Después de instalar Python puedes comprobarlo con:\n")

    codigo("""
python --version
""")

    print("o")

    codigo("""
python3 --version
""")

    salida()

    print("Python 3.x.x")

    pausa()
    limpiar()

    titulo("¿CÓMO EJECUTAR UN PROGRAMA?")

    print("Un programa en Python se guarda en un archivo .py\n")

    print("Ejemplo de ejecución desde la terminal:\n")

    print("""
python archivo.py
""")

    print("En Windows también puedes usar:\n")

    codigo("""
py archivo.py
""")

    pausa()
    limpiar()

    titulo("TU PRIMER PROGRAMA")

    print("La función más básica en Python es print().")
    print("Sirve para mostrar texto en la pantalla.\n")

    codigo("""
print("Hola mundo")
""")

    salida()

    print("Hola mundo")

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("print() envía texto a la salida del programa.")
    print("Lo que esté entre comillas se mostrará en pantalla.")

    pausa()
    limpiar()

    titulo("IMPRIMIR VARIAS COSAS")

    print("print() puede mostrar números y texto.\n")

    codigo("""
print("Hola")
print(10)
print("Python")
""")

    salida()

    print("Hola")
    time.sleep(0.3)
    print(10)
    time.sleep(0.3)
    print("Python")

    pausa()
    limpiar()

    titulo("COMENTARIOS")

    print("Los comentarios sirven para escribir notas en el código.")
    print("Python ignora los comentarios al ejecutar el programa.\n")

    codigo("""
# Esto es un comentario

print("Hola")
""")

    salida()

    print("Hola")

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("Todo lo que esté después de '#' en una línea")
    print("es considerado un comentario.")

    pausa()
    limpiar()

    titulo("INDENTACIÓN")

    print("Python utiliza la indentación para organizar el código.")
    print("La indentación son espacios al inicio de una línea.\n")

    print("Es muy importante respetarla.")

    pausa()
    limpiar()

    seccion("Ejemplo de indentación")

    codigo("""
if True:
    print("Esto está indentado")
""")

    salida()

    if True:
        print("Esto está indentado")

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("Las líneas indentadas pertenecen al bloque anterior.")
    print("En Python la indentación define la estructura del programa.")

    pausa()
    limpiar()

    titulo("ERRORES")

    print("Cuando Python encuentra un problema")
    print("muestra un mensaje de error.\n")

    print("Los errores son normales al programar.")
    print("Aprender a leerlos es parte del proceso.")

    pausa()
    limpiar()

    titulo("EJERCICIOS")

    print("""
Practica lo que aprendiste.

Ejercicio 1
Usa print() para mostrar tu nombre.

Ejercicio 2
Imprime un número.

Ejercicio 3
Escribe un comentario en el código.
""")

    pausa()
    limpiar()

    titulo("FIN DE LA LECCIÓN")

    print("Ahora sabes:\n")

    print("✓ qué es Python")
    print("✓ cómo instalar Python")
    print("✓ cómo ejecutar un programa")
    print("✓ usar print()")
    print("✓ escribir comentarios")
    print("✓ la importancia de la indentación")

    print("\nContinúa con la siguiente lección.")

except KeyboardInterrupt:
    print("\n\nLección cancelada por el usuario.")
    sys.exit(0)