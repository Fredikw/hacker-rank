import numpy as np
import pandas as pd

if __name__ == '__main__':
    physics_scores = input().split()[2:]
    history_scores = input().split()[2:]

    physics_scores = [int(x) for x in physics_scores]
    history_scores = [int(x) for x in history_scores]

    r = np.corrcoef(physics_scores, history_scores)[0, 1]

    print(f'Pearsons r: {r:.3f}')