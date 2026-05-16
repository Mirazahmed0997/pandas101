import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split



file = pd.read_csv('titanic.csv')
df=sns.load_dataset("tips")

# 1- *starter-filterout effective features or delete uneffective col
#    *split feature cols and target cols

file.drop(['Ticket','Name','PassengerId','Cabin'], axis=1,inplace=True)

x= file.drop(['Survived'], axis=1) # features cols
y=file['Survived'] # target cols

# 2- Splits the train & test data using sklearn
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

# print(x_train)
print(y_train)

# print(x)
# print(y)
# print(file.head())