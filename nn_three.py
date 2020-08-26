# -*- coding: utf-8 -*-
"""
@author: Thiru Nadesan
"""

'''This code implements forward and backward propagation of a 3-layered neural network######
The 3 layered neural network has been formed by 1 input layer, 1 hidden layer and 1 output layer.
The number of neurons in each layer are taken to be 2, 4 and 1 respectively.

Assumption: A binary classification problem has been defined with the output layer treated with
            sigmoid activation function.

Variables: W1, W2 - weights, while initializing the bias is also included as the final value
           b1, b2 - bias
           x - inputs
           y - binary output 
           A1 - activation of layer 1
           A2 - activation of output layer

Functions : "dat": planar classifier data generation
            "acti": returns sigmoid activation function
            "for_prop": applies forward propagation to the input data
            "compute_cost" : returns the logistic regression cost
            "back_prop": returns updated weights and biases
            '''
import numpy as np 

def dat():
    np.random.seed(42)
    m = 400 
    N = int(m/2) 
    D = 2 
    X = np.zeros((m,D))
    Y = np.zeros((m,1), dtype='uint8') 
    a = 4
    for j in range(2):
        ix = range(N*j,N*(j+1))
        t = np.linspace(j*3.12,(j+1)*3.12,N) + np.random.randn(N)*0.2 # theta
        r = a*np.sin(4*t) + np.random.randn(N)*0.2 # radius
        X[ix] = np.c_[r*np.sin(t), r*np.cos(t)]
        Y[ix] = j     
    X = X.T
    Y = Y.T
    
    return X, Y

def acti(z):
    return 1.0/(1.0+np.exp(-z))

def for_prop(X, W1, W2, b1, b2): 
  
    Z1 = np.dot(W1, X) + b1 
    A1 = np.tanh(Z1) 
    Z2 = np.dot(W2, A1) + b2 
    A2 = acti(Z2) 
      
    # here the cache is the data of previous iteration 
    # This will be used for backpropagation 
    cache = {"Z1": Z1, 
             "A1": A1, 
             "Z2": Z2, 
             "A2": A2} 
      
    return A2, cache  

def c_cost(A2, Y, m): 
     
    cost_sum = np.multiply(np.log(A2), Y) + np.multiply((1 - Y), np.log(1 - A2)) 
    cost = - np.sum(cost_sum) / m  
    cost = np.squeeze(cost) 
    return cost 

def back_prop(W1, b1, W2, b2, cache, learning_rate, m, x, y): 
    
    A1 = cache['A1'] 
    A2 = cache['A2'] 
    
    '''back prop'''  
    dZ2 = A2 - y
    dW2 = (1 / m) * np.dot(dZ2, A1.T) 
    db2 = (1 / m) * np.sum(dZ2, axis = 1, keepdims = True) 
  
    dZ1 = np.multiply(np.dot(W2.T, dZ2), 1 - np.power(A1, 2)) 
    dW1 = (1 / m) * np.dot(dZ1, x.T) 
    db1 = (1 / m) * np.sum(dZ1, axis = 1, keepdims = True) 
      
    '''weights and biases update'''
    W1 = W1 - learning_rate * dW1 
    b1 = b1 - learning_rate * db1 
    W2 = W2 - learning_rate * dW2 
    b2 = b2 - learning_rate * db2 
  
    return W1, W2, b1, b2 

if __name__=="__main__":
    x, y = dat()
    ''' initializing random weights and biases'''
    n_hidden = 4
    n_features = x.shape[0]
    n_output = y.shape[0]

    w1 = np.random.randn(n_hidden, n_features) * 0.01
    b1 = np.zeros(shape =(n_hidden, 1)) 
  
    w2 = np.random.randn(n_output, n_hidden) * 0.01
    b2 = np.zeros(shape =(n_output, 1))
    
    num_iterations = 100
    learning_rate = 0.01
    m = y.shape[1]
    '''forward and backward propagation'''
    for i in range(0, num_iterations): 
        A2, cache = for_prop(x, w1, w2, b1, b2) 
        cost = c_cost(A2, y, m)  
        w1, w2, b1, b2 = back_prop(w1, b1, w2, b2, cache, learning_rate, m, x, y)
        print ("Cost after iteration % i: % f" % (i, cost)) 