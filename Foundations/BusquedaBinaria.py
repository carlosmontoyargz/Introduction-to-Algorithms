#!/usr/bin/python
"""Programa que implementa el algoritmo de busqueda binaria."""


def busquedaBinaria(A, elemento):
    """Algoritmo de busqueda binaria."""
    primero = 0
    ultimo = len(A) - 1

    posicion = -1
    encontrado = False
    while primero <= ultimo and not encontrado:
        mitad = (primero + ultimo) // 2

        if A[mitad] == elemento:
            encontrado = True
            posicion = mitad

        else:
            if elemento < A[mitad]:
                ultimo = mitad - 1
            else:
                primero = mitad + 1

    return posicion


lista = [2, 5, 6, 8, 11, 15, 20, 21, 22, 30, 35, 50]
print(busquedaBinaria(lista, 7))
print(busquedaBinaria(lista, 21))
print(busquedaBinaria(lista, 50))
print(busquedaBinaria(lista, 2))
