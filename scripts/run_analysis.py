import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_pipeline import run_data_pipeline
from src.eda.eda_utils import visualize_clean_data 

def main():
    processed_new_df = "C:\\Users\\USER\\Desktop\\py\\APS_analysis\\data\\processed\\new_df.csv"
    # data cleaning
    print("\nStep 1: Starting data cleaning pipeline...")
    try:
        cleaned_df = run_data_pipeline(processed_new_df)
        print("Data has been cleaned successfully.")
    except FileNotFoundError:
        print(f"Error: Data file not found at '{processed_new_df}'.")
        print("Please ensure you are running the script from the project's root directory.")
        return
    except Exception as e:
        print(f"An error occurred during the data pipeline: {e}")
        return
    
    # data visualization 
    print("\nStep 2: Starting Exploratory Data Analysis (EDA)...")
    try:
        visualize_clean_data(cleaned_df)
        print("Exploratory data analysis completed successfully.")
    except Exception as e:
        print(f"An error occurred during analysis: {e}")
        return
        
    print("\nAnalysis finished successfully")

if __name__ == '__main__':
    main()