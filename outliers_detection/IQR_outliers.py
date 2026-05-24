import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

file = pd.read_csv('titanic.csv')
file.drop(['Ticket','Name','PassengerId'], axis=1,inplace=True)

x= file.drop(['Survived'], axis=1) 
y=file['Survived'] 

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

# for age

age_Q1= x_train['Age'].quantile(0.25) # 25% percentile
age_Q2= x_train['Age'].quantile(0.50) # 50% percentile
age_Q3= x_train['Age'].quantile(0.75) # 75% percentile


age_IQR= age_Q3-age_Q1

age_Min=  age_Q1 - 1.5 * age_IQR
age_Max=  age_Q3 + 1.5 * age_IQR

age_outliers= x_train[(x_train["Age"]<age_Min) | (x_train["Age"]>age_Max)]


#for Fare

Fare_Q1= x_train['Fare'].quantile(0.25) # 25% percentile
Fare_Q2= x_train['Fare'].quantile(0.50) # 50% percentile
Fare_Q3= x_train['Fare'].quantile(0.75) # 75% percentile


Fare_IQR= Fare_Q3-Fare_Q1

Fare_Min=  Fare_Q1 - 1.5 * Fare_IQR
Fare_Max=  Fare_Q3 + 1.5 * Fare_IQR

Fare_outliers= x_train[(x_train["Fare"]<Fare_Min) | (x_train["Fare"]>Fare_Max)]

print(Fare_Max)
print(Fare_Min)

print(len(Fare_outliers))
print(Fare_outliers)
