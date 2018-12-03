import numpy
# scipy.special for the sigmoid function expit()
import scipy.special
# library for plotting arrays
import matplotlib.pyplot


# ensure the plots are inside this notebook, not an external window
class NeuralNetwork:

    # initialise the neural network
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # set number of nodes in each input, hidden, output layer
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        # link weight matrices, wih and who
        # weights inside the arrays are w_i_j, where link is from node i to node j in the next layer
        # w11 w21
        # w12 w22 etc
        numpy.random.seed(44)

        self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
        numpy.random.seed(44)

        self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))
        # with open('wih.txt', 'w') as f:
        #     for item in self.wih:
        #         f.write("%s\n" % item)
        #
        # with open('who.txt', 'w') as f:
        #     for item in self.who.to:
        #         f.write("%s\n" % item)


        #
        # with open('wih.txt') as f:
        #     self.wih = f.read().splitlines()
        #
        # with open('who.txt') as f:
        #     self.who = f.read().splitlines()

        # learning rate
        self.lr = learningrate

        # activation function is the sigmoid function
        self.activation_function = lambda x: scipy.special.expit(x)

        pass

    # train the neural network
    def train(self, inputs_list, targets_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        # print(hidden_outputs)


        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        # output layer error is the (target - actual)
        output_errors = targets - final_outputs
        # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
        hidden_errors = numpy.dot(self.who.T, output_errors)

            # update the weights for the links between the hidden and output layers
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)),
                                        numpy.transpose(hidden_outputs))

        # update the weights for the links between the input and hidden layers
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                                        numpy.transpose(inputs))

        pass

    # query the neural network
    def query(self, inputs_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T

        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        return final_outputs

# all_values = data_list[0].split(',')
# image_array = np.asfarray(all_values[1:]).reshape((28,28))
# plt.imshow(image_array, cmap='Greys', interpolation='None')
# scaled_input=np.asfarray(all_values[1:])/(255*0.9)+0.1
# print(scaled_input)
# plt.show()

# scorecard = []
#
# # go through all the records in the test data set
# for record in test_data_list:
#     # split the record by the ',' commas
#     all_values = record.split(',')
#     # correct answer is first value
#     correct_label = int(all_values[0])
#     # scale and shift the inputs
#     inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
#     # query the network
#     outputs = n.query(inputs)
#     # the index of the highest value corresponds to the label
#     label = numpy.argmax(outputs)
#     # append correct or incorrect to list
#     if (label == correct_label):
#         # network's answer matches correct answer, add 1 to scorecard
#         scorecard.append(1)
#     else:
#         # network's answer doesn't match correct answer, add 0 to scorecard
#         scorecard.append(0)
#         pass
#
#     pass
#
# scorecard_array = numpy.asarray(scorecard)
# print ("performance = ", scorecard_array.sum() / scorecard_array.size)
