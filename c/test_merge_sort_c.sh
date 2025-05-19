#!/usr/bin/env bash
#
# test_merge_sort_c.sh
# Compila e testa o Merge Sort em C para vários tamanhos de entrada,
# salvando um CSV com ID único em c/tests.

# Sai na primeira falha
set -e

# Diretorios
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TESTS_DIR="${SCRIPT_DIR}/tests"
mkdir -p "${TESTS_DIR}"

# Gera ID único (requere uuidgen)
if ! command -v uuidgen &> /dev/null; then
    echo "Por favor instale uuidgen ou ajuste o generator de ID."
    exit 1
fi
RUN_ID="$(uuidgen | tr -d '-')"

# Arquivo de saída
OUTPUT_CSV="${TESTS_DIR}/${RUN_ID}.csv"

# Compilação
gcc -O2 -o "${SCRIPT_DIR}/merge_sort" "${SCRIPT_DIR}/merge_sort.c"

# Configurações de teste
declare -a TAMANHOS=(1000 5000 10000 20000 50000)
NUM_EXECUCOES=20

# Cabeçalho CSV
echo "tamanho,media_s,desvio_s" > "${OUTPUT_CSV}"

# Execução dos testes
for n in "${TAMANHOS[@]}"; do
    echo "Testando C Merge Sort com n=${n}..."
    RESULTADOS=$("${SCRIPT_DIR}/merge_sort" "${n}" "${NUM_EXECUCOES}")
    MEDIA=$(echo "${RESULTADOS}" | awk -F": " '/Tempo médio/ {print $2}')
    DESVIO=$(echo "${RESULTADOS}" | awk -F": " '/Desvio padrão/ {print $2}')
    echo "${n},${MEDIA},${DESVIO}" >> "${OUTPUT_CSV}"
done

echo "Resultados salvos em ${OUTPUT_CSV}"
