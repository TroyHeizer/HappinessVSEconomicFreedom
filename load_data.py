import pandas as pd

# Replace 'path_to_file1.csv' and 'path_to_file2.csv' with the actual file paths
df1 = pd.read_csv('happiness_index.csv', encoding='latin1')
df2 = pd.read_csv('economic_freedom_index.csv', encoding='latin1')

# Display the first few rows of each DataFrame to check the data
print("First DataFrame:")
print(df1.head())

print("\nSecond DataFrame:")
print(df2.head())

# Check the shape of the dataframes (number of rows and columns)
print("Shape of first DataFrame:", df1.shape)
print("Shape of second DataFrame:", df2.shape)

# Check for missing values
print("Missing values in first DataFrame:")
print(df1.isnull().sum())

print("\nMissing values in second DataFrame:")
print(df2.isnull().sum())

# Display column names
print("\nColumns in first DataFrame:")
print(df1.columns)

print("\nColumns in second DataFrame:")
print(df2.columns)