import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


exp= np.array([1,3,4,5,6,7])
sal= np.array([15,35,45,55,65,75])

# sns.scatterplot(x=exp,y=sal)
# plt.show()
# plt.grid()


def make_prediction(x,y,w,b):
    m=exp.shape[0]
    pred_list=np.zeros((m,))
    sns.scatterplot(x=exp,y=sal)
    plt.plot(exp,sal)
    plt.show()


    for i in range(m):
        pred_list[i]= w*exp[i]+b

    return pred_list

# predictions= make_prediction(exp,sal,0,0)
predictions= make_prediction(exp,sal,7,3)


print(predictions)



# print(x)