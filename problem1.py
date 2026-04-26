import pandas as pd

countries= pd.read_csv('countries.csv')

big_countries= countries.loc[(countries['area'] >= 3000000) | (countries['population']>=25000000)]


print(big_countries)