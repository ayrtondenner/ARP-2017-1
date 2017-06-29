# import matplotlib.pyplot as plt
import numpy as np
# import scipy.stats as stats
import csv 
# import sys
from datetime import datetime
# import glob
# import calendar
# from sklearn import preprocessing
# from sklearn import datasets, linear_model
# from sklearn import svm
# from sklearn.feature_selection import VarianceThreshold
# from sklearn.preprocessing import OneHotEncoder
import operator
# import math

OPCAO_CASA = 1
OPCAO_EMPATE = 2
OPCAO_VISITANTE = 3

#QUANTIDADE_DE_JOGOS_PASSADOS = 5 #3 #5

CAMINHO_ARQUIVO_BASE_CRUA = "Bet/Resultado/base_2016.csv"

LISTA_ORDEM_2015 = [
    "Corinthians",
    "Atletico MG",
    "Gremio",
    "Sao Paulo",
    "Internacional",
    "Sport Recife",
    "Santos",
    "Cruzeiro",
    "Palmeiras",
    "Atletico PR",
    "Ponte Preta",
    "Flamengo",
    "Fluminense",
    "Chapecoense",
    "Coritiba",
    "Figueirense",
    "Botafogo RJ",
    "Santa Cruz PE",
    "Vitoria BA",
    "America MG"
]

LISTA_ORDEM_2016 = [
    "Palmeiras",
    "Santos",
    "Flamengo",
    "Atletico MG",
    "Botafogo RJ",
    "Atletico PR",
    "Corinthians",
    "Ponte Preta",
    "Gremio",
    "Sao Paulo",
    "Chapecoense",
    "Cruzeiro",
    "Fluminense",
    "Sport Recife",
    "Coritiba",
    "Vitoria BA",
    "Atletico GO",
    "Avai",
    "Vasco da Gama",
    "Bahia"
]

def define_cabecalho(quantidade_de_jogos_passados):

    cabecalho = [
        "Posição 2015 do time da casa",
        "Posição 2015 do time visitante",

        str(LISTA_ORDEM_2015[0] + " - Casa"),
        str(LISTA_ORDEM_2015[1] + " - Casa"),
        str(LISTA_ORDEM_2015[2] + " - Casa"),
        str(LISTA_ORDEM_2015[3] + " - Casa"),
        str(LISTA_ORDEM_2015[4] + " - Casa"),
        str(LISTA_ORDEM_2015[5] + " - Casa"),
        str(LISTA_ORDEM_2015[6] + " - Casa"),
        str(LISTA_ORDEM_2015[7] + " - Casa"),
        str(LISTA_ORDEM_2015[8] + " - Casa"),
        str(LISTA_ORDEM_2015[9] + " - Casa"),
        str(LISTA_ORDEM_2015[10] + " - Casa"),
        str(LISTA_ORDEM_2015[11] + " - Casa"),
        str(LISTA_ORDEM_2015[12] + " - Casa"),
        str(LISTA_ORDEM_2015[13] + " - Casa"),
        str(LISTA_ORDEM_2015[14] + " - Casa"),
        str(LISTA_ORDEM_2015[15] + " - Casa"),
        str(LISTA_ORDEM_2015[16] + " - Casa"),
        str(LISTA_ORDEM_2015[17] + " - Casa"),
        str(LISTA_ORDEM_2015[18] + " - Casa"),
        str(LISTA_ORDEM_2015[19] + " - Casa"),

        str(LISTA_ORDEM_2015[0] + " - Visitante"),
        str(LISTA_ORDEM_2015[1] + " - Visitante"),
        str(LISTA_ORDEM_2015[2] + " - Visitante"),
        str(LISTA_ORDEM_2015[3] + " - Visitante"),
        str(LISTA_ORDEM_2015[4] + " - Visitante"),
        str(LISTA_ORDEM_2015[5] + " - Visitante"),
        str(LISTA_ORDEM_2015[6] + " - Visitante"),
        str(LISTA_ORDEM_2015[7] + " - Visitante"),
        str(LISTA_ORDEM_2015[8] + " - Visitante"),
        str(LISTA_ORDEM_2015[9] + " - Visitante"),
        str(LISTA_ORDEM_2015[10] + " - Visitante"),
        str(LISTA_ORDEM_2015[11] + " - Visitante"),
        str(LISTA_ORDEM_2015[12] + " - Visitante"),
        str(LISTA_ORDEM_2015[13] + " - Visitante"),
        str(LISTA_ORDEM_2015[14] + " - Visitante"),
        str(LISTA_ORDEM_2015[15] + " - Visitante"),
        str(LISTA_ORDEM_2015[16] + " - Visitante"),
        str(LISTA_ORDEM_2015[17] + " - Visitante"),
        str(LISTA_ORDEM_2015[18] + " - Visitante"),
        str(LISTA_ORDEM_2015[19] + " - Visitante"),

        "Dia do ano",
        "Minuto do dia",

        "Segunda- feira",
        "Terça-feira",
        "Quarta-feira",
        "Quinta-feira",
        "Sexta-feira",
        "Sábado",
        "Domingo",

        "Opção selecionada - Casa",
        "Opção selecionada - Empate",
        "Opção selecionada - Visitante",

        "Valor da odd",

        "Vitória do time da casa nos últimos " + str(quantidade_de_jogos_passados) + " jogos",
        "Vitória do time visitante nos últimos " + str(quantidade_de_jogos_passados) + " jogos",

        "Total de apostas",
        "Total apostado"]

    return cabecalho

def retorna_time_de_casa(row):
    return row[3].split('/')[3].split(' v ')[0].strip()

def retorna_time_visitante(row):
    return row[3].split('/')[3].split(' v ')[1].strip()

def retorna_dia_do_ano(row):
    return row[4].timetuple().tm_yday

def retorna_minuto_do_dia(row):
    return row[4].hour * 60 + row[4].minute

def retorna_dia_da_semana(row):
    encoder_dia = [0, 0, 0, 0, 0, 0, 0]

    encoder_dia[row[4].weekday()] = 1
    return encoder_dia

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

    indice = LISTA_ORDEM_2015.index(time)

    encoder_time[indice] = 1
    
    #raise ValueError("Time " + str(time)  + " não encontrado")

    return encoder_time

def retorna_quantidade_vitorias_time_da_casa(lista_ordenada, row, janela_jogos):
    nome_time = retorna_time_de_casa(row)
    return retorna_quantidade_vitorias_passadas(lista_ordenada, row, nome_time, janela_jogos)

def retorna_quantidade_vitorias_time_visitante(lista_ordenada, row, janela_jogos):
    nome_time = retorna_time_visitante(row)
    return retorna_quantidade_vitorias_passadas(lista_ordenada, row, nome_time, janela_jogos)

def retorna_quantidade_vitorias_passadas(lista_ordenada, row, nome_time, janela_jogos):
    if(janela_jogos <= 0):
        return 0

    quantidade_vitorias = 0
    lista_ultimos_jogos = []

    lista_jogos_anteriores = [x for x in lista_ordenada[:lista_ordenada.index(row)] if x[8] == nome_time and x[4] != row[4]]

    if len(lista_jogos_anteriores) > 0:

        lista_revertida = list(reversed(lista_jogos_anteriores))

        for linha_analisada in lista_revertida:

            if len([x for x in lista_ultimos_jogos if x[4] == linha_analisada[4]]) == 0:
                lista_ultimos_jogos.append(linha_analisada)

                if(len(lista_ultimos_jogos) == janela_jogos):
                    break

        quantidade_vitorias = len([x for x in lista_ultimos_jogos if x[14] == "1"])

    return quantidade_vitorias

def retorna_linha_tratada(lista_ordenada, row, quantidade_de_jogos_passados):

    row[3] = row[3].replace("Ateltico", "Atletico")
    row[8] = row[8].replace("Ateltico", "Atletico")

    row[3] = row[3].replace("Cortiba", "Coritiba")
    row[8] = row[8].replace("Cortiba", "Coritiba")

    colunas_time_casa = retorna_time(retorna_time_de_casa(row))
    colunas_time_visitante = retorna_time(retorna_time_visitante(row))
    #colunas_time_casa = encoder.transform([[LISTA_TIMES.index(retorna_time_de_casa(row))]]).toarray()[0]
    #colunas_time_visitante = encoder.transform([[LISTA_TIMES.index(retorna_time_visitante(row))]]).toarray()[0]
    colunas_opcao_selecionada = retorna_opcao_selecionada(row)
    colunas_dia_da_semana = retorna_dia_da_semana(row)
    

    linha_tratada = np.array([
        LISTA_ORDEM_2015.index(retorna_time_de_casa(row)),
        LISTA_ORDEM_2015.index(retorna_time_visitante(row)),

        colunas_time_casa[0],           # Time de casa
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

        colunas_dia_da_semana[0],       # Segunda-feira
        colunas_dia_da_semana[1],       # Terça-feira
        colunas_dia_da_semana[2],       # Quarta-feira
        colunas_dia_da_semana[3],       # Quinta-feira
        colunas_dia_da_semana[4],       # Sexta-feira
        colunas_dia_da_semana[5],       # Sábado
        colunas_dia_da_semana[6],       # Domingo

        colunas_opcao_selecionada[0],   # Opção selecionada - Casa
        colunas_opcao_selecionada[1],   # Opção selecionada - Empate
        colunas_opcao_selecionada[2],   # Opção selecionada - Visitante

        float(row[9]),                  # Valor da odd

        retorna_quantidade_vitorias_time_da_casa(lista_ordenada, row, quantidade_de_jogos_passados),    # N últimas vitórias
        retorna_quantidade_vitorias_time_visitante(lista_ordenada, row, quantidade_de_jogos_passados),

        float(row[10]),                 # Total de apostas
        float(row[11])                  # Total apostado
    ])

    return linha_tratada

def tratar_base(quantidade_de_jogos_passados):

    data_inicio = datetime.now()
    linhas_lidas = 0

    caminho_arquivo_final = "Bet/Resultado/base_tratada_2016_" + str(quantidade_de_jogos_passados) + "_jogos.csv"

    with open(caminho_arquivo_final, "wt", encoding='latin-1', newline='') as arquivo_final:

        writer = csv.writer(arquivo_final)
        writer.writerow(define_cabecalho(quantidade_de_jogos_passados))

        with open(CAMINHO_ARQUIVO_BASE_CRUA, "rt", encoding='latin-1') as arquivo_base:

            reader = csv.reader(arquivo_base)
            next(reader)

            lista_ordenada = []

            for row in reader:
                if row[2] != "":
                    row[2] = datetime.strptime(row[2], '%d-%m-%Y %H:%M:%S')

                if row[4] != "":
                    row[4] = datetime.strptime(row[4], '%d-%m-%Y %H:%M')

                if row[6] != "":
                    row[6] = datetime.strptime(row[6], '%d-%m-%Y %H:%M:%S')

                if row[12] != "":
                    row[12] = datetime.strptime(row[12], '%d-%m-%Y %H:%M:%S')

                if row[13] != "":
                    row[13] = datetime.strptime(row[13], '%d-%m-%Y %H:%M:%S')

                lista_ordenada.append(row)

            lista_ordenada = sorted(lista_ordenada, key=operator.itemgetter(4))
            #lista_ordenada = [x for x in lista_ordenada if x[12] <= x[4]]

            try:
                for row in lista_ordenada:
                    linhas_lidas += 1
                    linha_tratada = retorna_linha_tratada(lista_ordenada, row, quantidade_de_jogos_passados)
                    writer.writerow(linha_tratada)

            except Exception as e:
                excecao = e
            
    data_fim = datetime.now()

    print(str(linhas_lidas) + " linhas analisadas.")
    print("" + str(data_inicio) + " - " + str(data_fim) + " (" + str(data_fim - data_inicio) + ")")

lista_janela_jogos = [0, 3, 5]

for quantidade_de_jogos_passados in lista_janela_jogos:
    tratar_base(quantidade_de_jogos_passados)