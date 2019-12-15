import math
import numpy as np 
import random
import json

class Network():
    #sizes - a tuple, each element signifies layer size (in neurons)
    def __init__(self, sizes=None, path=None):
        if sizes:
            self.num_layers = len(sizes)
            self.sizes = sizes
            self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
            self.weights = [np.random.randn(y, x)
                            for x, y in zip(sizes[:-1], sizes[1:])]
            print(len(self.biases))
            print(len(self.weights))
            return

        if path:
            with open(path, "r") as f:
                data = json.loads(f.read())
                self.num_layers = data["num_layers"]
                self.sizes = data["sizes"]
                self.biases = np.array(data["biases"])
                self.weights = np.array(data["weights"])

    
    #evaluates whole network and returns output activations
    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b)
        return a
       
   
    def quadratic_cost_deri(self, activations, y):
        return (activations - y)


    def evaluate(self, test_data):
        correct = 0 
        for d in test_data:
            test_results = self.feedforward(d[0])
            #average results
            results = []
            for t in test_results:
                results.append(np.average(t))
            if np.argmax(results) == np.argmax(d[1]):
                correct += 1
        return correct






          #performs learning by using stochastic gradient descend and backpropagation algorithm
    #inputs - tuples of inputs and desired outputs for given input
    #test - if provided then evaluation will be made for every epoch, so you can track learning process
    #epochs - number of training epochs
    #batch_size - a number of inputs clumped together for faster learning (but less accurate one)
    def learn(self, inputs, training_rate, epochs, batch_size, test=None):

        print("begun learning...")
        for j in range(epochs):
            random.shuffle(inputs)
            #prepare batches
            batches = []
            for size in range(0, len(inputs), batch_size):
                batches.append(inputs[size:size+batch_size])
            for batch in batches:
                self.learn_batch(batch, training_rate)
            print("EPOCH" + str(j))
            if test:
                print("Epoch {0}: {1} / {2}".format(
                    j, self.evaluate(test), len(test)))
            else:
                print("Epoch {0} complete".format(j))

    def learn_batch(self, batch, training_rate):
        grad_w_sum = None
        grad_b_sum = None
        for x, y in batch: #for each training data in a batch
            grad_w, grad_b = self.backprop(x, y)
            for l in range(self.num_layers - 2, 0,-1):
                if grad_w_sum == None:
                    grad_w_sum = grad_w[l]
                    grad_b_sum = grad_b[l]
                    continue
                grad_w_sum += grad_w[l]
                grad_b_sum += grad_b[l]
                print(type(grad_w_sum))
                self.biases[l] -= grad_b_sum*float(training_rate/len(batch))
                self.weights[l] -= grad_w_sum*float(training_rate/len(batch))
        

    def backprop(self, x, y):
        grad_w = []
        grad_b = []
        #recreate weight and biases structure
        for i in self.biases:
            grad_b.append(np.zeros(i.shape))
        for i in self.weights:
            grad_w.append(np.zeros(i.shape))
        activations = []
        zs = []
        current_activation = np.asarray(x)
        activations.append(current_activation)
        #calculate activations for all layers and store them in the list
        for w, b in zip(self.weights,self.biases):
            z = np.dot(w, current_activation) + b
            zs.append(z)
            current_activation = sigmoid(z) 
            activations.append(current_activation)
        #calculate errors for each layer
        error = self.quadratic_cost_deri(current_activation, y) * sigmoid_deri(zs[-1])
        grad_w[-1] = np.dot(error, activations[-2].transpose())
        grad_b[-1] = error
        for l in range(self.num_layers-2, 0, -1):
            error = np.dot(self.weights[l].transpose(), error) * sigmoid_deri(zs[l])
            grad_b[l] = error
            grad_w[l] = np.dot(error, activations[l - 1].transpose())
        return (grad_w, grad_b)

    #dumps network to a file
    def dump(self):
        #dump format:
        with open("network.json","w+") as f:
            f.write(json.dumps({"sizes" : self.sizes, "num_layers" : self.num_layers, "biases" : [b.tolist() for b in self.biases], "weights" : [w.tolist() for w in self.weights]}))
            

#activation function
def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))
    
def sigmoid_deri(x):
    return sigmoid(x)*(1-sigmoid(x))



    



