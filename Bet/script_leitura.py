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

OPCAO_CASA = 1
OPCAO_EMPATE = 2
OPCAO_VISITANTE = 3

def retorna_time_de_casa(row):
    return row[3].split('/')[3].split(' v ')[0]

def retorna_time_visitante(row):
    return row[3].split('/')[3].split(' v ')[1]

def retorna_dia_do_ano(row):
    return datetime.strptime(row[4], '%d-%m-%Y %H:%M').timetuple().tm_yday

def retorna_minuto_do_dia(row):
    return datetime.strptime(row[4], '%d-%m-%Y %H:%M').hour * 60

def retorna_dia_da_semana(row):
    return calendar.day_name[datetime.strptime(row[4], '%d-%m-%Y %H:%M').weekday()]

def retorna_opcao_selecionada(row):
    if row[8] == retorna_time_de_casa(row):
        # TIME DA CASA
        return [1, 0, 0]
    elif row[8] == retorna_time_visitante(row):
        # TIME VISITANTE
        return [0, 0, 1]
    else:
        # EMPATE
        return [0, 1, 0]

data_inicio = datetime.now()

caminho_base = "Bet/Resultado/base_2017.csv"

array_entrada_principal = []
array_entrada_opcao_selecionada = []
array_saida = []

linhas = 0

opcao_selecionada_encoder = preprocessing.OneHotEncoder()
opcao_selecionada_encoder.fit([[OPCAO_CASA], [OPCAO_EMPATE], [OPCAO_VISITANTE]])

with open(caminho_base, "rt", encoding='utf-8') as arquivo_base:

    reader = csv.reader(arquivo_base)

    for row in reader:
        try:
            colunas_opcao_selecionada = retorna_opcao_selecionada(row)

            array_entrada_principal.append(
                np.array([
                   #retorna_time_de_casa(row),      # Time de casa
                   #retorna_time_visitante(row),    # Time visitante
                    retorna_dia_do_ano(row),        # Dia do ano
                    retorna_minuto_do_dia(row),     # Minuto do dia
                    #retorna_dia_da_semana(row),    # Dia da semana
                    colunas_opcao_selecionada[0],   # Opção selecionada - Casa
                    colunas_opcao_selecionada[1],   # Opção selecionada - Empate
                    colunas_opcao_selecionada[2],   # Opção selecionada - Visitante
                    float(row[9])                   # Valor da odd
                ])
            )

            array_saida.append(
                np.array([
                    float(row[10]),                  # Total de apostas
                    #row[11]                         # Total apostado
                ])
            )

            #array_entrada.append(array_entrada)
            #array_saida.append(array_saida)

            linhas += 1

        except Exception as e:
            excecao = e

np_array_entrada = np.array(array_entrada_principal)
np_array_saida = np.array(array_saida)

regr = linear_model.LinearRegression()
regr.fit(np_array_entrada, np_array_saida)

data_fim = datetime.now()

print("\n\n------------------------------------------------------\n\n")
print(str(linhas) + " linhas analisados.")
print("" + str(data_inicio) + " - " + str(data_fim) + " (" + str(data_fim - data_inicio) + ")")