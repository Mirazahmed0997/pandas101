import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Exploratory Data Analysis

file = pd.read_csv('titanic.csv')


# step -1, check how many row/data and col/feature exiting in the data set
shape= file.shape

# step -2, check the type of information in dataset or features
chk_file= file.head(10)

#step -3, check some random sample data and check if any features has null value and many null values
random_data = file.sample(10)
chk_null=file.isnull().sum()

#step -4, check repeated/duplicates value & drop/delete them
dup_data= file.duplicated().sum()
file.drop_duplicates(inplace=True)

#step -5, check check statistical value & data type in every features
data_type = file.info()
stat_data = file.describe()


# ------------------------------------------------------------------

#step- 6, Univariate analysis / single/specific col/feature analysis

# ------------------------------------------------------------------


# sns.countplot(data=file, x=file['Survived'])
# survival_count= file['Survived'].value_counts() #counts
# survival_ratio= (survival_count/len(file)) *100 #percentage

# label= file['Survived'].unique()

# plt.pie(survival_count,labels=label ,autopct="%1.1f",explode = (0.1, 0))
# plt.title("Survival rate")
# plt.grid()
# # plt.show()



# sns.countplot(data=file, x=file['Pclass'])
# class_count= file['Pclass'].value_counts() #counts
# class_ratio= (class_count/len(file)) *100 #percentage

# label= file['Pclass'].unique()

# plt.pie(class_count,labels=label ,autopct="%1.1f",explode = (0.05, 0,0.05))
# plt.title("class rate")
# plt.grid()
# # plt.show()





# sns.countplot(data=file, x=file['Pclass'])
# gender_count= file['Sex'].value_counts() #counts
# gender_ratio= (gender_count/len(file)) *100 #percentage

# label= file['Sex'].unique()

# plt.pie(gender_count,labels=label ,autopct="%1.1f",explode = (0.05, 0))
# plt.title("gender rate")
# plt.grid()
# # plt.show()



# sns.countplot(data=file, x=file['Embarked'])
# Embarked_count= file['Embarked'].value_counts() #counts
# Embarked_ratio= (Embarked_count/len(file)) *100 #percentage
# file = file.dropna(subset=['Embarked'])
# label= file['Embarked'].unique()


# plt.pie(Embarked_count,labels=label ,autopct="%1.1f")
# plt.title("Embarked rate")
# plt.grid()
# # plt.show()


# # step -7, Numerical features analysis with di-variate analysis



# sns.histplot(file['Age'],bins=50)
# sns.kdeplot(file['Age'])

# plt.title("KDE of ages")
# plt.xlabel("Ages")
# plt.ylabel("Probability")
# plt.grid()
# # plt.show()



# # sns.histplot(file['Fare'],bins=50)
# # sns.kdeplot(file['Fare'])
sns.boxplot(file['Fare']) # to detect outliers

plt.title("KDE of Fares")
plt.xlabel("Tickets price")
plt.ylabel("Probability / frequency")
plt.grid()
plt.show()



print(file[file['Age']>30])