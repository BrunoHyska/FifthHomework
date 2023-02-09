from task1 import get_dataframe


df= get_dataframe()

import matplotlib.pyplot as plt

# Plot a histogram for the 'column_name' column
plt.hist(df['CALORIES'], bins=10)

# Add labels and title to the plot
plt.xlabel('CALORIES')
plt.ylabel('Frequency')
plt.title('Histogram of Column Name')

# Show the plot
plt.show()