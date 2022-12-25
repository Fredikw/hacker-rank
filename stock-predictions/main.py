import csv
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor


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
    
    file_path = "data.csv"

    # Check if the file exists
    if os.path.exists(file_path):
        data = pd.read_csv(file_path)

        # Add stock prices for today
        data.loc[len(data)] = [prices[i][-1] for i in range(len(names))]

    else:
        data = pd.DataFrame()
    
        # Add stock prices for the last five days
        for i in range(k):
            data[names[i]] = prices[i]
    
    data.to_csv(file_path, index=False)

    # Sell everything
    orders = ""
    number_of_transactions = 0

    for i, shares in enumerate(owned):
        
        if shares == 0:
            continue
        
        orders += f"\n{names[i]} SELL {shares}"
        number_of_transactions += 1
        m += shares*prices[i][-1]

    # Find target values for prediction model
    daily_return = ((data.shift(periods=-1) - data)/data).dropna().values

    days = np.arange(1, len(daily_return)+1).reshape(-1, 1)

    # Prediction model
    model = MultiOutputRegressor(RandomForestRegressor())
    model.fit(days, daily_return)

    pred = model.predict([[len(days)+1]])

    # Find stock with positiv return
    sorted_returns = pred[0][np.argsort(-pred)][0]
    sorted_returns_stock_names = data.columns.to_numpy()[np.argsort(-pred)][0]

    # Buy stocks with expected positiv return
    for i in range(np.count_nonzero(sorted_returns > 0)):
        price = prices[np.where(names == sorted_returns_stock_names[i])[0][0]][-1]
        
        if m >= price:
            shares = m//price
            orders += f"\n{sorted_returns_stock_names[i]} BUY {shares}"
            number_of_transactions += 1
            m -= shares*price
    
    if number_of_transactions > 0:
        lines = orders.splitlines()
        lines[0] = str(number_of_transactions)
        orders = '\n'.join(lines)

    return orders

def main():    
    """Read data from a file, process it, and print the transactions."""

    os.remove("data.csv")

    data = pd.read_csv("data_train_raw.txt", sep=" ", header=None, index_col=0).transpose()
    # # Show data
    # data.plot()
    # plt.show()
    
    # Set variables
    m = 100  # money left
    k = 10   # number of stocks
    n = 5    # number of days for which stock prices are received

    names = data.columns.to_numpy()
    owned = np.zeros(k)

    # Iterate over the rows of the dataframe
    for i, row in data.iterrows():
        if i < 5:
            continue

        d = data.count() - i
        prices = data[i-n:i].to_numpy().transpose()

        orders = print_transactions(m, k, d, names, owned, prices)

        # Executing order
        for i, order in enumerate(orders.splitlines()):
            if i == 0: continue

            stock, order_type, num_shares = order.split()

            num_shares = int(float(num_shares))
            
            stock_price = row.loc[stock]

            name_idx = np.argwhere(names == stock)[0][0]

            if order_type == "SELL":

                owned[name_idx] -= num_shares
                
                m += stock_price*num_shares

            if order_type == "BUY":

                if stock_price*num_shares <= m:

                    m -= stock_price*num_shares
                  
                    owned[name_idx] += num_shares

    # Market value
    market_val = np.sum(owned*row.to_numpy()) + m
    print(market_val)

if __name__ == "__main__":
    main()