#!/usr/bin/python
"""Programa que ordena una secuencia usando el algoritmo Merge-Sort."""

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
    L.append(9999999)
    R.append(9999999)

    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


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
