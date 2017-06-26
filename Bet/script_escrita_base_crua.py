import csv 
from datetime import datetime
import glob
from itertools import islice

data_inicio_total = datetime.now()

linhas_lidas_total = 0
linhas_brasil_total = 0
arquivo_lido = 0

lista_arquivos = glob.glob("Bet/CSV/2016/bfinf_other_1*.csv")

caminho_arquivo_final = "Bet/Resultado/base_2016.csv"

with open(caminho_arquivo_final, "wt", encoding='latin-1', newline='') as arquivo_final:

    writer = csv.writer(arquivo_final)

    with open(lista_arquivos[0], "rt", encoding='latin-1') as primeiro_arquivo:

        reader = csv.reader(primeiro_arquivo)

        primeira_linha = next(islice(reader, 0, 1))

        # Salvando o cabeçalho
        writer.writerow(primeira_linha)

    for arquivo_csv in lista_arquivos:

        data_inicio = datetime.now()
        linhas_lidas = 0
        linhas_brasil = 0

        with open(arquivo_csv, "rt", encoding='latin-1') as arquivo:

            reader = csv.reader(arquivo)

            try:
                for row in reader:
                    linhas_lidas += 1

                    if("Brazilian Soccer/Campeonato" in row[3] and "2016" in row[4] and "Match Odds" == row[5]): # Se for uma linha da série A do ano em específico
                        writer.writerow(row)
                        linhas_brasil += 1

            except Exception as e:
                excecao = e

        linhas_brasil_total += linhas_brasil
        linhas_lidas_total += linhas_lidas
        arquivo_lido += 1

        data_fim = datetime.now()

        print("Arquivo #" + str(arquivo_lido) + " - " + arquivo_csv.split("\\")[-1] + ":")
        print("Tempo: " + str(data_inicio) + " - " + str(data_fim) + "(" + str(data_fim - data_inicio) + ")")
        print("Linhas: " + str(linhas_brasil) + "/" + str(linhas_lidas))
        print("\n")
        
data_fim_total = datetime.now()

print("\n\n------------------------------------------------------\n\n")
print(str(len(lista_arquivos)) + " arquivos analisados.")
print("" + str(data_inicio_total) + " - " + str(data_fim_total) + " (" + str(data_fim_total - data_inicio_total) + ")")
print("Total: " + str(linhas_brasil_total) + "/" + str(linhas_lidas_total))