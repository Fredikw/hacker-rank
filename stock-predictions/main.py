import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def print_transactions(m: float, k: int, d: int, names: np.ndarray, owned: np.ndarray) -> str:
    """Print the transactions for a given day.

    Parameters:
    - m: The amount of money left.
    - k: The number of stocks.
    - d: The number of days for which stock prices are received.
    - names: An array of the names of the stocks.
    - owned: An array of the number of stocks owned for each stock.

    Returns:
    - A string representing the transactions for the day.
    """
    return ""

def main():
    """Read data from a file, process it, and print the transactions."""
    # Read data from a file
    data = pd.read_csv("data_raw.txt", sep=" ", header=None, index_col=0).transpose()

    # Show data
    # data.plot()
    # plt.show()
    # # data.to_csv("output.csv")

    # Set variables
    m = 100  # money left
    k = 10  # number of stocks
    n = 5  # number of days for which stock prices are received

    d_tot = data.count()
    names = data.columns.to_numpy()
    owned = np.array([])

    # Iterate over the rows of the dataframe
    for i, row in data.iterrows():
        if i < 5:
            continue

        d = d_tot - i
        prices = data[i-n:i].to_numpy().transpose()

        print_transactions(m, k, d, names, owned)

        print(row)


if __name__ == "__main__":
    main()