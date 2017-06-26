import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import csv 
import sys
from datetime import datetime
import glob
import calendar
from sklearn import preprocessing
from sklearn import datasets, linear_model
from sklearn import svm
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import OneHotEncoder
import operator
import math
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import ExtraTreeRegressor
from sklearn.model_selection import cross_val_score


def imprime_resultado(regressor, array_entrada, array_saida):
    score = regressor.score(array_entrada, array_saida)
    print(str(score) + " - " + str(score * 100) + "%")

data_inicio = datetime.now()

caminho_base = "Bet/Resultado/base_tratada_2017_5_jogos.csv"
#caminho_base = "Bet/CSV/bfinf_other_170508to170514_170530073456.csv"
#caminho_base = "Bet/CSV/arquivo_teste.csv"

array_entrada_principal = []
array_entrada_opcao_selecionada = []
array_saida = []

with open(caminho_base, "rt", encoding='latin-1') as arquivo_base:

    reader = csv.reader(arquivo_base)

    next(reader)

    for row in reader:
        try:
            array_entrada_principal.append([
                float(row[0]), float(row[1]),
                float(row[2]), float(row[3]), float(row[4]), float(row[5]),
                float(row[6]), float(row[7]), float(row[8]), float(row[9]),
                float(row[10]), float(row[11]), float(row[12]), float(row[13]), float(row[14]), float(row[15]),
                float(row[16]), float(row[17]), float(row[18]), float(row[19]),
                float(row[20]), float(row[21]), float(row[22]), float(row[23]), float(row[24]), float(row[25]),
                float(row[26]), float(row[27]), float(row[28]), float(row[29]),
                float(row[30]), float(row[31]), float(row[32]), float(row[33]), float(row[34]), float(row[35]),
                float(row[36]), float(row[37]), float(row[38]), float(row[39]),
                float(row[40]), float(row[41]), float(row[42]), float(row[43]), float(row[44]), float(row[45]),
                float(row[46]), float(row[47]), float(row[48]), float(row[49]),
                float(row[50]), float(row[51]), float(row[52]), float(row[53]), float(row[54]), float(row[55]),
                float(row[56])
            ])
            # array_saida.append([float(row[57]),
            #     float(row[58])
            # ])
            array_saida.append(float(row[57]))
        except Exception as e:
            excecao = e

np_array_entrada = np.array(array_entrada_principal)
np_array_saida = np.array(array_saida)

#variancia = VarianceThreshold()
#np_array_entrada = variancia.fit_transform(np_array_entrada)

#regressao_nao_normalizada = linear_model.LinearRegression(normalize=False)
#regressao_normalizada = linear_model.LinearRegression(normalize=True)
#regressao_nao_normalizada.fit(np_array_entrada, np_array_saida)
#regressao_normalizada.fit(np_array_entrada, np_array_saida)

#imprime_resultado(regressao_nao_normalizada, np_array_entrada, np_array_saida)
# imprime_resultado(regressao_normalizada, np_array_entrada, np_array_saida)

# regr_1 = DecisionTreeRegressor(max_depth=2)
# regr_2 = DecisionTreeRegressor(max_depth=5)
regr_3 = ExtraTreeRegressor()
# regr_1.fit(np_array_entrada, np_array_saida)
# regr_2.fit(np_array_entrada, np_array_saida)
regr_3.fit(np_array_entrada, np_array_saida)

# imprime_resultado(regr_1, np_array_entrada, np_array_saida)
# imprime_resultado(regr_2, np_array_entrada, np_array_saida)
imprime_resultado(regr_3, np_array_entrada, np_array_saida)

# linear_svr = svm.NuSVR()
# linear_svr.fit(np_array_entrada, np_array_saida)
# imprime_resultado(linear_svr, np_array_entrada, np_array_saida)

#regressor = DecisionTreeRegressor(random_state=0)
#(regressor, np_array_entrada, np_array_saida, cv=10)

data_fim = datetime.now()

print("\n\n------------------------------------------------------\n\n")
print(str(len(array_entrada_principal)) + " linhas analisados com " + str(len(array_entrada_principal[0])) + " colunas cada.")
print("" + str(data_inicio) + " - " + str(data_fim) + " (" + str(data_fim - data_inicio) + ")")
result = 0