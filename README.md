# Merge Sort – Análise Teórica e Experimental 

## 📑 Objetivo
Investigar o desempenho **teórico** e **empírico** do algoritmo **Merge Sort** em duas linguagens de programação distintas (**Python** e **Java**), produzindo:
1. Slides de apresentação (Entrega 1).  
2. Relatório técnico em PDF contendo análise completa (Entrega 2).  
3. Código‑fonte totalmente reprodutível, scripts de benchmark e resultados.


## 🧩 Algoritmo estudado  
**Merge Sort** (von Neumann, 1945) é um algoritmo de ordenação **estável** baseado na estratégia *divide‑and‑conquer*:

1. **Dividir** o vetor em duas metades recursivamente;  
2. **Ordenar** cada metade;  
3. **Mesclar** as subsequências ordenadas em um único vetor ordenado.

### Complexidade Assintótica  

| Caso | Comparações / Movimentos | Classe |
|------|-------------------------|--------|
| Melhor | ≈ *n log n* | Ω(*n log n*) |
| Médio  | *n log n*  | Θ(*n log n*) |
| Pior   | *n log n*  | 𝑂(*n log n*) |
| Espaço | — | 𝑂(*n*) |

---

## 🔧 Aplicações Práticas  

| Cenário | Justificativa |
|---------|---------------|
| **Grandes arquivos externos** | Permite ordenação em disco, mesclando blocos em streaming. |
| **Listas ligadas** | A fusão pode ser feita por ponteiros, dispensando cópias extras. |
| **Sistemas que exigem estabilidade** | Mantém a ordem relativa de elementos iguais — essencial em rotinas de classificação múltipla. |
| **Paralelismo** | As chamadas recursivas são independentes, facilitando implementação paralela em múltiplos núcleos. |

⚠️ **Limitações**: uso de memória extra (𝑂(*n*)) torna‑o menos indicado em ambientes embarcados ou sistemas com RAM restrita.

---
