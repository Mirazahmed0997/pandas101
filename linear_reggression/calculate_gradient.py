import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

exp = np.array([1, 3, 4, 5, 6, 7])
sal = np.array([15, 35, 45, 55, 65, 75])


def calculate_gradient(x, y, w, b):
    m = x.shape[0]
    dj_dw=0.00
    dj_db=0.00

    for i in range(m):
        prediction = w * x[i] + b
        error = prediction - y[i]
        dj_dw=dj_dw + (error*x[i])
        dj_db=dj_db + error

    dj_dw=dj_dw/m
    dj_db=dj_db/m

    return dj_db, dj_dw

gradient_value=calculate_gradient(exp,sal, w=3, b=0)
print(gradient_value)