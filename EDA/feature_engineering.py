import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split



file = pd.read_csv('titanic.csv')
df=sns.load_dataset("tips")

# 1- *starter-filterout effective features or delete uneffective col & split feature cols and target cols


file.drop(['Ticket','Name','PassengerId'], axis=1,inplace=True)

x= file.drop(['Survived'], axis=1) # features cols
y=file['Survived'] # target cols



# 2- Splits the train & test data using sklearn


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

# 3- fill/impute/handle missing values 
# file.drop(['Cabin'], axis=1,inplace=True)


# numerical missing value imputation

# file_train=x_train.isnull().sum()
# file_test=x_test.isnull().sum()


# imputation for mean
mean_age= x_train['Age'].mean()
x_train['age_mean_imputor']=x_train['Age'].fillna(mean_age)
x_test['age_mean_imputor']=x_test['Age'].fillna(mean_age)


# imputation for median
median_age= x_train['Age'].median()
x_train['age_median_imputor']=x_train['Age'].fillna(median_age)
x_test['age_median_imputor']=x_test['Age'].fillna(median_age)


sns.kdeplot(data=x_train, x='age_mean_imputor')
sns.kdeplot(data=x_train, x='age_median_imputor')

plt.grid()
plt.show()






print(x_test.isnull().sum())



# print(x)
# print(y)
# print(file.head())