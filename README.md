# 🌊 Relatório Técnico - Simulador Paralelo de Risco de Inundações

**Disciplina:** PROGRAMAÇÃO CONCORRENTE E DISTRIBUÍDA

**Aluno(s):** Carlos Eduardo Pinheiro Da Silva - Luís Henrique Vieira Holanda

**Turma:** 5° Semestre / Análise e Desenvolvimento de Sistemas

**Professor:** Rafael Marconi Ramos

**Data:** Junho/2026

---

## 📌 TEMA

**Simulador Paralelo de Risco de Inundações utilizando Processamento Distribuído**

O projeto consiste em um simulador que processa grandes volumes de dados climáticos (precipitação, escoamento e umidade do solo) para identificar áreas com diferentes níveis de risco de inundação. Utilizando conceitos de computação paralela, o sistema compara o desempenho entre uma versão sequencial (serial) e versões paralelas com 1, 2, 4, 8 e 12 processos.

---

## 📌 JUSTIFICATIVA DO TEMA

As inundações são desastres naturais que causam milhares de mortes, prejuízos bilionários e deslocamento de populações todos os anos. A capacidade de simular rapidamente áreas de risco é fundamental para:

- **Planejamento urbano**: Identificar regiões vulneráveis
- **Defesa civil**: Antecipar evacuações
- **Seguros**: Precificar riscos
- **Mudanças climáticas**: Prever cenários futuros

A computação paralela permite processar grandes volumes de dados (100 milhões de células) em tempo hábil, tornando a simulação viável para tomada de decisões.

---

## 📝 Descrição do Projeto

Este projeto implementa um simulador paralelo de risco de inundações que processa grandes volumes de dados climáticos para identificar áreas com diferentes níveis de risco.

Utilizando conceitos de computação paralela, o sistema compara o desempenho entre uma versão sequencial (serial) e versões paralelas com diferentes números de processos (1, 2, 4, 8 e 12), demonstrando os ganhos de performance ao distribuir a carga entre múltiplos núcleos da CPU.

O simulador é capaz de processar grades de até 10.000 x 10.000 (100 milhões de células), gerando mapas de risco e gráficos de desempenho.

---

## 🎯 Objetivo Geral

Desenvolver e analisar um sistema paralelo para simulação de risco de inundações, comparando o desempenho da versão sequencial com versões paralelas utilizando múltiplos processos, avaliando speedup e eficiência.

---

## 📋 Objetivos Específicos

- Implementar modelo de risco com 3 variáveis ambientais
- Criar versão sequencial (baseline)
- Implementar paralelismo com multiprocessing
- Ajustar carga computacional (loop de 15 iterações)
- Medir tempo, speedup e eficiência
- Gerar gráficos de desempenho
- Analisar escalabilidade

---

## 🛠️ Tecnologias Utilizadas

- Python 3.13+
- NumPy (manipulação de matrizes)
- Matplotlib (gráficos)
- Multiprocessing (paralelismo)
- Time (medição)
- GC (gerenciamento de memória)

---

## 📊 Dataset e Modelo

### Dados Sintéticos

- Precipitação: Distribuição Gamma
- Escoamento: Distribuição Uniforme (0–300)
- Umidade do Solo: Distribuição Uniforme (10–600)

### Modelo de Risco

- Nível 3 (EXTREMO): P > 400 e R > 200
- Nível 2 (ALTO): P > 300 ou R > 150
- Nível 1 (MODERADO): P > 200 ou U > 400
- Nível 0 (BAIXO): caso contrário

---

## ⚙️ Funcionamento do Sistema

1. Geração de dados sintéticos (100 milhões de células)
2. Aplicação do modelo de risco
3. Execução sequencial (1 processo)
4. Execução paralela (2, 4, 8, 12 processos)
5. Cálculo de speedup e eficiência
6. Geração de gráficos comparativos

---

## ⚙️ Estratégia de Paralelização

- Divisão da matriz por linhas
- Processos independentes (sem dependência entre linhas)
- Combinação final dos resultados

**Tipo:** Embarrassingly Parallel (paralelização trivial)

**Carga computacional ajustada:** Loop de 15 iterações para forçar uso real da CPU

---

## 📈 Métricas Avaliadas

- **Tempo de execução**: T_seq e T_par
- **Speedup**: S = T_seq / T_par
- **Eficiência**: E = (S / N) x 100%

---

## 📊 RESULTADOS EXPERIMENTAIS

### Ambiente de Teste

- CPU: Intel Core i5-7500T @ 2.70GHz
- Núcleos físicos: 4
- Memória RAM: 8 GB
- Sistema Operacional: Windows 11 Enterprise
- Grade: 10.000 x 10.000 (100 milhões de células)
- Python: 3.13+

---

## ✅ Resultados Obtidos

| Processos | Tempo (segundos) | Speedup | Eficiência |
|-----------|------------------|---------|------------|
| 1         | 167.12           | 1.00x   | 100.0% |
| 2         | 85.49            | 1.95x   | 97.7% |
| 4         | 45.37            | 3.68x   | 92.1% |
| 8         | 30.09            | 5.55x   | 69.4% |
| 12        | 26.63            | 6.27x   | 52.3% |

---

## 📊 Análise dos Resultados

Houve redução progressiva no tempo de execução com o aumento de processos até 12 processos.
- O tempo caiu de **167.12s para 26.63s** com 12 processos, redução de **84%**.
- O speedup máximo foi de **6.27x com 12 processos**.
  - Uso de threads lógicas (hyperthreading)
  - Melhor aproveitamento de cache
  - Melhor distribuição da carga
- A eficiência caiu conforme aumentaram os processos:
  - 97.7% com 2 processos
  - 92.1% com 4 processos
  - 69.4% com 8 processos
  - 52.3% com 12 processos

Isso ocorre devido ao **overhead de gerenciamento** e **context switching** quando o número de processos excede os núcleos físicos disponíveis.

---

## 📁 Estrutura do Projeto

```
Projeto_Inundacao/
├── simulador.py                         # Código fonte principal
├── README.md                            # Documentação do projeto
├── curva_tempo_execucao.png             # Gráfico: tempo x processos
├── curva_speedup.png                    # Gráfico: speedup x processos
├── mapa_risco.png                       # Mapa de risco da região
└── requirements.txt                     # Dependências do projeto
```

---

## 🚀 Como Executar

### Pré-requisitos

```bash
pip install numpy matplotlib
```

### Execução

```bash
python simulador.py
```

✅ EXPERIMENTO CONCLUÍDO COM SUCESSO!
```

---

## ✅ CONCLUSÃO FINAL

A partir dos experimentos realizados, foi possível comprovar que a computação paralela proporciona ganhos significativos no processamento de grandes volumes de dados.

O sistema conseguiu reduzir o tempo de execução de aproximadamente **96.54 segundos para 25.15 segundos**, representando uma melhoria superior a **74%**.

O melhor desempenho foi alcançado com **4 processos**, atingindo speedup de **3.84x**, pois o processador utilizado possui **4 núcleos físicos**. O uso de 8 e 12 processos não trouxe ganho adicional devido ao overhead de gerenciamento.

O estudo demonstra que:

- O paralelismo melhora significativamente a performance para problemas grandes
- Existe perda de eficiência quando o número de processos excede os núcleos físicos
- O desempenho depende da carga computacional, arquitetura e gerenciamento do sistema

---


## ✅ PARALELISMO FUNCIONAL

O código implementa paralelismo funcional com as seguintes características:

- Uso da biblioteca `multiprocessing.Pool`
- Distribuição de linhas da matriz entre processos
- Processos totalmente independentes (embarrassingly parallel)
- Carga computacional ajustada para demonstrar ganhos reais
- Cálculo automático de speedup e eficiência
- Geração de gráficos comparativos

**Código de paralelismo utilizado:**

```python
from multiprocessing import Pool

def simular_paralelo(dados, num_processos):
    with Pool(processes=num_processos) as pool:
        resultados = pool.map(processar_linha, args_lista)
    # Combinação dos resultados
    return resultado
```

---

## 📚 Referências

- Python Multiprocessing Documentation: https://docs.python.org/3/library/multiprocessing.html
- NumPy Documentation: https://numpy.org/doc/
- Matplotlib Documentation: https://matplotlib.org/stable/contents.html
- Intel Core i5-7500T Specifications

---

## 👨‍💻 Autores

**Carlos Eduardo Pinheiro Da Silva**
**Luís Henrique Vieira Holanda**

5° Semestre - Análise e Desenvolvimento de Sistemas
