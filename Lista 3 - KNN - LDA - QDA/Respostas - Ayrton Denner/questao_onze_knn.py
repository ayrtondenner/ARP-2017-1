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

def calcula_distancias(lista_presentes_normalizados, novo_item):
    lista_distancias = []

    for x in range(0, len(lista_presentes_normalizados)):
        item_antigo = lista_presentes_normalizados[x]
        distancia = calcula_distancia_euclidiana(item_antigo, novo_item)

        resultado_distancia = [distancia, item_antigo[0]]
        lista_distancias.append(resultado_distancia)

    lista_distancias_ordenada = sorted(lista_distancias, key=lambda x: x[0])

    return lista_distancias_ordenada

def prever_classe(lista_distancias, k_vizinhos):
    lista_distancias_ordenada = sorted(lista_distancias, key=lambda x: x[0])

    lista_mais_proximos =  lista_distancias_ordenada[:k_vizinhos]

    nosso_mode = mode(lista_mais_proximos)

    previsao_classe = nosso_mode[0].item(1)

    return previsao_classe

lista_vinhos = []

file = open("lista_wines.txt", "r") 
for line in file: 
    linha = str.split(line, ",")
    lista_vinhos.append(list(map(float, linha)))

array_vinhos = np.array(lista_vinhos)

# Separando os itens por classe
array_c1 = [x for x in array_vinhos if x[0] == 1]
array_c2 = [x for x in array_vinhos if x[0] == 2]
array_c3 = [x for x in array_vinhos if x[0] == 3]

# Em todos os casos, iremos usar os 70% primeiros para treino e os 30% restantes para teste

# Tamanho: 59
# Treino: 41
# Teste: 18
array_treino_c1 = array_c1[:round(len(array_c1) * 0.7)]
array_teste_c1 = array_c1[-round(len(array_c1) * 0.3):]

# Tamanho: 71
# Treino: 50
# Teste: 21
array_treino_c2 = array_c2[:round(len(array_c2) * 0.7)]
array_teste_c2 = array_c2[-round(len(array_c2) * 0.3):]

# Tamanho: 48
# Treino: 34
# Teste: 14
array_treino_c3 = array_c3[:round(len(array_c3) * 0.7)]
array_teste_c3 = array_c3[-round(len(array_c3) * 0.3):]

array_treino = []
array_teste = []

for x in range(0, len(array_treino_c1)):
    array_treino.append(array_treino_c1[x])

for x in range(0, len(array_treino_c2)):
    array_treino.append(array_treino_c2[x])

for x in range(0, len(array_treino_c3)):
    array_treino.append(array_treino_c3[x])

for x in range(0, len(array_teste_c1)):
    array_teste.append(array_teste_c1[x])

for x in range(0, len(array_teste_c2)):
    array_teste.append(array_teste_c2[x])

for x in range(0, len(array_teste_c3)):
    array_teste.append(array_teste_c3[x])

array_estatisticas = calcula_estatisticas_de_normalizacao(array_treino)

array_treino = normalizar_por_desvio_padrao(array_treino, array_estatisticas)
array_teste = normalizar_por_desvio_padrao(array_teste, array_estatisticas)

quantidade_de_classes = 3

array_distancia = []

for x in range(0, len(array_teste)):
    calculo_distancia = calcula_distancias(array_treino, array_teste[x])
    array_distancia.append(calculo_distancia)

lista_dados_x = []
lista_dados_y = []

# K de zero até a quantidade de itens de treino
for x in range(1, len(array_treino) + 1):
    lista_previsoes = []
    if x % 2 != 0 and x % quantidade_de_classes != 0:
        for y in range(0, len(array_teste)):
            lista_previsoes.append(prever_classe(array_distancia[y], x) == array_teste[y][0])
            #(lista_presentes_normalizados, novo_item, k_vizinhos)

        lista_previsoes_corretas = [x for x in lista_previsoes if x == True]

        porcentagem_correta = len(lista_previsoes_corretas)/len(lista_previsoes) * 100
        lista_dados_x.append(x)
        lista_dados_y.append(porcentagem_correta)
        
        print("Lista de previsões com K =", x, "(", len(array_treino), ") :", len(lista_previsoes_corretas), "/", len(lista_previsoes), ":", porcentagem_correta, "%")

figure = plt.figure()
axis = figure.gca()
axis.set_axisbelow(True)    
plt.grid(linestyle = ":")

plt.plot(lista_dados_x, lista_dados_y)
plt.show()