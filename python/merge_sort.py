"""
merge_sort.py

Implementação do algoritmo Merge Sort em Python.
Uso:
    python merge_sort.py <tamanho> <num_execucoes>

Argumentos:
    tamanho - tamanho do array aleatório a ser gerado
    num_execucoes - número de vezes que o algoritmo será executado para cálculo de tempo médio

O script gera um array aleatório de inteiros, executa o Merge Sort múltiplas vezes,
mede o tempo de execução e imprime a média e desvio padrão dos tempos.
"""

import random
import time
import statistics
import sys

def merge(left, right):
    """
    Mescla dois arrays ordenados (left e right) em um único array ordenado.
    """
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # adiciona o restante
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def merge_sort(arr):
    """
    Função recursiva do Merge Sort.
    Retorna uma nova lista ordenada contendo os elementos de arr.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def main():
    if len(sys.argv) != 3:
        print("Uso: python merge_sort.py <tamanho> <num_execucoes>")
        sys.exit(1)

    tamanho = int(sys.argv[1])
    num_execucoes = int(sys.argv[2])

    # gera array aleatório de inteiros
    data = [random.randint(0, 1_000_000) for _ in range(tamanho)]

    tempos = []
    for _ in range(num_execucoes):
        arr_copy = list(data)  # cópia para não alterar o original
        start = time.perf_counter()
        _ = merge_sort(arr_copy)
        end = time.perf_counter()
        tempos.append(end - start)

    media = statistics.mean(tempos)
    desvio = statistics.stdev(tempos) if len(tempos) > 1 else 0.0

    print(f"Tamanho do array: {tamanho}")
    print(f"Número de execuções: {num_execucoes}")
    print(f"Tempo médio: {media:.6f} segundos")
    print(f"Desvio padrão: {desvio:.6f} segundos")


if __name__ == "__main__":
    main()
