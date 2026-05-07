import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


std= pd.read_csv('sns_data.csv')

# sns.lineplot(data=std, x='week',y='attendance_rate',errorbar=None,hue='gender')
sns.relplot(kind='line',data=std, x='week',y='test_scores',errorbar=None,hue='class_level')

# plt.ylabel("attendance_rate")
# plt.xlabel("Week")
# plt.title("Attendence Ratio")

plt.show()
print(std.head())