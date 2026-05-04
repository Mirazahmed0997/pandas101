import pandas as pd
import numpy as np

file= pd.read_csv("new_data.csv")


file['enrollment_date']= pd.to_datetime(file['enrollment_date'])

file['Enrollment year']=file['enrollment_date'].dt.year
file['Enrollment Date']=file['enrollment_date'].dt.day

# print(file['enrollment_date'])

print(file)