import matplotlib.pyplot as plt
import numpy as np

# Método para desenhar a grid e deixar ela atrás dos pontos e das retas
def prepara_grid():
    figure = plt.figure()
    axis = figure.gca()
    axis.set_axisbelow(True)    
    plt.grid(linestyle = ":")
    return

# Método para colocar os labels do gráfico
def seta_labels(title, xlabel, ylabel):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    return
    
# Método para calcular b0
def calcula_b0(lista_x, lista_y, b1):
    # Média(Y) - b1 * Média(X)
    return np.average(lista_y) - b1 * np.average(lista_x)

# Método para calcular b1
def calcula_b1(lista_x, lista_y):
    # Soma(X * Y)/Soma(X * X)
    return sum(np.multiply(lista_x, lista_y))/sum(np.multiply(lista_x, lista_x))

# Método para retornar os coeficientes da reta
def calcula_coeficientes(lista_x, lista_y):
    # Y = b0 + b1 * X
    b1 = calcula_b1(lista_x, lista_y)
    b0 = calcula_b0(lista_x, lista_y, b1)
    return {"b0": b0, "b1": b1}

# Método para calcular e desenhar a reta de acordo com os coeficientes
def calcula_reta(lista_x, b0, b1):
    # Y = b0 + b1 * X
    return b0 + lista_x * b1

def calcula_erro_quadratico_medio(lista_y_real, lista_y_estimado):
    return sum(np.subtract(lista_y_real, lista_y_estimado))**2/len(lista_y_real)

def calcula_coeficiente_determinacao(lista_x, lista_y):
    # R² = Soma(X * Y)/(Soma(X * X) * Soma(Y * Y))
    return sum(np.multiply(lista_x, lista_y))**2 / (sum(np.multiply(lista_x, lista_x)) * sum(np.multiply(lista_y, lista_y)))

prepara_grid()

array_idade = np.array([10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 44, 50, 60, 70])
array_probabilidade = np.array([0.05, 0.06, 0.07, 0.08, 0.1, 0.1, 0.11, 0.12, 0.12, 0.12, 0.18, 0.2, 0.21, 0.21, 0.23, 0.28, 0.4, 0.5, 0.6, 0.7])

lista_dados_x = array_idade[:10]
lista_dados_y = array_probabilidade[:10]

lista_coeficientes = calcula_coeficientes(lista_dados_x, lista_dados_y)

reta_calculada = calcula_reta(lista_dados_x, lista_coeficientes["b0"], lista_coeficientes["b1"])

plt.scatter(lista_dados_x, lista_dados_y)
plt.plot(lista_dados_x, reta_calculada, "-")

erro_quadratico_medio = calcula_erro_quadratico_medio(lista_dados_y, reta_calculada)
coeficiente_determinacao = calcula_coeficiente_determinacao(lista_dados_x, lista_dados_y)

seta_labels("Exercício um\nPrimeira parte", "Idade", "Probab. ataque cardíaco")

plt.show()