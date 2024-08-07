import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#lowest happiness 35 countries

# Load the merged dataset
df = pd.read_csv('merged_dataset.csv')

# Select the bottom 35 least happy countries based on the 'Score' column
bottom_35_sad = df[['Country', 'Score']].sort_values(by='Score', ascending=True).head(35)

# Reverse the order for plotting
bottom_35_sad = bottom_35_sad[::-1]

# Create a bar chart
plt.figure(figsize=(10, 7.5))  # Adjusted size to be about 3/4 of the previous size
sns.barplot(x='Score', y='Country', data=bottom_35_sad, palette='viridis')

plt.title('Happiness Levels of the Bottom 35 Least Happy Countries')
plt.xlabel('Happiness Score')
plt.ylabel('Country')
plt.tight_layout()  # Adjust layout to fit labels

# Show the plot
plt.show()

