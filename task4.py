from task1 import get_dataframe


df = get_dataframe()

columns = df.columns
print(list(columns))
df_sum = df.sum(numeric_only=True)
print(df_sum)