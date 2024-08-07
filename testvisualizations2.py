import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv('merged_dataset.csv')

# Print column names to verify
print("Columns in the dataset:")
print(df.columns)

# Aggregate happiness scores by region
# Assuming 'Region' is the column name for regions in your dataset
region_happiness = df.groupby('Region')['Score'].mean().reset_index()

# Sort regions for better visualization
region_happiness = region_happiness.sort_values(by='Score', ascending=False)

# Create a DataFrame for the heatmap
heatmap_data = pd.DataFrame({
    'Region': region_happiness['Region'],
    'Average Happiness Score': region_happiness['Score']
}).set_index('Region').T

# Create the heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', fmt=".2f", cbar_kws={'label': 'Happiness Score'})

# Add titles and labels
plt.title('Average Happiness Scores by Region')
plt.xlabel('Region')
plt.ylabel('Average Happiness Score')

# Show the plot
plt.show()

