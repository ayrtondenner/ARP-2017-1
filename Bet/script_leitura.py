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
    return row[3].split('/')[3].split(' v ')[0].strip()

def retorna_time_visitante(row):
    return row[3].split('/')[3].split(' v ')[1].strip()

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

def retorna_time(time):
    encoder_time = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    if time == "Atletico GO":
        encoder_time[0] = 1
    elif time == "Atletico MG":
        encoder_time[1] = 1
    elif time == "Atletico PR":
        encoder_time[2] = 1
    elif time == "Avai":
        encoder_time[3] = 1
    elif time == "Bahia":
        encoder_time[4] = 1
    elif time == "Botafogo RJ":
        encoder_time[5] = 1
    elif time == "Chapecoense":
        encoder_time[6] = 1
    elif time == "Corinthians":
        encoder_time[7] = 1
    elif time == "Coritiba":
        encoder_time[8] = 1
    elif time == "Cruzeiro":
        encoder_time[9] = 1
    elif time == "Flamengo":
        encoder_time[10] = 1
    elif time == "Fluminense":
        encoder_time[11] = 1
    elif time == "Gremio":
        encoder_time[12] = 1
    elif time == "Palmeiras":
        encoder_time[13] = 1
    elif time == "Ponte Preta":
        encoder_time[14] = 1
    elif time == "Santos":
        encoder_time[15] = 1
    elif time == "Sport Recife":
        encoder_time[16] = 1
    elif time == "Sao Paulo":
        encoder_time[17] = 1
    elif time == "Vasco da Gama":
        encoder_time[18] = 1
    elif time == "Vitoria BA":
        encoder_time[19] = 1
    else:
        raise ValueError("Time " + str(time)  + " não encontrado")

    return encoder_time

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

            #if(reader.line_num == 2784):
            #    nadaaa = 0

            colunas_time_casa = retorna_time(retorna_time_de_casa(row))
            colunas_time_visitante = retorna_time(retorna_time_visitante(row))
            colunas_opcao_selecionada = retorna_opcao_selecionada(row)

            array_entrada_principal.append(
                np.array([
                    colunas_time_casa[0],            # Time de casa
                    colunas_time_casa[1],
                    colunas_time_casa[2],
                    colunas_time_casa[3],
                    colunas_time_casa[4],
                    colunas_time_casa[5],
                    colunas_time_casa[6],
                    colunas_time_casa[7],
                    colunas_time_casa[8],
                    colunas_time_casa[9],
                    colunas_time_casa[10],
                    colunas_time_casa[11],
                    colunas_time_casa[12],
                    colunas_time_casa[13],
                    colunas_time_casa[14],
                    colunas_time_casa[15],
                    colunas_time_casa[16],
                    colunas_time_casa[17],
                    colunas_time_casa[18],
                    colunas_time_casa[19],

                    colunas_time_visitante[0],      # Time visitante
                    colunas_time_visitante[1],
                    colunas_time_visitante[2],
                    colunas_time_visitante[3],
                    colunas_time_visitante[4],
                    colunas_time_visitante[5],
                    colunas_time_visitante[6],
                    colunas_time_visitante[7],
                    colunas_time_visitante[8],
                    colunas_time_visitante[9],
                    colunas_time_visitante[10],
                    colunas_time_visitante[11],
                    colunas_time_visitante[12],
                    colunas_time_visitante[13],
                    colunas_time_visitante[14],
                    colunas_time_visitante[15],
                    colunas_time_visitante[16],
                    colunas_time_visitante[17],
                    colunas_time_visitante[18],
                    colunas_time_visitante[19],

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
                    float(row[10]),                 # Total de apostas
                   #float(row[11])                  # Total apostado
                ])
            )

            #array_entrada.append(array_entrada)
            #array_saida.append(array_saida)

            linhas += 1

        except Exception as e:
            excecao = e

np_array_entrada = np.array(array_entrada_principal)
np_array_saida = np.array(array_saida)

regr = linear_model.LinearRegression(normalize=False)
regr.fit(np_array_entrada, np_array_saida)
score = regr.score(np_array_entrada, np_array_saida)

data_fim = datetime.now()

print("\n\n------------------------------------------------------\n\n")
print(str(linhas) + " linhas analisados.")
print("" + str(data_inicio) + " - " + str(data_fim) + " (" + str(data_fim - data_inicio) + ")")
result = 0