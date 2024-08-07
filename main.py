import clean_merge_data
import visualization

def main():
    try:
        print("Running clean_merge_data.py...")
        clean_merge_data.main()
        
        print("Running visualization.py...")
        visualization.main()
        
        print("All scripts executed successfully.")
    except Exception as e:
        print(f"An error occurred while running the scripts: {e}")

if __name__ == "__main__":
    main()
