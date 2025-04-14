#include "matrix_inverse.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define EPSILON 1e-10

/* Allocate a matrix of size n x n */
double* allocate_matrix(int n) {
    if (n <= 0) {
        fprintf(stderr, "Invalid matrix size: %d\n", n);
        return NULL;
    }
    double* matrix = (double*)malloc(n * n * sizeof(double));
    if (!matrix) {
        fprintf(stderr, "Failed to allocate matrix of size %d x %d\n", n, n);
        return NULL;
    }
    printf("Allocated matrix at %p, size %d x %d\n", (void*)matrix, n, n);
    return matrix;
}

/* Free matrix memory */
void free_matrix(double* matrix) {
    if (matrix) {
        printf("Freeing matrix at %p\n", (void*)matrix);
        free(matrix);
    }
}

/* Copy matrix */
void copy_matrix(double* dest, const double* src, int n) {
    if (!dest || !src) {
        fprintf(stderr, "Null pointer in copy_matrix\n");
        return;
    }
    printf("Copying matrix from %p to %p\n", (void*)src, (void*)dest);
    memcpy(dest, src, n * n * sizeof(double));
}

/* Set matrix to identity */
void set_identity(double* matrix, int n) {
    if (!matrix) {
        fprintf(stderr, "Null pointer in set_identity\n");
        return;
    }
    printf("Setting identity matrix at %p\n", (void*)matrix);
    memset(matrix, 0, n * n * sizeof(double));
    for (int i = 0; i < n; i++) {
        matrix[i * n + i] = 1.0;
    }
}

/* Compute inverse matrix using Gauss-Jordan elimination */
/* Returns 0 on success, -1 if matrix is singular */
int inverse_matrix(const double* input, double* output, int n) {
    if (!input || !output) {
        fprintf(stderr, "Null pointer in inverse_matrix\n");
        return -1;
    }
    if (n <= 0) {
        fprintf(stderr, "Invalid matrix size: %d\n", n);
        return -1;
    }

    printf("Starting inverse_matrix with n=%d, input=%p, output=%p\n", 
           n, (void*)input, (void*)output);

    double* temp = allocate_matrix(n);
    if (!temp) {
        fprintf(stderr, "Failed to allocate temp matrix\n");
        return -1;
    }

    // Initialize temp as input matrix
    copy_matrix(temp, input, n);

    // Initialize output as identity matrix
    set_identity(output, n);

    // Gauss-Jordan elimination
    for (int i = 0; i < n; i++) {
        // Find pivot
        double pivot = temp[i * n + i];
        int pivot_row = i;
        for (int k = i + 1; k < n; k++) {
            if (fabs(temp[k * n + i]) > fabs(pivot)) {
                pivot = temp[k * n + i];
                pivot_row = k;
            }
        }

        // Check for singular matrix
        if (fabs(pivot) < EPSILON) {
            fprintf(stderr, "Singular matrix detected\n");
            free_matrix(temp);
            return -1;
        }

        // Swap rows if needed
        if (pivot_row != i) {
            printf("Swapping rows %d and %d\n", i, pivot_row);
            for (int j = 0; j < n; j++) {
                double t = temp[i * n + j];
                temp[i * n + j] = temp[pivot_row * n + j];
                temp[pivot_row * n + j] = t;

                t = output[i * n + j];
                output[i * n + j] = output[pivot_row * n + j];
                output[pivot_row * n + j] = t;
            }
        }

        // Scale pivot row
        printf("Scaling row %d with pivot %f\n", i, pivot);
        for (int j = 0; j < n; j++) {
            temp[i * n + j] /= pivot;
            output[i * n + j] /= pivot;
        }

        // Eliminate column
        for (int k = 0; k < n; k++) {
            if (k != i) {
                double factor = temp[k * n + i];
                printf("Eliminating column %d, row %d with factor %f\n", i, k, factor);
                for (int j = 0; j < n; j++) {
                    temp[k * n + j] -= factor * temp[i * n + j];
                    output[k * n + j] -= factor * output[i * n + j];
                }
            }
        }
    }

    free_matrix(temp);
    printf("Inverse matrix computed successfully\n");
    return 0;
}