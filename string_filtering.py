import pandas as pd
import numpy as np

data = [
    {
        "name": "Rahim",
        "city": "Dhaka",
        "department": "IT",
        "salary": 50000
    },
    {
        "name": "Akram",
        "city": "Chittagong",
        "department": "HR",
        "salary": 42000
    },
    {
        "name": "Salma",
        "city": "Khulna",
        "department": "Finance",
        "salary": 55000
    },
    {
        "name": "Jamal",
        "city": "Sylhet",
        "department": "Sales",
        "salary": 38000
    }
]


df = pd.DataFrame(data)

# -------------------string filtering-----------------------------
city=df.loc[df['city'].str.contains("dhaka",case=False)]

city_contains=df.loc[df['city'].str.contains(r"dhaka|syl",case=False)]

city_start_with=df.loc[df['city'].str.contains(r"^sy",case=False)]


name_end_with=df.loc[df['name'].str.contains(r"al$",case=False)]

name_start_with_vowel=df.loc[df['name'].str.contains(r"^[aeiou]",case=False)]

# print(city_contains)


# ---------------------adding col------------------------
file=pd.read_csv('file_csv.csv')

file['country']='Bangladesh'

file['Total Marks']= file['data_structure_marks'] + file['algorithm_marks']+file['python_marks']


file['DS Grade']=np.where(file['data_structure_marks']>=90,'A+','A')
file['Passed']= file['data_structure_marks'] > 50

# file.rename(columns={'fullname':'Full Name'})

file['First Name']= file['fullname'].str.split(' ').str[0]
file['Last Name']= file['fullname'].str.split(' ').str[1]


file.to_csv('new_data.csv')



# -----------------unique & null checking-------------------------

file= pd.read_csv('new_data.csv')
unique_value=file['fullname'].unique()

al_unique_marks=file['algorithm_marks'].unique()

unique_data=file.nunique()

isnull=file.isnull()
isnull_col=file['algorithm_marks'].isnull() #check for every row
isnull_col1=file['algorithm_marks'].notnull() #check for every row

isnull_col2=file['algorithm_marks'].hasnans #check specific col

# print(file)
print(isnull_col2)


