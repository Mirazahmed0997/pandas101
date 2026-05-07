import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


std= pd.read_csv('sns_data.csv')

sns.countplot(data=std,x='subject')
sns.barplot(data=std,x='gender',y='test_scores',errorbar=None)

plt.grid()
plt.show()


print(std.head())