!pip install panda

import pandas as pd

# Load the CSV file
df = pd.read_csv('KSE100-20years.csv')

# Display the first few rows of the DataFrame for debugging
print("Initial DataFrame:")
print(df.head())

# Display the data types of each column
print("\nData Types:")
print(df.dtypes)

# Check unique values in the 'High' column to identify non-numeric entries
print("\nUnique values in 'High' column:")
print(df['High'].unique())

# Remove commas from 'High' and convert to numeric, forcing errors to NaN
df['High'] = df['High'].str.replace(',', '').astype(float)

# Check if the conversion was successful
if df['High'].isnull().all():
    print("All values in 'High' column are NaN. Please check your CSV data.")
else:
    # Calculate the 'DIFF' column
    df['DIFF'] = df['High'].diff()

# Display the first few rows of the DataFrame after calculation
print("\nDataFrame after calculating 'DIFF':")
print(df[['Date', 'High', 'DIFF']].head())

# Save the new DataFrame to a new CSV file
df.to_csv('/content/KSE100_DIFF.csv', index=False)

print("New CSV file 'KSE100_DIFF.csv' created with the 'DIFF' column.")
