import sys
import os
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data.load_data import load_data
from src.data.clean_data import (
    fill_missing_arrival_with_departure,
    drop_columns,
    reorder_columns,
    clean_column_names,
    convert_column_type
)

def run_data_pipeline(file_path):
    # Load raw data
    print("Loading raw data...")
    df = load_data(file_path)

    # Clean data
    print("Cleaning data...")
    df = fill_missing_arrival_with_departure(df)
    df = drop_columns(df, ['Unnamed: 0'])
    df = reorder_columns(df, ['id', 'Gender', 'Age', 'Type of Travel', 'Class', 'Customer Type'])
    df = clean_column_names(df)
    df = convert_column_type(df, 'departure delay in minutes', float)

    return df

if __name__ == "__main__":

    processed_new_df = "C:\\Users\\USER\\Desktop\\py\\APS_analysis\\data\\processed\\new_df.csv"
    cleaned_df = run_data_pipeline(processed_new_df)

    processed_cleaned_data = "C:\\Users\\USER\\Desktop\\py\\APS_analysis\\data\\processed\\cleaned_data.csv"
    cleaned_df.to_csv(processed_cleaned_data , index=False)
