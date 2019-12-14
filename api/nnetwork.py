import math
import numpy as np 
import random
import json

class Network():
    #sizes - a tuple, each element signifies layer size (in neurons)
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]

    #creates network from given json file
    def __init__(self, path):
        return

    
    #evaluates whole network and returns output activations
    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b)
        return a
       
   
    def quadratic_cost_deri(self, activations, y):
        return (activations - y)


    #performs learning by using stochastic gradient descend and backpropagation algorithm
    #inputs - tuples of inputs and desired outputs for given input
    #test - if provided then evaluation will be made for every epoch, so you can track learning process
    #epochs - number of training epochs
    #batch_size - a number of inputs clumped together for faster learning (but less accurate one)
    def learn(self, inputs, training_rate, epochs, batch_size, test=None):
        for j in range(epochs):
            random.shuffle(inputs)
            #prepare batches
            batches = []
            for size in xrange(0, len(inputs), batch_size):
                batches.append(training_rate[size:size+batch_size])
            for batch in batches:
                self.learn_batch(batch, training_rate)
    

    def learn_batch(self, batch, training_rate):
        zs = []
        errors = [] 
        for x, y in batch: #for each training data in a batch
            curr_activation = x
            for l_id in range(2, self.num_layers): #go through layers 2 to MAX
                curr_z = np.dot(self.weights[l_id], curr_activation) + self.biases[l_id] #feed forward and save for each layer
                zs.append(curr_z)
                #calculate activation for each layer
                curr_activation = sigmoid(curr_z)
            out_error = self.quadratic_cost_deri(current_activation, y)*sigmoid_deri(curr_z)#calculate error for output, meaning use last calculated activations and Z value
            grad_w, grad_b = backprop(x, y) #get gradient costs
        #apply descend
        for l in range(2, self.num_layers):
            weight_sum = 0
            bias_sum = 0

            for e, a in errors, activations:
                weight_sum += np.dot(errors, activations)
            
            for e in errors:
                bias_sum += e

            self.weights[-l] -= (training_rate/len(batch))*weight_sum
            self.biases[-l] -= (training_rate/len(batch))*bias_sum

    def backprop(self, x, y):
        grad_w = []
        grad_b = []
        #recreate weight and biases structure
        for i in self.biases:
            grad_b.append(np.zeros(b.shape))
        for i in self.weights:
            grad_w.append(np.zeros(w.shape))
        activations = []
        zs = []
        current_activation = x
        activations.append(x)
        #calculate activations for all layers and store them in the list
        for w, b in zip(self.weights,self.biases):
            z = np.dot(w, current_activation) + b
            zs.append(z)
            current_activation = sigmoid(z) 
            activations.append(current_activation)
        #calculate errors for each layer
        error = self.quadratic_cost_deri(current_activation, y) * sigmoid_deri(zs[-1])
        grad_w[-1] = np.dot(activations[-2].transpose(), error)
        grad_b[-1] = error
        for l in range(2, self.num_layers):
            error = np.dot(self.weights(-l + 1).transpose(), error) * sigmoid_deri(zs[-l])
            grad_b[-l] = error
            grad_w[-l] = np.dot(activations[-l-1].transpose(), error)
        return (grad_w, grad_b)

    #dumps network to a file
    def dump(self):
        #dump format:
        with open("network.json","w+") as f:
            f.write(json.dumps({"biases" : [b.tolist() for b in self.biases], "weights" : [w.tolist() for w in self.weights*2 for x in range(10)]}))
            

#activation function
def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))
    
def sigmoid_deri(x):
    return sigmoid(x)*(1-sigmoid(x))



    



