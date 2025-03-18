# Projeto: Implementação do Algoritmo MaxMin Select

## Descrição do Projeto

Este projeto implementa o algoritmo **MaxMin Select** em Python, que encontra o maior e o menor elemento de uma lista de números usando a técnica de **divisão e conquista**. O algoritmo é implementado em Python e utiliza recursão para dividir a lista em sublistas menores, encontrar o maior e o menor elemento em cada sublista e, em seguida, combinar os resultados para obter o maior e o menor elemento da lista original.

### Lógica do Algoritmo

1. **Caso Base**:

   - Se a lista tiver apenas um elemento, esse elemento é tanto o maior quanto o menor.
   - Se a lista tiver dois elementos, compare-os e retorne o maior e o menor.

2. **Divisão**:

   - A lista é dividida em duas metades usando o índice médio (`mid`).

3. **Conquista**:

   - O algoritmo é chamado recursivamente para cada metade da lista.

4. **Combinação**:
   - O maior e o menor elemento de cada metade são comparados para determinar o maior e o menor elemento da lista completa.

## Como Executar o Projeto

### Pré-requisitos

- Python 3.x instalado.

### Passos para Execução

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu_usuario/trabalho_individual_2_FPAA.git

   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd MaxMinSelect

   ```

3. Execute o script
   ```bash
   python main.py
   ```

### Exemplo de Saída

- Se a lista for **[3, 5, 1, 7, 9, 2, 8, 4, 6]**, a saída será:
  ```bash
  Maior elemento: 9
  Menor elemento: 1
  ```

## Relatório Técnico

### Análise da Complexidade Assintótica

### Método de Contagem de Operações

O algoritmo MaxMin Select realiza as seguintes operações:

- **Divisão**: A lista é dividida em duas metades, o que ocorre em tempo constante O(1).
- **Conquista**: Cada metade é processada recursivamente, resultando em 2T(n/2).
- **Combinação**: A combinação dos resultados é feita em tempo constante O(1).

O número total de comparações é dado pela recorrência:

_T(n)=2T(n/2)+O(1)_

Resolvendo essa recorrência, obtemos que a complexidade temporal do algoritmo é O(n).

### Aplicação do Teorema Mestre

A recorrência do algoritmo é:

1. **Identificação dos valores**:

- a = 2 (número de subproblemas)
- b = 2 (tamanho de cada subproblema)
- f(n) = O(1) (tempo para combinar os resultados)

2. **Cálculo de log**

- log2 2=1
