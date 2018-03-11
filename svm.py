from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt

filename = 'dataset.txt'

puredata = np.loadtxt(filename, delimiter=',')
X = puredata[:, 1:]
Y = puredata[:, 0]