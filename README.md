# 🌊 Relatório Técnico - Simulador Paralelo de Risco de Inundações

Disciplina: PROGRAMAÇÃO CONCORRENTE E DISTRIBUÍDA  
Aluno(s): Carlos Eduardo Pinheiro Da Silva - Luís Henrique Vieira Holanda  
Turma: 5° Semestre / Análise e Desenvolvimento de Sistemas  
Professor: Rafael Marconi Ramos  
Data: Junho/2026

***

## 📝 Descrição do Projeto

Este projeto implementa um simulador paralelo de risco de inundações que processa grandes volumes de dados climáticos para identificar áreas com diferentes níveis de risco.

Utilizando conceitos de computação paralela, o sistema compara o desempenho entre uma versão sequencial (serial) e versões paralelas com diferentes números de processos (1, 2, 4, 8 e 12), demonstrando os ganhos de performance ao distribuir a carga entre múltiplos núcleos da CPU.

O simulador é capaz de processar grades de até 10.000 x 10.000 (100 milhões de células), gerando mapas de risco e gráficos de desempenho.

***

## 🎯 Objetivo Geral

Desenvolver e analisar um sistema paralelo para simulação de risco de inundações, comparando o desempenho da versão sequencial com versões paralelas utilizando múltiplos processos, avaliando speedup e eficiência.

***

## 📋 Objetivos Específicos

* Implementar modelo de risco com 3 variáveis ambientais
* Criar versão sequencial (baseline)
* Implementar paralelismo com multiprocessing
* Ajustar carga computacional (loop)
* Medir tempo, speedup e eficiência
* Gerar gráficos de desempenho
* Analisar escalabilidade

***

## 🛠️ Tecnologias Utilizadas

* Python 3.13+
* NumPy
* Matplotlib
* Multiprocessing
* Time
* GC

***

## 📊 Dataset e Modelo

Dados sintéticos:

* Precipitação: Gamma
* Escoamento: Uniforme (0–300)
* Umidade: Uniforme (10–600)

Modelo de risco:

* Nível 3: P > 400 e R > 200
* Nível 2: P > 300 ou R > 150
* Nível 1: P > 200 ou U > 400
* Nível 0: caso contrário

***

## ⚙️ Funcionamento

* Geração de dados
* Aplicação do modelo
* Execução sequencial
* Execução paralela
* Cálculo de métricas
* Geração de gráficos

***

## ⚙️ Estratégia de Paralelização

* Divisão por linhas
* Processos independentes
* Combinação final

👉 Tipo: Embarrassingly Parallel

***

## 📈 Métricas

* Tempo de execução
* Speedup = Tseq / Tpar
* Eficiência = (S / N) x 100

***

## 📊 RESULTADOS EXPERIMENTAIS

Ambiente

* CPU: Intel i5-7500T (4 núcleos)
* RAM: 8 GB
* Sistema: Windows 11
* Grade: 100 milhões de células

***

## ✔️ Resultados obtidos 

Processo 1 → 167.12 segundos (Speedup: 1.00x | Eficiência: 100%)  
Processo 2 → 85.49 segundos (Speedup: 1.95x | Eficiência: 97.7%)  
Processo 4 → 45.37 segundos (Speedup: 3.68x | Eficiência: 92.1%)  
Processo 8 → 30.09 segundos (Speedup: 5.55x | Eficiência: 69.4%)  
Processo 12 → 26.63 segundos (Speedup: 6.27x | Eficiência: 52.3%)

***

## 📊 Análise dos Resultados

* Houve redução progressiva no tempo de execução com o aumento de processos

* O tempo caiu de **167.12s para 26.63s**, redução superior a **84%**

* O speedup máximo foi de **6.27x com 12 processos**

* Mesmo com apenas 4 núcleos físicos, houve ganho com 8 e 12 processos, indicando:
  * Uso de threads lógicas (hyperthreading)
  * Melhor aproveitamento de cache
  * Melhor distribuição da carga

* A eficiência caiu conforme aumentaram os processos:
  * 97.7% com 2 processos
  * 52.3% com 12 processos

* Isso acontece devido a:
  * Overhead de gerenciamento
  * Troca de contexto
  * Comunicação entre processos

* O melhor equilíbrio entre desempenho e eficiência foi entre **4 e 8 processos**

***

## 📁 Estrutura

Projeto\_Inundacao/  
├── simulador.py  
├── README.md  
├── curva\_tempo\_execucao.png  
├── curva\_speedup.png  
├── mapa\_risco.png  
└── requirements.txt

***

## 🚀 Execução

pip install numpy matplotlib  
python simulador.py

***

## ✅ ✅ CONCLUSÃO FINAL

A partir dos experimentos realizados, foi possível comprovar que a computação paralela proporciona ganhos significativos no processamento de grandes volumes de dados.

O sistema conseguiu reduzir o tempo de execução de aproximadamente **167 segundos para 26 segundos**, representando uma melhoria superior a **84%**.

Diferentemente de cenários limitados apenas pelos núcleos físicos, foi observado que o desempenho continuou melhorando até **12 processos**, demonstrando que o paralelismo pode aproveitar melhor os recursos disponíveis do sistema.

Esses ganhos podem ser explicados principalmente por:

* Uso de threads lógicas do processador
* Melhor aproveitamento de memória cache
* Distribuição eficiente das tarefas

Por outro lado, a eficiência diminuiu conforme o número de processos aumentou, mostrando o impacto do overhead de paralelização.

O estudo demonstra que:

* O paralelismo melhora significativamente a performance
* Existe perda de eficiência com muitos processos
* O desempenho depende da carga, arquitetura e gerenciamento do sistema

***

## 🏆 Conclusão técnica

O paralelismo não depende apenas do número de núcleos físicos, mas da combinação entre carga computacional, arquitetura e gerenciamento de processos.

***

## 🔥 Frase final

“O melhor desempenho não acontece com o maior número de processos, mas com o melhor equilíbrio entre paralelismo, eficiência e capacidade do hardware.”

***

## 📚 Referências

* Python Multiprocessing
* NumPy
* Matplotlib

***

## 👨‍💻 Autores

Carlos Eduardo Pinheiro Da Silva  
Luís Henrique Vieira Holanda
