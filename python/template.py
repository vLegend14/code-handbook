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
except KeyboardInterrupt:
    print("\n\nLección cancelada por el usuario.")
    sys.exit(0)
