#!/usr/bin/python
"""Programa que ordena una secuencia usando el algoritmo Merge-Sort."""

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
    L.append(9999999)
    R.append(9999999)

    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def MergeSortR(A, p, r):
    """Ordena la sublista A[p..r] por medio del algoritmo Merge-Sort."""
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
