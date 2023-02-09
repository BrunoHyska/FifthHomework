from task1 import get_dataframe

df = get_dataframe()

def exchange_columns(df, col1, col2):
    df[col1], df[col2] = df[col2], df[col1]
    return df

df = exchange_columns(df, 'FOOD NAME', 'SCIENTIFIC NAME')
print(df)

df.sort_index(axis=1, inplace=True)
print(df)