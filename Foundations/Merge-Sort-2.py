#!/usr/bin/python
"""Programa que ordena una secuencia usando el algoritmo Merge-Sort.

Es una modificacion en la que el algoritmo agrega todo el arreglo L o R
restante cuando se encuentra el sentinela.
"""
import random


def Merge(A, p, q, r):
    """Combina dos subsecuencias ordenadas dentro de un arreglo."""
    n1 = q - p
    n2 = r - q

    L = []
    R = []
    for i in range(n1):
        L.append(A[p + i])
    for j in range(n2):
        R.append(A[q + j])
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
    A[k:r] = L[i:n1] if R[j] is None else R[j:n2]


def MergeSort(A, p, r):
    """Ordena la subsecuencia A[p..r] por medio del algoritmo Merge-Sort."""
    if p < (r - 1):
        q = (p + r) / 2
        MergeSort(A, p, q)
        MergeSort(A, q, r)
        Merge(A, p, q, r)


A = random.sample(range(20), 20)
print(A)

MergeSort(A, 0, len(A))
print(A)
