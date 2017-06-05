import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

def get_range():
    return np.arange(0, 10, 0.1)

def plot_gaussiana(lista_valores_treino, lista_valores_teste):

    media = np.average(lista_valores_treino)

    variancia = sum((lista_valores_treino - media)**2)/len(lista_valores_treino)

    gaussiana = 1/(np.sqrt(2 * np.pi * variancia)) * np.e ** (-(lista_valores_teste - media) ** 2/(2 * variancia))

    return gaussiana

def calcula_probabilidade(classe, lista_valores):

    lista_classes = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
    classe_selecionada = lista_classes[classe]

    array_treino = []
    array_treino.extend(array_c1_treino)
    array_treino.extend(array_c2_treino)
    array_treino.extend(array_c3_treino)

    array_classe = [np.array([float(x[0]), float(x[1]), float(x[2]), float(x[3])]) for x in array_treino if x[4] == classe_selecionada]

    probabilidade_classe = len(array_classe)/len(array_treino)

    probabilidade_SL = plot_gaussiana([x[0] for x in array_classe], float(lista_valores[0]))
    probabilidade_SW = plot_gaussiana([x[1] for x in array_classe], float(lista_valores[1]))
    probabilidade_PL = plot_gaussiana([x[2] for x in array_classe], float(lista_valores[2]))
    probabilidade_PW = plot_gaussiana([x[3] for x in array_classe], float(lista_valores[3]))

    probabilidades_propriedades = probabilidade_SL * probabilidade_SW * probabilidade_PL * probabilidade_PW

    probabilidade_final = probabilidade_classe * probabilidades_propriedades
    return probabilidade_final

def retorna_provavel_resultado(lista_valores):
    lista_resultado = [calcula_probabilidade(0, lista_valores), calcula_probabilidade(1, lista_valores), calcula_probabilidade(2, lista_valores)]
    classe_escolhida = lista_resultado.index(max(lista_resultado))

    lista_classes = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
    classe_selecionada = lista_classes[classe_escolhida]

    print("Entrada:", lista_valores, "Probabilidades:", lista_resultado, "Escolhido:", classe_selecionada, "Resposta:", lista_valores[4])
    print("Resultado:", classe_selecionada == lista_valores[4])
    return classe_escolhida

array_todo = np.array([
    np.array([5.1, 3.5, 1.4, 0.2, "Iris-setosa"]),
    np.array([4.9, 3.0, 1.4, 0.2, "Iris-setosa"]),
    np.array([4.7, 3.2, 1.3, 0.2, "Iris-setosa"]),
    np.array([4.6, 3.1, 1.5, 0.2, "Iris-setosa"]),
    np.array([5.0, 3.6, 1.4, 0.2, "Iris-setosa"]),
    np.array([5.4, 3.9, 1.7, 0.4, "Iris-setosa"]),
    np.array([4.6, 3.4, 1.4, 0.3, "Iris-setosa"]),
    np.array([5.0, 3.4, 1.5, 0.2, "Iris-setosa"]),
    np.array([4.4, 2.9, 1.4, 0.2, "Iris-setosa"]),
    np.array([4.9, 3.1, 1.5, 0.1, "Iris-setosa"]),
    np.array([5.4, 3.7, 1.5, 0.2, "Iris-setosa"]),
    np.array([4.8, 3.4, 1.6, 0.2, "Iris-setosa"]),
    np.array([4.8, 3.0, 1.4, 0.1, "Iris-setosa"]),
    np.array([4.3, 3.0, 1.1, 0.1, "Iris-setosa"]),
    np.array([5.8, 4.0, 1.2, 0.2, "Iris-setosa"]),
    np.array([5.7, 4.4, 1.5, 0.4, "Iris-setosa"]),
    np.array([5.4, 3.9, 1.3, 0.4, "Iris-setosa"]),
    np.array([5.1, 3.5, 1.4, 0.3, "Iris-setosa"]),
    np.array([5.7, 3.8, 1.7, 0.3, "Iris-setosa"]),
    np.array([5.1, 3.8, 1.5, 0.3, "Iris-setosa"]),
    np.array([5.4, 3.4, 1.7, 0.2, "Iris-setosa"]),
    np.array([5.1, 3.7, 1.5, 0.4, "Iris-setosa"]),
    np.array([4.6, 3.6, 1.0, 0.2, "Iris-setosa"]),
    np.array([5.1, 3.3, 1.7, 0.5, "Iris-setosa"]),
    np.array([4.8, 3.4, 1.9, 0.2, "Iris-setosa"]),
    np.array([5.0, 3.0, 1.6, 0.2, "Iris-setosa"]),
    np.array([5.0, 3.4, 1.6, 0.4, "Iris-setosa"]),
    np.array([5.2, 3.5, 1.5, 0.2, "Iris-setosa"]),
    np.array([5.2, 3.4, 1.4, 0.2, "Iris-setosa"]),
    np.array([4.7, 3.2, 1.6, 0.2, "Iris-setosa"]),
    np.array([4.8, 3.1, 1.6, 0.2, "Iris-setosa"]),
    np.array([5.4, 3.4, 1.5, 0.4, "Iris-setosa"]),
    np.array([5.2, 4.1, 1.5, 0.1, "Iris-setosa"]),
    np.array([5.5, 4.2, 1.4, 0.2, "Iris-setosa"]),
    np.array([4.9, 3.1, 1.5, 0.1, "Iris-setosa"]),

    np.array([5.0, 3.2, 1.2, 0.2, "Iris-setosa"]),
    np.array([5.5, 3.5, 1.3, 0.2, "Iris-setosa"]),
    np.array([4.9, 3.1, 1.5, 0.1, "Iris-setosa"]),
    np.array([4.4, 3.0, 1.3, 0.2, "Iris-setosa"]),
    np.array([5.1, 3.4, 1.5, 0.2, "Iris-setosa"]),
    np.array([5.0, 3.5, 1.3, 0.3, "Iris-setosa"]),
    np.array([4.5, 2.3, 1.3, 0.3, "Iris-setosa"]),
    np.array([4.4, 3.2, 1.3, 0.2, "Iris-setosa"]),
    np.array([5.0, 3.5, 1.6, 0.6, "Iris-setosa"]),
    np.array([5.1, 3.8, 1.9, 0.4, "Iris-setosa"]),
    np.array([4.8, 3.0, 1.4, 0.3, "Iris-setosa"]),
    np.array([5.1, 3.8, 1.6, 0.2, "Iris-setosa"]),
    np.array([4.6, 3.2, 1.4, 0.2, "Iris-setosa"]),
    np.array([5.3, 3.7, 1.5, 0.2, "Iris-setosa"]),
    np.array([5.0, 3.3, 1.4, 0.2, "Iris-setosa"]),

    np.array([7.0, 3.2, 4.7, 1.4, "Iris-versicolor"]),
    np.array([6.4, 3.2, 4.5, 1.5, "Iris-versicolor"]),
    np.array([6.9, 3.1, 4.9, 1.5, "Iris-versicolor"]),
    np.array([5.5, 2.3, 4.0, 1.3, "Iris-versicolor"]),
    np.array([6.5, 2.8, 4.6, 1.5, "Iris-versicolor"]),
    np.array([5.7, 2.8, 4.5, 1.3, "Iris-versicolor"]),
    np.array([6.3, 3.3, 4.7, 1.6, "Iris-versicolor"]),
    np.array([4.9, 2.4, 3.3, 1.0, "Iris-versicolor"]),
    np.array([6.6, 2.9, 4.6, 1.3, "Iris-versicolor"]),
    np.array([5.2, 2.7, 3.9, 1.4, "Iris-versicolor"]),
    np.array([5.0, 2.0, 3.5, 1.0, "Iris-versicolor"]),
    np.array([5.9, 3.0, 4.2, 1.5, "Iris-versicolor"]),
    np.array([6.0, 2.2, 4.0, 1.0, "Iris-versicolor"]),
    np.array([6.1, 2.9, 4.7, 1.4, "Iris-versicolor"]),
    np.array([5.6, 2.9, 3.6, 1.3, "Iris-versicolor"]),
    np.array([6.7, 3.1, 4.4, 1.4, "Iris-versicolor"]),
    np.array([5.6, 3.0, 4.5, 1.5, "Iris-versicolor"]),
    np.array([5.8, 2.7, 4.1, 1.0, "Iris-versicolor"]),
    np.array([6.2, 2.2, 4.5, 1.5, "Iris-versicolor"]),
    np.array([5.6, 2.5, 3.9, 1.1, "Iris-versicolor"]),
    np.array([5.9, 3.2, 4.8, 1.8, "Iris-versicolor"]),
    np.array([6.1, 2.8, 4.0, 1.3, "Iris-versicolor"]),
    np.array([6.3, 2.5, 4.9, 1.5, "Iris-versicolor"]),
    np.array([6.1, 2.8, 4.7, 1.2, "Iris-versicolor"]),
    np.array([6.4, 2.9, 4.3, 1.3, "Iris-versicolor"]),
    np.array([6.6, 3.0, 4.4, 1.4, "Iris-versicolor"]),
    np.array([6.8, 2.8, 4.8, 1.4, "Iris-versicolor"]),
    np.array([6.7, 3.0, 5.0, 1.7, "Iris-versicolor"]),
    np.array([6.0, 2.9, 4.5, 1.5, "Iris-versicolor"]),
    np.array([5.7, 2.6, 3.5, 1.0, "Iris-versicolor"]),
    np.array([5.5, 2.4, 3.8, 1.1, "Iris-versicolor"]),
    np.array([5.5, 2.4, 3.7, 1.0, "Iris-versicolor"]),
    np.array([5.8, 2.7, 3.9, 1.2, "Iris-versicolor"]),
    np.array([6.0, 2.7, 5.1, 1.6, "Iris-versicolor"]),
    np.array([5.4, 3.0, 4.5, 1.5, "Iris-versicolor"]),

    np.array([6.0, 3.4, 4.5, 1.6, "Iris-versicolor"]),
    np.array([6.7, 3.1, 4.7, 1.5, "Iris-versicolor"]),
    np.array([6.3, 2.3, 4.4, 1.3, "Iris-versicolor"]),
    np.array([5.6, 3.0, 4.1, 1.3, "Iris-versicolor"]),
    np.array([5.5, 2.5, 4.0, 1.3, "Iris-versicolor"]),
    np.array([5.5, 2.6, 4.4, 1.2, "Iris-versicolor"]),
    np.array([6.1, 3.0, 4.6, 1.4, "Iris-versicolor"]),
    np.array([5.8, 2.6, 4.0, 1.2, "Iris-versicolor"]),
    np.array([5.0, 2.3, 3.3, 1.0, "Iris-versicolor"]),
    np.array([5.6, 2.7, 4.2, 1.3, "Iris-versicolor"]),
    np.array([5.7, 3.0, 4.2, 1.2, "Iris-versicolor"]),
    np.array([5.7, 2.9, 4.2, 1.3, "Iris-versicolor"]),
    np.array([6.2, 2.9, 4.3, 1.3, "Iris-versicolor"]),
    np.array([5.1, 2.5, 3.0, 1.1, "Iris-versicolor"]),
    np.array([5.7, 2.8, 4.1, 1.3, "Iris-versicolor"]),

    np.array([6.3, 3.3, 6.0, 2.5, "Iris-virginica"]),
    np.array([5.8, 2.7, 5.1, 1.9, "Iris-virginica"]),
    np.array([7.1, 3.0, 5.9, 2.1, "Iris-virginica"]),
    np.array([6.3, 2.9, 5.6, 1.8, "Iris-virginica"]),
    np.array([6.5, 3.0, 5.8, 2.2, "Iris-virginica"]),
    np.array([7.6, 3.0, 6.6, 2.1, "Iris-virginica"]),
    np.array([4.9, 2.5, 4.5, 1.7, "Iris-virginica"]),
    np.array([7.3, 2.9, 6.3, 1.8, "Iris-virginica"]),
    np.array([6.7, 2.5, 5.8, 1.8, "Iris-virginica"]),
    np.array([7.2, 3.6, 6.1, 2.5, "Iris-virginica"]),
    np.array([6.5, 3.2, 5.1, 2.0, "Iris-virginica"]),
    np.array([6.4, 2.7, 5.3, 1.9, "Iris-virginica"]),
    np.array([6.8, 3.0, 5.5, 2.1, "Iris-virginica"]),
    np.array([5.7, 2.5, 5.0, 2.0, "Iris-virginica"]),
    np.array([5.8, 2.8, 5.1, 2.4, "Iris-virginica"]),
    np.array([6.4, 3.2, 5.3, 2.3, "Iris-virginica"]),
    np.array([6.5, 3.0, 5.5, 1.8, "Iris-virginica"]),
    np.array([7.7, 3.8, 6.7, 2.2, "Iris-virginica"]),
    np.array([7.7, 2.6, 6.9, 2.3, "Iris-virginica"]),
    np.array([6.0, 2.2, 5.0, 1.5, "Iris-virginica"]),
    np.array([6.9, 3.2, 5.7, 2.3, "Iris-virginica"]),
    np.array([5.6, 2.8, 4.9, 2.0, "Iris-virginica"]),
    np.array([7.7, 2.8, 6.7, 2.0, "Iris-virginica"]),
    np.array([6.3, 2.7, 4.9, 1.8, "Iris-virginica"]),
    np.array([6.7, 3.3, 5.7, 2.1, "Iris-virginica"]),
    np.array([7.2, 3.2, 6.0, 1.8, "Iris-virginica"]),
    np.array([6.2, 2.8, 4.8, 1.8, "Iris-virginica"]),
    np.array([6.1, 3.0, 4.9, 1.8, "Iris-virginica"]),
    np.array([6.4, 2.8, 5.6, 2.1, "Iris-virginica"]),
    np.array([7.2, 3.0, 5.8, 1.6, "Iris-virginica"]),
    np.array([7.4, 2.8, 6.1, 1.9, "Iris-virginica"]),
    np.array([7.9, 3.8, 6.4, 2.0, "Iris-virginica"]),
    np.array([6.4, 2.8, 5.6, 2.2, "Iris-virginica"]),
    np.array([6.3, 2.8, 5.1, 1.5, "Iris-virginica"]),
    np.array([6.1, 2.6, 5.6, 1.4, "Iris-virginica"]),
    
    np.array([7.7, 3.0, 6.1, 2.3, "Iris-virginica"]),
    np.array([6.3, 3.4, 5.6, 2.4, "Iris-virginica"]),
    np.array([6.4, 3.1, 5.5, 1.8, "Iris-virginica"]),
    np.array([6.0, 3.0, 4.8, 1.8, "Iris-virginica"]),
    np.array([6.9, 3.1, 5.4, 2.1, "Iris-virginica"]),
    np.array([6.7, 3.1, 5.6, 2.4, "Iris-virginica"]),
    np.array([6.9, 3.1, 5.1, 2.3, "Iris-virginica"]),
    np.array([5.8, 2.7, 5.1, 1.9, "Iris-virginica"]),
    np.array([6.8, 3.2, 5.9, 2.3, "Iris-virginica"]),
    np.array([6.7, 3.3, 5.7, 2.5, "Iris-virginica"]),
    np.array([6.7, 3.0, 5.2, 2.3, "Iris-virginica"]),
    np.array([6.3, 2.5, 5.0, 1.9, "Iris-virginica"]),
    np.array([6.5, 3.0, 5.2, 2.0, "Iris-virginica"]),
    np.array([6.2, 3.4, 5.4, 2.3, "Iris-virginica"]),
    np.array([5.9, 3.0, 5.1, 1.8, "Iris-virginica"])])

array_c1 = [np.array([float(x[0]), float(x[1]), float(x[2]), float(x[3]), str(x[4])]) for x in array_todo if x[4] == "Iris-setosa"]
array_c2 = [np.array([float(x[0]), float(x[1]), float(x[2]), float(x[3]), str(x[4])]) for x in array_todo if x[4] == "Iris-versicolor"]
array_c3 = [np.array([float(x[0]), float(x[1]), float(x[2]), float(x[3]), str(x[4])]) for x in array_todo if x[4] == "Iris-virginica"]

array_c1_treino = array_c1[:35]
array_c1_teste = array_c1[-15:]

array_c2_treino = array_c2[:35]
array_c2_teste = array_c2[-15:]

array_c3_treino = array_c3[:35]
array_c3_teste = array_c3[-15:]

comparacoes_c1 = []
comparacoes_c2 = []
comparacoes_c3 = []

for linha in array_c1_teste:
    comparacoes_c1.append(retorna_provavel_resultado(linha))

for linha in array_c2_teste:
    comparacoes_c2.append(retorna_provavel_resultado(linha))

for linha in array_c3_teste:
    comparacoes_c3.append(retorna_provavel_resultado(linha))


tamanho_vetor_corretos_c1 = len([x for x in comparacoes_c1 if x == 0])
tamanho_vetor_total_c1 = len(comparacoes_c1)
tamanho_vetor_corretos_c2 = len([x for x in comparacoes_c2 if x == 1])
tamanho_vetor_total_c2 = len(comparacoes_c2)
tamanho_vetor_corretos_c3 = len([x for x in comparacoes_c3 if x == 2])
tamanho_vetor_total_c3 = len(comparacoes_c3)

print("Resultado da 1ª classe: ", tamanho_vetor_corretos_c1, "/", tamanho_vetor_total_c1, " = ", tamanho_vetor_corretos_c1/tamanho_vetor_total_c1 * 100, "%")
print("Resultado da 2ª classe: ", tamanho_vetor_corretos_c2, "/", tamanho_vetor_total_c2, " = ", tamanho_vetor_corretos_c2/tamanho_vetor_total_c2 * 100, "%")
print("Resultado da 3ª classe: ", tamanho_vetor_corretos_c3, "/", tamanho_vetor_total_c3, " = ", tamanho_vetor_corretos_c3/tamanho_vetor_total_c3 * 100, "%")