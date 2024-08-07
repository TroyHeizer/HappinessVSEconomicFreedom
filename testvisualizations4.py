import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#-----correlation between happiness and property rights top 35 countires-----

# Load the merged dataset
df = pd.read_csv('merged_dataset.csv')

# Select the top 35 happiest countries based on the 'Score' column
top_35_happiest = df[['Country', 'Score', 'Property Rights']].sort_values(by='Score', ascending=False).head(35)

# Plot a scatter plot with a regression line
plt.figure(figsize=(10, 6))
sns.regplot(x='Property Rights', y='Score', data=top_35_happiest, ci=None, scatter_kws={'s': 100}, line_kws={'color': 'red'})
plt.title('Correlation between Happiness Scores and Property Rights for Top 35 Happiest Countries')
plt.xlabel('Property Rights')
plt.ylabel('Happiness Score')

# Annotate the points with country names
for i in range(top_35_happiest.shape[0]):
    plt.text(top_35_happiest['Property Rights'].iloc[i], top_35_happiest['Score'].iloc[i], top_35_happiest['Country'].iloc[i], fontsize=8, ha='right')

plt.tight_layout()
plt.show()
