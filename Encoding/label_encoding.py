import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder




file = pd.read_csv('titanic.csv')


file.drop(['Ticket','Name','PassengerId'], axis=1,inplace=True)

x= file.drop(['Survived'], axis=1) 
y=file['Survived'] 



x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

label_encoder= LabelEncoder()

label_encoder.fit(y_train)

y_train_encoded_array=label_encoder.transform(y_train)
y_test_encoded_array=label_encoder.transform(y_test)

y_train_encoded=pd.Series(y_train_encoded_array,index=y_train.index,name=y_train.name)
y_test_encoded=pd.Series(y_test_encoded_array,index=y_test.index,name=y_test.name)

print(y_train_encoded)


