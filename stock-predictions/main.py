import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def print_transactions(m: float, k: int, d: int, names: np.ndarray, owned: np.ndarray, prices: np.ndarray) -> str:
    """Print the transactions for a given day.

    Parameters:
    - m: The amount of money left.
    - k: The number of stocks.
    - d: The number of days for which stock prices are received.
    - names: An array of the names of the stocks.
    - owned: An array of the number of stocks owned for each stock.
    - prices: An array of the prices for the stocks for the current and last four days

    Returns:
    - A string representing the transactions for the day.
    """
    return "2 \nUFL BUY 1\nUCB BUY 1"

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
    owned = np.zeros(k)

    # Iterate over the rows of the dataframe
    for i, row in data.iterrows():
        if i < 4:
            continue

        d = d_tot - i
        prices = data[i-n:i].to_numpy().transpose()

        orders = print_transactions(m, k, d, names, owned, prices)

        # Executing order
        for i, order in enumerate(orders.splitlines()):
            if i == 0: continue

            stock, order_type, num_shares = order.split()

            num_shares = int(num_shares)
            
            stock_price = row.loc[stock]

            name_idx = np.argwhere(names == stock)[0][0]

            if order_type == "SELL":

                m += stock_price*num_shares

                owned[name_idx] -= num_shares

            if order_type == "BUY":

                if stock_price*num_shares <= m:

                    m -= stock_price*num_shares

                    owned[name_idx] += num_shares

if __name__ == "__main__":
    main()