from load_data import load_datasets, inspect_data
from clean_merge_data import clean_and_merge

def main():
    df1, df2 = load_datasets()
    inspect_data(df1, df2)
    
    merged_df = clean_and_merge(df1, df2)
    
    # Here you would call functions from analysis.py to perform analysis and create visualizations
    # Example:
    # analyze_data(merged_df)
    # create_visualizations(merged_df)

if __name__ == "__main__":
    main()