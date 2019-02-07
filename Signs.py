import random

import numpy
import matplotlib.pyplot as plt

from Calc import NeuralNetwork
from Data import train_data_0, test_data_0, test_data_1, train_data_3
from Utils import getSignsForData, normalization

sizeInput = 6
input_nodes = sizeInput - 1
hidden_nodes = 4
output_nodes = 2
learning_rate = 0.1
formatedTrainData = []
formatedTestData = []
epochs = 10


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


prepareDataForTest(train_data_0, formatedTrainData, 0, "not calm")  # not calm 1
prepareDataForTest(train_data_3, formatedTrainData, 1, "calm")  # calm 3
prepareDataForTest(test_data_1, formatedTestData,0, "not calm")  # serdun
random.shuffle(formatedTrainData)

n = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
trainNetwork()

test = formatedTestData[0][1:]
result = n.query(((numpy.asfarray(test) * 0.99) + 0.01))
print(result)
