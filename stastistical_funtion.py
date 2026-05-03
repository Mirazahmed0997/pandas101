import pandas as pd
import numpy as np


df= pd.read_csv('file_csv.csv')

file= df.dropna() 


ds_total_marks= file[['data_structure_marks','algorithm_marks']].sum()
ds_total_marks_row= file[['data_structure_marks','algorithm_marks','python_marks']].sum(axis=1) #row wise sum
ds_avg_marks= file['data_structure_marks'].mean()
ds_max_marks= file['data_structure_marks'].max()
ds_min_marks= file['data_structure_marks'].min()
ds_median_marks= file['data_structure_marks'].median()
ds_highest_frequency_num_of_marks= file['data_structure_marks'].mode()
ds_standart_diviation_of_marks= file['data_structure_marks'].std()

file['Total Marks']= file.iloc[::,2:5].sum(axis=1) #using indexes rang.  "::" ,takes every row's data & "2:5" is taking data from 3-4 col's value, 



co_relation_mat = file[['data_structure_marks', 'algorithm_marks']].corr()

file['Sum of Marks']=ds_total_marks_row


print(file)
# print(file.describe)
# print(ds_total_marks)
# print(ds_total_marks_row)
# print(ds_avg_marks)
# print(ds_max_marks)
# print(ds_min_marks)
# print(ds_median_marks)
# print(ds_highest_frequency_num_of_marks)
# print(ds_standart_diviation_of_marks)
# print(co_relation_mat)