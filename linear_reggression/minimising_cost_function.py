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

    cost = cost / m
    return cost


w=[]
cost=[]

for i in range(-100,100):
    cost_i= compute_cost(exp,sal,w=i,b=0)
    w.append(i)
    cost.append(cost_i)

plt.plot(w,cost)
plt.show()