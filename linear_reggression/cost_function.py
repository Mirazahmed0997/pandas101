import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

exp = np.array([1, 3, 4, 5, 6, 7])
sal = np.array([15, 35, 45, 55, 65, 75])


def compute_cost(x, y, w, b):
    m = x.shape[0]
    cost = 0.0

    for i in range(m):
        prediction = w * x[i] + b
        error = prediction - y[i]
        cost += error ** 2

    cost = cost / 2*m
    return cost


def make_prediction(x,y, w, b):
    m = x.shape[0]
    pred_list = np.zeros(m)

    for i in range(m):
        pred_list[i] = w * x[i] + b

    return pred_list


w = 10.0
b = 5.0

# predictions = make_prediction(exp, w, b)

# sns.scatterplot(x=exp, y=sal)
# plt.plot(exp, predictions)
# plt.title(f"Cost: {compute_cost(exp, sal, w, b):.2f}, w={w}, b={b}")
# plt.grid(True)
# plt.show()

# print("Predictions:", predictions)
# print("Cost:", compute_cost(exp, sal, w, b))


