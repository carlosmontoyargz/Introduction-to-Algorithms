#!/usr/bin/python
"""Programa que calcular el producto de dos matrices cuadradas."""
import numpy


def SquareMatrixMultiplication(A, B):
    """Calcula el producto A*B.

    Si alguna de las dos matrices no es de tamano nxn lanza una excepcion de
    tipo IndexError.

    Retorna:
    C -- El resultado de la multiplicacion de las matrices
    """
    n = len(A)
    C = numpy.zeros((n, n))

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


A = [[1, 3],
     [7, 5]]

B = [[6, 8],
     [4, 2]]

print(SquareMatrixMultiplication(A, B))
