#! /usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Adaptative Linear Neuron
class Adaline(object):
    """ ADAptative LInear NEuron classifier

        Args:
            eta : float
                Learning rate (between 0.0 and 1.0)
            n_iter : int
                Passes over the training dataset

        Attributes:
            w_ : 1D array
                Weights after fitting
            errors_ : list
                Number of misclassifications in every epoch
    """
    eta = 0.01
    n_inter = 10
    w_ = []
    errors_ = []
    cost_ = []

    def __init__(self, eta=0.01, n_inter=50):
        self.eta = eta
        self.n_inter = n_inter

    def fit(self, X, y):
        """ Fit training data

            Args:
                X : {array-like}, shape = [n_samples, n_features]
                    Training vectors, where n_samples is the number of samples and n_features is the number of features.
                y : array-like, shape = [n_samples]
                    Target values

            Returns:
                self : object
        """
        self.w_ = np.zeros(1 + X.shape[1])
        self.cost_ = []

        for i in range(self.n_inter):
            output = self.net_input(X)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)

        return self

    def net_input(self, X):
        """ Calculate net input """
        return np.dot(X, self.w[1:]) + self.w_[0]

    def activation(self, X):
        """ Compute linear activation """
        return self.net_input(X)

    def predict(self, X):
        """ Return class label after unit sptep """
        return np.where(self.activation(X) >= 0.0, 1, -1)

def main():
    ada = Adaline()

if __name__ == '__main__':
    main()
