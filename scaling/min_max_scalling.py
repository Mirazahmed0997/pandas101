import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import MinMaxScaler




file = pd.read_csv('titanic.csv')


file.drop(['Ticket','Name','PassengerId'], axis=1,inplace=True)

x= file.drop(['Survived'], axis=1) 
y=file['Survived'] 



x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

minmax=MinMaxScaler()
minmax.fit(x_train[['Fare']])

x_train['Fare'] =minmax.transform(x_train[['Fare']]).ravel()
x_test['Fare'] =minmax.transform(x_test[['Fare']]).ravel()

# sns.kdeplot(data=x_train,x='Fare')
# plt.grid()
# plt.show()


print(x_train['Fare'].describe())