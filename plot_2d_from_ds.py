import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file= pd.read_csv('enrollment_data.csv')

plt.plot(file['Year'],file['Python_Enrollments'],label='Python',linestyle='dashed',marker='o',markersize=5)
plt.plot(file['Year'],file['Digital_Marketing_Enrollments'],label='Digital Marketing',color='red',marker='x',markersize=5)

plt.xlabel("Years")
plt.ylabel("Enrolled Student")
plt.title("Enrollment per year")
plt.grid()

plt.legend()
plt.show()

print(file)