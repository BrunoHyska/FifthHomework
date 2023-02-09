import pandas as pd

# Task 1
def get_dataframe():
    dataframe = pd.read_csv('CSVFolder/generic-food.csv')
    return dataframe

df= get_dataframe()
