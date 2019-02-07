import random

import numpy as np
import numpy
import matplotlib.pyplot as plt

from Calc import NeuralNetwork
from Data import train_data_1, train_data_2, train_data_3, train_data_4, train_data_5, test_data_1, test_data_2, \
    test_data_3, test_data_4, test_data_5
from Utils import interpolateAndNormalizeDate, prepareArray

sizeInput = 900
input_nodes = sizeInput - 1
hidden_nodes = 200
output_nodes = 5
learning_rate = 0.01
formatedTrainData = []
epochs = 20


# Підготовка навчальних даних


def predict_result(msg, json):
    result = interpolateAndNormalizeDate(json, 1)
    formatedTestData = prepareArray(result, sizeInput)
    result = n.query(((numpy.asfarray(formatedTestData[:sizeInput - 1]) * 0.99) + 0.01))
    print(str(msg) + " ->")
    print(str(result))


# Підготовка тренувальних даних


def prepareDataForTest(data, title, id_result):
    secondPersonData = []
    for x in range(len(data)):
        result = interpolateAndNormalizeDate(data[x], id_result)
        if result != None:
            flush = prepareArray(result[:sizeInput], sizeInput)
            secondPersonData.append(flush)
    formatedTrainData.extend(secondPersonData)


def trainNetwork():
    for e in range(epochs):
        for record in formatedTrainData:
            all_values = record

            inputs = (numpy.asfarray(all_values[1:]) * 0.99) + 0.01
            targets = numpy.zeros(output_nodes) + 0.01

            index_correct_answer = int(all_values[0])
            targets[index_correct_answer] = 0.99
            n.train(inputs, targets)

random.seed(69)

prepareDataForTest(train_data_1, "1", 0)
prepareDataForTest(train_data_2, "2", 1)
prepareDataForTest(train_data_3, "3", 2)
prepareDataForTest(train_data_4, "4", 3)
prepareDataForTest(train_data_5, "5", 4)

random.shuffle(formatedTrainData)

n = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
trainNetwork()

predict_result("Calm: ", test_data_5[2])



x = test_data_2[2]["xReal"]
y = test_data_2[2]["yReal"]
plt.plot(x, y)

x = train_data_2[2]["xReal"]
y = train_data_2[2]["yReal"]
plt.gca().invert_yaxis()
plt.plot(x, y)
plt.show()