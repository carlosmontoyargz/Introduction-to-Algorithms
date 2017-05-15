#!/usr/bin/python
import random


def Bubblesort(A):
    """Algoritmo de ordenamiento burbuja."""
    for i in range(len(A) - 1):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                aux = A[j]
                A[j] = A[j - 1]
                A[j - 1] = aux


A = random.sample(range(20), 20)
print(A)

Bubblesort(A)
print(A)
