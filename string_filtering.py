import pandas as pd

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
city=df.loc[df['city'].str.contains("dhaka",case=False)]

city_contains=df.loc[df['city'].str.contains(r"dhaka|syl",case=False)]

city_start_with=df.loc[df['city'].str.contains(r"^sy",case=False)]


name_end_with=df.loc[df['name'].str.contains(r"al$",case=False)]

name_start_with_vowel=df.loc[df['name'].str.contains(r"^[aeiou]",case=False)]

print(city_contains)