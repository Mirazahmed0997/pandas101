import pandas as pd
import numpy as np

file= pd.read_csv("new_data.csv")

min_val=file['Total Marks'].min()
max_val=file['Total Marks'].max()

file['scaled_marks']= file['Total Marks'].apply(lambda x: (x-min_val)/(max_val-min_val))

# print(file)
# print(file['scaled_marks'])
# print(min_val)
# print(max_val)



# ------------custom build function-----------

def grading_system(marks):
    if marks >= 260:
        return 'A+'
    elif marks >= 250:
        return 'A'
    elif marks >= 220:
        return 'A-'
    else: 
        return 'F'


file['Grade']=file['Total Marks'].apply(grading_system)

# print(file[['Total Marks', 'Grade', 'scaled_marks']])


def marking_system(file):
    data_structure_marks=file['data_structure_marks']*2
    python_marks=file['python_marks']*3
    algorithm_marks=file['algorithm_marks']*4

    return data_structure_marks+python_marks+algorithm_marks


file['Exceptional_Marks']=file.apply(marking_system,axis=1)

print(file[['Total Marks', 'Grade', 'scaled_marks','Exceptional_Marks']])
