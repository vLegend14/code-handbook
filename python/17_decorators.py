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
    titulo("DECORADORES EN PYTHON")

    print("Los decoradores modifican el comportamiento de una función")
    print("sin cambiar su código interno.\n")

    print("Se usan para:\n")
    print("• agregar funcionalidad extra a funciones")
    print("• medir tiempos de ejecución")
    print("• verificar permisos o condiciones")
    print("• registrar llamadas a funciones")

    pausa()
    limpiar()

    titulo("FUNCIONES COMO OBJETOS")

    print("En Python las funciones son objetos.")
    print("Se pueden pasar como argumentos y devolver desde otras funciones.\n")

    codigo("""
def saludar():
    print("Hola")

def ejecutar(funcion):
    funcion()

ejecutar(saludar)
""")

    salida()

    def saludar():
        print("Hola")

    def ejecutar(funcion):
        funcion()

    ejecutar(saludar)

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("saludar se pasa como argumento sin paréntesis.")
    print("ejecutar recibe la función y la llama internamente.")
    print("\nEsto es la base de cómo funcionan los decoradores.")

    pausa()
    limpiar()

    titulo("CREAR UN DECORADOR")

    print("Un decorador es una función que recibe otra función")
    print("y devuelve una versión modificada.\n")

    codigo("""
def mi_decorador(funcion):
    def envoltura():
        print("Antes de ejecutar")
        funcion()
        print("Después de ejecutar")
    return envoltura

def saludar():
    print("Hola")

saludar = mi_decorador(saludar)

saludar()
""")

    salida()

    def mi_decorador(funcion):
        def envoltura():
            print("Antes de ejecutar")
            funcion()
            print("Después de ejecutar")
        return envoltura

    def saludar():
        print("Hola")

    saludar = mi_decorador(saludar)

    saludar()

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("mi_decorador recibe la función original.")
    print("envoltura agrega código antes y después.")
    print("mi_decorador devuelve envoltura.")
    print("\nsaludar = mi_decorador(saludar) reemplaza la función original.")

    pausa()
    limpiar()

    titulo("SINTAXIS CON @")

    print("Python tiene una forma más corta usando '@'.")
    print("Es equivalente a lo anterior pero más legible.\n")

    codigo("""
def mi_decorador(funcion):
    def envoltura():
        print("Antes de ejecutar")
        funcion()
        print("Después de ejecutar")
    return envoltura

@mi_decorador
def saludar():
    print("Hola")

saludar()
""")

    salida()

    def mi_decorador(funcion):
        def envoltura():
            print("Antes de ejecutar")
            funcion()
            print("Después de ejecutar")
        return envoltura

    @mi_decorador
    def saludar():
        print("Hola")

    saludar()

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("@mi_decorador antes de la función")
    print("es equivalente a escribir:")
    print("\nsaludar = mi_decorador(saludar)")

    pausa()
    limpiar()

    titulo("DECORADOR CON PARÁMETROS")

    print("Para decorar funciones que reciben argumentos")
    print("se usa *args y **kwargs en la envoltura.\n")

    codigo("""
def mi_decorador(funcion):
    def envoltura(*args, **kwargs):
        print("Ejecutando función...")
        resultado = funcion(*args, **kwargs)
        print("Función terminada.")
        return resultado
    return envoltura

@mi_decorador
def sumar(a, b):
    return a + b

total = sumar(3, 5)
print(f"Resultado: {total}")
""")

    salida()

    def mi_decorador(funcion):
        def envoltura(*args, **kwargs):
            print("Ejecutando función...")
            resultado = funcion(*args, **kwargs)
            print("Función terminada.")
            return resultado
        return envoltura

    @mi_decorador
    def sumar(a, b):
        return a + b

    total = sumar(3, 5)
    print(f"Resultado: {total}")

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("*args captura argumentos posicionales.")
    print("**kwargs captura argumentos con nombre.")
    print("\nUsarlos en la envoltura permite decorar")
    print("cualquier función sin importar sus parámetros.")

    pausa()
    limpiar()

    titulo("EJEMPLO PRÁCTICO: MEDIR TIEMPO")

    print("Un uso común de los decoradores es medir")
    print("cuánto tarda en ejecutarse una función.\n")

    codigo("""
import time

def medir_tiempo(funcion):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"{funcion.__name__} tardó {fin - inicio:.4f} segundos")
        return resultado
    return envoltura

@medir_tiempo
def tarea_lenta():
    time.sleep(1)
    print("Tarea completada")

tarea_lenta()
""")

    salida()

    def medir_tiempo(funcion):
        def envoltura(*args, **kwargs):
            inicio = time.time()
            resultado = funcion(*args, **kwargs)
            fin = time.time()
            print(f"{funcion.__name__} tardó {fin - inicio:.4f} segundos")
            return resultado
        return envoltura

    @medir_tiempo
    def tarea_lenta():
        time.sleep(1)
        print("Tarea completada")

    tarea_lenta()

    pausa()
    limpiar()

    titulo("EJEMPLO PRÁCTICO: VERIFICAR CONDICIÓN")

    print("Los decoradores también sirven para controlar")
    print("si una función debe ejecutarse o no.\n")

    codigo("""
def solo_mayores(funcion):
    def envoltura(edad):
        if edad < 18:
            print("Acceso denegado")
            return
        funcion(edad)
    return envoltura

@solo_mayores
def entrar(edad):
    print(f"Bienvenido, tienes {edad} años")

entrar(20)
entrar(15)
""")

    salida()

    def solo_mayores(funcion):
        def envoltura(edad):
            if edad < 18:
                print("Acceso denegado")
                return
            funcion(edad)
        return envoltura

    @solo_mayores
    def entrar(edad):
        print(f"Bienvenido, tienes {edad} años")

    entrar(20)
    time.sleep(0.3)
    entrar(15)

    pausa()
    limpiar()

    titulo("APILAR DECORADORES")

    print("Una función puede tener más de un decorador.")
    print("Se aplican de abajo hacia arriba.\n")

    codigo("""
def negrita(funcion):
    def envoltura():
        print("**", end=" ")
        funcion()
    return envoltura

def mayusculas(funcion):
    def envoltura():
        print(">>>", end=" ")
        funcion()
    return envoltura

@negrita
@mayusculas
def mensaje():
    print("hola")

mensaje()
""")

    salida()

    def negrita(funcion):
        def envoltura():
            print("**", end=" ")
            funcion()
        return envoltura

    def mayusculas(funcion):
        def envoltura():
            print(">>>", end=" ")
            funcion()
        return envoltura

    @negrita
    @mayusculas
    def mensaje():
        print("hola")

    mensaje()

    pausa()
    limpiar()

    titulo("EJERCICIOS")

    print("""
Practica lo que aprendiste.

Ejercicio 1
Crea un decorador llamado anunciar()
que imprima el nombre de la función
antes de ejecutarla.

Ejercicio 2
Crea un decorador que cuente
cuántas veces se llama una función.

Ejercicio 3
Crea un decorador que verifique
que el argumento de una función sea positivo.
Si no lo es, imprima un error y no ejecute la función.
""")

    pausa()
    limpiar()

    titulo("FIN DE LA LECCIÓN")

    print("Ahora sabes:\n")

    print("✓ qué es un decorador")
    print("✓ funciones como objetos")
    print("✓ crear un decorador manualmente")
    print("✓ usar la sintaxis con @")
    print("✓ decorar funciones con parámetros")
    print("✓ medir tiempos de ejecución")
    print("✓ verificar condiciones con decoradores")
    print("✓ apilar varios decoradores")

    print("\nExplora más modificando el código.")

except KeyboardInterrupt:
    print("\n\nLección cancelada por el usuario.")
    sys.exit(0)

