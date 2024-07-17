# Cálculo de Probabilidade com Distribuição de Poisson

## Descrição

Este script em Python calcula a probabilidade de um hospital atender exatamente um determinado número de pacientes em um dia, usando a distribuição de Poisson. A distribuição de Poisson é apropriada para modelar o número de eventos que ocorrem em um intervalo fixo de tempo, assumindo que os eventos ocorrem independentemente e com uma taxa média constante.

## Contexto

Suponha que um hospital atende, em média, 5 pacientes por dia. Queremos saber a probabilidade de o hospital atender exatamente 7 pacientes em um determinado dia.

## Solução

A distribuição de Poisson é utilizada para este cálculo. A fórmula da distribuição de Poisson é:

\[ P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!} \]

onde:
- \( \lambda \) é a taxa média de ocorrência (número médio de pacientes por dia),
- \( k \) é o número de ocorrências desejadas (número de pacientes),
- \( e \) é a base do logaritmo natural (aproximadamente 2.71828),
- \( k! \) é o fatorial de \( k \).

## Requisitos

- Python 3.x

## Como Usar

1. **Clone o repositório ou copie o código para seu ambiente local.**
2. **Execute o script Python.**


