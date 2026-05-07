import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


std= pd.read_csv('sns_data.csv')

# sns.regplot(data=std,x='study_hours',y="test_scores") #axes
sns.lmplot(data=std,x='study_hours',y="test_scores",hue='gender') #figure

plt.grid()
plt.show()


print(std.head())