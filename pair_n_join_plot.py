import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


std= pd.read_csv('sns_data.csv')

std_marks=std[['test_scores','study_hours','attendance_rate','gender']]

# sns.pairplot(data=std_marks,hue='gender')
# sns.pairplot(kind='hist',data=std_marks)


# sns.jointplot(data=std_marks,x='study_hours',y='test_scores')
sns.jointplot(data=std_marks,x='study_hours',y='test_scores',kind='kde',hue='gender')

plt.grid()
plt.show()


print(std_marks.head())