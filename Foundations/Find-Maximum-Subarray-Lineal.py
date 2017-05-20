#!/usr/bin/python
"""Programa que encuentra la mayor subsecuencia dentro de un arreglo.

A diferencia de la version recursiva, este algoritmo se ejecuta en tiempo
lineal.
"""


def FindMaximumSubarray(A):
    """Encuentra la mayor subsecuencia dentro de la lista A.

    Si se recibe una lista vacia se retorna 0, 0, 0.

    Retorna:
    max_left -- El indice izquierdo del subarreglo
    max_right -- El indice derecho del subarreglo
    suma -- La suma total del subarreglo

    """
    max_left = 0
    max_right = 0
    suma = 0
    p = 0
    suma_p = 0

    for i in range(0, len(A)):
        suma_p += A[i]
        if suma_p <= 0:
            p = i
            suma_p = A[i]

        if suma_p > suma:
            max_left = p
            max_right = i
            suma = suma_p

    return (max_left, max_right, suma)


A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(A)
res = FindMaximumSubarray(A)
print A[res[0]:res[1] + 1], res[2]

B = [-2, -1, -13, -4, -3, -7]
print(B)
res = FindMaximumSubarray(B)
print B[res[0]:res[1] + 1], res[2]
