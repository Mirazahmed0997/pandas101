import pandas as pd
import numpy as np


# -----------handiling null values---------
df= pd.read_csv('file_csv.csv')


#if any null value in a row drop full row and create a copy of main file
remove_null= file.dropna() 

remove_null_values = file.dropna(how='all')

# remove_col_null_values= file.dropna(subset='algorithm_marks') #remove data by specific col

fill_null_values= file.fillna(0)




null_name=df['fullname'].fillna("unknown")
fill_null_marks=df['algorithm_marks'].fillna(df['algorithm_marks'].mean(), inplace=True)
# print(null_algo_marks)
print(fill_null_marks)
print(df)