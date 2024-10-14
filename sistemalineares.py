def eliminacao_gauss(matrix, resultados):
    n = len(resultados)
    
    for i in range(n):
        max_index = i + max(range(n - i), key=lambda k: abs(matrix[i + k][i]))
        if i != max_index:
            matrix[i], matrix[max_index] = matrix[max_index], matrix[i]
            resultados[i], resultados[max_index] = resultados[max_index], resultados[i]
        
        for j in range(i + 1, n):
            fator = matrix[j][i] / matrix[i][i]
            for k in range(i, n):
                matrix[j][k] -= fator * matrix[i][k]
            resultados[j] -= fator * resultados[i]

    solucao = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        soma_ax = sum(matrix[i][j] * solucao[j] for j in range(i + 1, n))
        solucao[i] = (resultados[i] - soma_ax) / matrix[i][i]
    
    return solucao

def entrada_usuario():
    n = int(input("Digite o número de variáveis/equações: "))
    
    matriz = []
    print("Digite os coeficientes da matriz linha por linha, separados por espaços:")
    for i in range(n):
        linha = list(map(float, input(f"Linha {i+1}: ").split()))
        matriz.append(linha)
    
    resultados = list(map(float, input("Digite os resultados (separados por espaços): ").split()))
    
    return matriz, resultados

def exibir_exemplo():
    print("\nExemplo de sistema linear:")
    print(" x + 2y + z = 0")
    print("-x + 3z = 5")
    print(" x - 2y + z = 1\n")
    
    matriz_exemplo = [
        [1, 2, 1],
        [-1, 0, 3],
        [1, -2, 1]
    ]
    resultados_exemplo = [0, 5, 1]
    
    solucao_exemplo = eliminacao_gauss(matriz_exemplo, resultados_exemplo)
    
    print("Solução do exemplo:")
    for i, x in enumerate(solucao_exemplo):
        print(f"Variável {i + 1}: {x}")

    while True:
        print("\nO que deseja fazer agora?")
        print("1. Voltar ao menu principal")
        print("2. Sair")
        escolha = input("Digite 1 ou 2: ")
        if escolha == '1':
            return  # Volta para o menu principal
        elif escolha == '2':
            print("Saindo do programa...")
            exit()  # Sai do programa
        else:
            print("Opção inválida. Por favor, tente novamente.")

def main():
    while True:
        print("\nBem-vindo ao solucionador de sistemas lineares!")
        print("Escolha uma opção:")
        print("1. Ver exemplo de sistema linear")
        print("2. Inserir um novo sistema linear")
        print("3. Sair")
        
        escolha = input("Digite 1, 2 ou 3: ")
        
        if escolha == '1':
            exibir_exemplo()
        elif escolha == '2':
            matriz, resultados = entrada_usuario()
            solucao = eliminacao_gauss(matriz, resultados)
            print("\nSolução para o sistema inserido:")
            for i, x in enumerate(solucao):
                print(f"Variável {i + 1}: {x}")
        elif escolha == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
