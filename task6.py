from task1 import get_dataframe

df= get_dataframe()

def trim_outliers(df):
    quantiles = df.quantile([0.05, 0.95], numeric_only=True).transpose()
    lower_bound = quantiles[0.05]
    upper_bound = quantiles[0.95]
    trimmed_df = df.clip(lower_bound, upper_bound, axis=1)
    return trimmed_df

trimmed_df = trim_outliers(df)
print(trimmed_df)