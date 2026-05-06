import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file= pd.read_csv('student_data.csv')

# max_hour=file['Study_Hours'].max()


# plt.hist(file['IQ_Score'],edgecolor='black')
plt.hist(file['Study_Hours'],bins=[1,2,3,4,5,6,7],edgecolor='black')

plt.ylabel("Number of students")
plt.xlabel("Study_Hours")
plt.title("Students count")
plt.grid()

plt.show()

print(file)