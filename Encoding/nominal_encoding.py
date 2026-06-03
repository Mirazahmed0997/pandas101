# one hot encoding for nominal catagories
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder



file = pd.read_csv('titanic.csv')


file.drop(['Ticket','Name','PassengerId'], axis=1,inplace=True)

x= file.drop(['Survived'], axis=1) 
y=file['Survived'] 



x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

# -------------------Pclass-------------------------


pclass_encoder= OrdinalEncoder(categories=[['third','second','first']])

pclass_encoder.fit(x_train[['Pclass']])


x_train['encoded_pclass']= pclass_encoder.transform(x_train[['Pclass']]).ravel()
x_test['encoded_pclass']= pclass_encoder.transform(x_test[['Pclass']]).ravel()


# -------------------Gender-------------------------



gender_h_encoding= OneHotEncoder(sparse_output=False).set_output(transform='pandas')

gender_h_encoding.fit(x_train[['Sex']])

encodded_df_train=gender_h_encoding.transform(x_train[['Sex']])
x_train = pd.concat([x_train,encodded_df_train],axis=1)

encodded_df_test=gender_h_encoding.transform(x_test[['Sex']])
x_test = pd.concat([x_test,encodded_df_test],axis=1)


# -------------------Embarked-------------------------


Embarked_h_encoding= OneHotEncoder(sparse_output=False).set_output(transform='pandas')

Embarked_h_encoding.fit(x_train[['Embarked']])

encodded_df_train=Embarked_h_encoding.transform(x_train[['Embarked']])
x_train = pd.concat([x_train,encodded_df_train],axis=1)

encodded_df_test=Embarked_h_encoding.transform(x_test[['Embarked']])
x_test = pd.concat([x_test,encodded_df_test],axis=1)

# -------------------Cabin-------------------------

x_train['Cabin_deck']= x_train['Cabin'].astype(str).str[0] # convert obj to str & split first char
x_test['Cabin_deck']= x_test['Cabin'].astype(str).str[0] # convert obj to str & split first char


Cabin_deck_h_encoding= OneHotEncoder(sparse_output=False,drop='first').set_output(transform='pandas')

Cabin_deck_h_encoding.fit(x_train[['Cabin_deck']])

encodded_df_train=Cabin_deck_h_encoding.transform(x_train[['Cabin_deck']])
x_train = pd.concat([x_train,encodded_df_train],axis=1)



encodded_df_test=Cabin_deck_h_encoding.transform(x_test[['Cabin_deck']])
x_test = pd.concat([x_test,encodded_df_test],axis=1)



x_train.drop(['Pclass','Sex','Embarked','Cabin','Cabin_deck'],axis=1,inplace=True)
x_test.drop(['Pclass','Sex','Embarked','Cabin','Cabin_deck'],axis=1,inplace=True)

# print(x_train['Cabin_deck'].value_counts())


print(x_train.sample(5))