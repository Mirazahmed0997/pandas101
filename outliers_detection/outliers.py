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




# outliers of age

mean_of_age=x_train['Age'].mean()
std_of_age=x_train['Age'].std()


x_train['Z_Score_Age']=( x_train['Age']-mean_of_age)/std_of_age

x_train=x_train[abs(x_train['Z_Score_Age'])<=3]

print(len(x_train))
print(x_train)


# outliers of fare

Fare_Q1= x_train['Fare'].quantile(0.25) # 25% percentile
Fare_Q2= x_train['Fare'].quantile(0.50) # 50% percentile
Fare_Q3= x_train['Fare'].quantile(0.75) # 75% percentile


Fare_IQR= Fare_Q3-Fare_Q1

Fare_Min=  (0,Fare_Q1 - 1.5 * Fare_IQR)
Fare_Max=  Fare_Q3 + 1.5 * Fare_IQR

Fare_outliers= x_train[(x_train["Fare"]<Fare_Min) | (x_train["Fare"]>Fare_Max)]


x_train['Fare']= x_train['Fare'].clip(Fare_Min,Fare_Max)


# winsorization_percentile





