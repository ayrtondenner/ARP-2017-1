import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

excelFile = pd.ExcelFile('População de 18 a 24 anos com ensino médio completo - municípios SP.xlsx')
parsedFile = excelFile.parse(0)
primeira_coluna = parsedFile.iloc[:,0]
terceira_coluna = parsedFile.iloc[:,2]

array_primeira_coluna = [x for x in primeira_coluna]
array_terceira_coluna = [x for x in terceira_coluna]

array_valores = []

for x in range(0, len(primeira_coluna)):
    array_valores.append([array_primeira_coluna[x], array_terceira_coluna[x]])

media = np.average(array_terceira_coluna)

variancia = sum((array_terceira_coluna - media)**2)/len(array_terceira_coluna)
desvio_padrao = np.sqrt(variancia)

desvio_padrao_maximo = media + 3 * desvio_padrao
desvio_padrao_minimo = media - 3 * desvio_padrao

lista_final = []

for x in range(0, len(primeira_coluna)):
    if terceira_coluna[x] < desvio_padrao_minimo or terceira_coluna[x] > desvio_padrao_maximo:
        lista_final.append([primeira_coluna[x], terceira_coluna[x]])

print("Desvio padrão: ", desvio_padrao, ", mínimo do desvio padrão: ", desvio_padrao_minimo, ", máximo do desvio padrão: ", desvio_padrao_maximo)
print(lista_final)