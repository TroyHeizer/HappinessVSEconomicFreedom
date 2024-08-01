import pandas as pd

def load_datasets():
    df1 = pd.read_csv('happiness_index.csv', encoding='latin1')
    df2 = pd.read_csv('economic_freedom_index.csv', encoding='latin1')
    return df1, df2

def clean_and_merge(df1, df2):
    # Handle missing values (example: drop rows with any missing values)
    df1_clean = df1.dropna()
    df2_clean = df2.dropna()

    # Ensure consistent formatting (example: trimming whitespace and converting to lower case)
    df1_clean['Country'] = df1_clean['Country'].str.strip().str.lower()
    df2_clean['Country'] = df2_clean['Country'].str.strip().str.lower()

    # Merge the datasets on the 'Country' column
    merged_df = pd.merge(df1_clean, df2_clean, on='Country', how='inner')

    return merged_df

if __name__ == "__main__":
    df1, df2 = load_datasets()
    merged_df = clean_and_merge(df1, df2)
    
    # Display the first few rows of the merged DataFrame
    print("\nMerged DataFrame:")
    print(merged_df.head())

    # Check for missing values in the merged DataFrame
    print("\nMissing values in merged DataFrame:")
    print(merged_df.isnull().sum())

    # Save the merged DataFrame to a new CSV file (optional)
    merged_df.to_csv('merged_dataset.csv', index=False)
