import random

import numpy as np
import numpy
import matplotlib.pyplot as plt

from Calc import NeuralNetwork
from Data import train_data_0, train_data_3, test_data_1, test_data_0
from Utils import interpolateAndNormalizeDate, prepareArray
from VisualizationData import drawNormalizarionValue

sizeInput = 900
input_nodes = sizeInput - 1
hidden_nodes = 50
output_nodes = 2
learning_rate = 0.1
formatedTrainData = []
epochs = 20

# Підготовка навчальних даних



def guessTest(msg, json):
    result = interpolateAndNormalizeDate(json, 1)
    formatedTestData = prepareArray(result, sizeInput)
    result = n.query(((numpy.asfarray(formatedTestData[:sizeInput - 1]) * 0.99) + 0.01))
    drawNormalizarionValue([formatedTestData], msg)
    print(str(msg) + " ->")
    print(str(result))


# Підготовка тренувальних даних





def prepareDataForTest(data, title, id_result):
    secondPersonData = []
    for x in range(len(data)):
        result = interpolateAndNormalizeDate(data[x], id_result)
        flush = prepareArray(result[:sizeInput], sizeInput)
        secondPersonData.append(flush)
    formatedTrainData.extend(secondPersonData)
    drawNormalizarionValue(secondPersonData, title)


def trainNetwork():
    for e in range(epochs):
        for record in formatedTrainData:
            all_values = record

            inputs = (numpy.asfarray(all_values[1:]) * 0.99) + 0.01
            targets = numpy.zeros(output_nodes) + 0.01

            index_correct_answer = int(all_values[0])
            targets[index_correct_answer] = 0.99
            n.train(inputs, targets)


random.seed(33)
prepareDataForTest(train_data_0, "not calm 1", 0)
prepareDataForTest(train_data_3, "calm 3", 1)
random.shuffle(formatedTrainData)


n = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
trainNetwork()

guessTest(" not Calm: ", test_data_0[0])



x = test_data_0[1]["xReal"]
y = test_data_0[1]["yReal"]
plt.plot(x, y)

plt.gca().invert_yaxis()
plt.show()


x = train_data_0[1]["xReal"]
y = train_data_0[1]["yReal"]
plt.gca().invert_yaxis()
plt.plot(x, y)
plt.show()



