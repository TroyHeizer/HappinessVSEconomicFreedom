import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the merged dataset
merged_df = pd.read_csv('merged_dataset.csv')

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
