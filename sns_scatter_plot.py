import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


std= pd.read_csv('sns_data.csv')
# tips = sns.load_dataset("tips")


# sns.scatterplot(data=std,x='study_hours',y='test_scores',hue='gender',style='subject')
# sns.relplot(kind='scatter',data=tips,x='total_bill',y='tip',hue='sex',style='smoker')
# sns.relplot(kind='scatter',data=tips,x='total_bill',y='tip',col='sex',row='smoker')
sns.relplot(kind='scatter',data=std,x='study_hours',y='test_scores',col='gender',row='week')

plt.show()

print(std.head())
