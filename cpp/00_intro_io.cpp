#include <iostream>
#include <string>
#include "utils.h"

int main() {

    limpiar();
    titulo("INTRODUCCIÓN A C++");

    std::cout << "C++ es un lenguaje de programación de propósito general.\n";
    std::cout << "Es una extensión del lenguaje C con soporte para\n";
    std::cout << "programación orientada a objetos y programación genérica.\n\n";

    std::cout << "Se utiliza para:\n\n";
    std::cout << "• sistemas operativos\n";
    std::cout << "• motores de videojuegos\n";
    std::cout << "• aplicaciones de alto rendimiento\n";
    std::cout << "• software embebido\n";
    std::cout << "• compiladores\n";

    pausa();
    limpiar();

    titulo("INSTALAR C++");

    std::cout << "Para compilar programas necesitas un compilador instalado.\n\n";

    std::cout << "El más común es g++, parte de GCC.\n\n";

    std::cout << R"(
┌───────────┬────────────────────────────────────────┐
│ Linux     │ normalmente ya viene instalado         │
│ macOS     │ Xcode Command Line Tools               │
│ Windows   │ MinGW o Visual Studio                  │
└───────────┴────────────────────────────────────────┘
)";

    pausa();
    limpiar();

    seccion("Instalar en Linux");

    std::cout << "Verifica si ya está instalado:\n\n";

    codigo(R"(
g++ --version
)");

    std::cout << "Si no está instalado:\n\n";

    codigo(R"(
sudo apt install g++
)");

    pausa();
    limpiar();

    seccion("Instalar en macOS");

    std::cout << "Instala las herramientas de línea de comandos de Xcode:\n\n";

    codigo(R"(
xcode-select --install
)");

    std::cout << "Esto incluye g++ y clang++.\n";

    pausa();
    limpiar();

    seccion("Instalar en Windows");

    std::cout << "La forma más sencilla es usar winget con MinGW:\n\n";

    codigo(R"(
winget install MinGW.MinGW
)");

    std::cout << "O instalar Visual Studio Community que incluye\n";
    std::cout << "el compilador MSVC.\n";

    pausa();
    limpiar();

    seccion("Verificar instalación");

    codigo(R"(
g++ --version
)");

    salida();

    std::cout << "g++ (GCC) 13.x.x\n";

    pausa();
    limpiar();

    titulo("¿CÓMO COMPILAR Y EJECUTAR?");

    std::cout << "Un programa en C++ se guarda en un archivo .cpp\n\n";

    std::cout << "Primero se compila y luego se ejecuta:\n\n";

    codigo(R"(
g++ archivo.cpp -o programa
./programa
)");

    std::cout << "\nEn Windows:\n\n";

    codigo(R"(
g++ archivo.cpp -o programa.exe
programa.exe
)");

    pausa();
    limpiar();

    titulo("TU PRIMER PROGRAMA");

    std::cout << "El programa más básico en C++ muestra texto en pantalla.\n\n";

    codigo(R"(
#include <iostream>

int main() {
    std::cout << "Hola mundo" << std::endl;
    return 0;
}
)");

    salida();

    std::cout << "Hola mundo\n";

    pausa();
    limpiar();

    seccion("EXPLICACIÓN");

    std::cout << "#include <iostream>  →  incluye la librería de entrada y salida\n";
    std::cout << "int main()          →  función principal, donde empieza el programa\n";
    std::cout << "std::cout           →  muestra texto en pantalla\n";
    std::cout << "<<                  →  operador de inserción\n";
    std::cout << "std::endl           →  salto de línea\n";
    std::cout << "return 0            →  indica que el programa terminó correctamente\n";

    pausa();
    limpiar();

    titulo("ENTRADA DE DATOS");

    std::cout << "std::cin permite leer datos ingresados por el usuario.\n\n";

    codigo(R"(
#include <iostream>
#include <string>

int main() {
    std::string nombre;

    std::cout << "Ingresa tu nombre: ";
    std::cin >> nombre;

    std::cout << "Hola, " << nombre << std::endl;
    return 0;
}
)");

    salida();

    std::cout << "Ingresa tu nombre: José\n";
    std::cout << "Hola, José\n";

    pausa();
    limpiar();

    seccion("EXPLICACIÓN");

    std::cout << "std::cin   →  lee datos desde el teclado\n";
    std::cout << ">>         →  operador de extracción\n";
    std::cout << "string     →  tipo de dato para texto\n\n";

    std::cout << "El programa se detiene y espera a que el usuario escriba algo.\n";
    std::cout << "Al presionar ENTER el valor se guarda en la variable.\n";

    pausa();
    limpiar();

    titulo("LEER UNA LÍNEA COMPLETA");

    std::cout << "std::cin >> se detiene en el primer espacio.\n";
    std::cout << "Para leer una línea completa se usa getline().\n\n";

    codigo(R"(
#include <iostream>
#include <string>

int main() {
    std::string nombre;

    std::cout << "Ingresa tu nombre completo: ";
    std::getline(std::cin, nombre);

    std::cout << "Hola, " << nombre << std::endl;
    return 0;
}
)");

    salida();

    std::cout << "Ingresa tu nombre completo: José García\n";
    std::cout << "Hola, José García\n";

    pausa();
    limpiar();

    titulo("COMENTARIOS");

    std::cout << "Los comentarios sirven para escribir notas en el código.\n";
    std::cout << "El compilador los ignora.\n\n";

    codigo(R"(
// Esto es un comentario de una línea

/*
   Esto es un comentario
   de varias líneas
*/

std::cout << "Hola" << std::endl;
)");

    salida();

    std::cout << "Hola\n";

    pausa();
    limpiar();

    titulo("INDENTACIÓN Y ESTILO");

    std::cout << "C++ no exige indentación como Python.\n";
    std::cout << "Pero es obligatorio usarla para mantener el código legible.\n\n";

    std::cout << "Los bloques de código van entre llaves {}.\n\n";

    codigo(R"(
int main() {
    if (true) {
        std::cout << "Indentado correctamente" << std::endl;
    }
    return 0;
}
)");

    pausa();
    limpiar();

    titulo("ERRORES COMUNES");

    std::cout << "Los errores más frecuentes al empezar:\n\n";

    std::cout << R"(
┌──────────────────────────┬──────────────────────────────────────┐
│  Olvidar el ;            │  cada instrucción termina en ;       │
│  Olvidar return 0        │  main debe devolver un entero        │
│  Olvidar #include        │  cada librería debe incluirse        │
│  Llaves sin cerrar       │  cada { necesita su }                │
└──────────────────────────┴──────────────────────────────────────┘
)";

    pausa();
    limpiar();

    titulo("EJERCICIOS");

    std::cout << R"(
Practica lo que aprendiste.

Ejercicio 1
Escribe un programa que muestre tu nombre.

Ejercicio 2
Escribe un programa que pida tu nombre
e imprima un saludo personalizado.

Ejercicio 3
Agrega comentarios explicando qué hace
cada línea de tu programa.
)";

    pausa();
    limpiar();

    titulo("FIN DE LA LECCIÓN");

    std::cout << "Ahora sabes:\n\n";

    std::cout << "✓ qué es C++\n";
    std::cout << "✓ cómo instalar g++\n";
    std::cout << "✓ cómo compilar y ejecutar un programa\n";
    std::cout << "✓ usar std::cout para mostrar texto\n";
    std::cout << "✓ usar std::cin para leer datos\n";
    std::cout << "✓ usar getline() para leer líneas completas\n";
    std::cout << "✓ escribir comentarios\n";
    std::cout << "✓ estructura básica de un programa\n";

    std::cout << "\nContinúa con la siguiente lección.\n";

    pausa();

    return 0;
}
