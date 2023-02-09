from task1 import get_dataframe


df= get_dataframe()

# Calculate the average value for the column but in integer
mean_value = int(df['CALORIES'].mean())
# Replace missing values with the average value
df['CALORIES'].fillna(mean_value, inplace=True)

print(df)
