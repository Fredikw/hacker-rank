import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

if __name__ == '__main__':
    # Read the first line of the file to get the values of F and N
    F, N = pd.read_csv('data.txt', sep=' ', header=None, nrows=1).iloc[0]

    # Read the T value from the line after the data set
    T = pd.read_csv('data.txt', header=None, skiprows=N+1, nrows=1)[0][0]

    # Read the first N lines of the file as the data set
    data = pd.read_csv('data.txt', sep=' ', header=None, skiprows=1, nrows=N)

    # Read the next T lines of the file as the test set
    test = pd.read_csv('data.txt', sep=' ', header=None, skiprows=N+2, nrows=T)

    # Transform the data into polynomial features of degree 4
    poly = PolynomialFeatures(degree=4)
    x_poly = poly.fit_transform(data.iloc[:, :2].values)

    # Fit a linear regression model to the transformed data
    model = LinearRegression()
    model.fit(x_poly, data.iloc[:, -1].values)

    # Transform the test set using the same transformation as the data set
    x_test = poly.transform(test.values)

    # Use the trained model to make predictions on the transformed test set
    pred = model.predict(x_test)

    # Print the predictions
    for val in pred:
        print("{:.2f}".format(val))