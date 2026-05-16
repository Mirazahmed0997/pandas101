import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# multivariate analysis


file = pd.read_csv('titanic.csv')
df=sns.load_dataset("tips")



#-----count plot------------

# sns.countplot(x=file['Embarked'],hue=file['Survived'])
# sns.countplot(x=file['Pclass'],hue=file['Survived'])
# sns.countplot(x=file['Sex'],hue=file['Survived'])


#----------------------bar plot----------------------------

# sns.barplot(x=file['Sex'],y=file['Pclass'])
# sns.barplot(x=file['Survived'],y=file['Age'],hue=file['Sex'])


#-----------------------------count plot---------------------------

# group_by_gender= file.groupby("Sex")['Survived'].value_counts(normalize=True)
# group_by_gender= file.groupby("Pclass")['Survived'].value_counts(normalize=True)
# group_by_gender= file.groupby("Pclass")['Sex'].value_counts(normalize=True)
# group_by_gender= file.groupby("Embarked")['Survived'].value_counts(normalize=True)
# group_by_gender= file.groupby("Embarked")['Survived'].value_counts(normalize=True)


# --------------------------KDE plot--------------------------------

# sns.kdeplot(data=file,x=file['Age'],hue=file['Survived'])


# ------------------scatter plot----------------------------
sns.scatterplot(data=df,x=df['total_bill'],y=df['tip'],hue=df['sex'])


plt.grid()
plt.show()


# print(group_by_gender)
# print(df.head())
