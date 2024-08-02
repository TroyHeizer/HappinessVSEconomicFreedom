import pandas as pd

# Load the merged dataset
merged_df = pd.read_csv('merged_dataset.csv')

# Calculate correlations
correlation_matrix = merged_df[['Score', 'GDP per capita', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption', '2019 Score']].corr()

# Display the correlation matrix
print("Correlation matrix:")
print(correlation_matrix)