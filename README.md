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
