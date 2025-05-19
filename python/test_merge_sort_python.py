"""
test_merge_sort_python.py

Script para testar o desempenho do Merge Sort em Python
para diferentes tamanhos de entrada. Gera CSV com os resultados.
"""

import subprocess
import csv
import os
import sys
import uuid

# Configurações
tamanhos = [1000, 5000, 10000, 20000, 50000]
num_execucoes = 20
python_script = "merge_sort.py"

# Define diretórios
base_dir = os.path.dirname(os.path.abspath(__file__))
tests_dir = os.path.join(base_dir, "tests")
os.makedirs(tests_dir, exist_ok=True)

# Gera ID único para o teste
run_id = uuid.uuid4().hex
output_csv = os.path.join(tests_dir, f"{run_id}.csv")

# Cabeçalho CSV
with open(output_csv, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["tamanho", "media_s", "desvio_s"])

# Executa testes
for n in tamanhos:
    print(f"Testando Python Merge Sort com n={n}...")
    cmd = ["python3", python_script, str(n), str(num_execucoes)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    saida = proc.stdout.splitlines()
    # extrai média e desvio padrão
    media = float(saida[-2].split(":")[1].split()[0])
    desvio = float(saida[-1].split(":")[1].split()[0])
    # grava no CSV
    with open(output_csv, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([n, f"{media:.6f}", f"{desvio:.6f}"])
    print(f"→ média={media:.6f}s | desvio={desvio:.6f}s")

print(f"Resultados em {output_csv}")
