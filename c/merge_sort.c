/*
    merge_sort.c

    Implementação do algoritmo Merge Sort em C.
    Uso:
        gcc -O2 -o merge_sort merge_sort.c
        ./merge_sort <tamanho> <num_execucoes>

    O programa gera um array aleatório de inteiros, executa o Merge Sort múltiplas
    vezes, mede o tempo de execução e imprime a média e desvio padrão dos tempos.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/time.h>
#include <math.h>

// Mescla dois subarrays arr[left..mid] e arr[mid+1..right]
void merge(int *arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    int *L = malloc(n1 * sizeof(int));
    int *R = malloc(n2 * sizeof(int));

    if (!L || !R) { 
        perror("malloc"); 
        exit(EXIT_FAILURE); 
    };

    for (int i = 0; i < n1; i++) {
        L[i] = arr[left + i];
    };

    for (int j = 0; j < n2; j++) {
        R[j] = arr[mid + 1 + j];
    };

    int i = 0, j = 0, k = left;
    
    while (i < n1 && j < n2) {
        arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
    };

    while (i < n1) {
        arr[k++] = L[i++];
    };

    while (j < n2) {
        arr[k++] = R[j++];
    };

    free(L); 
    free(R);
}

// Função recursiva do Merge Sort
void mergeSort(int *arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        merge(arr, left, mid, right);
    }
}

// Retorna tempo atual em segundos (double)
double now() {
    struct timeval tv;
    gettimeofday(&tv, NULL);

    return tv.tv_sec + tv.tv_usec / 1e6;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Uso: %s <tamanho> <num_execucoes>\n", argv[0]);
        return EXIT_FAILURE;
    }

    int tamanho = atoi(argv[1]);
    int num_execucoes = atoi(argv[2]);

    int *data = malloc(tamanho * sizeof(int));

    if (!data) { 
        perror("malloc"); 
        return EXIT_FAILURE;
    };

    srand(time(NULL));
    
    for (int i = 0; i < tamanho; i++) {
        data[i] = rand();
    };

    double *tempos = malloc(num_execucoes * sizeof(double));

    if (!tempos) { 
        perror("malloc"); 
        free(data); 
        
        return EXIT_FAILURE; 
    }

    for (int run = 0; run < num_execucoes; run++) {
        int *arr_copy = malloc(tamanho * sizeof(int));

        memcpy(arr_copy, data, tamanho * sizeof(int));

        double t0 = now();
        mergeSort(arr_copy, 0, tamanho - 1);

        double t1 = now();
        tempos[run] = t1 - t0;

        free(arr_copy);
    };

    double soma = 0.0;

    for (int i = 0; i < num_execucoes; i++) {
        soma += tempos[i];
    };

    double media = soma / num_execucoes;
    double var = 0.0;

    for (int i = 0; i < num_execucoes; i++) {
        var += pow(tempos[i] - media, 2);
    };

    double desvio = sqrt(var / (num_execucoes - 1));

    printf("Tamanho do array: %d\n", tamanho);
    printf("Número de execuções: %d\n", num_execucoes);
    printf("Tempo médio: %.6f\n", media);
    printf("Desvio padrão: %.6f\n", desvio);

    free(data);
    free(tempos);

    return EXIT_SUCCESS;
}
