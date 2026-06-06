import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import StandardScaler




file = pd.read_csv('titanic.csv')


file.drop(['Ticket','Name','PassengerId'], axis=1,inplace=True)

x= file.drop(['Survived'], axis=1) 
y=file['Survived'] 



x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

ss= StandardScaler()

ss.fit(x_train[['Age']])

x_train['Age'] =ss.transform(x_train[['Age']]).ravel()
x_test['Age'] =ss.transform(x_test[['Age']]).ravel()

# sns.kdeplot(data=x_train,x='Age')
# plt.grid()
# plt.show()


# print(round(x_train['Age'].mean(),5))
# print(round(x_train['Age'].std(),5))
print(x_train.sample(5))