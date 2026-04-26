import pandas as pd
import numpy as np

file = pd.read_csv('file_csv.csv')

file_head=file.head(3)
file_tail=file.tail(3)

specific_col=file['data_structure_marks']
conv_to_array=np.array(file['data_structure_marks'])

indexes= file.index

describe= file.describe()

# print(file_head)
# print(file_tail)
# print(specific_col)

# print(describe)
print(conv_to_array)