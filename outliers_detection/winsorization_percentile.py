import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

file = pd.read_csv('marks_dataset.csv')

sns.boxplot(data=file,x='maths_marks')

# plt.show()

x=12
x=x/100

min_range=file['maths_marks'].quantile(x)
max_range=file['maths_marks'].quantile(1-x)


file['maths_marks']= file['maths_marks'].clip(min_range,max_range)

print(file['maths_marks'].describe())






# print(file.head())