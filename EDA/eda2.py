import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# multivariate analysis


file = pd.read_csv('titanic.csv')

sns.countplot(x=file['Pclass'],hue=file['Survived'])
# sns.countplot(x=file['Sex'],hue=file['Survived'])

# group_by_gender= file.groupby("Sex")['Survived'].value_counts(normalize=True)
group_by_gender= file.groupby("Pclass")['Survived'].value_counts(normalize=True)

plt.grid()
# plt.show()


print(group_by_gender)
# print(file.head())
