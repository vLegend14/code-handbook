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
    titulo("EXCEPCIONES EN PYTHON")

    print("Las excepciones son errores que ocurren mientras el programa corre.")
    print("Si no se controlan, el programa se detiene.\n")

    print("Manejar excepciones permite que el programa:")
    print("• continúe funcionando ante errores")
    print("• muestre mensajes útiles al usuario")
    print("• tome acciones alternativas")

    pausa()
    limpiar()

    titulo("ERRORES COMUNES")

    print("""
┌──────────────────────┬────────────────────────────────────┐
│  ZeroDivisionError   │  dividir por cero                  │
│  ValueError          │  valor incorrecto para el tipo     │
│  TypeError           │  operación entre tipos distintos   │
│  IndexError          │  índice fuera del rango            │
│  KeyError            │  clave inexistente en diccionario  │
│  FileNotFoundError   │  archivo no encontrado             │
└──────────────────────┴────────────────────────────────────┘
""")

    pausa()
    limpiar()

    titulo("TRY Y EXCEPT")

    print("El bloque try contiene el código que puede fallar.")
    print("El bloque except captura el error si ocurre.\n")

    codigo("""
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: no se puede dividir por cero")
""")

    salida()

    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero")

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("Python intenta ejecutar el código dentro de try.")
    print("Si ocurre un error, salta al bloque except.")
    print("El programa continúa en lugar de detenerse.")

    pausa()
    limpiar()

    titulo("CAPTURAR VARIOS ERRORES")

    print("Se pueden tener múltiples bloques except\n"
          "para manejar distintos tipos de errores.\n")

    codigo("""
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: división por cero")
    except TypeError:
        print("Error: los valores deben ser números")

dividir(10, 0)
dividir(10, "dos")
""")

    salida()

    def dividir(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Error: división por cero")
        except TypeError:
            print("Error: los valores deben ser números")

    dividir(10, 0)
    time.sleep(0.3)
    dividir(10, "dos")

    pausa()
    limpiar()

    titulo("BLOQUE ELSE")

    print("El bloque else se ejecuta solo si no hubo ningún error.\n")

    codigo("""
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Error: división por cero")
else:
    print(f"Resultado: {resultado}")
""")

    salida()

    try:
        resultado = 10 / 2
    except ZeroDivisionError:
        print("Error: división por cero")
    else:
        print(f"Resultado: {resultado}")

    pausa()
    limpiar()

    titulo("BLOQUE FINALLY")

    print("El bloque finally se ejecuta siempre.")
    print("Haya error o no.\n")

    codigo("""
try:
    numero = int("abc")
except ValueError:
    print("Error: no es un número válido")
finally:
    print("Esto siempre se ejecuta")
""")

    salida()

    try:
        numero = int("abc")
    except ValueError:
        print("Error: no es un número válido")
    finally:
        print("Esto siempre se ejecuta")

    pausa()
    limpiar()

    seccion("EXPLICACIÓN")

    print("finally se usa para liberar recursos.")
    print("Por ejemplo: cerrar archivos o conexiones.")
    print("Se ejecuta sin importar lo que pase en try.")

    pausa()
    limpiar()

    titulo("OBTENER EL MENSAJE DEL ERROR")

    print("Se puede guardar el error en una variable\n"
          "para leer su mensaje.\n")

    codigo("""
try:
    lista = [1, 2, 3]
    print(lista[10])
except IndexError as e:
    print(f"Error capturado: {e}")
""")

    salida()

    try:
        lista = [1, 2, 3]
        print(lista[10])
    except IndexError as e:
        print(f"Error capturado: {e}")

    pausa()
    limpiar()

    titulo("LANZAR EXCEPCIONES")

    print("Se puede lanzar un error manualmente con 'raise'.\n")

    codigo("""
def verificar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    print(f"Edad válida: {edad}")

try:
    verificar_edad(-5)
except ValueError as e:
    print(f"Error: {e}")
""")

    salida()

    def verificar_edad(edad):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        print(f"Edad válida: {edad}")

    try:
        verificar_edad(-5)
    except ValueError as e:
        print(f"Error: {e}")

    pausa()
    limpiar()

    titulo("EJERCICIOS")

    print("""
Practica lo que aprendiste.

Ejercicio 1
Escribe un programa que intente convertir
un texto a número con int().
Captura el error si el texto no es válido.

Ejercicio 2
Crea una función que reciba dos números y los divida.
Maneja el error si el segundo número es cero.

Ejercicio 3
Usa finally para mostrar un mensaje
que siempre se imprima al final.
""")

    pausa()
    limpiar()

    titulo("FIN DE LA LECCIÓN")

    print("Ahora sabes:\n")

    print("✓ qué es una excepción")
    print("✓ errores comunes en Python")
    print("✓ usar try y except")
    print("✓ capturar varios tipos de error")
    print("✓ usar else y finally")
    print("✓ obtener el mensaje del error")
    print("✓ lanzar errores con raise")

    print("\nExplora más modificando el código.")

except KeyboardInterrupt:
    print("\n\nLección cancelada por el usuario.")
    sys.exit(0)