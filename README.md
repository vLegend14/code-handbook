# 📚 Diccionario Interactivo de Programación

Repositorio personal con ejemplos y lecciones simples de programación en distintos lenguajes.

Cada archivo está pensado como una **pequeña lección ejecutable**, donde se explica un concepto y se muestran ejemplos.

## 🎯 Objetivos

* Guardar mis conocimientos como **bitácora personal**.
* Crear material sencillo para **personas que están aprendiendo**.
* Tener ejemplos rápidos para **consultar conceptos**.

## 📂 Estructura del repositorio

```
.
├── cpp
├── java
├── javascript
├── python
│   ├── 00_fundamentos.py
│   ├── 01_tipos_de_datos.py
│   ├── 02_variables.py
│   ├── 03_strings.py
│   ├── 04_conditionals.py
│   ├── 05_loops.py
│   ├── 06_lists.py
│   ├── 07_arrays.py
│   ├── 08_tuples_sets.py
│   ├── 09_functions.py
│   ├── 10_dictionaries.py
│   ├── 11_exceptions.py
│   ├── 12_files.py
│   ├── 13_modules.py
│   ├── 14_classes.py
│   ├── 15_comprehensions.py
│   ├── 16_generators.py
│   ├── 17_decorators.py
│   ├── launcher.py
│   └── template.py
├── README.md
└── typescript
```

Cada carpeta corresponde a **un lenguaje de programación**.

Dentro de cada lenguaje hay archivos que explican **un concepto específico**.

## ▶️ Cómo usar los archivos

### Lanzador

La forma recomendada es usar el lanzador. Ejecuta las lecciones en orden,
guarda el progreso y permite retomar desde donde se dejó.

```
cd python
python launcher.py
```

### Lección individual

También se puede ejecutar cualquier lección directamente desde la terminal.

```
python python/00_fundamentos.py
```

Los scripts muestran explicaciones, ejemplos de código y pausas para leer.

## 🐍 Contenido — Python

| Archivo | Concepto |
|---|---|
| 00_fundamentos.py | Introducción, instalación, print, comentarios, indentación |
| 01_tipos_de_datos.py | int, float, str, bool, None, type(), conversión de tipos |
| 02_variables.py | Creación, reglas de nombres, reasignación, operadores de asignación |
| 03_strings.py | Índices, slicing, métodos, f-strings |
| 04_conditionals.py | if, elif, else, operadores de comparación y lógicos |
| 05_loops.py | for, while, range, enumerate, zip, break, continue |
| 06_lists.py | Creación, índices, métodos, recorrido |
| 07_arrays.py | Módulo array, códigos de tipo, diferencias con listas |
| 08_tuples_sets.py | Tuplas inmutables, desempaquetado, sets, operaciones de conjuntos |
| 09_functions.py | def, parámetros, return, valores por defecto, scope |
| 10_dictionaries.py | Creación, acceso, métodos, recorrido |
| 11_exceptions.py | try, except, else, finally, raise |
| 12_files.py | Modos de apertura, read, write, with |
| 13_modules.py | import, from, as, librería estándar, módulos propios |
| 14_classes.py | class, __init__, self, métodos, herencia, __str__ |
| 15_comprehensions.py | List, dict y set comprehensions |
| 16_generators.py | yield, next, generator expressions |
| 17_decorators.py | Funciones como objetos, @, *args, **kwargs |

## 📖 Filosofía del proyecto

* Un archivo = **un concepto**
* Explicaciones **simples y directas**
* Ejemplos **pequeños y claros**
* Pensado para **aprender leyendo y ejecutando**

## 🚧 Estado del proyecto

En desarrollo.
Se irán agregando más conceptos y lenguajes con el tiempo.
