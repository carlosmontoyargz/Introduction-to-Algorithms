#!/usr/bin/python
"""Programa que implementa el algoritmo de ordenamiento por insercion."""


def InsertionSort(lista):
    """Algoritmo de ordenamiento por insercion."""
    for j in range(1, len(lista)):
        key = lista[j]

        # Inserta lista[j] en la secuecia ordenada lista[0.. j]
        i = j - 1
        while i >= 0 and lista[i] > key:
            lista[i + 1] = lista[i]
            i -= 1

        lista[i + 1] = key


lista = [5, 3, 2, 1, 6, 7, 10, 0, 4, 8, 9]
print(lista)

InsertionSort(lista)
print(lista)
