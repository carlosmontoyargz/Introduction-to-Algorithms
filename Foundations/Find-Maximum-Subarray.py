#!/usr/bin/python
"""Programa que encuentra la subsecuencia con la mayor suma en un arreglo."""


def FindMaxCrossingSubarray(A, low, mid, high):
    """Encuentra la subsecuencia con suma mayor que atraviesa la mitad."""
    left_sum = -9999999
    sum1 = 0
    max_left = 0
    for i in range(mid, low - 1, -1):
        sum1 += A[i]
        if sum1 > left_sum:
            left_sum = sum1
            max_left = i

    right_sum = -9999999
    sum1 = 0
    max_right = 0
    for j in range(mid + 1, high):
        sum1 += A[j]
        if sum1 > right_sum:
            right_sum = sum1
            max_right = j

    return (max_left, max_right, left_sum + right_sum)


def FindMaximumSubarray(A, low, high):
    """Encuentra la subsecuencia con mayor suma dentro de un arreglo."""
    if high == low:
        return (low, high, A[low])

    else:
        mid = (low + high) / 2

        left = FindMaximumSubarray(A, low, mid)
        right = FindMaximumSubarray(A, mid + 1, high)
        cross = FindMaxCrossingSubarray(A, low, mid, high)

        if left[2] >= right[2] and left[2] >= cross[2]:
            return left

        elif right[2] >= left[2] and right[2] >= cross[2]:
            return right

        else:
            return cross


A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(A)

res = FindMaximumSubarray(A, 0, len(A) - 1)
print(A[res[0]:res[1] + 1])
print(res[2])
