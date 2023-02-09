from task1 import get_dataframe


df= get_dataframe()

corr_matrix = df.corr(numeric_only=True)

# Extract the correlation value for the 'column_name' column
corr_value = corr_matrix['CALORIES']

# Print the correlation value
print("Correlation for column 'CALORIES':", corr_value)