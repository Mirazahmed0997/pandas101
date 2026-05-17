import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer



file = pd.read_csv('titanic.csv')



file.drop(['Ticket','Name','PassengerId'], axis=1,inplace=True)

x= file.drop(['Survived'], axis=1) # features cols
y=file['Survived'] # target cols





x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
# sns.countplot(data=x_train, x='Cabin')
# plt.show()

cabin_imputor= SimpleImputer(missing_values=np.nan,strategy='constant',fill_value='Missing',add_indicator=True)

cabin_imputor.fit(x_train[['Cabin']])
x_train[['Cabin','Cabin_missing_indicator']]=cabin_imputor.transform(x_train[['Cabin']])

x_test[['Cabin','Cabin_missing_indicator']]=cabin_imputor.transform(x_test[['Cabin']])



# print(x_train.head())
# print(x_test.head())
print(x_train.isnull().sum())
print(x_test.isnull().sum())