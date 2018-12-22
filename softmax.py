import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    expL = np.exp(L)
    sumexpL = sum(expL)
    result =  [i/sumexpL for i in expL]
    return result

def sigmoid(L):
    result = [1 / float(1 + np.exp(- x)) for x in L] 
    return result

#Lets consider the score after the perceptron
# Duck = 2 
# Bever = 1
# penguin = 0 
lis = [2,1,0]
sigmoid_inputs = [2, 3, 5, 6]
result = softmax(sigmoid_inputs)
resultsig = sigmoid(sigmoid_inputs)
print(" Softmax \n \nThe probability of it being Duck is {}\nThe probability of it being Bevenr is {}\nThe probability of it being Penguin is {}\n".format(result[0],result[1],result[2]))
print(" Sigmoid \n \nThe Prediction of it being Duck is {}\nThe Prediction of it being Bevenr is {}\nThe Prediction of it being Penguin is {}\n".format(resultsig[0],resultsig[1],resultsig[2]))