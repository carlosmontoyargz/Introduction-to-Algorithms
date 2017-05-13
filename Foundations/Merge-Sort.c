#include <stdio.h>
#define INF 999999

void merge(int A[], int p, int q, int r);
void merge_sort(int A[], int p, int r);
void imprimir(int A[], int n);

int main(int argc, char const *argv[]) {

    int A[] = {4, 2, 10, 5, 3, 6, 9, 7, 8, 1};
    imprimir(A, 10);

    merge_sort(A, 0, 10);
    imprimir(A, 10);

    return 0;
}

void merge(int A[], int p, int q, int r)
{
    int n1 = q - p, n2 = r - q;
    int L[n1 + 1], R[n2 + 1];

    int i, j;

    for (i = 0; i < n1; i++) L[i] = A[p + i];
    for (j = 0; j < n2; j++) R[j] = A[q + j];
    L[n1] = INF; R[n2] = INF;

    i = 0; j = 0;
    for (int k = p; k < r; k++)
    {
        if (L[i] <= R[j])
        {
            A[k] = L[i];
            i += 1;
        }
        else
        {
            A[k] = R[j];
            j += 1;
        }
    }
}

void merge_sort(int A[], int p, int r)
{
    int q;

    if (p < (r - 1))
    {
        q = (p + r) / 2;
        merge_sort(A, p, q);
        merge_sort(A, q, r);
        merge(A, p, q, r);
    }
}

void imprimir(int A[], int n)
{
    for (int i = 0; i < n; i++)
        printf("%d ", A[i]);
    printf("\n");
}
