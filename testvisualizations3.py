import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#-----economic impact on happiness scale-----

# Load the merged dataset
df = pd.read_csv('merged_dataset.csv')

# Select the columns for economic freedoms and 'Overall rank'
economic_freedom_columns = [
    'Property Rights', 'Judical Effectiveness', 'Government Integrity', 
    'Tax Burden', "Gov't Spending", 'Fiscal Health', 'Business Freedom', 
    'Labor Freedom', 'Monetary Freedom', 'Trade Freedom', 'Investment Freedom ', 
    'Financial Freedom'
]

# Ensure all necessary columns are present in the dataset
missing_columns = set(economic_freedom_columns) - set(df.columns)
if missing_columns:
    raise ValueError(f"Missing columns in dataset: {missing_columns}")

# Create a DataFrame with the relevant columns
rank_economic_freedom = df[['Overall rank'] + economic_freedom_columns]

# Calculate the correlation matrix
correlation_matrix = rank_economic_freedom.corr()

# Extract the correlation with 'Overall rank'
rank_correlation = correlation_matrix['Overall rank'].drop('Overall rank')

# Sort the correlations by absolute value
rank_correlation = rank_correlation.abs().sort_values(ascending=False)

# Plot the bar chart
plt.figure(figsize=(12, 8))
sns.barplot(x=rank_correlation.values, y=rank_correlation.index, palette='coolwarm')
plt.title('Impact of Economic Freedoms on Overall Happiness Rank')
plt.xlabel('Correlation with Overall Happiness Rank')
plt.ylabel('Economic Freedom Indicators')
plt.tight_layout()

# Show the plot
plt.show()
