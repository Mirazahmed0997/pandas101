import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer



file = pd.read_csv('titanic.csv')

# 1- *starter-filterout effective features or delete uneffective col & split feature cols and target cols


file.drop(['Ticket','Name','PassengerId'], axis=1,inplace=True)

x= file.drop(['Survived'], axis=1) # features cols
y=file['Survived'] # target cols



# 2- Splits the train & test data using sklearn


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

embarked_imputor= SimpleImputer(missing_values=np.nan,strategy='most_frequent')

embarked_imputor.fit(x_train[['Embarked']])

x_train['Embarked']=embarked_imputor.transform(x_train[['Embarked']]).ravel()

x_test['Embarked']=embarked_imputor.transform(x_test[['Embarked']]).ravel()









# sns.countplot(data=x_train, x='Embarked')
# sns.kdeplot(data=x_train, x='age_median_imputor')

plt.grid()
# plt.show()
print(x_train.isnull().sum())
print(x_test.isnull().sum())
# print(x_test)



# print(x)
# print(y)
# print(file.head())