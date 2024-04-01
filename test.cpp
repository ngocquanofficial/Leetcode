#include <omp.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

const int N = 1000;

int A[N][N];
int B[N][N];
int C[N][N];

int main() {
  clock_t start = clock();

  double elapsed;
  int i, j, k;
  omp_set_num_threads(20);

  for (i = 0; i < N; i++)
    for (j = 0; j < N; j++) {
      A[i][j] = 2;
      B[i][j] = 2;
    }
    /// Pham Ngoc Quan - 20210704
#pragma omp parallel for private(i, j, k) shared(A, B, C)
  for (i = 0; i < N; ++i) {
    for (k = 0; k < N; ++k) {
      int r = A[i][k];
      for (j = 0; j < N; ++j) {
        C[i][j] += r * B[k][j];
      }
    }
  }

  clock_t end = clock();

  // Calculate the running time
  double running_time = (double)(end - start) / CLOCKS_PER_SEC;

  // Print the running time
  printf("Running time: %f seconds\n", running_time);

//   for (int i = 0; i < N; ++i) {
//     for (int j = 0; j < N; ++j) {
//       printf("%d ", C[i][j]);
//       if (j == N - 1) {
//         printf("\n");
//       }
//     }
//   }
}