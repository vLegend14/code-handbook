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
    titulo("CLASES EN PYTHON")

    print("Las clases permiten crear tus propios tipos de datos.")
    print("Son la base de la programación orientada a objetos.\n")

    print("Una clase agrupa:\n")
    print("• atributos → los datos que describe")
    print("• métodos   → las acciones que puede hacer")

    pausa()
    limpiar()

    titulo("CLASES Y OBJETOS")

    print("""
Una clase es como un molde.
Un objeto es lo que se crea a partir de ese molde.

Ejemplo de la vida real:

┌─────────────┬──────────────────────────────────────┐
│  Clase      │  Persona                             │
│  Atributos  │  nombre, edad, ciudad                │
│  Métodos    │  saludar(), caminar(), hablar()      │
├─────────────┼──────────────────────────────────────┤
│  Objeto 1   │  José, 20, Santiago                    │
│  Objeto 2   │  gonzalo, 25, Viña del mar                │
└─────────────┴──────────────────────────────────────┘
""")

    pausa()
    limpiar()

    titulo("CREAR UNA CLASE")

    print("Las clases se definen con la palabra clave 'class'.\n")

    codigo("""
class Persona:
    pass
""")

    print("\npass indica que la clase está vacía por ahora.")

    pausa()
    limpiar()

    titulo("EL MÉTODO __init__")

    print("__init__ se ejecuta automáticamente al crear un objeto.")
    print("Se usa para definir los atributos iniciales.\n")

    codigo("""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p = Persona("José", 20)

print(p.nombre)
print(p.edad)
""")

    salida()

    class Persona:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

    p = Persona("José", 20)

    print(p.nombre)
    time.sleep(0.3)
    print(p.edad)

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("self representa al propio objeto.")
    print("self.nombre guarda el nombre dentro del objeto.")
    print("Al crear Persona('Ana', 20) se llama __init__ automáticamente.")

    pausa()
    limpiar()

    titulo("AGREGAR MÉTODOS")

    print("Los métodos son funciones que pertenecen a la clase.\n")

    codigo("""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

p1 = Persona("José", 20)
p2 = Persona("Gonzalo", 25)

p1.saludar()
p2.saludar()
""")

    salida()

    class Persona:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

        def saludar(self):
            print(f"Hola, soy {self.nombre}")

    p1 = Persona("José", 20)
    p2 = Persona("Gonzalo", 25)

    p1.saludar()
    time.sleep(0.3)
    p2.saludar()

    pausa()
    limpiar()

    titulo("MODIFICAR ATRIBUTOS")

    print("Los atributos de un objeto se pueden cambiar directamente.\n")

    codigo("""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p = Persona("José", 20)
print(p.edad)

p.edad = 21
print(p.edad)
""")

    salida()

    class Persona:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

    p = Persona("José", 20)
    print(p.edad)

    time.sleep(0.3)

    p.edad = 21
    print(p.edad)

    pausa()
    limpiar()

    titulo("HERENCIA")

    print("Una clase puede heredar atributos y métodos de otra.")
    print("Esto evita repetir código.\n")

    codigo("""
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("...")

class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: guau")

class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: miau")

p = Perro("Rex")
g = Gato("Luna")

p.hablar()
g.hablar()
""")

    salida()

    class Animal:
        def __init__(self, nombre):
            self.nombre = nombre

        def hablar(self):
            print("...")

    class Perro(Animal):
        def hablar(self):
            print(f"{self.nombre} dice: guau")

    class Gato(Animal):
        def hablar(self):
            print(f"{self.nombre} dice: miau")

    p = Perro("Rex")
    g = Gato("Luna")

    p.hablar()
    time.sleep(0.3)
    g.hablar()

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("Perro y Gato heredan de Animal.")
    print("Ambas tienen el atributo nombre sin repetir el código.")
    print("Cada clase redefine hablar() a su manera.")
    print("\nEsto se llama sobreescritura de métodos.")

    pausa()
    limpiar()

    titulo("EL MÉTODO __str__")

    print("__str__ define cómo se muestra el objeto al hacer print().\n")

    codigo("""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona({self.nombre}, {self.edad})"

p = Persona("José", 20)
print(p)
""")

    salida()

    class Persona:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

        def __str__(self):
            return f"Persona({self.nombre}, {self.edad})"

    p = Persona("José", 20)
    print(p)

    pausa()
    limpiar()

    titulo("EJERCICIOS")

    print("""
Practica lo que aprendiste.

Ejercicio 1
Crea una clase Libro con atributos
titulo, autor y año.
Agrega un método que imprima la información.

Ejercicio 2
Crea una clase Vehiculo con atributos
marca y velocidad.
Agrega métodos acelerar() y frenar()
que modifiquen la velocidad.

Ejercicio 3
Crea una clase Lampara con un atributo
estado (que comience en "apagada").
Agrega métodos encender() y apagar()
que cambien el valor del atributo estado.
""")

    pausa()
    limpiar()

    titulo("FIN DE LA LECCIÓN")

    print("Ahora sabes:\n")

    print("✓ qué es una clase")
    print("✓ diferencia entre clase y objeto")
    print("✓ usar __init__")
    print("✓ definir atributos con self")
    print("✓ crear métodos")
    print("✓ modificar atributos")
    print("✓ herencia entre clases")
    print("✓ usar __str__")

    print("\nExplora más modificando el código.")

except KeyboardInterrupt:
    print("\n\nLección cancelada por el usuario.")
    sys.exit(0)