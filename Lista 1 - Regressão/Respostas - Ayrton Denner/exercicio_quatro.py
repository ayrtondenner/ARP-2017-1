import matplotlib.pyplot as plt
import numpy as np

# Método para desenhar a grid e deixar ela atrás dos pontos e das retas
def prepara_grid():
    figure = plt.figure()
    axis = figure.gca()
    axis.set_axisbelow(True)    
    plt.grid(linestyle = ":")
    return

# Método para colocar os labels do gráfico
def seta_labels(title, xlabel, ylabel):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    return    

# Método para retornar os coeficientes da reta
def calcula_coeficientes(matriz_x, matriz_y):
    # y = b0 + b1 * x1 + b2 * x2 + b3 * x3
    return (matriz_x.T * matriz_x).I * np.transpose(matriz_x) * matriz_y

# Método para calcular e desenhar a reta de acordo com os coeficientes
def calcula_novo_item(novo_x, lista_coeficientes):
    # Y = b0 + b1 * x1 + b2 * x2 + b3 * x3 ...

    calculo = lista_coeficientes.item(0, 0) + novo_x[0] * lista_coeficientes.item(1, 0) + novo_x[1] * lista_coeficientes.item(2, 0) + novo_x[2] * lista_coeficientes.item(3, 0)

    return calculo

prepara_grid()

array_tamanho = np.array([87, 86, 105, 100, 88, 100, 136, 86, 84, 94, 100, 86, 78, 84, 78, 93, 104, 71, 86, 101, 83, 77, 78, 98, 98, 84, 89, 107, 138, 83, 96, 94, 104,
                            100, 100, 94, 111, 104, 103, 103])

array_idade = np.array([9, 10, 8, 11, 8, 9, 9, 10, 11, 6, 14, 13, 10, 8, 6, 4, 11, 15, 5, 9, 10, 10, 13, 11, 11, 8, 12, 7, 9, 11, 8, 10, 12, 14, 7, 14, 7, 6, 9, 9])

array_andar = np.array([9, 1, 12, 7, 13, 8, 6, 8, 9, 6, 4, 14, 3, 6, 11, 3, 4, 8, 8, 9, 6, 9, 6, 11, 3, 15, 4, 2, 12, 5, 14, 17, 11, 8, 6, 2, 7, 8, 10, 4])

array_preco = np.array([814364, 837887, 1094109, 727129, 784800, 1158339, 1080046, 839743, 920737, 713176, 859764, 982291, 733894, 915152, 980419, 1061956, 981657,
                        711479, 830290, 965093, 849199, 640924, 688660, 821829, 982912, 1020831, 710888, 801885, 1307216, 671028, 918318, 843974, 923510, 836419, 967390,
                        601516, 1297396, 918891, 1279741, 860217])

array_vazio = [1] * len(array_preco)

matriz_x = np.matrix([array_vazio, array_tamanho, array_idade, array_andar]).T

matriz_y = np.matrix([array_preco]).T

lista_coeficientes = calcula_coeficientes(matriz_x, matriz_y)

# Qual é o preço previsto de um imóvel com 80m2, 10 anos e que está no 9º andar?
novo_item = np.array([80, 10, 9,])

resultado_novo_item = calcula_novo_item(novo_item, lista_coeficientes)

print(resultado_novo_item)