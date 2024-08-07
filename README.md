Project Statement
This project aims to compare the happiness levels of countries with their overall economic freedom. By analyzing two datasets — the Economic Freedom Index and the World Happiness Index from Kaggle — the goal is to uncover correlations and insights to understand if and how economic freedom influences the happiness of a nation’s citizens.

Required Features List
1. Read Two Data Files (CSV):
    * Load and read the datasets from CSV files.
2. Clean and Merge Data:
    * Clean the datasets and perform a pandas merge to combine the two datasets.
    * Calculate additional values based on the merged dataset.
3. Create Visualizations:
    * Produce at least three visualizations using matplotlib, seaborn, or another plotting library to display the data.
4. Build a Custom Data Dictionary:
    * Create a data dictionary if the datasets do not already include one. Include it in the README or as a separate document.
5. Annotate Your Code:
    * Ensure all Python scripts are well-commented and the README.md is clear and informative.

Setup Instructions

Clone repo to your local machien

Prerequisites
Ensure you have the following Python packages installed:
* pandas
* matplotlib
* seaborn
You can install them using pip:

“pip install pandas matplotlib seaborn”

File Structure
* load_data.py: Contains functions for loading and cleaning datasets.
* visualizations.py: Contains functions for generating visualizations.
* merged_dataset.csv: The cleaned and merged dataset used for analysis.

Running the Project

1. Load and Prepare Data:
    * Run load_data.py to load and clean the datasets. This script will generate merged_dataset.csv which is required for the visualizations.
    * Execute the script from the command line:shCopy codepython load_data.py
2. Generate Visualizations:
    * To create and view the visualizations, run the visualizations.py script. This script will generate various charts and plots based on the merged_dataset.csv.
    * Execute the script from the command line:“python visualizations.py”
3. Viewing the Results:
    * The visualizations will appear in separate windows. Ensure your environment supports graphical output to view these plots.

Troubleshooting
* Import Errors:
    * Check for circular imports and ensure your import statements in visualizations.py are correctly defined. Avoid importing modules from visualizations.py within visualizations.py itself.
* Missing Data:
    * Ensure merged_dataset.csv is present in the correct directory and is properly formatted. This file should be generated by running load_data.py.
Notes
* Ensure all CSV files are correctly placed in the project directory.
* Adjust file paths in the code if running scripts from a different directory.