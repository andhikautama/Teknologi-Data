import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams["figure.figsize"] = (10, 5)
rcParams["axes.spines.top"] = False
rcParams["axes.spines.right"] = False

# The entire code for the class to implement multiple linear regression
class LinearRegression:
    def __init__(self, learning_rate=0.01, n_iterations=10000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights, self.bias = None, None
        self.loss = []

    @staticmethod
    def _mean_squared_error(y, y_hat):
        error = 0
        for i in range(len(y)):
            error += (y[i] - y_hat[i]) ** 2
        return error / len(y)

    def fit(self, X, y):
        # 1. Initialize weights and bias to zeros
        self.weights = np.zeros(X.shape[1])
        self.bias = 0

        # 2. Perform gradient descent
        for i in range(self.n_iterations):
            # Line equation
            y_hat = np.dot(X, self.weights) + self.bias
            loss = self._mean_squared_error(y, y_hat)
            self.loss.append(loss)

            # Calculate derivatives
            partial_w = (1 / X.shape[0]) * (2 * np.dot(X.T, (y_hat - y)))
            partial_d = (1 / X.shape[0]) * (2 * np.sum(y_hat - y))

            # Update the coefficients
            self.weights -= self.learning_rate * partial_w
            self.bias -= self.learning_rate * partial_d

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias


from sklearn.datasets import load_diabetes

data = load_diabetes()
X = data.data
y = data.target

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
preds = model.predict(X_test)
print(preds)
print(model._mean_squared_error(y_test, preds))

# The plotting of the loss
xs = np.arange(len(model.loss))
ys = model.loss

plt.plot(xs, ys, lw=3, c="#087E8B")
plt.title("Loss per iteration (MSE)", size=20)
plt.xlabel("Iteration", size=14)
plt.ylabel("Loss", size=14)
plt.show()

# We train a couple of models with different learning rates and compare loss curves to produce a good quality model
losses = {}
for lr in [0.5, 0.1, 0.01, 0.001]:
    model = LinearRegression(learning_rate=lr)
    model.fit(X_train, y_train)
    losses[f"LR={str(lr)}"] = model.loss

xs = np.arange(len(model.loss))

plt.plot(
    xs, losses["LR=0.5"], lw=3, label=f"LR = 0.5, Final = {losses['LR=0.5'][-1]:.2f}"
)
plt.plot(
    xs, losses["LR=0.1"], lw=3, label=f"LR = 0.1, Final = {losses['LR=0.1'][-1]:.2f}"
)
plt.plot(
    xs, losses["LR=0.01"], lw=3, label=f"LR = 0.01, Final = {losses['LR=0.01'][-1]:.2f}"
)
plt.plot(
    xs,
    losses["LR=0.001"],
    lw=3,
    label=f"LR = 0.001, Final = {losses['LR=0.001'][-1]:.2f}",
)
plt.title("Loss per iteration (MSE) for different learning rates", size=20)
plt.xlabel("Iteration", size=14)
plt.ylabel("Loss", size=14)
plt.legend()
plt.show()

model = LinearRegression(learning_rate=0.5)
model.fit(X_train, y_train)
preds = model.predict(X_test)

# Here's the corresponding MSE value on the test set:
print(model._mean_squared_error(y_test, preds))