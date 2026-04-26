import pandas as pd
import numpy as np

list_data = [
    [101, "Rahim", 85],
    [102, "Karim", 78],
    [103, "Nusrat", 92]
]

tuple_data = (
    (101, "Rahim", 85),
    (102, "Karim", 78),
    (103, "Nusrat", 92)
)


dict_data = {
    "studentId": [101, 102, 103],
    "fullname": ["Rahim", "Karim", "Nusrat"],
    "marks": [85, 78, 92]
}

dict_data_list = [
    {"id": 101, "name": "Rahim", "marks": 85},
    {"id": 102, "name": "Karim", "marks": 78},
    {"id": 103, "name": "Nusrat", "marks": 92}
]

list_df= pd.DataFrame(list_data, columns=['Id','Name','Marks'],index=[1,2,3])
tuple_df= pd.DataFrame(tuple_data, columns=['Id','Name','Marks'],index=[1,2,3])
dict_df= pd.DataFrame(dict_data)
dict_df_list= pd.DataFrame(dict_data_list)

print(type(dict_df_list))
print(dict_df_list)
# print(type(dict_df))
# print(dict_df)
# print(type(tuple_df))
# print(tuple_df)
# print(type(list_df))
# print(list_df)