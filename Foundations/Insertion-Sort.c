#include "stdio.h"

void InsertionSort(int A[], int n);
void Leer(int A[], int n);
void Imprimir(int A[], int n);

int main(int argc, char const *argv[]) {

    int n = 5;
    int A[n];

    printf("Ingresar %d numeros: \n", n);

    Leer(A, n);
    InsertionSort(A, n);
    Imprimir(A, n);

    printf("\n");

    return 0;
}

void InsertionSort(int A[], int n)
{
    int key, i;

    for (int j = 1; j < n; j++) {
        key = A[j];

        // Inserta A[j] en la secuencia ordenada A[0.. j]
        i = j - 1;
        while (i >= 0 && A[i] > key) {
            A[i + 1] = A[i];
            i -= 1;
        }
        A[i + 1] = key;
    }
}

void Leer(int A[], int n)
{
    for (int i = 0; i < n; i++)
        scanf("%d", &A[i]);
}

void Imprimir(int A[], int n)
{
    for (int i = 0; i < n; i++)
        printf("%d ", A[i]);
}
