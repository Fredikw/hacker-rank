import numpy as np
from statistics import mode
from scipy.stats import norm

if __name__ == "__main__":

    # Read input from STDIN
    input = input("Sample Input: ")

    values = np.array(input.splitlines()[1].split(), dtype=int)
    
    conf_interval = norm.interval(0.95, loc=np.mean(values), scale=np.std(values))

    print(np.mean(values))
    print(np.median(values))
    print(mode(values))
    print(np.std(values))
    print(conf_interval[0], conf_interval[1])