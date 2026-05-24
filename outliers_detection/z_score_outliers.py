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

# sns.kdeplot(data=x_train, x='Age')
# plt.show()


# outliers of age

mean_of_age=x_train['Age'].mean()
std_of_age=x_train['Age'].std()

x_train['Z_Score_Age']=( x_train['Age']-mean_of_age)/std_of_age


age_outliers= x_train[abs(x_train['Z_Score_Age'])>3]


# outliers of Fare

mean_of_Fare=x_train['Fare'].mean()
std_of_Fare=x_train['Fare'].std()

x_train['Z_Score_Fare']=( x_train['Fare']-mean_of_Fare)/std_of_Fare


fare_outliers= x_train[abs(x_train['Z_Score_Fare'])>3]




print(std_of_Fare)
print(len(fare_outliers))
print(fare_outliers)