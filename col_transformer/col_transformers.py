import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import RobustScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder




file = pd.read_csv('titanic.csv')

file.drop(['Ticket','Name','PassengerId'], axis=1,inplace=True)
file['Family_Size']= file['SibSp']+file['Parch']+1

x= file.drop(['Survived'], axis=1) 
y=file['Survived'] 

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)


x_train['Cabin_deck']= x_train['Cabin'].astype(str).str[0] # convert obj to str & split first char
x_test['Cabin_deck']= x_test['Cabin'].astype(str).str[0] # convert obj to str & split first char



imputer_transformar= ColumnTransformer(
    transformers=[
        ('age',SimpleImputer(missing_values=np.nan,strategy='mean'),['Age']),
        ('embarked',SimpleImputer(missing_values=np.nan,strategy='most_frequent'),['Embarked']),
        ('cabin',SimpleImputer(missing_values=np.nan,strategy='constant',fill_value='Missing',add_indicator=True),['Cabin']),
        
    ],
    remainder='passthrough',
    verbose_feature_names_out=False
)





imputer_transformar.set_output(transform='pandas')

imputer_transformar.fit(x_train)

x_train=imputer_transformar.transform(x_train)
x_test=imputer_transformar.transform(x_test)


encoder_scaler= ColumnTransformer(
    transformers=[
        ('pclass',OrdinalEncoder(categories=[['third','second','first']]),['Pclass']),
        ('embarked',OneHotEncoder(sparse_output=False,drop='first').set_output(transform='pandas'),['Embarked','Sex','Cabin_deck']),
        ('age_scaller',StandardScaler(),['Age']),
        ('fare_scaller',MinMaxScaler(),['Fare','Family_Size'])
    ],
    remainder='passthrough',
    verbose_feature_names_out=False
)
encoder_scaler.set_output(transform='pandas')

encoder_scaler.fit(x_train)

x_train=encoder_scaler.transform(x_train)
x_test=encoder_scaler.transform(x_test)

x_train.drop(['Cabin','SibSp','Parch','missingindicator_Cabin'], axis=1,inplace=True)
x_test.drop(['Cabin','SibSp','Parch','missingindicator_Cabin'], axis=1,inplace=True)



print(x_train.sample(5))