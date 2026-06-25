# 🌊 Relatório Técnico - Simulador Paralelo de Risco de Inundações

**Disciplina:** PROGRAMAÇÃO CONCORRENTE E DISTRIBUÍDA

**Aluno(s):** Carlos Eduardo Pinheiro Da Silva - Luís Henrique Vieira Holanda

**Turma:** 5° Semestre / Análise e Desenvolvimento de Sistemas

**Professor:** Rafael Marconi Ramos

**Data:** Junho/2026

---

## 📝 Descrição do Projeto

Este projeto implementa um simulador paralelo de risco de inundações que processa grandes volumes de dados climáticos para identificar áreas com diferentes níveis de risco. Utilizando conceitos de computação paralela, o sistema compara o desempenho entre uma versão sequencial (serial) e versões paralelas com diferentes números de processos (1, 2, 4, 8 e 12), demonstrando os ganhos de performance obtidos ao distribuir a carga de processamento entre múltiplos núcleos da CPU.

O simulador é capaz de processar grades de até 10.000 x 10.000 (100 milhões de células), gerando mapas de risco e gráficos de desempenho comparativos.

---

## 🎯 Objetivo Geral

Desenvolver e analisar um sistema paralelo para simulação de risco de inundações, utilizando dados climáticos sintéticos (precipitação, escoamento superficial e umidade do solo), comparando o desempenho da versão sequencial (serial) com versões paralelas utilizando 1, 2, 4, 8 e 12 processos, medindo o speedup e a eficiência obtidos em cada configuração.

---

## 📋 Objetivos Específicos

1. Implementar um modelo de risco de inundação baseado em regras matemáticas que consideram três variáveis ambientais: precipitação, escoamento e umidade do solo.

2. Desenvolver uma versão sequencial (serial) do simulador para servir como baseline de desempenho.

3. Implementar versões paralelas utilizando a biblioteca multiprocessing do Python, distribuindo o processamento por linhas da matriz para 1, 2, 4, 8 e 12 processos.

4. Adicionar carga computacional ajustada (loop de 15 iterações) para forçar o uso real da CPU e demonstrar escalabilidade em todos os núcleos.

5. Medir e comparar o desempenho entre as diferentes configurações, calculando tempo de execução, speedup e eficiência.

6. Gerar visualizações gráficas do mapa de risco, da relação tempo vs processos e do speedup vs processos.

7. Analisar a escalabilidade do sistema em diferentes números de processos, com ênfase na grade de 10.000 x 10.000 (100 milhões de células).

---

## 🛠️ Tecnologias Utilizadas

- Python 3.13+ (linguagem principal)
- NumPy 1.24+ (manipulação de matrizes)
- Matplotlib 3.7+ (geração de gráficos)
- Multiprocessing (paralelismo - Pool, map)
- Time (medição de tempo)
- GC (gerenciamento de memória)

---

## 📊 Dataset e Modelo de Risco

### Dados Sintéticos Gerados

O projeto utiliza dados sintéticos gerados aleatoriamente com distribuições estatísticas realistas:

- Precipitação: Distribuição Gamma (shape=2, scale=50) - mm/mês
- Escoamento: Distribuição Uniforme (0 a 300) - mm
- Umidade do Solo: Distribuição Uniforme (10 a 600) - mm

### Modelo de Risco

O nível de risco é calculado célula por célula com base em três variáveis:

- Nível 3 (EXTREMO): Precipitação > 400 e Escoamento > 200
- Nível 2 (ALTO): Precipitação > 300 ou Escoamento > 150
- Nível 1 (MODERADO): Precipitação > 200 ou Umidade > 400
- Nível 0 (BAIXO): Caso contrário

---

## ⚙️ Funcionamento do Sistema

O simulador funciona da seguinte forma:

1. Os dados de entrada (precipitação, escoamento, umidade do solo) são gerados aleatoriamente
2. O modelo de risco aplica regras baseadas em limiares críticos
3. A versão sequencial processa célula por célula (1 processo)
4. A versão paralela distribui as linhas da matriz entre 2, 4, 8 e 12 processos
5. As métricas de desempenho são calculadas (speedup, eficiência)
6. Gráficos e mapas de risco são gerados

### Estratégia de Paralelização

A paralelização utiliza a técnica "embarrassingly parallel" (paralelização trivial), onde:

1. A matriz de dados é dividida por linhas
2. Cada processo recebe uma ou mais linhas para processar
3. Não há dependência entre as linhas (processamento independente)
4. Os resultados são combinados no final

### Carga Computacional Ajustada

Para garantir que o paralelismo fosse realmente perceptível e que os núcleos fossem devidamente utilizados, foi adicionada uma carga computacional extra com um loop de 15 iterações para forçar o uso da CPU. Isso garante que o ganho de performance com o aumento de processos seja claramente observado.

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
- E = 100%: aproveitamento máximo
- E < 100%: perda devido ao overhead
- E > 100%: efeito superlinear

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

### Configuração do Ambiente de Teste

- Processador: Intel Core i5-7500T @ 2.70GHz
- Núcleos físicos: 4
- Memória RAM: 8 GB
- Sistema Operacional: Windows 11 Enterprise
- Python: 3.13+
- Grade processada: 10.000 x 10.000 (100 milhões de células)
- Memória utilizada: aproximadamente 1.1 GB
- Processos testados: 1, 2, 4, 8, 12

### Resultados Obtidos

- 1 processo (serial): 96.54 segundos (Speedup: 1.00x, Eficiência: 100.0%)
- 2 processos: 40.51 segundos (Speedup: 2.38x, Eficiência: 119.2%)
- 4 processos: 25.15 segundos (Speedup: 3.84x, Eficiência: 95.9%)
- 8 processos: 25.51 segundos (Speedup: 3.78x, Eficiência: 47.3%)
- 12 processos: 26.22 segundos (Speedup: 3.68x, Eficiência: 30.7%)

### Distribuição do Risco (100 milhões de células)

- BAIXO: aproximadamente 30.100.000 células (30.1%)
- MODERADO: aproximadamente 19.100.000 células (19.1%)
- ALTO: aproximadamente 50.700.000 células (50.7%)
- EXTREMO: aproximadamente 100.000 células (0.1%)

### Análise dos Resultados

O computador utilizado possui 4 núcleos físicos (Intel Core i5-7500T). Por isso, o speedup máximo foi alcançado com 4 processos (3.84x). O uso de 8 e 12 processos não trouxe ganho adicional significativo, pois o processador não possui núcleos suficientes para executá-los simultaneamente. O overhead de criação e gerenciamento de processos adicionais (context switching) resultou em eficiência reduzida (47.3% e 30.7%, respectivamente).

O efeito superlinear observado com 2 processos (eficiência > 100%) ocorre devido a melhorias no uso de cache e redução de overhead de paginação de memória.

Principais números:
- Speedup máximo: 3.84x com 4 processos
- Melhor eficiência: 119.2% com 2 processos
- Tempo serial (baseline): 96.54 segundos
- Tempo paralelo (4 processos): 25.15 segundos
- Redução de tempo: 74% (de 96.54s para 25.15s)

---

## 📁 Estrutura do Projeto

Projeto_Inundacao/
├── simulador.py                         # Código fonte principal
├── README.md                            # Documentação do projeto
├── curva_tempo_execucao.png             # Gráfico: tempo x processos
├── curva_speedup.png                    # Gráfico: speedup x processos
├── mapa_risco.png                       # Mapa de risco (opcional)
└── requirements.txt                     # Dependências do projeto

### Organização do Código Fonte

simulador.py
├── calcular_risco_vetorizado()   # Função vetorizada de cálculo de risco
├── processar_bloco()             # Processa um bloco da matriz
├── simular_sequencial()          # Versão sequencial (1 processo)
├── simular_paralelo()            # Versão paralela (Pool de processos)
└── main                          # Programa principal:
    ├── Geração de dados (100 milhões de células)
    ├── Loop de testes: 1, 2, 4, 8, 12 processos
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
GRADE: 10.000 x 10.000 = 100 MILHÕES de células
======================================================================

[INFORMAÇÃO]
   Grade: 10000 x 10000 = 100,000,000 células
   Memória estimada: ~1144 MB (cerca de 1.1 GB)
   Processos a testar: 1, 2, 4, 8, 12

[ETAPA 1] Gerando dados sintéticos...
   ✓ Dados gerados em 8.50 segundos

[ETAPA 2] Testando com diferentes números de processos...
   Rodando com 1 processo(s)... ✅ 96.54 segundos
   Rodando com 2 processo(s)... ✅ 40.51 segundos
   Rodando com 4 processo(s)... ✅ 25.15 segundos
   Rodando com 8 processo(s)... ✅ 25.51 segundos
   Rodando com 12 processo(s)... ✅ 26.22 segundos

[ETAPA 3] RESULTADOS COMPARATIVOS:
   -------------------------------------------------------------
   Núcleos: 1  | Tempo: 96.54s  | Speedup: 1.00x  | Eficiência: 100.0%
   Núcleos: 2  | Tempo: 40.51s  | Speedup: 2.38x  | Eficiência: 119.2%
   Núcleos: 4  | Tempo: 25.15s  | Speedup: 3.84x  | Eficiência: 95.9%
   Núcleos: 8  | Tempo: 25.51s  | Speedup: 3.78x  | Eficiência: 47.3%
   Núcleos: 12 | Tempo: 26.22s  | Speedup: 3.68x  | Eficiência: 30.7%
   -------------------------------------------------------------

[ETAPA 4] Gerando gráficos comparativos...
   ✓ Gráfico salvo: curva_tempo_execucao.png
   ✓ Gráfico salvo: curva_speedup.png

✅ EXPERIMENTO CONCLUÍDO COM SUCESSO!

---

## 📚 Referências

1. Abatzoglou, J. T., et al. (2018). "TerraClimate: A high-resolution global dataset of monthly climate and climatic water balance." Scientific Data.

2. Python Multiprocessing Documentation: https://docs.python.org/3/library/multiprocessing.html

3. NumPy Documentation: https://numpy.org/doc/

4. Matplotlib Documentation: https://matplotlib.org/stable/contents.html

5. Intel Core i5-7500T Specifications: https://www.intel.com.br/content/www/br/pt/products/sku/97123/intel-core-i57500t-processor-6m-cache-up-to-3-30-ghz/specifications.html

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

O simulador demonstrou que a computação paralela é uma ferramenta poderosa para processamento de grandes volumes de dados, com os seguintes resultados:

1. O paralelismo é eficaz para problemas grandes. Para 100 milhões de células, o speedup máximo atingiu 3.84x com 4 processos, representando uma redução de tempo de 74%.

2. O speedup máximo foi limitado pelos núcleos físicos do processador (4 núcleos). O uso de 8 ou 12 processos não trouxe ganho adicional.

3. A eficiência máxima foi de 119.2% (efeito superlinear) com 2 processos, e 95.9% com 4 processos, demonstrando excelente aproveitamento dos recursos.

4. A carga computacional ajustada permitiu que o paralelismo fosse claramente observado e mensurado.

5. A estratégia de decomposição por linhas mostrou-se eficaz e escalável até o número de núcleos físicos disponíveis.

6. O tempo serial de 96.54 segundos serve como baseline, demonstrando que a paralelização com 4 processos reduz o tempo para apenas 25.15 segundos.

---

## 📊 Gráficos Gerados

O gráfico curva_tempo_execucao.png mostra a redução no tempo de execução à medida que o número de processos aumenta, com estabilização a partir de 4 processos devido à limitação de núcleos físicos.

O gráfico curva_speedup.png compara o speedup real obtido com o speedup ideal (linear), demonstrando claramente o ganho de performance e a limitação imposta pelo hardware.
