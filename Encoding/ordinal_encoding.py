import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder


file = pd.read_csv('titanic.csv')

file.drop(['Ticket','Name','PassengerId'], axis=1,inplace=True)

x= file.drop(['Survived'], axis=1) 
y=file['Survived'] 

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

pclass_encoder= OrdinalEncoder(categories=[['third','second','first']])

pclass_encoder.fit(x_train[['Pclass']])


x_train['encoded_pclass']= pclass_encoder.transform(x_train[['Pclass']]).ravel()
x_test['encoded_pclass']= pclass_encoder.transform(x_test[['Pclass']]).ravel()

x_test.drop(['Pclass'], axis=1,inplace=True)


print(x_test.head(5))

# print(x_train.head(5))