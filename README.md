# 🧠 Merge Sort — Análise Teórica e Experimental

**Integrantes:** Guilherme Alencar, Henrique Lobo e Luiz Felipe Soriano

---

## 📑 Objetivo

Analisar de forma **teórica** e **empírica** o comportamento do algoritmo **Merge Sort** utilizando duas linguagens de programação distintas: **C** (baixo nível, compilada) e **Python** (alto nível, interpretada). O projeto contempla:

1. 📄 Um **relatório técnico completo** em PDF (Entrega 2), contendo análise de complexidade, desempenho, aplicabilidade prática e reflexões finais.
2. 💻 Código‑fonte reprodutível, com scripts automatizados de benchmark e geração de gráficos.

---

## 🧩 Algoritmo Estudado

**Merge Sort** (proposto por John von Neumann, 1945) é um algoritmo de ordenação **estável** que utiliza a estratégia *Divide and Conquer*:

1. **Dividir:** o array é recursivamente dividido ao meio;
2. **Ordenar:** cada metade é ordenada de forma independente;
3. **Mesclar:** os subarrays ordenados são combinados em um único array final.

### 🔢 Complexidade Assintótica

| Caso   | Comparações / Movimentos | Classe        |
|--------|--------------------------|---------------|
| Melhor | ≈ *n log n*              | Ω(*n log n*)  |
| Médio  | *n log n*                | Θ(*n log n*)  |
| Pior   | *n log n*                | O(*n log n*)  |
| Espaço | —                        | O(*n*)        |

---

## 🔧 Aplicações Práticas

| Cenário                              | Justificativa                                                                                      |
|--------------------------------------|------------------------------------------------------------------------------------------------------|
| **Grandes arquivos externos**        | Permite ordenação em disco, mesclando blocos em streaming com uso eficiente de memória.              |
| **Listas ligadas**                   | A mesclagem pode ser feita apenas com ponteiros, dispensando cópias adicionais.                     |
| **Sistemas que exigem estabilidade** | Mantém a ordem relativa entre elementos com chaves iguais, essencial em ordenações múltiplas.       |
| **Paralelismo**                      | Divisões recursivas são independentes, facilitando a execução paralela em múltiplos núcleos.        |

⚠️ **Limitação:** o uso de memória adicional O(n) pode ser um entrave em sistemas com recursos restritos.

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
