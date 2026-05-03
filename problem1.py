import pandas as pd

countries= pd.read_csv('countries.csv')

big_countries= countries.loc[(countries['area'] >= 3000000) | (countries['population']>=25000000),['name','area','population']]



print(big_countries)


employees = file.loc[
    (file['emp_age'] > 25) & (file['emp_age'] < 40),
    ['emp_id', 'emp_age', 'role']
]

print(employees)






emplyees= file.loc[
    (file['emp_age'] > 25) & (file['emp_age'] < 40)],
    ['emp_id','emp_age','role']


print(emplyees)

