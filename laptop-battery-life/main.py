#!/bin/python3

import math
import os
import random
import re
import sys
from sklearn.linear_model import LinearRegression
import pandas as pd

if __name__ == '__main__':
    timeCharged = float(input().strip())
    
    dataset = pd.read_csv('trainingdata.txt', header=None)
    
    # Remove items with a duration greater then 8.
    dataset = dataset[dataset.iloc[:,1] < 8]
    
    dataset.insert(0, len(dataset.columns), 0)
    
    # Separe variables
    X = dataset.iloc[:,0:2]
    Y = dataset.iloc[:,2]

    model = LinearRegression().fit(X, Y)
    
    result = model.predict([[0, timeCharged]])
    
    if result[0] > 8:
        print (8.0)
    else:
        print("{:.2f}".format(result[0]))   