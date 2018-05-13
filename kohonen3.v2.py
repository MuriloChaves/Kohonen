from random import random

class Neuronio:

    def __init__(self, n):
        self.w = [0.0] * n

def criar_mapa(dimX, dimY, conexoes):
    
    mapa = []

    for i in range(0, dimY): # linha
        mapa.append([])

        for j in range(0, dimX): # coluna
            mapa[i].append(Neuronio(conexoes))
    
    # só pra mostrar o mapa no console
    for i in range(len(mapa)):
        print(mapa[i])

    return mapa

def inicia_pesos(mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            for k in range(len(mapa[i][j].w)):
                mapa[i][j].w[k] = random()
            print('Neurônio: ', mapa[i][j])
            print(mapa[i][j].w, '\n')

def retorna_vizinhos(linha, coluna, matriz, R):

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

def getVizinhos(matriz, R):
    
    getVizinhos = []

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            aux = retorna_vizinhos(i, j, matriz, R)
            #aux.append(vizinhos(i, j, matriz, R))
            getVizinhos.append(aux)
                
    return getVizinhos

def treina_Kohonen(dimX, dimY, conexoes, R):
    
    print('\n### Mapa de neurônios ###')
    mapa = criar_mapa(dimX, dimY, conexoes)
    
    print('\n### Pesos w_ij ###')
    inicia_pesos(mapa)

    print('\n### Vizinhança ###')
    vizinhos = getVizinhos(mapa, R)
    for i in range(len(vizinhos)):
        print(vizinhos[i], '\n')

    alpha = alpha

    #print(len(mapa[0][0].w))

    return mapa






######## TESTE #######

dimX = 4
dimY = 4
conexoes = 3 # depois ler automaticamente com as entradas
R = 1

kohonen = treina_Kohonen(dimX, dimY, conexoes, R)