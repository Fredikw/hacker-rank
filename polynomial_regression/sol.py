import numpy
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

F , N = input().split()
F , N = int(F) , int(N)

train = numpy.array([input().split() for _ in range(N)] , float)

T = int(input())

test = numpy.array([input().split() for _ in range(T)] , float)

#polynomial pre-processing
poly = PolynomialFeatures(degree = 3)

train_poly = poly.fit_transform(train[: , : -1])
test_poly = poly.fit_transform(test)

#linear model
linear_model = LinearRegression()

linear_model.fit(train_poly , train[: , -1])
predictions = linear_model.predict(test_poly)

predictions = numpy.around(predictions , decimals = 2)
print(*predictions , sep = "\n")