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
    """Versão SEQUENCIAL - processa célula por célula (TEMPO SERIAL)"""
    altura, largura = dados['precipitacao'].shape
    resultado = np.zeros((altura, largura), dtype=np.int8)
    
    for i in range(altura):
        for j in range(largura):
            resultado[i, j] = calcular_risco(
                dados['precipitacao'][i, j],
                dados['escoamento'][i, j],
                dados['umidade_solo'][i, j]
            )
        # Feedback a cada 10% do processamento
        if (i + 1) % (altura // 10) == 0:
            print(f"      Progresso sequencial: {(i+1)/altura*100:.0f}%")
    
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
# PROGRAMA PRINCIPAL
# ============================================

if __name__ == "__main__":
    print("=" * 70)
    print("SIMULADOR PARALELO DE RISCO DE INUNDAÇÕES")
    print("GRADE: 10.000 x 10.000 = 100 MILHÕES de células")
    print("Disciplina: PROGRAMAÇÃO CONCORRENTE E DISTRIBUÍDA")
    print("=" * 70)
    
    # Configurações
    TAMANHO = 10000  # 10000x10000 = 100 MILHÕES de células
    NUM_PROCESSOS = 4  # Número de núcleos para versão paralela
    
    # Calcular memória necessária
    memoria_mb = (TAMANHO * TAMANHO * 3 * 4) / (1024 * 1024)  # 3 matrizes de float32
    print(f"\n[INFORMAÇÃO]")
    print(f"   Grade: {TAMANHO} x {TAMANHO} = {TAMANHO * TAMANHO:,} células")
    print(f"   Processos: {NUM_PROCESSOS} núcleos")
    print(f"   Memória estimada: ~{memoria_mb:.0f} MB (cerca de {memoria_mb/1024:.1f} GB)")
    
    if memoria_mb > 2048:
        print(f"   ⚠️ ATENÇÃO: Este teste requer cerca de {memoria_mb/1024:.1f} GB de RAM!")
        print(f"   ⚠️ Pode demorar vários minutos e consumir muita memória.")
        resposta = input(f"\n   Continuar mesmo assim? (s/N): ")
        if resposta.lower() != 's':
            print("   Operação cancelada pelo usuário.")
            sys.exit(0)
    
    # ========== ETAPA 1: GERAR DADOS ==========
    print(f"\n[ETAPA 1] Gerando dados sintéticos...")
    print(f"   Isso pode levar alguns segundos/minutos...")
    inicio_geracao = time.time()
    
    # Gerar dados com float32 para economizar memória
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
    
    # ========== ETAPA 2: EXECUÇÃO SEQUENCIAL (TEMPO SERIAL) ==========
    print(f"\n[ETAPA 2] Executando versão SEQUENCIAL (TEMPO SERIAL)...")
    print(f"   Processando {TAMANHO * TAMANHO:,} células...")
    print(f"   ⏱️ Isso pode levar vários minutos...")
    
    inicio_seq = time.time()
    resultado_seq = simular_sequencial(dados)
    fim_seq = time.time()
    TEMPO_SEQUENCIAL = fim_seq - inicio_seq
    
    print(f"   ✓ TEMPO SEQUENCIAL (SERIAL): {TEMPO_SEQUENCIAL:.2f} segundos")
    print(f"   ({TEMPO_SEQUENCIAL/60:.2f} minutos)")
    
    # ========== ETAPA 3: EXECUÇÃO PARALELA ==========
    print(f"\n[ETAPA 3] Executando versão PARALELA ({NUM_PROCESSOS} processos)...")
    print(f"   ⏱️ Isso pode levar alguns minutos...")
    
    inicio_par = time.time()
    resultado_par = simular_paralelo(dados, NUM_PROCESSOS)
    fim_par = time.time()
    TEMPO_PARALELO = fim_par - inicio_par
    
    print(f"   ✓ TEMPO PARALELO: {TEMPO_PARALELO:.2f} segundos")
    print(f"   ({TEMPO_PARALELO/60:.2f} minutos)")
    
    # ========== ETAPA 4: CÁLCULO DAS MÉTRICAS ==========
    print(f"\n[ETAPA 4] MÉTRICAS DE DESEMPENHO:")
    print(f"   " + "-" * 50)
    print(f"   Tempo Sequencial (Serial):  {TEMPO_SEQUENCIAL:.2f} s")
    print(f"   Tempo Paralelo:            {TEMPO_PARALELO:.2f} s")
    
    SPEEDUP = TEMPO_SEQUENCIAL / TEMPO_PARALELO
    EFICIENCIA = (SPEEDUP / NUM_PROCESSOS) * 100
    
    print(f"   SPEEDUP:                   {SPEEDUP:.2f}x")
    print(f"   Eficiência:                {EFICIENCIA:.1f}%")
    print(f"   Economia de tempo:         {TEMPO_SEQUENCIAL - TEMPO_PARALELO:.2f} s")
    print(f"   " + "-" * 50)
    
    # ========== ETAPA 5: DISTRIBUIÇÃO DO RISCO ==========
    print(f"\n[ETAPA 5] DISTRIBUIÇÃO DO RISCO DE INUNDAÇÃO:")
    print(f"   " + "-" * 50)
    
    unique, counts = np.unique(resultado_seq, return_counts=True)
    niveis = {0: "🟢 BAIXO", 1: "🟡 MODERADO", 2: "🟠 ALTO", 3: "🔴 EXTREMO"}
    
    for nivel, count in zip(unique, counts):
        percentual = count / (TAMANHO * TAMANHO) * 100
        print(f"   {niveis[nivel]}: {count:>12,} células ({percentual:>6.2f}%)")
    print(f"   " + "-" * 50)
    
    # ========== ETAPA 6: GERAR GRÁFICOS ==========
    print(f"\n[ETAPA 6] Gerando visualizações...")
    
    # Amostragem para visualização (1 ponto a cada 100)
    fator_amostragem = 100
    tamanho_amostra = TAMANHO // fator_amostragem
    amostra = resultado_seq[::fator_amostragem, ::fator_amostragem]
    
    print(f"   Gerando mapa de risco (amostragem {fator_amostragem}x)...")
    plt.figure(figsize=(12, 10))
    im = plt.imshow(amostra, cmap='YlOrRd', interpolation='nearest', vmin=0, vmax=3)
    cbar = plt.colorbar(im, ticks=[0, 1, 2, 3])
    cbar.set_label('Nível de Risco', fontsize=12)
    plt.title(f'Mapa de Risco de Inundação - 10.000x10.000\n'
              f'Tempo Serial: {TEMPO_SEQUENCIAL:.1f}s | Speedup: {SPEEDUP:.2f}x',
              fontsize=14)
    plt.xlabel('Longitude (pixels)', fontsize=12)
    plt.ylabel('Latitude (pixels)', fontsize=12)
    plt.tight_layout()
    plt.savefig('mapa_risco_10000.png', dpi=150)
    print(f"   ✓ Mapa salvo: mapa_risco_10000.png")
    
    # Gráfico de comparação
    print(f"   Gerando gráfico de comparação...")
    plt.figure(figsize=(10, 6))
    bars = plt.bar(['Sequencial (Serial)', f'Paralelo ({NUM_PROCESSOS} núcleos)'], 
                   [TEMPO_SEQUENCIAL, TEMPO_PARALELO], 
                   color=['#ff6b6b', '#51cf66'], 
                   edgecolor='black', linewidth=1.5)
    plt.ylabel('Tempo de Execução (segundos)', fontsize=12)
    plt.title(f'Comparação de Desempenho - Grade 10.000x10.000', fontsize=14)
    plt.grid(axis='y', alpha=0.3)
    
    for bar, tempo in zip(bars, [TEMPO_SEQUENCIAL, TEMPO_PARALELO]):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
                 f'{tempo:.1f}s\n({tempo/60:.1f}min)', 
                 ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('comparacao_desempenho_10000.png', dpi=150)
    print(f"   ✓ Gráfico salvo: comparacao_desempenho_10000.png")
    
    # Gráfico de Speedup
    print(f"   Gerando gráfico de speedup...")
    plt.figure(figsize=(8, 6))
    plt.bar(['Speedup Obtido'], [SPEEDUP], color=['#4dabf7'], edgecolor='black', linewidth=1.5)
    plt.axhline(y=NUM_PROCESSOS, color='r', linestyle='--', linewidth=2, label=f'Ideal ({NUM_PROCESSOS}x)')
    plt.ylabel('Speedup', fontsize=12)
    plt.title(f'Ganho de Performance - 10.000x10.000', fontsize=14)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.text(0, SPEEDUP + 0.5, f'{SPEEDUP:.2f}x', ha='center', fontsize=14, fontweight='bold')
    plt.ylim(0, max(NUM_PROCESSOS + 1, SPEEDUP + 1))
    plt.tight_layout()
    plt.savefig('speedup_10000.png', dpi=150)
    print(f"   ✓ Gráfico salvo: speedup_10000.png")
    
    # ========== RESULTADO FINAL ==========
    print(f"\n" + "=" * 70)
    print(f"✅ SIMULAÇÃO CONCLUÍDA COM SUCESSO!")
    print(f"=" * 70)
    print(f"\n📊 RESUMO DOS RESULTADOS - GRADE 10.000x10.000:")
    print(f"   • Total de células: {TAMANHO * TAMANHO:,} (100 milhões)")
    print(f"   • Tempo Serial (Sequencial):  {TEMPO_SEQUENCIAL:.2f} segundos ({TEMPO_SEQUENCIAL/60:.1f} minutos)")
    print(f"   • Tempo Paralelo:             {TEMPO_PARALELO:.2f} segundos ({TEMPO_PARALELO/60:.1f} minutos)")
    print(f"   • SPEEDUP:                    {SPEEDUP:.2f}x")
    print(f"   • Eficiência:                 {EFICIENCIA:.1f}%")
    print(f"\n📁 Arquivos gerados na pasta:")
    print(f"   • mapa_risco_10000.png")
    print(f"   • comparacao_desempenho_10000.png")
    print(f"   • speedup_10000.png")
    print(f"\n" + "=" * 70)
    
    # Liberar memória
    gc.collect()