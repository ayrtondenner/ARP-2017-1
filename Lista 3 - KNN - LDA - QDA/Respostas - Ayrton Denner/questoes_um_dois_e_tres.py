import matplotlib.pyplot as plt
import numpy as np

def variancia(lista_valores):
    return sum((lista_valores - np.mean(lista_valores))**2)/len(lista_valores)

def desvio_padrao(lista_valores):
    return np.sqrt(variancia(lista_valores))

array_venda = np.array([489, 467, 524, 499, 498, 477, 471, 509, 492, 523, 483, 501, 487, 532, 465, 498, 478])

media = np.average(array_venda)
desvio_padrao = desvio_padrao(array_venda)

normalizacao_linear = [(x - min(array_venda))/(max(array_venda) - min(array_venda)) for x in array_venda]
normalizacao_por_desvio_padrao = [(x - media)/(desvio_padrao) for x in array_venda]

# Para essa base de dados, seria melhor utilizar a normalização por desvio padrão. Por mais que a normalização linear se utilize
# do valor máximo e do valor mínimo, e por mais que conheçamos o valor mínimo dentro do nosso problema (que é zero, não há como vender um número negativo de carros),
# não há a priori um número máximo ou um teto de carros que possam ser vendidos. Sendo assim, não conhecemos o valor máximo que o problema pode atingir,
# e por isso devemos utilizar a normalização por desvio padrão
