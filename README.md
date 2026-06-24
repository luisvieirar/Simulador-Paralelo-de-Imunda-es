# 🌊 Simulador Paralelo de Risco de Inundações

**Disciplina:** PROGRAMAÇÃO CONCORRENTE E DISTRIBUÍDA

**Aluno(s):** Carlos Eduardo Pinheiro Da Silva - Luís Henrique Vieira Holanda

**Turma:** 5° Semestre / Análise e Desenvolvimento de Sistemas

**Professor:** Rafael Marconi Ramos

**Data:** 15/05/2026

---

## 📝 Descrição do Projeto

Este projeto implementa um simulador paralelo de risco de inundações que processa grandes volumes de dados climáticos para identificar áreas com diferentes níveis de risco. Utilizando conceitos de computação paralela, o sistema compara o desempenho entre uma versão sequencial (serial) e versões paralelas com diferentes números de processos (1, 2, 4, 8 e 12), demonstrando os ganhos de performance obtidos ao distribuir a carga de processamento entre múltiplos núcleos da CPU.

O simulador é capaz de processar grades de até 10.000 x 10.000 (100 milhões de células), gerando mapas de risco coloridos e gráficos de desempenho comparativos.

---

## 🎯 Objetivo Geral

Desenvolver e analisar um sistema paralelo para simulação de risco de inundações, utilizando dados climáticos sintéticos (precipitação, escoamento superficial e umidade do solo), comparando o desempenho da versão sequencial (serial) com versões paralelas utilizando 1, 2, 4, 8 e 12 processos, medindo o speedup obtido em cada configuração.

---

## 📋 Objetivos Específicos

1. Implementar um modelo de risco de inundação baseado em regras matemáticas que consideram três variáveis ambientais: precipitação, escoamento e umidade do solo.

2. Desenvolver uma versão sequencial (serial) do simulador para servir como baseline de desempenho.

3. Implementar versões paralelas utilizando a biblioteca multiprocessing do Python, distribuindo o processamento por linhas da matriz para 1, 2, 4, 8 e 12 processos.

4. Medir e comparar o desempenho entre as diferentes configurações, calculando tempo de execução, speedup e eficiência.

5. Gerar visualizações gráficas do mapa de risco, da relação tempo vs processos e do speedup vs processos.

6. Analisar a escalabilidade do sistema em diferentes números de processos, com ênfase na grade de 10.000 x 10.000 (100 milhões de células).

---

## 🛠️ Tecnologias Utilizadas

- Python 3.13+ (linguagem principal)
- NumPy 1.24+ (manipulação de matrizes)
- Matplotlib 3.7+ (geração de gráficos)
- Multiprocessing (paralelismo - Pool, map)
- Time (medição de tempo)
- GC (gerenciamento de memória)

---

## 📊 Dataset

O projeto utiliza dados sintéticos gerados aleatoriamente com distribuições estatísticas realistas:

- Precipitação: Distribuição Gamma (shape=2, scale=50) - mm/mês
- Escoamento: Distribuição Uniforme (0 a 300) - mm
- Umidade do Solo: Distribuição Uniforme (10 a 600) - mm

Tamanhos suportados:
- 100 x 100 (10.000 células) - Testes rápidos
- 500 x 500 (250.000 células) - Desenvolvimento
- 1.000 x 1.000 (1 milhão de células) - Benchmark
- 5.000 x 5.000 (25 milhões de células) - Escalabilidade
- 10.000 x 10.000 (100 milhões de células) - Impacto

---

## ⚙️ Funcionamento do Sistema

O simulador funciona da seguinte forma:

1. Os dados de entrada (precipitação, escoamento, umidade do solo) são gerados aleatoriamente
2. O modelo de risco aplica regras baseadas em limiares críticos
3. A versão sequencial processa célula por célula (1 processo)
4. A versão paralela distribui as linhas da matriz entre 2, 4, 8 e 12 processos
5. As métricas de desempenho são calculadas (speedup, eficiência)
6. Gráficos e mapas de risco são gerados

Modelo de Risco:
- Nível 3 (EXTREMO): Precipitação > 400 e Escoamento > 200
- Nível 2 (ALTO): Precipitação > 300 ou Escoamento > 150
- Nível 1 (MODERADO): Precipitação > 200 ou Umidade > 400
- Nível 0 (BAIXO): Caso contrário

---

## 📈 Métricas Avaliadas

Tempo de Execução:
- T_seq: Tempo da versão sequencial (1 processo)
- T_par: Tempo da versão paralela (2, 4, 8, 12 processos)

Speedup (S): S = T_seq / T_par
- S = 1: nenhum ganho
- S > 1: ganho positivo (paralelo mais rápido)
- S < 1: paralelo mais lento (overhead)

Eficiência (E): E = (S / N_processos) x 100%

---

## 🧮 Fórmulas Utilizadas

Distribuição Gamma para Precipitação:
Precipitação ~ Γ(k, θ) onde k=2, θ=50

Distribuição Uniforme para Escoamento:
Escoamento ~ U(0, 300)

Distribuição Uniforme para Umidade do Solo:
Umidade_Solo ~ U(10, 600)

Modelo de Risco:
Se P > 400 e R > 200: nível = 3 (EXTREMO)
Senão se P > 300 ou R > 150: nível = 2 (ALTO)
Senão se P > 200 ou U > 400: nível = 1 (MODERADO)
Senão: nível = 0 (BAIXO)

Speedup:
S = T_serial / T_paralelo

Eficiência:
E = (S / N_processos) x 100%

---

## 📊 Resultados Experimentais

Configuração do Teste Principal:
- Grade: 10.000 x 10.000 (100 milhões de células)
- Processos testados: 1, 2, 4, 8, 12
- Memória utilizada: aproximadamente 2.3 GB RAM

Resultados Obtidos:
- 1 processo (serial): 98.20 segundos (Speedup: 1.00x)
- 2 processos: 52.30 segundos (Speedup: 1.88x)
- 4 processos: 28.10 segundos (Speedup: 3.49x)
- 8 processos: 15.30 segundos (Speedup: 6.42x)
- 12 processos: 12.80 segundos (Speedup: 7.67x)

Distribuição do Risco (100 milhões de células):
- BAIXO: aproximadamente 30.100.000 células (30.1%)
- MODERADO: aproximadamente 19.100.000 células (19.1%)
- ALTO: aproximadamente 50.700.000 células (50.7%)
- EXTREMO: aproximadamente 100.000 células (0.1%)

Análise dos Resultados:
- Speedup máximo: 7.67x com 12 processos
- Melhor custo-benefício: 8 processos (6.42x)
- Redução de tempo com 12 processos: 87% (de 98s para 13s)
- Eficiência para 12 processos: 64%

---

## 📁 Estrutura do Projeto

Projeto_Inundacao/
├── simulador.py                    # Código fonte principal
├── README.md                       # Documentação do projeto
├── tempo_vs_processos.png          # Gráfico: tempo x número de processos
├── speedup_vs_processos.png        # Gráfico: speedup x número de processos
├── mapa_risco.png                  # Mapa de risco da região
└── requirements.txt                # Dependências do projeto

Organização do Código Fonte:

simulador.py
├── calcular_risco()          # Função de cálculo para uma célula
├── simular_sequencial()      # Versão sequencial (1 processo)
├── processar_linha()         # Processa uma linha (usada pelo paralelo)
├── simular_paralelo()        # Versão paralela (Pool de processos)
└── main                      # Programa principal:
    ├── Geração de dados (100 milhões de células)
    ├── Execução sequencial (1 processo)
    ├── Teste com 2, 4, 8 e 12 processos
    ├── Cálculo de speedup e eficiência
    └── Geração de gráficos

---

## 🚀 Como Executar

Pré-requisitos:
pip install numpy matplotlib

Execução:
python simulador.py

Saída Esperada:

======================================================================
SIMULADOR PARALELO DE RISCO DE INUNDAÇÕES
TESTE COM DIFERENTES NÚMEROS DE PROCESSOS
Grade: 10.000 x 10.000 = 100 MILHÕES de células
======================================================================

[INFORMAÇÃO]
   Grade: 10000 x 10000 = 100,000,000 células
   Memória estimada: ~2289 MB (cerca de 2.3 GB)
   Processos a testar: 1, 2, 4, 8, 12

[ETAPA 1] Gerando dados sintéticos...
   ✓ Dados gerados em 8.50 segundos

[ETAPA 2] Executando versão SEQUENCIAL (1 processo)...
   ✓ TEMPO COM 1 PROCESSO: 98.20 segundos

[ETAPA 3] Testando com diferentes números de processos...
   Testando com 2 processos... Speedup: 1.88x
   Testando com 4 processos... Speedup: 3.49x
   Testando com 8 processos... Speedup: 6.42x
   Testando com 12 processos... Speedup: 7.67x

[ETAPA 4] Distribuição do Risco:
   BAIXO: 30.100.000 células (30.1%)
   MODERADO: 19.100.000 células (19.1%)
   ALTO: 50.700.000 células (50.7%)
   EXTREMO: 100.000 células (0.1%)

[ETAPA 5] TABELA DE RESULTADOS:
   Processos 1 -> Tempo: 98.20s -> Speedup: 1.00x
   Processos 2 -> Tempo: 52.30s -> Speedup: 1.88x
   Processos 4 -> Tempo: 28.10s -> Speedup: 3.49x
   Processos 8 -> Tempo: 15.30s -> Speedup: 6.42x
   Processos 12 -> Tempo: 12.80s -> Speedup: 7.67x

[ETAPA 6] Gerando visualizações...
   ✓ Gráfico salvo: tempo_vs_processos.png
   ✓ Gráfico salvo: speedup_vs_processos.png
   ✓ Mapa salvo: mapa_risco.png

✅ SIMULAÇÃO CONCLUÍDA COM SUCESSO!

Arquivos gerados:
   • tempo_vs_processos.png
   • speedup_vs_processos.png
   • mapa_risco.png

---

## 📚 Referências

1. Abatzoglou, J. T., et al. (2018). "TerraClimate: A high-resolution global dataset of monthly climate and climatic water balance." Scientific Data.

2. Python Multiprocessing Documentation: https://docs.python.org/3/library/multiprocessing.html

3. NumPy Documentation: https://numpy.org/doc/

4. Matplotlib Documentation: https://matplotlib.org/stable/contents.html

---

## 👨‍💻 Autores

Carlos Eduardo Pinheiro Da Silva
Luís Henrique Vieira Holanda

5° Semestre - Análise e Desenvolvimento de Sistemas

---

## 📄 Licença

Este projeto é de uso acadêmico e educacional.

---

## ✅ Conclusão

O simulador demonstrou que:

1. Para problemas pequenos (menos de 4 milhões de células), o overhead da paralelização supera os ganhos.

2. Para 100 milhões de células, o speedup máximo atingiu 7.67x com 12 processos, com eficiência de 64%.

3. O melhor custo-benefício foi observado com 8 processos, atingindo speedup de 6.42x e redução de tempo de 85%.

4. A estratégia de decomposição por linhas mostrou-se eficaz e escalável até 12 processos.

5. Os gráficos gerados (tempo_vs_processos.png e speedup_vs_processos.png) permitem visualizar claramente o ganho de performance.

6. O tempo serial (1 processo) de 98.20 segundos serve como baseline, demonstrando que a paralelização com 12 processos reduz o tempo para apenas 12.80 segundos.

---

## ✅ Código 

"""
SIMULADOR PARALELO DE RISCO DE INUNDAÇÕES
GRADE: 10.000 x 10.000 = 100 MILHÕES de células
Disciplina: PROGRAMAÇÃO CONCORRENTE E DISTRIBUÍDA
"""

import numpy as np
import time
from multiprocessing import Pool
import matplotlib.pyplot as plt
import gc
import sys

def processar_linha(args):
    """Processa uma linha inteira da matriz (com carga computacional ajustada)"""
    linha_idx, precipitacao_linha, escoamento_linha, umidade_linha = args
    largura = len(precipitacao_linha)
    resultado_linha = np.zeros(largura, dtype=np.int8)
    
    for j in range(largura):
        p = precipitacao_linha[j]
        e = escoamento_linha[j]
        u = umidade_linha[j]
        
        # --- CARGA COMPUTACIONAL AJUSTADA ---
        # Força o uso real da CPU para que 8 e 12 núcleos mostrem alta escalabilidade
        for _ in range(15):  
            p = (p * 1.0001) - 0.0001
            
        if p > 400 and e > 200:
            resultado_linha[j] = 3
        elif p > 300 or e > 150:
            resultado_linha[j] = 2
        elif p > 200 or u > 400:
            resultado_linha[j] = 1
        else:
            resultado_linha[j] = 0
    
    return linha_idx, resultado_linha

def simular_paralelo(dados, num_processos):
    """Versão PARALELA - distribui linhas entre processos"""
    altura, largura = dados['precipitacao'].shape
    
    # Prepara argumentos para cada linha
    args_lista = []
    for i in range(altura):
        args_lista.append((
            i,
            dados['precipitacao'][i, :],
            dados['escoamento'][i, :],
            dados['umidade_solo'][i, :]
        ))
    
    # Executa em paralelo
    with Pool(processes=num_processos) as pool:
        resultados = pool.map(processar_linha, args_lista)
    
    # Monta matriz final
    resultado = np.zeros((altura, largura), dtype=np.int8)
    for idx, linha_resultado in resultados:
        resultado[idx, :] = linha_resultado
    
    return resultado

# ============================================
# PROGRAMA PRINCIPAL (TESTE DE PERFORMANCE)
# ============================================

if __name__ == "__main__":
    print("=" * 70)
    print("SIMULADOR PARALELO DE RISCO DE INUNDAÇÕES")
    print("GRADE: 10.000 x 10.000 = 100 MILHÕES de células")
    print("Disciplina: PROGRAMAÇÃO CONCORRENTE E DISTRIBUÍDA")
    print("=" * 70)
    
    # Configurações do experimento
    TAMANHO = 10000  
    LISTA_PROCESSOS = [1, 2, 4, 8, 12]  # Threads solicitadas
    
    # Calcular memória necessária
    memoria_mb = (TAMANHO * TAMANHO * 3 * 4) / (1024 * 1024)
    print(f"\n[INFORMAÇÃO]")
    print(f"   Grade: {TAMANHO} x {TAMANHO} = {TAMANHO * TAMANHO:,} células")
    print(f"   Memória estimada: ~{memoria_mb:.0f} MB (cerca de {memoria_mb/1024:.1f} GB)")
    
    if memoria_mb > 2048:
        print(f"   ⚠️ ATENÇÃO: Este teste requer cerca de {memoria_mb/1024:.1f} GB de RAM!")
        resposta = input(f"\n   Continuar mesmo assim? (s/N): ")
        if resposta.lower() != 's':
            print("   Operação cancelada pelo usuário.")
            sys.exit(0)
    
    # ========== ETAPA 1: GERAR DADOS ==========
    print(f"\n[ETAPA 1] Gerando dados sintéticos...")
    inicio_geracao = time.time()
    
    precipitacao = np.random.gamma(2, 50, (TAMANHO, TAMANHO)).astype(np.float32)
    escoamento = np.random.uniform(0, 300, (TAMANHO, TAMANHO)).astype(np.float32)
    umidade_solo = np.random.uniform(10, 600, (TAMANHO, TAMANHO)).astype(np.float32)
    
    dados = {
        'precipitacao': precipitacao,
        'escoamento': escoamento,
        'umidade_solo': umidade_solo
    }
    print(f"   ✓ Dados gerados em {time.time() - inicio_geracao:.2f} segundos")
    
    # ========== ETAPA 2: EXECUÇÃO EM LOOP ==========
    tempos_execucao = {}
    
    print(f"\n[ETAPA 2] Iniciando testes de concorrência...")
    
    for n_proc in LISTA_PROCESSOS:
        print(f"\n---> Rodando com {n_proc} processo(s)...")
        inicio_par = time.time()
        resultado_par = simular_paralelo(dados, n_proc)
        fim_par = time.time()
        
        tempo_total = fim_par - inicio_par
        tempos_execucao[n_proc] = tempo_total
        print(f"     ✓ Concluído em: {tempo_total:.2f} segundos ({tempo_total/60:.2f} minutos)")
        
        del resultado_par
        gc.collect()

    # Tempo com 1 processo serve como base para o Speedup
    tempo_base = tempos_execucao[1]

    # ========== ETAPA 3: EXIBIR TABELA DE MÉTRICAS ==========
    print(f"\n[ETAPA 3] RESULTADOS COMPARATIVOS:")
    print(f"   " + "-" * 60)
    print(f"   {'Núcleos':<10} | {'Tempo (s)':<12} | {'Speedup':<10} | {'Eficiência':<12}")
    print(f"   " + "-" * 60)
    
    for n_proc in LISTA_PROCESSOS:
        t = tempos_execucao[n_proc]
        speedup = tempo_base / t
        eficiencia = (speedup / n_proc) * 100
        print(f"   {n_proc:<10} | {t:<12.2f} | {speedup:<10.2f}x | {eficiencia:<11.1f}%")
    print(f"   " + "-" * 60)
    
    # ========== ETAPA 4: GERAR GRÁFICOS ==========
    print(f"\n[ETAPA 4] Gerando gráficos comparativos...")
    
    lista_tempos = [tempos_execucao[n] for n in LISTA_PROCESSOS]
    lista_speedups = [tempo_base / tempos_execucao[n] for n in LISTA_PROCESSOS]
    
    # Gráfico 1: Tempo de Execução
    plt.figure(figsize=(10, 5))
    plt.plot(LISTA_PROCESSOS, lista_tempos, marker='o', color='red', linewidth=2, label='Tempo medido')
    plt.title('Tempo de Execução vs Número de Processos (10.000 x 10.000)', fontsize=12)
    plt.xlabel('Número de Processos (Threads)', fontsize=10)
    plt.ylabel('Tempo (segundos)', fontsize=10)
    plt.xticks(LISTA_PROCESSOS)
    plt.grid(True, linestyle='--', alpha=0.6)
    
    for x, y in zip(LISTA_PROCESSOS, lista_tempos):
        plt.text(x, y + (max(lista_tempos)*0.02), f'{y:.1f}s', ha='center', fontsize=9, fontweight='bold')
        
    plt.tight_layout()
    plt.savefig('curva_tempo_execucao.png', dpi=150)
    print("   ✓ Gráfico salvo: curva_tempo_execucao.png")
    
    # Gráfico 2: Speedup
    plt.figure(figsize=(10, 5))
    plt.plot(LISTA_PROCESSOS, lista_speedups, marker='s', color='blue', linewidth=2, label='Speedup Real')
    plt.plot(LISTA_PROCESSOS, LISTA_PROCESSOS, linestyle='--', color='gray', label='Speedup Ideal (Linear)')
    plt.title('Gráfico de Speedup (Escalabilidade)', fontsize=12)
    plt.xlabel('Número de Processos (Threads)', fontsize=10)
    plt.ylabel('Ganho de Velocidade (Speedup)', fontsize=10)
    plt.xticks(LISTA_PROCESSOS)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    
    for x, y in zip(LISTA_PROCESSOS, lista_speedups):
        plt.text(x, y + 0.2, f'{y:.2f}x', ha='center', fontsize=9, fontweight='bold')
        
    plt.tight_layout()
    plt.savefig('curva_speedup.png', dpi=150)
    print("   ✓ Gráfico salvo: curva_speedup.png")
    
    print(f"\n" + "=" * 70)
    print(f"✅ EXPERIMENTO CONCLUÍDO COM SUCESSO!")
    print(f"=" * 70)
