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
    
    return mapa

def inicia_pesos(mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            for k in range(len(mapa[i][j].w)):
                mapa[i][j].w[k] = random()
            print(mapa[i][j].w)

def treina_Kohonen(dimX, dimY, conexoes):
    
    mapa = criar_mapa(dimX, dimY, conexoes)

    print('\n### Pesos w_ij ###')
    inicia_pesos(mapa)

    #print(len(mapa[0][0].w))

    return mapa

######## TESTE #######

dimX = 4
dimY = 4

kohonen = treina_Kohonen(dimX, dimY, 3)