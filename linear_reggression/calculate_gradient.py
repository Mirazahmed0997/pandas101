import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import minimising_cost_function
import cost_function

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

    return dj_dw,dj_db

def gradient_descent(x,y,w_input,b_input,max_iteration,alpha):
    w=w_input
    b=b_input
    cost_memo=[]
    iteration=[]

    for i in range(max_iteration):
        dj_dw,dj_db=calculate_gradient(x,y,w,b)

        w=w-(alpha*dj_dw)
        b=b-(alpha*dj_db)

        cost=minimising_cost_function.compute_cost(x,y,w,b)

        cost_memo.append(cost)
        iteration.append(i)

        # if i%100==0:
            # print(f'w:{w:0.4f},b:{b:0.4f}, dj_dw:{dj_dw:0.4f}, dj_db:{dj_db:0.4f}, cost:{cost:0.4f}')
    return w,b,cost_memo,iteration


w,b,cost_memo,iteration=gradient_descent(exp,sal,w_input=0,b_input=0,max_iteration=10000,alpha=0.01)


print(w,b)

predictions = cost_function.make_prediction(exp,sal, w, b)

sns.scatterplot(x=exp, y=sal)
plt.plot(iteration[:100], cost_memo[:100])
plt.xlabel("Number of iterations")
plt.ylabel("Number of costs")
# plt.title(f"Cost: {minimising_cost_function.compute_cost(exp, sal, w, b):.2f}, w={w}, b={b}")
plt.grid(True)
plt.show()


# gradient_value=calculate_gradient(exp,sal, w=3, b=0)
# print(gradient_value)