import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import csv 
import sys
import datetime
import glob

#1,"131769911","28-05-2017 23:52:05","Brazilian Soccer/Campeonato/Fixtures 28 May
# /Botafogo RJ v Bahia","28-05-2017 22:00","Over/Under 1.5 Goals","28-05-2017 22:00:04","1221385","Under 1.5 Goals","2.96","25","246.98",
# "28-05-2017 23:09:31","28-05-2017 22:04:12","1","IP"

data_inicio = datetime.datetime.now()

caminho_base = "Bet/CSV/base_2017.csv"

array_entrada = []
array_saida = []

with open(caminho_base, "rt", encoding='utf-8') as arquivo_base:

        reader = csv.reader(arquivo_base)

        try:
            for row in reader:
                array_linha_entrada = np.array([
                    row[3].split('/')[3].split(' v ')[0],   # Time de casa
                    row[3].split('/')[3].split(' v ')[1],   # Time visitante
                    row[4],                                 # Dia do ano
                    row[4],                                 # Minuto do dia
                    row[8],                                 # Opção selecionada
                    row[9]                                  # Valor da odd
                ])

                array_linha_saida = np.array([
                    row[10],                                # Total de apostas
                    row[11]                                 # Total apostado
                ])

                array_entrada.append(array_linha_entrada)
                array_saida.append(array_linha_saida)

        except Exception as e:
            nada = e
        
data_fim = datetime.datetime.now()

print("\n\n------------------------------------------------------\n\n")
#print(str(len(lista_arquivos)) + " linhas analisados.")
print("" + str(data_inicio) + " - " + str(data_fim) + " (" + str(data_fim - data_inicio) + ")")