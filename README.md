# Projeto: Implementação do Algoritmo MaxMin Select

## Descrição do Projeto

Este projeto implementa o algoritmo **MaxMin Select** em Python, que encontra o maior e o menor elemento de uma lista de números utilizando a técnica de **divisão e conquista**. O algoritmo divide a lista em sublistas menores, encontra o maior e o menor elemento em cada sublista e, em seguida, combina os resultados para obter o maior e o menor elemento da lista original.

## Lógica do Algoritmo

O algoritmo segue os seguintes passos:

1. **Caso Base**:
   - Se a lista contiver apenas um elemento, esse elemento é tanto o maior quanto o menor.
   - Se a lista contiver dois elementos, eles são comparados diretamente para determinar o maior e o menor.

2. **Divisão**:
   - A lista é dividida em duas metades usando o índice médio (`mid`).

3. **Conquista**:
   - O algoritmo é chamado recursivamente para cada metade da lista.

4. **Combinação**:
   - O maior e o menor elemento de cada metade são comparados para determinar o maior e o menor elemento da lista completa.

## Implementação do Algoritmo

Aqui está a implementação do algoritmo MaxMin Select em Python:

```python
def max_min_select(arr, low, high):
   
    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[high], arr[low]
        else:
            return arr[low], arr[high]
    
    mid = (low + high) // 2
    
    left_max, left_min = max_min_select(arr, low, mid)
    right_max, right_min = max_min_select(arr, mid + 1, high)
    
    overall_max = max(left_max, right_max)
    overall_min = min(left_min, right_min)  
    
    return overall_max, overall_min

if __name__ == "__main__":
    arr = [3, 5, 1, 7, 9, 2, 8, 4, 6]
    n = len(arr)
    max_val, min_val = max_min_select(arr, 0, n - 1)
    print(f"Maior elemento: {max_val}")
    print(f"Menor elemento: {min_val}")
```

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

3. Execute o script:
   ```bash
   python main.py
   ```

### Exemplo de Saída

Se a lista for **[3, 5, 1, 7, 9, 2, 8, 4, 6]**, a saída será:

```bash
Maior elemento: 9
Menor elemento: 1
```

## Relatório Técnico

### Análise da Complexidade Assintótica

#### Método de Contagem de Operações

O algoritmo MaxMin Select realiza as seguintes operações:

- **Divisão**: A lista é dividida em duas metades, o que ocorre em tempo constante O(1).
- **Conquista**: Cada metade é processada recursivamente, resultando em 2T(n/2).
- **Combinação**: A combinação dos resultados é feita em tempo constante O(1).

O número total de comparações é dado pela recorrência:

\[ T(n) = 2T(n/2) + O(1) \]

Resolvendo essa recorrência, obtemos que a complexidade temporal do algoritmo é **O(n)**.

### Aplicação do Teorema Mestre

A recorrência do algoritmo é:

1. **Identificação dos valores**:
   - a = 2 (número de subproblemas)
   - b = 2 (tamanho de cada subproblema)
   - f(n) = O(1) (tempo para combinar os resultados)

2. **Cálculo de log**
   - \[ \log_2 2 = 1 \]

3. **Classificação segundo o Teorema Mestre**:
   - Como f(n) = O(n^c) para c < log_b a, o caso 2 do Teorema Mestre se aplica.
   - A solução assintótica é O(n), confirmando a eficiência do algoritmo.

## Pontos Extras

### Diagrama da Recursão

