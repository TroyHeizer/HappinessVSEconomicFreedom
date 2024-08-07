import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#-----happiest 35 countries-----

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

#-----lowest happiness 35 countries-----

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

#-----happiness by region visualization-----

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
