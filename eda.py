import pandas as pd

# Load the merged dataset
merged_df = pd.read_csv('merged_dataset.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(merged_df.head())

# Display the column names and data types
print("\nColumn names and data types:")
print(merged_df.dtypes)

# Display summary statistics
print("\nSummary statistics:")
print(merged_df.describe())

# Check for missing values
print("\nMissing values in each column:")
print(merged_df.isnull().sum())
