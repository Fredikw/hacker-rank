import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras

def main():

    '''
    Read data
    '''
    data = pd.read_csv("data.txt", sep=" ", header=None, index_col=0).transpose()
    # Read row in dataframe as with df[start:stop:step]
    
    '''
    Plot data
    '''
    # data.plot()
    # plt.show()
    # plt.savefig("data.svg")

    '''
    Model
    '''
    model = keras.models.Sequential()


if __name__ == "__main__":

    main()