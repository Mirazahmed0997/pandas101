import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import RobustScaler


file = pd.read_csv('file_csv.csv')

#  sns.kdeplot(data=file,x='data_structure_marks')
# plt.grid()
# plt.show()

# x= file.drop(['Survived'], axis=1) 
# y=file['Survived'] 

rs= RobustScaler()

rs.fit(file[['data_structure_marks']])

file['data_structure_marks']=rs.transform(file[['data_structure_marks']]).ravel()

print(file.sample(5).describe())