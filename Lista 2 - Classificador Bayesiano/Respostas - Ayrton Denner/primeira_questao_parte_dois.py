import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from numpy.linalg import inv
from mpl_toolkits.mplot3d import Axes3D
import itertools

def get_range():
    return np.arange(0, 10, 0.1)

def calcula_variancia(lista_um, lista_dois):
    return sum((lista_um - np.average(lista_um)) * (lista_dois - np.average(lista_dois)))/len(lista_um)

def calcula_matriz_covariancia(lista_um, lista_dois):
    return np.matrix([[calcula_variancia(lista_um, lista_um), calcula_variancia(lista_um, lista_dois)],
                      [calcula_variancia(lista_dois, lista_um), calcula_variancia(lista_dois, lista_dois)]])

def calcula_gaussiana_multivariada(lista_propriedades, x_values):

    lista_um = lista_propriedades[0]
    lista_dois = lista_propriedades[1]

    covariancia = calcula_matriz_covariancia(lista_um, lista_dois)

    media = np.array([np.average(lista_um), np.average(lista_dois)])

    z_values = []
    for x in x_values[0]:
        z_line = []
        for y in x_values[0]:
            diferenca_media = np.array([x, y]) - media
            calculo_gaussiana_multivariada = plot_gaussiana_multivariada(lista_propriedades, diferenca_media, covariancia)
            if calculo_gaussiana_multivariada <= 0.01:
                calculo_gaussiana_multivariada = float('nan')
            z_line.append(calculo_gaussiana_multivariada)
        z_values.append(z_line)
    
    return z_values

def plot_gaussiana_multivariada(lista_propriedades, diferenca_media, covariancia):

    divisor = (2 * np.pi)**(len(lista_propriedades)/2) * np.linalg.det(covariancia)**(1/2)

    expoente = np.dot(-1/2 * np.transpose(diferenca_media) * inv(covariancia), diferenca_media)

    gaussiana_multivariada = (1/(divisor)) * (np.e ** float(expoente)) 

    return gaussiana_multivariada

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

array_c1 = [np.array([float(x[0]), float(x[1]), float(x[2]), float(x[3])]) for x in array_todo if x[4] == "Iris-setosa"]
array_c2 = [np.array([float(x[0]), float(x[1]), float(x[2]), float(x[3])]) for x in array_todo if x[4] == "Iris-versicolor"]
array_c3 = [np.array([float(x[0]), float(x[1]), float(x[2]), float(x[3])]) for x in array_todo if x[4] == "Iris-virginica"]

array_c1_treino = array_c1[:35]
array_c1_teste = array_c1[-15:]

array_c2_treino = array_c2[:35]
array_c2_teste = array_c2[-15:]

array_c3_treino = array_c3[:35]
array_c3_teste = array_c3[-15:]

switcher = {
    0: "Sepal Lenght",
    1: "Sepal Width",
    2: "Petal Lenght",
    3: "Petal Width",
}

casa_um = 0
casa_dois = 0
casa_tres = 0

# 0 = Sepal Lenght (SL)
# 1 = Sepal Width (SW)
# 2 = Petal Lenght (PL)
# 3 = Petal Width (PW)
for i in np.arange(4):
    for j in np.arange(4):
        if i < j:
            array_c1 = np.array([[x[i] for x in array_c1_treino], [x[j] for x in array_c1_treino]])
            array_c2 = np.array([[x[i] for x in array_c2_treino], [x[j] for x in array_c2_treino]])
            array_c3 = np.array([[x[i] for x in array_c3_treino], [x[j] for x in array_c3_treino]])

            x_values = np.arange(-1, 10, 0.1)
            y_values = np.arange(-1, 10, 0.1)
            x_values, y_values = np.meshgrid(x_values, y_values)

            figure = plt.figure(1)
            ax = figure.add_subplot(2, 3, casa_tres + 1, projection='3d')
            ax.set_xlabel(str(switcher.get(i, "")))
            ax.set_ylabel(str(switcher.get(j, "")))
            ax.set_zlabel("Resultado")

            z_values = calcula_gaussiana_multivariada(np.array([array_c1[0], array_c1[1]]), x_values)
            ax.plot_surface(y_values, x_values, z_values, color = "green")

            z_values = calcula_gaussiana_multivariada(np.array([array_c2[0], array_c2[1]]), x_values)
            ax.plot_surface(y_values, x_values, z_values, color = "red")

            z_values = calcula_gaussiana_multivariada(np.array([array_c3[0], array_c3[1]]), x_values)
            ax.plot_surface(y_values, x_values, z_values, color = "blue")

            casa_tres += 1

plt.show()