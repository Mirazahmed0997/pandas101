import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


std= pd.read_csv('sns_data.csv')
# tips = sns.load_dataset("tips")

# sns.histplot(data=std,x='attendance_rate',hue='gender')
sns.displot(kind='hist',data=std,x='attendance_rate',col='gender')

plt.grid()
plt.show()


print(std.head())