# Merge Sort – Análise Teórica e Experimental

Integrantes : Guilherme Alencar, Henrique Lobo e Luiz Felipe Soriano

## 📑 Objetivo

Investigar o desempenho **teórico** e **empírico** do algoritmo **Merge Sort** em duas linguagens de programação distintas (**Python** e **C**), produzindo:

1. Slides de apresentação (Entrega 1).
2. Relatório técnico em PDF contendo análise completa (Entrega 2).
3. Código‑fonte totalmente reprodutível, scripts de benchmark e resultados.

## 🧩 Algoritmo estudado

**Merge Sort** (von Neumann, 1945) é um algoritmo de ordenação **estável** baseado na estratégia *divide‑and‑conquer*:

1. **Dividir** o vetor em duas metades recursivamente;
2. **Ordenar** cada metade;
3. **Mesclar** as subsequências ordenadas em um único vetor ordenado.

### Complexidade Assintótica

| Caso   | Comparações / Movimentos | Classe        |
| ------ | ------------------------ | ------------- |
| Melhor | ≈ *n log n*              | Ω(*n log n*)  |
| Médio  | *n log n*                | Θ(*n log n*)  |
| Pior   | *n log n*                | 𝑂(*n log n*) |
| Espaço | —                        | 𝑂(*n*)       |

---

## 🔧 Aplicações Práticas

| Cenário                              | Justificativa                                                                                      |
| ------------------------------------ | -------------------------------------------------------------------------------------------------- |
| **Grandes arquivos externos**        | Permite ordenação em disco, mesclando blocos em streaming.                                         |
| **Listas ligadas**                   | A fusão pode ser feita por ponteiros, dispensando cópias extras.                                   |
| **Sistemas que exigem estabilidade** | Mantém a ordem relativa de elementos iguais — essencial em rotinas de classificação múltipla.      |
| **Paralelismo**                      | As chamadas recursivas são independentes, facilitando implementação paralela em múltiplos núcleos. |

⚠️ **Limitações**: uso de memória extra (𝑂(*n*)) torna‑o menos indicado em ambientes embarcados ou sistemas com RAM restrita.

---

## 🚀 Como executar os scripts de benchmark

A seguir, o passo a passo para compilar e rodar os testes em Python e C, incluindo geração dos CSVs de resultados.

### 1. Benchmark em Python

1. Navegue até a pasta do código Python:

   ```bash
   cd python/
   ```
2. Certifique-se de ter o `merge_sort.py` e `test_merge_sort_python.py` na pasta.
3. Execute o script de teste:

   ```bash
   python3 test_merge_sort_python.py
   ```
4. Ao final, será criada a pasta `python/tests/` com um arquivo `<run_id>.csv` contendo as colunas:

   * `tamanho`: tamanho do array testado
   * `media_s`: tempo médio em segundos
   * `desvio_s`: desvio-padrão em segundos

### 2. Benchmark em C

1. Navegue até a pasta do código em C:

   ```bash
   cd c/
   ```
2. Certifique-se de ter `merge_sort.c` e `test_merge_sort_c.sh` na pasta.
3. Torne o script executável (se ainda não fez):

   ```bash
   chmod +x test_merge_sort_c.sh
   ```
4. Execute o script de teste:

   ```bash
   ./test_merge_sort_c.sh
   ```
5. Ao final, será criada a pasta `c/tests/` com um arquivo `<RUN_ID>.csv` contendo as colunas:

   * `tamanho`: tamanho do array testado
   * `media_s`: tempo médio em segundos
   * `desvio_s`: desvio-padrão em segundos

Pronto! Agora você possui os resultados empíricos para comparar o desempenho do Merge Sort em Python e C.
