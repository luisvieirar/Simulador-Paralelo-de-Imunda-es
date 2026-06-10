# 🌊 Simulador Paralelo de Risco de Inundações

**Disciplina:** PROGRAMAÇÃO CONCORRENTE E DISTRIBUÍDA

**Aluno(s):** Carlos Eduardo Pinheiro Da Silva - Luís Henrique Vieira Holanda

**Turma:** 5° Semestre / Análise e Desenvolvimento de Sistemas

**Professor:** Rafael Marconi Ramos

**Data:** 15/05/2026

---

## 📝 Descrição do Projeto

Este projeto implementa um simulador paralelo de risco de inundações que processa grandes volumes de dados climáticos para identificar áreas com diferentes níveis de risco. Utilizando conceitos de computação paralela, o sistema compara o desempenho entre uma versão sequencial (serial) e uma versão paralela (com multiprocessing), demonstrando os ganhos de performance obtidos ao distribuir a carga de processamento entre múltiplos núcleos da CPU.

O simulador é capaz de processar grades de até 10.000 x 10.000 (100 milhões de células), gerando mapas de risco coloridos e métricas de desempenho detalhadas.

---

## 🎯 Objetivo Geral

Desenvolver e analisar um sistema paralelo para simulação de risco de inundações, utilizando dados climáticos sintéticos (precipitação, escoamento superficial e umidade do solo), comparando o desempenho da versão sequencial (serial) com a versão paralela e medindo o speedup obtido.

---

## 📋 Objetivos Específicos

1. Implementar um modelo de risco de inundação baseado em regras matemáticas que consideram três variáveis ambientais: precipitação, escoamento e umidade do solo.

2. Desenvolver uma versão sequencial (serial) do simulador para servir como baseline de desempenho.

3. Implementar uma versão paralela utilizando a biblioteca multiprocessing do Python, distribuindo o processamento por linhas da matriz.

4. Medir e comparar o desempenho entre as duas versões, calculando métricas como tempo de execução sequencial, tempo de execução paralela, speedup e eficiência.

5. Gerar visualizações gráficas do mapa de risco e da comparação de desempenho.

6. Analisar a escalabilidade do sistema em diferentes tamanhos de grade, com ênfase na grade de 10.000 x 10.000.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.13+ (linguagem principal)
- NumPy 1.24+ (manipulação de matrizes)
- Matplotlib 3.7+ (geração de gráficos)
- Multiprocessing (paralelismo - Pool, map)
- Time (medição de tempo)

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
3. A versão sequencial processa célula por célula (tempo serial)
4. A versão paralela distribui as linhas da matriz entre múltiplos processos
5. As métricas de desempenho são calculadas (speedup, eficiência)
6. Gráficos e mapas de risco são gerados

Modelo de Risco:
- Nível 3 (EXTREMO): Precipitação > 400 e Escoamento > 200
- Nível 2 (ALTO): Precipitação > 300 ou Escoamento > 150
- Nível 1 (MODERADO): Precipitação > 200 ou Umidade > 400
- Nível 0 (BAIXO): Caso contrário

---

## 📈 Métricas Avaliadas

Tempo de Execução (T):
- T_seq: Tempo da versão sequencial (serial)
- T_par: Tempo da versão paralela

Speedup (S): S = T_seq / T_par
- S = 1: nenhum ganho
- S > 1: ganho positivo
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

---

## 📊 Resultados Experimentais

Configuração do Teste Principal:
- Grade: 10.000 x 10.000 (100 milhões de células)
- Processos: 4 núcleos
- Memória utilizada: aproximadamente 2.3 GB RAM

Resultados Obtidos:
- Tempo Serial (Sequencial): 98.20 segundos (1.6 minutos)
- Tempo Paralelo: 15.30 segundos
- Speedup: 6.42x
- Eficiência: 160.5%

Distribuição do Risco (100 milhões de células):
- BAIXO: aproximadamente 30.100.000 células (30.1%)
- MODERADO: aproximadamente 19.100.000 células (19.1%)
- ALTO: aproximadamente 50.700.000 células (50.7%)
- EXTREMO: aproximadamente 100.000 células (0.1%)

Teste de Escalabilidade:
- 500x500 (250k células): Speedup 0.57x
- 1.000x1.000 (1M células): Speedup 0.53x
- 2.000x2.000 (4M células): Speedup 2.67x
- 5.000x5.000 (25M células): Speedup 5.94x
- 10.000x10.000 (100M células): Speedup 6.42x

Conclusão: O paralelismo compensa para grades maiores que 2.000x2.000. Para 100 milhões de células, o speedup atinge 6.42x, representando uma redução de tempo de cerca de 85%.

---

## 📁 Estrutura do Projeto

Projeto_Inundacao/
├── simulador.py                 # Código fonte principal
├── README.md                    # Documentação
├── mapa_risco_10000.png         # Mapa de risco
├── comparacao_desempenho_10000.png  # Gráfico comparativo
├── speedup_10000.png            # Gráfico do speedup
└── requirements.txt             # Dependências

---

## 🚀 Como Executar

1. Instalar as dependências:
   pip install numpy matplotlib

2. Executar o simulador:
   python simulador.py

3. O programa irá:
   - Gerar dados sintéticos (100 milhões de células)
   - Executar a versão sequencial (tempo serial)
   - Executar a versão paralela
   - Calcular speedup e eficiência
   - Salvar os gráficos na pasta do projeto

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

1. Para problemas pequenos (menos de 4 milhões de células), o overhead da paralelização supera os ganhos, resultando em speedup menor que 1.

2. Para problemas grandes (mais de 4 milhões de células), o speedup atinge aproximadamente 6.42x com 4 núcleos na grade de 10.000x10.000 (100 milhões de células), representando uma redução de tempo de cerca de 85%.

3. A estratégia de decomposição por linhas mostrou-se eficaz e escalável.

4. O tempo serial de 98.20 segundos serve como baseline de desempenho, demonstrando claramente o ganho da paralelização.

---

## ✅ Código

"""
SIMULADOR PARALELO DE RISCO DE INUNDAÇÕES
TESTE COM DIFERENTES NÚMEROS DE PROCESSOS: 1, 2, 4, 8, 12
GRADE: 10.000 x 10.000 = 100 MILHÕES de células
"""

import numpy as np
import time
from multiprocessing import Pool
import matplotlib.pyplot as plt
import gc
import sys

def calcular_risco(precipitacao, escoamento, umidade_solo):
    """Calcula nível de risco para uma célula"""
    if precipitacao > 400 and escoamento > 200:
        return 3
    elif precipitacao > 300 or escoamento > 150:
        return 2
    elif precipitacao > 200 or umidade_solo > 400:
        return 1
    else:
        return 0

def simular_sequencial(dados):
    """Versão SEQUENCIAL (1 processo/thread) - TEMPO SERIAL"""
    altura, largura = dados['precipitacao'].shape
    resultado = np.zeros((altura, largura), dtype=np.int8)
    
    for i in range(altura):
        for j in range(largura):
            resultado[i, j] = calcular_risco(
                dados['precipitacao'][i, j],
                dados['escoamento'][i, j],
                dados['umidade_solo'][i, j]
            )
        if (i + 1) % (altura // 10) == 0:
            print(f"      Progresso: {(i+1)/altura*100:.0f}%")
    
    return resultado

def processar_linha(args):
    """Processa uma linha inteira da matriz (usado no paralelo)"""
    linha_idx, precipitacao_linha, escoamento_linha, umidade_linha = args
    largura = len(precipitacao_linha)
    resultado_linha = np.zeros(largura, dtype=np.int8)
    
    for j in range(largura):
        if precipitacao_linha[j] > 400 and escoamento_linha[j] > 200:
            resultado_linha[j] = 3
        elif precipitacao_linha[j] > 300 or escoamento_linha[j] > 150:
            resultado_linha[j] = 2
        elif precipitacao_linha[j] > 200 or umidade_linha[j] > 400:
            resultado_linha[j] = 1
        else:
            resultado_linha[j] = 0
    
    return linha_idx, resultado_linha

def simular_paralelo(dados, num_processos):
    """Versão PARALELA com número específico de processos"""
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
# PROGRAMA PRINCIPAL
# ============================================

if __name__ == "__main__":
    print("=" * 70)
    print("SIMULADOR PARALELO DE RISCO DE INUNDAÇÕES")
    print("TESTE COM DIFERENTES NÚMEROS DE PROCESSOS")
    print("Grade: 10.000 x 10.000 = 100 MILHÕES de células")
    print("=" * 70)
    
    # Configurações
    TAMANHO = 10000  # 10000x10000 = 100 MILHÕES
    PROCESSOS_TESTE = [1, 2, 4, 8, 12]  # Núcleos/processos que o professor pediu
    
    # Calcular memória necessária
    memoria_mb = (TAMANHO * TAMANHO * 3 * 4) / (1024 * 1024)
    print(f"\n[INFORMAÇÃO]")
    print(f"   Grade: {TAMANHO} x {TAMANHO} = {TAMANHO * TAMANHO:,} células")
    print(f"   Memória estimada: ~{memoria_mb:.0f} MB (cerca de {memoria_mb/1024:.1f} GB)")
    print(f"   Processos a testar: {PROCESSOS_TESTE}")
    
    if memoria_mb > 2048:
        print(f"   ⚠️ ATENÇÃO: Este teste requer cerca de {memoria_mb/1024:.1f} GB de RAM!")
        resposta = input(f"\n   Continuar? (s/N): ")
        if resposta.lower() != 's':
            print("   Operação cancelada.")
            sys.exit(0)
    
    # ========== ETAPA 1: GERAR DADOS ==========
    print(f"\n[ETAPA 1] Gerando dados sintéticos (100 milhões de células)...")
    inicio_geracao = time.time()
    
    print(f"   Gerando precipitação...")
    precipitacao = np.random.gamma(2, 50, (TAMANHO, TAMANHO)).astype(np.float32)
    
    print(f"   Gerando escoamento...")
    escoamento = np.random.uniform(0, 300, (TAMANHO, TAMANHO)).astype(np.float32)
    
    print(f"   Gerando umidade do solo...")
    umidade_solo = np.random.uniform(10, 600, (TAMANHO, TAMANHO)).astype(np.float32)
    
    dados = {
        'precipitacao': precipitacao,
        'escoamento': escoamento,
        'umidade_solo': umidade_solo
    }
    
    fim_geracao = time.time()
    print(f"   ✓ Dados gerados em {fim_geracao - inicio_geracao:.2f} segundos")
    
    # ========== ETAPA 2: EXECUÇÃO SEQUENCIAL (1 processo) ==========
    print(f"\n[ETAPA 2] Executando versão SEQUENCIAL (1 processo/thread)...")
    print(f"   Processando {TAMANHO * TAMANHO:,} células...")
    print(f"   ⏱️ Isso pode levar vários minutos...")
    
    inicio_seq = time.time()
    resultado_seq = simular_sequencial(dados)
    fim_seq = time.time()
    TEMPO_1_PROCESSO = fim_seq - inicio_seq
    
    print(f"   ✓ TEMPO COM 1 PROCESSO: {TEMPO_1_PROCESSO:.2f} segundos ({TEMPO_1_PROCESSO/60:.2f} min)")
    
    # ========== ETAPA 3: TESTAR DIFERENTES PROCESSOS ==========
    print(f"\n[ETAPA 3] Testando com diferentes números de processos...")
    
    resultados = []
    resultados.append({'processos': 1, 'tempo': TEMPO_1_PROCESSO, 'speedup': 1.0})
    
    for num_proc in PROCESSOS_TESTE:
        if num_proc == 1:
            continue  # Já executamos
        
        print(f"\n   Testando com {num_proc} processos...")
        inicio_par = time.time()
        resultado_par = simular_paralelo(dados, num_proc)
        fim_par = time.time()
        tempo_par = fim_par - inicio_par
        speedup = TEMPO_1_PROCESSO / tempo_par
        
        resultados.append({
            'processos': num_proc,
            'tempo': tempo_par,
            'speedup': speedup
        })
        
        print(f"      Tempo: {tempo_par:.2f} segundos")
        print(f"      Speedup: {speedup:.2f}x")
        
        # Liberar memória do resultado anterior
        del resultado_par
        gc.collect()
    
    # ========== ETAPA 4: DISTRIBUIÇÃO DO RISCO ==========
    print(f"\n[ETAPA 4] Distribuição do Risco de Inundação:")
    print(f"   " + "-" * 50)
    
    unique, counts = np.unique(resultado_seq, return_counts=True)
    niveis = {0: "🟢 BAIXO", 1: "🟡 MODERADO", 2: "🟠 ALTO", 3: "🔴 EXTREMO"}
    
    for nivel, count in zip(unique, counts):
        percentual = count / (TAMANHO * TAMANHO) * 100
        print(f"   {niveis[nivel]}: {count:>12,} células ({percentual:>6.2f}%)")
    print(f"   " + "-" * 50)
    
    # ========== ETAPA 5: TABELA DE RESULTADOS ==========
    print(f"\n[ETAPA 5] TABELA DE RESULTADOS - Speedup por número de processos:")
    print(f"   " + "=" * 50)
    print(f"   | {'Processos':<10} | {'Tempo (s)':<12} | {'Speedup':<10} |")
    print(f"   " + "-" * 50)
    
    for r in resultados:
        print(f"   | {r['processos']:<10} | {r['tempo']:<12.2f} | {r['speedup']:<10.2f}x |")
    
    print(f"   " + "=" * 50)
    
    # ========== ETAPA 6: GERAR GRÁFICOS ==========
    print(f"\n[ETAPA 6] Gerando visualizações...")
    
    # Gráfico 1: Tempo x Processos
    processos = [r['processos'] for r in resultados]
    tempos = [r['tempo'] for r in resultados]
    
    plt.figure(figsize=(10, 6))
    plt.plot(processos, tempos, 'bo-', linewidth=2, markersize=10)
    plt.xlabel('Número de Processos/Threads', fontsize=12)
    plt.ylabel('Tempo de Execução (segundos)', fontsize=12)
    plt.title(f'Tempo de Execução vs Número de Processos\nGrade: 10.000x10.000 (100M células)', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.xticks(processos)
    
    for i, (proc, tempo) in enumerate(zip(processos, tempos)):
        plt.annotate(f'{tempo:.1f}s', (proc, tempo), textcoords="offset points", xytext=(0,10), ha='center')
    
    plt.tight_layout()
    plt.savefig('tempo_vs_processos.png', dpi=150)
    print(f"   ✓ Gráfico salvo: tempo_vs_processos.png")
    
    # Gráfico 2: Speedup x Processos
    speedups = [r['speedup'] for r in resultados]
    
    plt.figure(figsize=(10, 6))
    plt.plot(processos, speedups, 'go-', linewidth=2, markersize=10, label='Speedup Obtido')
    plt.plot(processos, processos, 'r--', linewidth=2, label='Speedup Ideal (linear)')
    plt.xlabel('Número de Processos/Threads', fontsize=12)
    plt.ylabel('Speedup', fontsize=12)
    plt.title(f'Speedup vs Número de Processos\nGrade: 10.000x10.000 (100M células)', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(processos)
    
    for i, (proc, sp) in enumerate(zip(processos, speedups)):
        plt.annotate(f'{sp:.2f}x', (proc, sp), textcoords="offset points", xytext=(0,10), ha='center')
    
    plt.tight_layout()
    plt.savefig('speedup_vs_processos.png', dpi=150)
    print(f"   ✓ Gráfico salvo: speedup_vs_processos.png")
    
    # Gráfico 3: Mapa de Risco (amostragem)
    fator_amostragem = 100
    amostra = resultado_seq[::fator_amostragem, ::fator_amostragem]
    
    plt.figure(figsize=(12, 10))
    im = plt.imshow(amostra, cmap='YlOrRd', interpolation='nearest', vmin=0, vmax=3)
    plt.colorbar(im, ticks=[0, 1, 2, 3], label='Nível de Risco')
    plt.title(f'Mapa de Risco de Inundação - 10.000x10.000\nSpeedup Máximo: {max(speedups):.2f}x com {processos[speedups.index(max(speedups))]} processos', fontsize=14)
    plt.xlabel('Longitude (pixels)', fontsize=12)
    plt.ylabel('Latitude (pixels)', fontsize=12)
    plt.tight_layout()
    plt.savefig('mapa_risco.png', dpi=150)
    print(f"   ✓ Mapa salvo: mapa_risco.png")
    
    # ========== RESULTADO FINAL ==========
    print(f"\n" + "=" * 70)
    print(f"✅ SIMULAÇÃO CONCLUÍDA COM SUCESSO!")
    print(f"=" * 70)
    print(f"\n📊 RESUMO DOS RESULTADOS - GRADE 10.000x10.000:")
    print(f"   • Total de células: {TAMANHO * TAMANHO:,} (100 milhões)")
    print(f"   • Tempo com 1 processo (serial): {TEMPO_1_PROCESSO:.2f} s ({TEMPO_1_PROCESSO/60:.1f} min)")
    
    melhor = max(resultados, key=lambda x: x['speedup'])
    print(f"   • Melhor Speedup: {melhor['speedup']:.2f}x com {melhor['processos']} processos")
    
    print(f"\n📁 Arquivos gerados:")
    print(f"   • tempo_vs_processos.png")
    print(f"   • speedup_vs_processos.png")
    print(f"   • mapa_risco.png")
    print(f"\n" + "=" * 70)
    
    # Liberar memória
    gc.collect()
