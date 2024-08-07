import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv('merged_dataset.csv')

# Select the top 10 happiest countries
top_10_happiest = df[['Country', 'Score', 'Freedom to make life choices']].sort_values(by='Score', ascending=False).head(10)

# Create a scatter plot with a regression line
plt.figure(figsize=(12, 8))
sns.regplot(x='Freedom to make life choices', y='Score', data=top_10_happiest, scatter_kws={'s':100}, line_kws={'color':'red', 'linewidth':2})

# Add labels for each country
for i in range(top_10_happiest.shape[0]):
    plt.text(
        top_10_happiest.iloc[i]['Freedom to make life choices'], 
        top_10_happiest.iloc[i]['Score'], 
        top_10_happiest.iloc[i]['Country'], 
        fontsize=10,
        ha='right',  # Horizontal alignment
        va='bottom', # Vertical alignment
        alpha=0.8    # Transparency to reduce overlap
    )

# Add titles and labels
plt.title('Happiness Score vs. Freedom to Make Life Choices (Top 10 Happiest Countries)')
plt.xlabel('Freedom to Make Life Choices')
plt.ylabel('Happiness Score')

# Show the plot
plt.show()
