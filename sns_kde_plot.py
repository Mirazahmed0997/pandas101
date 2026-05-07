import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


std= pd.read_csv('sns_data.csv')
# tips = sns.load_dataset("tips")

sns.displot(kind='kde',data=std,x='attendance_rate',col='gender',fill=True)
# KDE plot using sns
# sns.kdeplot(data=std,x='attendance_rate')

plt.grid()
plt.show()

print(std.head())