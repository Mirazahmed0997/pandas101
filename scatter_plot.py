import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file= pd.read_csv('student_data.csv')

# plt.scatter(file['Study_Hours'],file['IQ_Score'])
plt.scatter(file['Chilling_Hours'],file['IQ_Score'])


plt.xlabel("Study hours")
plt.ylabel("IQ scores")
plt.title("Study & IQ Ratio")
plt.grid()

plt.show()

print(file)