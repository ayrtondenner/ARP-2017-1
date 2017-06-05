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

data_inicio_total = datetime.datetime.now()

linhas_lidas_total = 0
linhas_brasil_total = 0
arquivo_lido = 0

lista_arquivos = glob.glob("Bet/CSV/bfinf_other_17*.csv")

for arquivo_csv in lista_arquivos:

    data_inicio = datetime.datetime.now()
    linhas_lidas = 0
    linhas_brasil = 0

    with open(arquivo_csv, "rt", encoding='utf-8') as arquivo:

        #csv_file = open('Bet/csv_teste.csv', "rt")

        reader = csv.reader(arquivo)
        try:
            for row in reader:
                linha = str(row).replace('[', '').replace(']', '')
                linhas_lidas += 1

                if(linha.find("Brazilian Soccer/Campeonato") != -1) and (linha.find("Match Odds") != -1):
                    linha_result = linha.split(',')
                    nada = linha_result[3]
                    linhas_brasil += 1

                if(reader.line_num == 1394):
                    vazio = 0
        except Exception as e:
            nada = e

    linhas_brasil_total += linhas_brasil
    linhas_lidas_total += linhas_lidas
    arquivo_lido += 1

    data_fim = datetime.datetime.now()

    print("Arquivo #" + str(arquivo_lido) + ":")
    print("Tempo: " + str(data_inicio) + " - " + str(data_fim) + "(" + str(data_fim - data_inicio) + ")")
    print("Linhas: " + str(linhas_brasil) + "/" + str(linhas_lidas))
    print("\n")
        
data_fim_total = datetime.datetime.now()

print("\n\n------------------------------------------------------\n\n")
print(str(len(lista_arquivos)) + " arquivos analisados.")
print("" + str(data_inicio_total) + " - " + str(data_fim_total) + "(" + str(data_fim_total - data_inicio_total) + ")")
print("Total: " + str(linhas_brasil_total) + "/" + str(linhas_lidas_total))
nada = 0