from clean_merge_data import load_datasets, clean_and_merge
from visualization import vis_main

def main():
    try:
        print("Running clean_merge_data.py...")
        df1, df2 = load_datasets()
        clean_and_merge(df1, df2)
        
        print("Running visualization.py...")
        vis_main()
        
        print("All scripts executed successfully.")
    except Exception as e:
        print(f"An error occurred while running the scripts: {e}")

if __name__ == "__main__":
    main()