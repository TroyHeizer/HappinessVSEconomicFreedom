import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#happiest 35 countries

# Load the merged dataset
df = pd.read_csv('merged_dataset.csv')

# Select the top 35 happiest countries based on the 'Score' column
top_35_happiest = df[['Country', 'Score']].sort_values(by='Score', ascending=False).head(35)

# Create a bar chart
plt.figure(figsize=(10, 7.5))  # Adjusted size to be about 3/4 of the previous size
sns.barplot(x='Score', y='Country', data=top_35_happiest, palette='viridis')

plt.title('Happiness Levels of the Top 35 Happiest Countries')
plt.xlabel('Happiness Score')
plt.ylabel('Country')
plt.tight_layout()  # Adjust layout to fit labels

# Show the plot
plt.show()
