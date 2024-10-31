# Solucionador de Sistemas Lineares em Python

Este projeto implementa um solucionador de sistemas lineares de equações utilizando o método de eliminação de Gauss, desenvolvido em Python sem a utilização de bibliotecas externas.

## Funcionalidades

- **Resolução de sistemas lineares**: O código permite a resolução de qualquer sistema linear de equações que tenha o mesmo número de variáveis e equações.
- **Exemplo aplicado**: O programa inclui um exemplo pré-definido de sistema linear para demonstração.
- **Entrada personalizada**: O usuário pode inserir seu próprio sistema de equações diretamente no terminal.
- **Sem dependências externas**: Todo o código foi implementado manualmente, sem o uso de bibliotecas externas como NumPy ou SciPy.

### Método de Eliminação de Gauss

O algoritmo de eliminação de Gauss é utilizado para resolver o sistema linear. O processo consiste em:
1. Converter o sistema em uma forma triangular superior.
2. Resolver o sistema por substituição retroativa para encontrar os valores das variáveis.

### Entrada de Dados

O usuário deve fornecer:
1. O número de equações/variáveis.
2. Os coeficientes de cada equação, um por vez.
3. Os resultados de cada equação, formando o vetor de resultados.

### Exemplo Integrado

O programa apresenta o seguinte exemplo pré-definido para o usuário:

x + 2y + z &= 0 
-x + 3z &= 5 
x - 2y + z &= 1

A solução desse sistema será calculada e exibida ao usuário.

