matriz = [
    [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
    [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6],
    [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6],
    [3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6],
    [4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 0.6],
    [5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6],
    [6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6]
]



def vizinhos(linha, coluna, matriz, R):

    vizinhos = []
    
    if R < 0:
        R = 0

    while R >= len(matriz) or R >= len(matriz[0]):
        R = R - 1

    #linha = linha
    #coluna = coluna
    
    #print('\nLinha: ', linha)
    #print('Coluna: ', coluna)

    linhaInicial = linha - R
    linhaFinal = linha + R
    
    if linhaInicial < 0:
        linhaInicial = 0
    while linhaFinal > len(matriz)-1:
        linhaFinal = linhaFinal - 1

    #print('\nLinhaInicial: ', linhaInicial)
    #print('LinhaFinal: ', linhaFinal)

    colunaInicial = coluna - R
    colunaFinal = coluna + R
    
    if colunaInicial < 0:
        colunaInicial = 0
    while colunaFinal > len(matriz[0])-1:
        colunaFinal = colunaFinal - 1

    #print('\nColunaInicial: ', colunaInicial)
    #print('colunaFinal: ', colunaFinal, '\n')
    
    for i in range(linhaInicial, linhaFinal+1):
        for j in range(colunaInicial, colunaFinal+1):
            if R == 0:
                vizinhos.append(matriz[i][j])
            if R != 0 and matriz[i][j] != matriz[linha][coluna]:
                vizinhos.append(matriz[i][j])
            #vizinhos.append(matriz[i][j])

    return vizinhos

R = 1

teste = vizinhos(3, 3, matriz, R)

print(teste)