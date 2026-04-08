#!/usr/bin/env python3

import os
import sys
import json
import subprocess
import glob

PROGRESO_ARCHIVO = ".progreso.json"
CARPETA = os.path.dirname(os.path.abspath(__file__))


def limpiar():
    os.system("clear" if os.name == "posix" else "cls")


def obtener_modulos():
    patron = os.path.join(CARPETA, "[0-9][0-9]_*.py")
    archivos = sorted(glob.glob(patron))
    return archivos


def nombre_modulo(ruta):
    return os.path.basename(ruta)


def cargar_progreso():
    ruta = os.path.join(CARPETA, PROGRESO_ARCHIVO)
    if os.path.exists(ruta):
        with open(ruta, "r") as f:
            return json.load(f)
    return {"ultimo": 0}


def guardar_progreso(indice):
    ruta = os.path.join(CARPETA, PROGRESO_ARCHIVO)
    with open(ruta, "w") as f:
        json.dump({"ultimo": indice}, f)


def borrar_progreso():
    ruta = os.path.join(CARPETA, PROGRESO_ARCHIVO)
    if os.path.exists(ruta):
        os.remove(ruta)


def imprimir_banner():
    limpiar()
    print("\n" + "=" * 50)
    print("  CURSO DE PYTHON — LANZADOR DE LECCIONES")
    print("=" * 50 + "\n")


def imprimir_modulos(modulos, desde):
    total = len(modulos)
    completados = desde
    print(f"  Progreso: {completados}/{total} lecciones completadas\n")

    for i, ruta in enumerate(modulos):
        nombre = nombre_modulo(ruta)
        if i < desde:
            estado = "✓"
        elif i == desde:
            estado = "→"
        else:
            estado = " "
        print(f"  {estado} {nombre}")

    print()


def preguntar_al_terminar(indice, total):
    print("\n" + "-" * 50)
    print("  Lección completada.")
    print("-" * 50 + "\n")

    if indice + 1 >= total:
        return "fin"

    print("  ¿Qué deseas hacer?\n")
    print("  [1] Continuar con la siguiente lección")
    print("  [2] Guardar progreso y cerrar")
    print()

    while True:
        try:
            opcion = input("  Opción: ").strip()
        except KeyboardInterrupt:
            print("\n\nInterrumpido.")
            return "guardar"

        if opcion == "1":
            return "continuar"
        elif opcion == "2":
            return "guardar"
        else:
            print("  Ingresa 1 o 2.")


def menu_inicio(modulos, progreso):
    imprimir_banner()
    desde = progreso["ultimo"]

    if desde > 0 and desde < len(modulos):
        nombre = nombre_modulo(modulos[desde])
        print(f"  Tienes progreso guardado.\n")
        print(f"  Siguiente lección: {nombre}\n")
        print("  [1] Continuar desde donde dejaste")
        print("  [2] Empezar desde el principio")
        print("  [3] Elegir lección")
        print("  [4] Salir")
        print()

        while True:
            try:
                opcion = input("  Opción: ").strip()
            except KeyboardInterrupt:
                print("\n\nHasta luego.")
                sys.exit(0)

            if opcion == "1":
                return desde
            elif opcion == "2":
                borrar_progreso()
                return 0
            elif opcion == "3":
                return menu_elegir(modulos)
            elif opcion == "4":
                print("\n  Hasta luego.\n")
                sys.exit(0)
            else:
                print("  Ingresa una opción válida.")

    else:
        imprimir_modulos(modulos, 0)
        print("  [1] Iniciar curso")
        print("  [2] Elegir lección")
        print("  [3] Salir")
        print()

        while True:
            try:
                opcion = input("  Opción: ").strip()
            except KeyboardInterrupt:
                print("\n\nHasta luego.")
                sys.exit(0)

            if opcion == "1":
                return 0
            elif opcion == "2":
                return menu_elegir(modulos)
            elif opcion == "3":
                print("\n  Hasta luego.\n")
                sys.exit(0)
            else:
                print("  Ingresa una opción válida.")


def menu_elegir(modulos):
    limpiar()
    print("\n" + "=" * 50)
    print("  ELEGIR LECCIÓN")
    print("=" * 50 + "\n")

    for i, ruta in enumerate(modulos):
        print(f"  [{i}] {nombre_modulo(ruta)}")

    print()

    while True:
        try:
            opcion = input("  Número de lección: ").strip()
        except KeyboardInterrupt:
            print("\n\nHasta luego.")
            sys.exit(0)

        if opcion.isdigit() and 0 <= int(opcion) < len(modulos):
            return int(opcion)
        else:
            print(f"  Ingresa un número entre 0 y {len(modulos) - 1}.")


def ejecutar_modulo(ruta):
    nombre = nombre_modulo(ruta)
    limpiar()
    print("\n" + "=" * 50)
    print(f"  Iniciando: {nombre}")
    print("=" * 50 + "\n")

    try:
        subprocess.run([sys.executable, ruta], check=False)
    except KeyboardInterrupt:
        pass


def main():
    modulos = obtener_modulos()

    if not modulos:
        print("\nNo se encontraron archivos de lecciones.")
        print("Asegúrate de ejecutar launcher.py desde la carpeta python/\n")
        sys.exit(1)

    progreso = cargar_progreso()
    desde = menu_inicio(modulos, progreso)

    i = desde

    while i < len(modulos):
        ejecutar_modulo(modulos[i])

        accion = preguntar_al_terminar(i, len(modulos))

        if accion == "continuar":
            i += 1
            guardar_progreso(i)

        elif accion == "guardar":
            guardar_progreso(i + 1)
            limpiar()
            print("\n" + "=" * 50)
            print("  Progreso guardado.")
            print(f"  Última lección completada: {nombre_modulo(modulos[i])}")
            if i + 1 < len(modulos):
                print(f"  Próxima lección: {nombre_modulo(modulos[i + 1])}")
            print("=" * 50 + "\n")
            print("  Hasta luego.\n")
            sys.exit(0)

        elif accion == "fin":
            borrar_progreso()
            limpiar()
            print("\n" + "=" * 50)
            print("  ¡Curso completado!")
            print("  Has terminado todas las lecciones.")
            print("=" * 50 + "\n")
            sys.exit(0)

    borrar_progreso()
    limpiar()
    print("\n" + "=" * 50)
    print("  ¡Curso completado!")
    print("  Has terminado todas las lecciones.")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
