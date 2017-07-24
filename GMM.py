import numpy as np
import operator
import random
import math
import sys
import matplotlib.pyplot as mp

datanup = np.loadtxt("clusters.txt", delimiter=',')
ha = datanup.shape[0]
lie = datanup.shape[1]

def calmean(datanup,k):
    ric = np.zeros((1, k))
    for i in range(0,k):
        ric[0,i]=random.uniform(0,1)


    np.mean(datanup, axis=0)

