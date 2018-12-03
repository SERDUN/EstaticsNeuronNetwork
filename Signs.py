import random

import numpy
import matplotlib.pyplot as plt

from Calc import NeuralNetwork
from Data import train_data_0, train_data_1, test_data_0, test_data_1, train_data_2
from Utils import getSignsForData, normalization

sizeInput = 6
input_nodes = sizeInput - 1
hidden_nodes = 100
output_nodes = 3
learning_rate = 0.2
formatedTrainData = []
formatedTestData = []
epochs = 15


def trainNetwork():
    for e in range(epochs):
        for record in formatedTrainData:
            all_values = record

            inputs = (numpy.asfarray(all_values[1:]) * 0.99) + 0.01
            targets = numpy.zeros(output_nodes) + 0.01

            index_correct_answer = int(all_values[0])
            targets[index_correct_answer] = 0.99
            n.train(inputs, targets)


def prepareDataForTest(data, list, id_result, name):
    resultSigns = []
    for i in range(len(data)):
        x = numpy.array(data[i]["xReal"])
        y = 1080 - numpy.array(data[i]["yReal"])
        signs = getSignsForData(x, y)
        signs = normalization(signs)
        resultSigns.extend([id_result])
        resultSigns.extend(signs)
        list.append(resultSigns)
        plt.plot(resultSigns[1:])

        resultSigns = []

    plt.axis([0, 4, 0, 1])
    plt.title(name)

    plt.grid(True)
    plt.show()
    print()


prepareDataForTest(train_data_0, formatedTrainData, 0, "vlad")  # vlad
prepareDataForTest(train_data_1, formatedTrainData, 1, "serdun")  # serdun
prepareDataForTest(train_data_2, formatedTrainData, 2, "loha")  # loha

prepareDataForTest(test_data_0, formatedTestData, 1, "serdun")  # serdun
random.shuffle(formatedTrainData)

# prepareDataForTest(train_data_1, "Kate", 1)

n = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
trainNetwork()

test = formatedTestData[0][1:]
result = n.query(((numpy.asfarray(test) * 0.99) + 0.01))
print(result)
