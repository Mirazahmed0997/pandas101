import pandas as pd
import numpy as np

file = pd.read_csv('file_csv.csv')
conv_to_array=np.array(file['data_structure_marks'])

indexes= file.index

describe= file.describe()

file_head=file.head(3)
file_tail=file.tail(3)



name_col=file['fullname']

access_indexes=file.loc[0] #accessing data with indexes & columns
access_multi_indexes=file.loc[[2,5,4]] #accessing data with multiple indexes & columns
access_indexes_inRange=file.loc[3:6] #accessing data  indexes & columns in range
access_col=file.loc[:,'algorithm_marks'] #accessing data of col
access_multi_col=file.loc[:,['algorithm_marks','data_structure_marks','python_marks']] #accessing data of multiple col
access_multi_col_row=file.loc[3:6,['algorithm_marks','data_structure_marks','python_marks','completion_status']] #accessing data of multiple col & indexes


# print(file_head)
# print(file_tail)
# print(specific_col)

# print(describe)
# print(access_indexes)
# print(access_multi_indexes)
# print(access_indexes_inRange)
# print(access_col)
# print(access_multi_col)
print(access_multi_col_row)
# print(file)