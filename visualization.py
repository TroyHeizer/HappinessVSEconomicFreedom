import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the merged dataset
merged_df = pd.read_csv('merged_dataset.csv')

# Calculate the correlation matrix
correlation_matrix = merged_df[['Score', 'GDP per capita', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption', '2019 Score']].corr()

# Example scatter plot: Happiness Score vs GDP per Capita
plt.figure(figsize=(10, 6))
sns.scatterplot(data=merged_df, x='GDP per capita', y='Score')
plt.title('Happiness Score vs GDP per Capita')
plt.xlabel('GDP per Capita')
plt.ylabel('Happiness Score')
plt.show()

# Example heatmap of the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap')
plt.show()

# Calculate the average Happiness Score by Region
average_happiness_by_region = merged_df.groupby('Region')['Score'].mean().reset_index()

# Create a bar chart
plt.figure(figsize=(14, 8))
sns.barplot(data=average_happiness_by_region, x='Region', y='Score', palette='viridis')
plt.title('Average Happiness Score by Region')
plt.xlabel('Region')
plt.ylabel('Average Happiness Score')
plt.xticks(rotation=45, ha='right')
plt.show()
