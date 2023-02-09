from task1 import get_dataframe
import pandas as pd


df= get_dataframe()

# Create two dictionaries
dict1 = {'Name': ['John', 'Jane', 'Jim', 'Joan'],
         'Age': [25, 30, 35, 40]}

dict2 = {'Name': ['John', 'Jane', 'Jim', 'Joan'],
         'Salary': [5000, 6000, 7000, 8000]}

# Create two dataframes from the dictionaries
df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

# Merge the two dataframes on the 'Name' column
df_merged = pd.merge(df1, df2, on='Name')

# Append df2 as a new column to df1
df1['Salary'] = df2['Salary']

print(df2)
