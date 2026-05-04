import pandas as pd
import numpy as np

file= pd.read_csv("updated_data.csv")
# print(file.min())


instructor_group= file.groupby('instructor')  #grouping row by instructor name
total_marks_avg=instructor_group['Total Marks'].mean() #avg marks value for each group

for key, instructor in instructor_group:
    print(key)
    total_marks=instructor['Total Marks']
    

    file['Total Marks']=file['Total Marks'].fillna(file['instructor'].map(total_marks_avg))
    # print("Total: ",total_marks)
    # print("avg :",total_marks_avg)
    # print(instructor)
    # print(instructor.min())
    # print(instructor.describe())
    # print(instructor[['key', 'Total Marks', 'Avg']])
    # print(instructor)
    # print(file)


print(total_marks_avg)
print(file)



