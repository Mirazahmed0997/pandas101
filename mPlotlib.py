import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st1_hours=[2,3,4,2,5,7,3]
st2_hours=[2,5,4,3,6,2,9]
st3_hours=[1,5,7,1,9,2,8]
days=[1,2,3,4,5,6,7]

plt.plot(days,st1_hours)
plt.plot(days,st2_hours)
plt.plot(days,st3_hours)

plt.xlabel("Days")
plt.ylabel("Study Hours")
plt.title("Study of student over a week")

plt.show()