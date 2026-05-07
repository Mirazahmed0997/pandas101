import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file= pd.read_csv('file_csv.csv')

group_by_completion_status=file.groupby('completion_status').size()

indexes=group_by_completion_status.index
values=group_by_completion_status.values

# max_hour=file['Study_Hours'].max()


# plt.hist(file['IQ_Score'],edgecolor='black')
plt.pie(group_by_completion_status,labels=indexes,autopct='%1.1f%%',explode = (0.1, 0, 0))

# plt.ylabel("Number of students")
# plt.xlabel("completion_status")
# plt.title("Students count")
plt.grid()

plt.show()

print(file)