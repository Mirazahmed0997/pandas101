import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer



file = pd.read_csv('titanic.csv')
df=sns.load_dataset("tips")

# 1- *starter-filterout effective features or delete uneffective col & split feature cols and target cols


file.drop(['Ticket','Name','PassengerId'], axis=1,inplace=True)

x= file.drop(['Survived'], axis=1) # features cols
y=file['Survived'] # target cols



# 2- Splits the train & test data using sklearn


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

# 3- fill/impute/handle missing values 
file.drop(['Cabin'], axis=1,inplace=True)


# numerical missing value imputation

# file_train=x_train.isnull().sum()
# file_test=x_test.isnull().sum()


# imputation for mean using pandas
mean_age= x_train['Age'].mean()
x_train['age_mean_imputor']=x_train['Age'].fillna(mean_age)
x_test['age_mean_imputor']=x_test['Age'].fillna(mean_age)


# imputation for median using pandas
median_age= x_train['Age'].median()
x_train['age_median_imputor']=x_train['Age'].fillna(median_age)
x_test['age_median_imputor']=x_test['Age'].fillna(median_age)


#simple imputation using ML ecoflow

age_imputor= SimpleImputer(missing_values=np.nan,strategy='mean')

age_imputor.fit(x_train[['Age']])

x_train['Age']= age_imputor.transform(x_train[['Age']])

x_train.drop(['age_median_imputor','age_mean_imputor'], axis=1,inplace=True)



x_test['Age']= age_imputor.transform(x_test[['Age']]).ravel()
x_test.drop(['age_median_imputor','age_mean_imputor'], axis=1,inplace=True)




# sns.kdeplot(data=x_train, x='age_mean_imputor')
# sns.kdeplot(data=x_train, x='age_median_imputor')

# plt.grid()
# plt.show()
print(x_test.isnull().sum())
print(x_test)



# print(x)
# print(y)
# print(file.head())