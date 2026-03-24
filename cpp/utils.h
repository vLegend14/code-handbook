#pragma once

#include <iostream>
#include <string>
#include <limits>

// ─────────────────────────────────────────
//  Limpiar pantalla
// ─────────────────────────────────────────
void limpiar() {
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
}

// ─────────────────────────────────────────
//  Pausa — espera que el usuario presione ENTER
// ─────────────────────────────────────────
void pausa() {
    std::cout << "\nPresiona ENTER para continuar...";
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::cin.get();
}

// ─────────────────────────────────────────
//  Título con separador doble
// ─────────────────────────────────────────
void titulo(const std::string& texto) {
    std::cout << "\n" << std::string(50, '=') << "\n";
    std::cout << texto << "\n";
    std::cout << std::string(50, '=') << "\n\n";
}

// ─────────────────────────────────────────
//  Sección con separador simple
// ─────────────────────────────────────────
void seccion(const std::string& texto) {
    std::cout << "\n" << std::string(50, '-') << "\n";
    std::cout << texto << "\n";
    std::cout << std::string(50, '-') << "\n\n";
}

// ─────────────────────────────────────────
//  Bloque de código
// ─────────────────────────────────────────
void codigo(const std::string& texto) {
    std::cout << "Código:\n";
    std::cout << texto << "\n";
}

// ─────────────────────────────────────────
//  Etiqueta de salida
// ─────────────────────────────────────────
void salida() {
    std::cout << "Salida:\n";
}
