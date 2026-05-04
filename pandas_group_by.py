import pandas as pd
import numpy as np

file= pd.read_csv("updated_data.csv")
# print(file.min())


instructor_group= file.groupby('instructor')

for key, instructor in instructor_group:
    print(key)
    # print(instructor)
    # print(instructor.min())
    print(instructor.describe())



