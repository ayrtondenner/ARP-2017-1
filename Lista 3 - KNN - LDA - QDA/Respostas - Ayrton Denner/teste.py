import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import copy
from scipy.stats import mode

def calcula_variancia(lista_itens):
    return sum((lista_itens - np.average(lista_itens))**2)/len(lista_itens)

def calcula_desvio_padrao(lista_itens):
    return np.sqrt(calcula_variancia(lista_itens))

def calcula_distancia_euclidiana(item_antigo, item_novo):

    # Temos que remover os valores das classes, ou eles irão interferir no cálculo de distância euclidiana
    item_antigo_sem_classe = copy.deepcopy(item_antigo)
    item_antigo_sem_classe[0] = 0
    item_antigo_sem_classe = np.array([item_antigo_sem_classe])

    item_novo_sem_classe = copy.deepcopy(item_novo)
    item_novo_sem_classe[0] = 0
    item_novo_sem_classe = np.array([item_novo_sem_classe])

    return np.sqrt(np.sum((item_antigo_sem_classe - item_novo_sem_classe)**2))

def calcula_estatisticas_de_normalizacao(array_treino):
    array_estatisticas = []

    for x in range(1, len(array_treino[0])):
        array_propriedades = [y[x] for y in array_treino]
        array_estatisticas.append([np.average(array_propriedades), calcula_desvio_padrao(array_propriedades)])

    return array_estatisticas


def normalizar_por_desvio_padrao(array_valores, array_estatisticas):
    array_normalizado = []

    for x in range(1, len(array_valores[0])):
        array_propriedades = [y[x] for y in array_valores]
        array_estatisticas.append([np.average(array_propriedades), calcula_desvio_padrao(array_propriedades)])

    for x in range(0, len(array_valores)):

        # O primeiro valor, que é o resultado da classe, não precisa ser normalizado
        array_linha = [array_valores[x][0]]
        for y in range(1, len(array_valores[x])):
            array_linha.append((array_valores[x][y] - array_estatisticas[y - 1][0])/array_estatisticas[y - 1][1])
        
        array_normalizado.append(array_linha)

    return array_normalizado

def prever_classe(lista_presentes_normalizados, novo_item, k_vizinhos):
    lista_distancias = []

    for x in range(0, len(lista_presentes_normalizados)):
        item_antigo = lista_presentes_normalizados[x]
        distancia = calcula_distancia_euclidiana(item_antigo, novo_item)

        resultado_distancia = [distancia, item_antigo[0]]
        lista_distancias.append(resultado_distancia)

    lista_distancias_ordenada = sorted(lista_distancias, key=lambda x: x[0])

    lista_mais_proximos = lista_distancias_ordenada[:k_vizinhos]

    nosso_mode = mode(lista_mais_proximos)

    previsao_classe = nosso_mode[0].item(1)

    return previsao_classe

array_itens = np.array([
    np.array([2, 1000, 1000]),
    np.array([1, 7000, 2000]),
    np.array([2, 2000, 1500]),
    np.array([2, 3000, 2500]),
    np.array([1, 5500, 3500]),
    np.array([1, 5000, 3000]),
    np.array([2, 3500, 2000]),
    np.array([1, 5500, 2000]),
])

array_treino = array_itens[:6]
array_teste = array_itens[-2:]

array_estatisticas = calcula_estatisticas_de_normalizacao(array_treino)

array_treino = normalizar_por_desvio_padrao(array_treino, array_estatisticas)
array_teste = normalizar_por_desvio_padrao(array_teste, array_estatisticas)

quantidade_de_classes = 2

for x in range(1, len(array_treino) + 1):
    lista_previsoes = []
    if x % 2 != 0 and x % quantidade_de_classes != 0:
        for y in range(0, len(array_teste)):
            lista_previsoes.append(prever_classe(array_treino, array_teste[y], x) == array_teste[y][0])
            #(lista_presentes_normalizados, novo_item, k_vizinhos)

        lista_previsoes_corretas = [x for x in lista_previsoes if x == True]
        print("Lista de previsões com K = ", x, " : ", len(lista_previsoes_corretas), "/", len(lista_previsoes), ": ", len(lista_previsoes_corretas)/len(lista_previsoes)*100, "%")