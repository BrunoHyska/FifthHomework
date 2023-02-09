from task1 import get_dataframe


df= get_dataframe()

df.loc[df['FOOD NAME'].str.len() < 10, 'FOOD NAME'] = df['FOOD NAME'].str.upper()
print(df)