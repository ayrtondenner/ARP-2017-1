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
from itertools import groupby
import copy
import re

OPCAO_CASA = 0
OPCAO_EMPATE = 1
OPCAO_VISITANTE = 2

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

        # "Opção selecionada - Casa",
        # "Opção selecionada - Empate",
        # "Opção selecionada - Visitante",

        # "Valor da odd",

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

def retorna_vetor_opcao_selecionada(row):
    encoder_opcao = [0, 0, 0]

    encoder_opcao[retorna_opcao_selecionada(row)] = 1

    return encoder_opcao

def retorna_opcao_selecionada(row):
    if row[8] == retorna_time_de_casa(row):
        # TIME DA CASA
        return OPCAO_CASA
    elif row[8] == retorna_time_visitante(row):
        # TIME VISITANTE
        return OPCAO_VISITANTE
    else:
        # EMPATE
        return OPCAO_EMPATE

def converte_opcao_pelo_numero(numero):

    if numero == OPCAO_CASA:
        return "Casa"
    elif numero == OPCAO_EMPATE:
        return "Empate"
    elif numero == OPCAO_VISITANTE:
        return "Visitante"
    else:
        raise ValueError("Valor não encontrado")

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
    if janela_jogos <= 0:
        return 0

    quantidade_vitorias = 0
    lista_ultimos_jogos = []

    lista_jogos_anteriores = [x for x in lista_ordenada[:lista_ordenada.index(row)] if nome_time in x[3] and x[3] != row[3]]

    lista_janela = lista_jogos_anteriores[-janela_jogos:]

    if len(lista_janela) > 0:

        quantidade_vitorias = len([x for x in lista_janela if x[8] == nome_time])

    return quantidade_vitorias

def retorna_linha_tratada(lista_ordenada, row, quantidade_de_jogos_passados):

    row[3] = row[3].replace("Ateltico", "Atletico")
    row[8] = row[8].replace("Ateltico", "Atletico")

    row[3] = row[3].replace("Cortiba", "Coritiba")
    row[8] = row[8].replace("Cortiba", "Coritiba")

    colunas_time_casa = retorna_time(retorna_time_de_casa(row))
    colunas_time_visitante = retorna_time(retorna_time_visitante(row))

    #colunas_opcao_selecionada = retorna_vetor_opcao_selecionada(row)

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

        #colunas_opcao_selecionada[0],   # Opção selecionada - Casa
        #colunas_opcao_selecionada[1],   # Opção selecionada - Empate
        #colunas_opcao_selecionada[2],   # Opção selecionada - Visitante

        #float(row[9]),                  # Valor da odd

        retorna_quantidade_vitorias_time_da_casa(lista_ordenada, row, quantidade_de_jogos_passados),    # N últimas vitórias
        retorna_quantidade_vitorias_time_visitante(lista_ordenada, row, quantidade_de_jogos_passados),

        #float(row[10]),                 # Total de apostas
        #float(row[11])                  # Total apostado

        row[9],                         # Opção com maior quantidade de apostas
        row[10]                         # Opção com maior quantidade apostada
    ])

    return linha_tratada

def tratar_base(quantidade_de_jogos_passados):

    data_inicio = datetime.now()
    linhas_lidas = 0

    caminho_arquivo_final = "Bet/Resultado/base_tratada_2016_" + str(quantidade_de_jogos_passados) + "_jogos_categorizado.csv"

    with open(caminho_arquivo_final, "wt", encoding='latin-1', newline='') as arquivo_final:

        writer = csv.writer(arquivo_final)
        writer.writerow(define_cabecalho(quantidade_de_jogos_passados))

        with open(CAMINHO_ARQUIVO_BASE_CRUA, "rt", encoding='latin-1') as arquivo_base:

            reader = csv.reader(arquivo_base)
            next(reader) # O script vai pular a leitura do cabeçalho do arquivo original

            lista_itens = [x for x in reader]

            # Organiza as strings da descrição do evento
            for item in lista_itens:
                # Brazilian Soccer/Campeonato/Fixtures 01 October   / Santos v Atletico PR
                #item[1] = int(item[1])
                item[3] = re.sub('\s+', ' ', item[3]).replace(" /", "/").replace("/ ", "/")

            # # Ordena lista pela descrição do evento
            lista_ordenada = sorted(lista_itens, key=operator.itemgetter(3))

            lista_com_grupos = groupby(lista_ordenada, lambda x: x[3])

            lista_agrupada = []

            for key, group in lista_com_grupos:

                # Soma de apostas de casa, empate e visitante
                quantidade_apostas = [0, 0, 0]

                # Soma de valores apostados de casa, empate e visitante
                quantidade_apostado = [0, 0, 0]

                lista_grupo = list(group)

                for item in lista_grupo:
                    opcao_selecionada = retorna_opcao_selecionada(item)

                    quantidade_apostas[opcao_selecionada] += int(item[10])
                    quantidade_apostado[opcao_selecionada] += float(item[11])

                linha_agrupada = copy.copy(item)

                # Removendo coisas específicas da opção selecionada
                del linha_agrupada[14]  # WIN_FLAG
                del linha_agrupada[13]  # FIRST_TAKEN
                del linha_agrupada[12]  # LATEST_TAKEN
                del linha_agrupada[11]  # VOLUME_MATCHED
                del linha_agrupada[10]  # NUMBER_BETS
                del linha_agrupada[9]   # ODDS
                del linha_agrupada[8]   # SELECTION
                del linha_agrupada[7]   # SELECTION_ID

                if linha_agrupada[2] != "":
                    linha_agrupada[2] = datetime.strptime(linha_agrupada[2], '%d-%m-%Y %H:%M:%S')

                if linha_agrupada[4] != "":
                    linha_agrupada[4] = datetime.strptime(linha_agrupada[4], '%d-%m-%Y %H:%M')

                if linha_agrupada[6] != "":
                    linha_agrupada[6] = datetime.strptime(linha_agrupada[6], '%d-%m-%Y %H:%M:%S')

                try:
                    time_vencedor = [x for x in lista_grupo if x[14] == "1"][0][8]
                except Exception as ex:
                    if linha_agrupada[1] == 125204259:
                        time_vencedor = "America MG"
                    elif linha_agrupada[1] == 126779168:
                        time_vencedor = "Flamengo"
                    elif linha_agrupada[1] == 127817213:
                        time_vencedor = "Atletico PR"
                    else:
                        raise RuntimeError("Alternativa para jogo com exceção não encontrada!")

                linha_agrupada.append(time_vencedor)

                indice_quantidade_apostas = quantidade_apostas.index(max(quantidade_apostas))
                indice_quantidade_apostado = quantidade_apostado.index(max(quantidade_apostado))

                linha_agrupada.append(converte_opcao_pelo_numero(indice_quantidade_apostas))
                linha_agrupada.append(converte_opcao_pelo_numero(indice_quantidade_apostado))

                lista_agrupada.append(linha_agrupada)

        # Ordena as linhas pela data de início do jogo
        lista_ordenada = sorted(lista_agrupada, key=operator.itemgetter(4))

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

####################################################################################################

#lista_janela_jogos = [0, 3, 5]
lista_janela_jogos = [5]

for quantidade_de_jogos_passados in lista_janela_jogos:
    tratar_base(quantidade_de_jogos_passados)