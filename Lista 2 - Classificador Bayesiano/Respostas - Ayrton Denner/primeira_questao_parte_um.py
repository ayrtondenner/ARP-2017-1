import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

def get_range():
    return np.arange(0, 10, 0.1)

def plot_gaussiana(lista_itens):

    media = np.average(lista_itens)

    variancia = sum((lista_itens - media)**2)/len(lista_itens)

    gaussiana = 1/(np.sqrt(2 * np.pi * variancia)) * np.e ** (-(get_range() - media) ** 2/(2 * variancia))

    return gaussiana

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
    0: "SL",
    1: "SW",
    2: "PL",
    3: "PW",
}

# 0 = Sepal Lenght (SL)
# 1 = Sepal Width (SW)
# 2 = Petal Lenght (PL)
# 3 = Petal Width (PW)
for n in range(0, 4):

    figure = plt.figure(1)

    lista_array_treino = [sorted([x[n] for x in array_c1_treino]), sorted([x[n] for x in array_c2_treino]), sorted([x[n] for x in array_c3_treino])]

    plot_sl_1 = plot_gaussiana(lista_array_treino[0])
    plot_sl_2 = plot_gaussiana(lista_array_treino[1])
    plot_sl_3 = plot_gaussiana(lista_array_treino[2])

    range = get_range()

    #axes = plt.gca()
    #axes.set_ylim([0, 5])
    #plt.subplot(211 + n) #211 => 212 => 213 => 214
    axes = figure.add_subplot(2, 2, n+1)
    axes.set_ylim([0, 4])

    plt.plot(range, plot_sl_1, color = "green")
    plt.plot(range, plot_sl_2, color = "red")
    plt.plot(range, plot_sl_3, color = "blue")

    propriedade = [str(switcher.get(n, "") + ": Iris-setosa"), str(switcher.get(n, "") + ": Iris-versicolor"), str(switcher.get(n, "") + ": Iris-virginica")]

    plt.legend(handles=[mpatches.Patch(color='green', label=propriedade[0]), mpatches.Patch(color='red', label=propriedade[1]), mpatches.Patch(color='blue', label=propriedade[2])])

plt.show()