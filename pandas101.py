import pandas as pd
import numpy as np

file = pd.read_csv('file_csv.csv')
indexed_file=file.set_index('studentId')
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


multi_col_row= file.iloc[:,1:4] # show data col wise(1-3) iloc[ start_row : end_row , start_col : end_col ]

chnaged_name=indexed_file.rename(columns={'fullname':"Full Name"}) #change col/thead name



file.drop(index=0, inplace=True) # delete row
file.drop('enrollment_date',axis=1, inplace=True) # delete col

file.loc[4,'data_structure_marks']= 90 #assign value
file.loc[3,'completion_status']= 'Completed' #assign value
file.loc[1:3,'python_marks'] += 2 #assign value

# for i in file.itertuples(index=False):
    # print(f'{i} ')


#sorting
asc_sorted_file=file.sort_values('algorithm_marks')
desc_sorted_file=file.sort_values('algorithm_marks',ascending=False)


#filtering data

in_progress= file.loc[file['completion_status']=='In Progress']

#completed and data marks more than 80
completed= file.loc[(file['completion_status']=='Completed') & (file['data_structure_marks']>=80)]

# print(file_head)
# print(file_tail)
# print(specific_col)

# print(describe)
# print(access_indexes)
# print(access_multi_indexes)
# print(access_indexes_inRange)
# print(access_col)
# print(access_multi_col)
# print(access_multi_col_row)
# print(multi_col_row)
# print(indexed_file)
# print(file)
print(completed)