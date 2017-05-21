#!/usr/bin/python
"""Programa que ordena una secuencia usando el algoritmo Merge-Sort.

Es una modificacion en la que el algoritmo agrega todo el arreglo L o R
restante cuando el sentinela es encontrado.
"""
import random


def Merge(A, p, q, r):
    """Combina dos subsecuencias ordenadas dentro de un arreglo."""
    n1 = q - p + 1
    n2 = r - q

    L = []
    R = []
    for i in range(n1):
        L.append(A[p + i])
    for j in range(n2):
        R.append(A[q + j + 1])
    L.append(None)
    R.append(None)

    i = 0
    j = 0
    k = p
    while L[i] is not None and R[j] is not None:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    # Cuando se encuentra el sentinela se agrega el resto de la otra lista
    A[k:r+1] = L[i:n1] if R[j] is None else R[j:n2]


def MergeSortR(A, p, r):
    """Ordena la subsecuencia A[p..r] por medio del algoritmo Merge-Sort."""
    if p < r:
        q = (p + r) / 2
        MergeSortR(A, p, q)
        MergeSortR(A, q + 1, r)
        Merge(A, p, q, r)


def MergeSort(A):
    """Ordena la lista A por medio del algoritmo MergeSort."""
    MergeSortR(A, 0, len(A) - 1)


A = random.sample(range(20), 20)
print(A)
MergeSort(A)
print(A)
