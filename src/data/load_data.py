import pandas as pd
def load_data(file_path):
    """Load CSV file into DataFrame."""
    return pd.read_csv(file_path)

